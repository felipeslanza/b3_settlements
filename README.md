b3_settlements
==============

(Unofficial) API for querying futures' settlements from B3 exchange (Brazil)


Installation
------------

You can install it with `pip`. Requires `python>=3.8`:

```shell
pip install git+https://github.com/felipeslanza/b3_settlements
```


Usage
-----

The API has two very simple usages, as shown below. Always use dates in the `YYYY-MM-DD`
format.

```python
from b3_settlements import get_daily, get_history

# Query a precise date
df = get_daily("2020-02-11")  # YYYY-MM-DD format

# Query historical data
df = get_history(start_dt="2020-02-03", end_dt="2020-02-28")  # YYYY-MM-DD format
```
