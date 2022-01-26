import pandas as pd

from b3_settlements.api import get_daily, get_history
from b3_settlements.constants import API_TABLE_COLUMNS


def test_get_daily():
    for date in ("2000-5-4", "2006-5-4", "2021-1-18"):
        df = get_daily(date)

        assert df.size, f"Returned empty DataFrame in {date}"
        assert (df.columns == API_TABLE_COLUMNS).all(), f"Invalid columns formatting"


def test_get_history():
    start_dt = "2013-01-07"
    end_dt = "2013-01-11"
    cols = ["exch_ticker", *API_TABLE_COLUMNS]
    df = get_history(start_dt=start_dt, end_dt=end_dt)

    assert df.size, f"Returned empty DataFrame"
    assert (df.columns == cols).all(), f"Invalid columns formatting"
    assert df.index[0] == pd.to_datetime(start_dt), "Missing first date"
    assert df.index[-1] == pd.to_datetime(end_dt), "Missing first date"
