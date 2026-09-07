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

total_rows = 0

for chunk in pd.read_csv(
    FILE_PATH,
    header=None,
    names=COLUMNS,
    chunksize=100_000
):
    print(f"Loaded {len(chunk):,} rows")
    total_rows += len(chunk)

    ### --- PRICES --- ###
    # (chunk["price"]) creates a boolean output (True or False)
    # .sum() then counts the total amount of values less than or equal to 0 
    # (True is treated as a 1, False as a 0)
    invalid_prices = (chunk["price"] <= 0).sum()
    print(f"Invalid prices in chunk: {invalid_prices}")

    ### --- DATES --- ###
    # Convert all values in date column into datetime objects
    # errors="coerce" - error check, if it cant convert just put NaT
    chunk["date"] = pd.to_datetime(chunk["date"], errors="coerce")

    # Count the number of NaT values
    invalid_dates = chunk["date"].isna().sum()
    print(f"Invalid dates in chunk: {invalid_dates}", "\n")

    ### --- PROPERTY TYPES --- ###
    property_types = chunk["property_type"].unique()
    print("Property Types: ", *property_types)
    property_type_counts = chunk["property_type"].value_counts()
    print(f"Property Type Counts: {property_type_counts}")

    valid_property_types = {"D", "S", "T", "F", "O"}
    invalid_property_types = set(property_types) - valid_property_types
    print("Invalid Property Types:", *invalid_property_types, "\n")


    ### --- NEW BUILD --- ###
    new_build_values = chunk["new_build"].unique()
    print("New Build Values:", *new_build_values)

    valid_new_build_values = {"Y", "N"}
    invalid_new_build_values = set(new_build_values) - valid_new_build_values
    print("Invalid New Build Values:", *invalid_new_build_values, "\n")

    ### --- DURATION --- ###
    duration_values = chunk["duration"].unique()
    print("Duration Values:", *duration_values)

    valid_duration_types = {"L", "F"}
    invalid_duration_values = set(duration_values) - valid_duration_types
    print("Invalid Duration Values:", *invalid_duration_values, "\n")

    ### --- PPD Category --- ###
    ppd_category_values = chunk["ppd_category"].unique()
    print("PPD Category Values", *ppd_category_values)

    valid_ppd_categories = {"A", "B"}
    invalid_ppd_category_types = set(ppd_category_values) - valid_ppd_categories
    print("Invalid PPD_Category Values:", *invalid_ppd_category_types, "\n")





    print(chunk.head(2))
    break
print(f"Total rows processed: {total_rows:,}")
