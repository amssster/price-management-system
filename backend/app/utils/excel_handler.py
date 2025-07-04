import pandas as pd

def read_excel_file(file_path: str, sheet_name=None) -> pd.DataFrame:
    """Чтение Excel-файла (xls, xlsx)."""
    return pd.read_excel(file_path, sheet_name=sheet_name)

def read_google_sheet_url(url: str) -> pd.DataFrame:
    """Чтение публично доступной Google Sheets таблицы по ссылке."""
    if 'docs.google.com/spreadsheets' not in url:
        raise ValueError('URL не является ссылкой на Google Sheets')
    if 'export?format=' not in url:
        if '/edit#gid=' in url:
            url = url.replace('/edit#gid=', '/export?format=csv&gid=')
        else:
            url = url.rstrip('/') + '/export?format=csv'
    return pd.read_csv(url)
