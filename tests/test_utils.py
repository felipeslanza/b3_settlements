import pandas as pd

from b3_settlements.utils import *
from b3_settlements.constants import API_TABLE_COLUMNS


def test_make_payload():
    date_str = "05/05/2021"
    date = pd.to_datetime(date_str)
    assert make_payload(date) == {"dData1": date_str}, "Failed payload"


def test_extract_table():
    res = pd.read_pickle("tests/sample_response.pkl")
    df = extract_table(res)
    assert df.size, f"Returned empty DataFrame in {date}"
    assert (df.columns == API_TABLE_COLUMNS).all(), f"Invalid formatting"
