import os
from typing import Tuple

import pandas as pd


class FileProcessor:
    """Универсальная обработка файлов разных форматов (CSV, Excel, XML, Google Sheets)."""

    @staticmethod
    def detect_format(file_path: str) -> str:
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".csv":
            return "csv"
        if ext in (".xls", ".xlsx"):
            return "excel"
        if ext == ".xml":
            return "xml"
        if file_path.startswith("http") and "docs.google.com/spreadsheets" in file_path:
            return "google_sheets"
        raise ValueError(f"Неизвестный формат файла: {ext}")

    @staticmethod
    def process(file_path: str) -> Tuple[pd.DataFrame, str]:
        fmt = FileProcessor.detect_format(file_path)
        if fmt == "csv":
            df = pd.read_csv(file_path)
        elif fmt == "excel":
            from app.utils.excel_handler import read_excel_file

            df = read_excel_file(file_path)
        elif fmt == "xml":
            df = pd.read_xml(file_path)
        elif fmt == "google_sheets":
            from app.utils.excel_handler import read_google_sheet_url

            df = read_google_sheet_url(file_path)
        else:
            raise ValueError(f"Unsupported format: {fmt}")
        return df, fmt
