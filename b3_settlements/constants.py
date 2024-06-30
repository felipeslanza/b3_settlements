# API settings
# ----
API_ENDPOINT = r"https://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-ajustes-do-pregao-ptBR.asp"

API_DATE_FORMAT = "%d/%m/%Y"

# Order matters
API_TABLE_COLUMNS = [
    "underlying",
    "mty",
    "previous_settlement",
    "last_settlement",
    "delta_points",
    "delta_by_contract",
]


# General
# ----
DATE_FORMAT = "%Y-%m-%d"

TEMP_FILENAME = "local_b3_historical_data.csv"
