import pandas as pd

from b3_settlements.api import get_history


# ++++++++++++++++++++++++++
# Settings
# ++++++++++++++++++++++++++
START_DT = "2024-01-01"
END_DT = "2024-01-05"
# ++++++++++++++++++++++++++


if __name__ == "__main__":
    df = get_history(START_DT, END_DT)
