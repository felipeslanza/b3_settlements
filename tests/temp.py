from b3_settlements.main import get_daily, get_history


if __name__ == "__main__":
    #  df = get_daily()
    df = get_history("2021-01-01", "2021-01-15")
