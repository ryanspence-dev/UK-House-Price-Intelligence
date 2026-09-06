import pandas as pd

FILE_PATH = "data/raw/pp-complete.csv"

COLUMNS = [
    "transaction_id",
    "price",
    "date",
    "postcode",
    "property_type",
    "new_build",
    "duration",
    "paon",
    "saon",
    "street",
    "locality",
    "town_city",
    "district",
    "county",
    "ppd_category",
    "record_status",
]

for chunk in pd.read_csv(
    FILE_PATH,
    header=None,
    names=COLUMNS,
    chunksize=100_000
):
    print(f"Loaded {len(chunk):,} rows")
    print(chunk.head(2))
    break