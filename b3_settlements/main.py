import requests
from datetime import datetime
from typing import Optional, Union

import pandas as pd

from .constants import API_ENDPOINT
from .utils import make_payload, parse_table

__all__ = ("get_daily", "get_history")


def get_daily(date: Optional[Union[str, datetime]] = None) -> pd.DataFrame:
    data = make_payload(date or datetime.today().date())

    try:
        res = requests.get(API_ENDPOINT, data=data)
    except (ConnectionError, TimeoutError):
        print("ERROR - Service unavailable, try again later")
        return

    if res.status_code != 200:
        print("ERROR - Unhandled status code")
        return

    table = parse_table(res)

    return table


def get_history() -> dict:
    pass
