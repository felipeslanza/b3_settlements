import requests
from contextlib import redirect_stdout
from datetime import datetime
from typing import Optional, Tuple, Union

import pandas as pd
from joblib import Parallel, delayed

from .constants import API_ENDPOINT, DATE_FORMAT
from .utils import make_payload, extract_table

__all__ = ("get_daily", "get_history")


# Private
# ----
def _safely_get_daily(date_str: str, verbose: bool) -> Tuple[str, pd.DataFrame]:
    try:
        with redirect_stdout(None):
            daily = get_daily(date_str)
        if daily.empty:
            if verbose:
                print(f"ERROR - Returned empty for {date_str}")
    except Exception as e:
        print(f"ERROR - Unhandled exception at {date_str} - {e}")

    return (date_str, daily)


# Public
# ----
def get_daily(date: Optional[Union[str, datetime]] = None) -> pd.DataFrame:
    """Query settlements' data for a single date. Returns a table in the
    following format:

        [index]
            exch_ticker: contract's exchange ticker/code

        [columns]
            underlying: name of the underlying asset
            mty: contract's maturity code
            previous_settlement: settlemente price in the PREVIOUS date
            last_settlement: settlemente price in the CURRENT date
            delta_points: daily variation in points
            delta_by_contract: daily variation of a single contract in BRL

    ...

    Parameters
    -----------
    date : str or datetime (default=None)
        if using `str`, must be in YYYY-MM-DD format. If not provided, will
        use `datetime.today`.
    """
    date = pd.to_datetime(date or datetime.today().date())
    data = make_payload(date)

    try:
        res = requests.get(API_ENDPOINT, data=data)
    except (ConnectionError, TimeoutError):
        print("ERROR - Service unavailable, try again later")
        return pd.DataFrame()

    if res.status_code != 200:
        print("ERROR - Unhandled status code")
        return pd.DataFrame()

    return extract_table(res)


def get_history(
    start_dt: Union[str, datetime],
    end_dt: Optional[Union[str, datetime]] = None,
    n_jobs: int = -1,
    verbose: bool = True,
) -> pd.DataFrame:
    """Query settlements' data for a date range. Returns a table in the
    following format:

        [index]
            dates: close date

        [columns]
            exch_ticker: contract's exchange ticker/code
            underlying: name of the underlying asset
            mty: contract's maturity code
            previous_settlement: settlemente price in the PREVIOUS date
            last_settlement: settlemente price in the CURRENT date
            delta_points: daily variation in points
            delta_by_contract: daily variation of a single contract in BRL

    ...

    Parameters
    ----------
    start_dt : str or datetime
        if using `str`, must be in YYYY-MM-DD format
    end_dt : str or datetime (default=None)
        if using `str`, must be in YYYY-MM-DD format. If not provided, will
        use `datetime.today()`.
    n_jobs : int
        # of jobs
    verbose : bool
        if True, will print out missed dates
    """

    start_dt = pd.to_datetime(start_dt)
    end_dt = pd.to_datetime(end_dt or datetime.today().date())
    if end_dt <= start_dt:
        raise ValueError("`end_dt` must be >= `start_dt")

    date_strings = pd.date_range(start_dt, end_dt).strftime(DATE_FORMAT)
    print(f"INFO - Scraping data from {date_strings[0]} to {date_strings[-1]}")

    daily_queue = Parallel(n_jobs=n_jobs)(
        delayed(_safely_get_daily)(date_str, verbose) for date_str in date_strings
    )

    df = (
        pd.concat(dict(daily_queue))
        .reset_index(level=1)
        .rename(columns={"level_1": "exch_ticker"})
    )

    df.index = pd.to_datetime(df.index)

    return df
