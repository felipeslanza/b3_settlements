import requests
from datetime import datetime
from typing import Union

import pandas as pd

from .constants import DATE_FORMAT, TABLE_COLUMNS


__all__ = ("make_payload", "parse_table")


def make_payload(date: Union[str, datetime]) -> str:
    date_str = pd.to_datetime(date).strftime(DATE_FORMAT)
    return {"dData1": date_str}


def parse_table(response: requests.models.Response) -> pd.DataFrame:
    table = pd.read_html(response.text, decimal=",")[0]

    # Parsing
    table.columns = TABLE_COLUMNS
    table.iloc[:, 0] = table.iloc[:, 0].ffill()
    table.set_index(TABLE_COLUMNS[0], inplace=True)
    table["settlement"] = pd.to_numeric(
        table["settlement"].str.replace(".", "").str.replace(",", "."),  # TODO: improve!
        errors="ignore",
    )
    table["exch_ticker"] = table.index.str.split(" - ").str[0] + table[TABLE_COLUMNS[1]]

    return table
