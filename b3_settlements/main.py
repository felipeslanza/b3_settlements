import requests
from datetime import datetime
from typing import Optional, Union

import pandas as pd

from .constants import API_ENDPOINT, DATE_FORMAT
from .utils import make_payload, parse_table

__all__ = ("get_daily", "get_history")


def get_daily(date: Optional[Union[str, datetime]] = None) -> pd.DataFrame:
    """Query settlements' datat for a single date

    ...

    Parameters
    -----------
    date : str or datetime
        if using `str`, must be in YYYY-MM-DD format
    """
    date = pd.to_datetime(date or datetime.today().date())
    data = make_payload(date)

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


def get_history(
    start_dt: Union[str, datetime],
    end_dt: Optional[Union[str, datetime]] = None,
) -> dict:
    """Query historical data for the requested period

    ...

    Parameters
    ----------
    start_dt : str or datetime
        if using `str`, must be in YYYY-MM-DD format
    end_dt : str or datetime, default=None
        if using `str`, must be in YYYY-MM-DD format
    """
    start_dt = pd.to_datetime(start_dt)
    end_dt = pd.to_datetime(end_dt or datetime.today().date())

    date_strings = pd.date_range(start_dt, end_dt).strftime(DATE_FORMAT)
    print(f"INFO - Scraping data from {date_strings[0]} to {date_strings[-1]}")

    results = {}
    for date_str in date_strings:
        try:
            results[date_str] = get_daily(date_str)
        except Exception as e:
            print(f"ERROR - Unhandled exception at {date}")

    return results
