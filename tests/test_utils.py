import requests

import pandas as pd

from b3_settlements.utils import *


def test_make_payload():
    date_str = "05/05/2021"
    date = pd.to_datetime(date_str)
    assert make_payload(date) == {"dData1": date_str}, "Failed payload"


def test_parse_table():
    pass
