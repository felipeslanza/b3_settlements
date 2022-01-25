# API settings
# ----
API_ENDPOINT = (
    r"http://www2.bmf.com.br/pages/portal/bmfbovespa/lumis/lum-ajustes-do-pregao-ptBR.asp"
)

API_DATE_FORMAT = "%d/%m/%Y"

# Order matters
API_TABLE_COLUMNS = [
    "underlying",
    "mty",
    "last_settlement",
    "settlement",
    "delta",
    "delta_by_contract",
]


# General
# ----
DATE_FORMAT = "%Y-%m-%d"
