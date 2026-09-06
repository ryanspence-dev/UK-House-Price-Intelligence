import pandas as pd

file_path = "data/raw/pp-complete.csv"

columns = [
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

df = pd.read_csv(
    file_path,
    nrows=1000,
    header=None,
    names=columns
)

print("Shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head().to_string())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("\nProperty types:")
print(df["property_type"].value_counts())

print("\nNew build values:")
print(df["new_build"].value_counts())

print("\nDuration values:")
print(df["duration"].value_counts())

print("\nPrice statistics:")
print(df["price"].describe())

print("\nDuplicate transaction IDs:")
print(df["transaction_id"].duplicated().sum())