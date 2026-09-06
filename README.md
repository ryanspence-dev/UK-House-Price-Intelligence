## Data Source

The primary dataset used by this project is the **HM Land Registry Price Paid Data (PPD)**.

The dataset contains residential property transactions in England and Wales and covers transactions from **1 January 1995 onwards**. The complete dataset is updated monthly.

### Dataset Fields

The raw HM Land Registry CSV does not include column headers, so the following schema is applied during ingestion:

| Field            | Description                                                     |
| ---------------- | --------------------------------------------------------------- |
| `transaction_id` | Unique identifier for the transaction                           |
| `price`          | Sale price in GBP                                               |
| `date`           | Date of property transfer                                       |
| `postcode`       | Property postcode                                               |
| `property_type`  | Type of property                                                |
| `new_build`      | Whether the property was newly built                            |
| `duration`       | Property tenure                                                 |
| `paon`           | Primary Addressable Object Name, typically house number or name |
| `saon`           | Secondary Addressable Object Name, such as a flat number        |
| `street`         | Street name                                                     |
| `locality`       | Locality                                                        |
| `town_city`      | Town or city                                                    |
| `district`       | Administrative district                                         |
| `county`         | County                                                          |
| `ppd_category`   | Price Paid Data category                                        |
| `record_status`  | Record status                                                   |

### Coded Fields

Some fields use short codes in the raw dataset:

| Field           | Code | Meaning               |
| --------------- | ---- | --------------------- |
| `property_type` | `D`  | Detached              |
| `property_type` | `S`  | Semi-detached         |
| `property_type` | `T`  | Terraced              |
| `property_type` | `F`  | Flat/Maisonette       |
| `property_type` | `O`  | Other                 |
| `new_build`     | `Y`  | Newly built           |
| `new_build`     | `N`  | Established building  |
| `duration`      | `F`  | Freehold              |
| `duration`      | `L`  | Leasehold             |
| `ppd_category`  | `A`  | Standard Price Paid   |
| `ppd_category`  | `B`  | Additional Price Paid |
| `record_status` | `A`  | Addition              |
| `record_status` | `C`  | Change                |
| `record_status` | `D`  | Delete                |

### Source

HM Land Registry — Price Paid Data

The raw dataset is stored locally in:

`data/raw/pp-complete.csv`

The raw data is excluded from version control because of its size.

### Attribution

Contains HM Land Registry data © Crown copyright and database right 2021. This data is licensed under the Open Government Licence v3.0.
