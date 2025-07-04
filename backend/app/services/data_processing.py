from typing import Dict, Type
import difflib
import pandas as pd

def auto_map(df: pd.DataFrame, model_class: Type) -> Dict[str, str]:
    """
    Автоматическое сопоставление столбцов DataFrame с полями модели по близости имен.
    Возвращает словарь mapping: ключ — исходное имя столбца, значение — имя поля модели.
    """
    model_fields = [col.name for col in model_class.__table__.columns]
    mapping: Dict[str, str] = {}
    for col in df.columns:
        matches = difflib.get_close_matches(col, model_fields, n=1, cutoff=0.8)
        if matches:
            mapping[col] = matches[0]
    return mapping

def apply_mapping(df: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
    """
    Переименование столбцов DataFrame в соответствии с mapping.
    """
    return df.rename(columns=mapping)
