import pandas as pd
from typing import List, Dict

def validate_required_fields(df: pd.DataFrame, required_fields: List[str]) -> Dict[int, List[str]]:
    """
    Проверка обязательных столбцов в DataFrame.
    Возвращает словарь, где ключи — индексы строк с отсутствующими данными,
    а значения — список отсутствующих столбцов.
    """
    missing: Dict[int, List[str]] = {}
    for idx, row in df.iterrows():
        absent = [col for col in required_fields if pd.isna(row.get(col))]
        if absent:
            missing[idx] = absent
    return missing
