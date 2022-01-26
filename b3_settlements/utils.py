import requests
from datetime import datetime
from typing import Union

import pandas as pd

from .constants import API_DATE_FORMAT, API_TABLE_COLUMNS


__all__ = ("make_payload", "extract_table")


def make_payload(date: datetime) -> str:
    date_str = date.strftime(API_DATE_FORMAT)
    return {"dData1": date_str}


def extract_table(response: requests.models.Response) -> pd.DataFrame:
    table = pd.read_html(response.text, decimal=",")[0]
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
