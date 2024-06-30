from io import StringIO
import sys
import requests
from datetime import datetime

import pandas as pd

from .constants import API_DATE_FORMAT, API_TABLE_COLUMNS


__all__ = (
    "extract_table",
    "get_temp_directory",
    "make_payload",
)


def get_temp_directory() -> str:
    if sys.platform.startswith("linux"):
        temp_dir = "/tmp"
    elif sys.platform.startswith("win32") or sys.platform.startswith("cygwin"):
        temp_dir = os.getenv("TEMP", "C:\\Temp")
    elif sys.platform.startswith("darwin"):
        temp_dir = "/tmp"
    else:
        raise NotImplementedError("Unsupported operating system")
    return temp_dir


def extract_table(response: requests.models.Response) -> pd.DataFrame:
    try:
        tables = pd.read_html(StringIO(response.text), decimal=",")
        table = tables[0]
    except ValueError:
        print("ERROR - No tables found")
        return pd.DataFrame(dtype="float")

    table = tables[0]
    first_col, second_col = API_TABLE_COLUMNS[:2]
    table.columns = API_TABLE_COLUMNS
    table.iloc[:, 0] = table.iloc[:, 0].ffill()

    for col in API_TABLE_COLUMNS[2:]:
        table[col] = pd.to_numeric(
            table[col].astype(str).str.replace(".", "").str.replace(",", "."),
            errors="raise",
        )

    index = table[first_col].str.split(" - ").str[0] + table[second_col]
    table.set_index(index, inplace=True)

    return table


def make_payload(date: datetime) -> dict:
    date_str = date.strftime(API_DATE_FORMAT)
    return {"dData1": date_str}
