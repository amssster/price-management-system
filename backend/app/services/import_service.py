import os
from typing import Optional, Dict

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.import_log import ImportLog
from app.utils.file_processor import FileProcessor
from app.utils.formatters import normalize_dataframe_columns
from app.services.data_processing import auto_map, apply_mapping


def import_data(
    db: Session,
    file: UploadFile,
    supplier_id: int,
    mapping_config: Optional[Dict[str, str]] = None,
) -> ImportLog:
    """
    Обработка загрузки файла импорта: сохранение, чтение и маппинг полей.
    Возвращает запись ImportLog с результатами.
    """
    os.makedirs(settings.UPLOAD_PATH, exist_ok=True)
    file_path = os.path.join(settings.UPLOAD_PATH, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    df, fmt = FileProcessor.process(file_path)
    df = normalize_dataframe_columns(df)

    import_log = ImportLog(
        file_name=file.filename,
        file_path=file_path,
        file_size=os.path.getsize(file_path),
        format=fmt,
        status="processing",
        total_records=len(df),
        supplier_id=supplier_id,
        mapping_config=mapping_config or {},
    )
    db.add(import_log)
    db.commit()
    db.refresh(import_log)

    if not mapping_config:
        from app.models.product import Product

        mapping_config = auto_map(df, Product)
        import_log.mapping_config = mapping_config
        db.commit()

    df = apply_mapping(df, mapping_config)


    import_log.processed_records = len(df)
    import_log.status = "completed"
    db.commit()
    return import_log
