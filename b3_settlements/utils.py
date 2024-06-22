from io import StringIO
import requests
from datetime import datetime

import pandas as pd

from .constants import API_DATE_FORMAT, API_TABLE_COLUMNS


__all__ = ("make_payload", "extract_table")


def make_payload(date: datetime) -> dict:
    date_str = date.strftime(API_DATE_FORMAT)
    return {"dData1": date_str}


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
            table[col]
            .astype(str)
            .str.replace(".", "", regex=True)
            .str.replace(",", ".", regex=True),
            errors="ignore",
        )

    index = table[first_col].str.split(" - ").str[0] + table[second_col]
    table.set_index(index, inplace=True)

    return table
