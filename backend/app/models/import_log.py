from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class ImportLog(Base):
    __tablename__ = "import_logs"

    id = Column(Integer, primary_key=True, index=True)

    # Информация об импорте
    file_name = Column(String(255))
    file_path = Column(String(500))
    file_size = Column(Integer)
    format = Column(String(20))

    # Статус
    status = Column(String(20))  # pending, processing, completed, failed

    # Результаты
    total_records = Column(Integer, default=0)
    processed_records = Column(Integer, default=0)
    created_records = Column(Integer, default=0)
    updated_records = Column(Integer, default=0)
    error_records = Column(Integer, default=0)

    # Детали
    errors = Column(JSON)
    warnings = Column(JSON)
    mapping_config = Column(JSON)

    # Временные метки
    started_at = Column(DateTime, default=func.now())
    completed_at = Column(DateTime)

    # Связи
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))

    # Отношения
    supplier = relationship("Supplier", back_populates="import_logs")

    def __str__(self):
        return f"ImportLog(id={self.id}, file_name={self.file_name}, status={self.status})"
