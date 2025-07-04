import re

def normalize_column_name(name: str) -> str:
    """
    Приведение имени столбца к нижнему регистру, замена
    пробелов на подчеркивания и удаление неалфанумерических символов.
    """
    s = name.strip().lower()
    s = re.sub(r'\s+', '_', s)
    s = re.sub(r'[^\w_]', '', s)
    return s

def normalize_dataframe_columns(df):
    """
    Применение нормализации ко всем именам столбцов DataFrame.
    """
    df = df.copy()
    df.columns = [normalize_column_name(c) for c in df.columns]
    return df
