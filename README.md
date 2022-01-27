b3_settlements
==============

(Unofficial) API for querying futures' settlements from B3 exchange (Brazil)


Installation
------------

Requires `python>=3.8`:

```python
pip install https://github.com/felipeslanza/b3_settlements.git
```


Usage
-----

The API has two simple usages, as shown below. Always use dates in the `YYYY-MM-DD`
format.

```python
from b3_settlements import get_daily, get_history

# Query a precise date
df = get_daily("2020-02-11")  # YYYY-MM-DD format

# Query historical data
df = get_history(start_dt="2020-02-03", end_dt="2020-02-28")  # YYYY-MM-DD format
```


License
-------

MIT License

Copyright (c) 2022 Felipe Lanza

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
