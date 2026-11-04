# Part 7 — Lesson 06: Data Cleaning with Pandas

README path: `python/07-data-science-foundation/lessons/06-pandas-data-cleaning/README.md`

In Lesson 05, you learned to inspect CSV files, identify missing values, check duplicates, and understand data types. Now you'll learn how to clean a dataset before analyzing it.

We'll use an e-commerce sales dataset similar to the data you've been working with.

Lesson objectives

By the end of this lesson, you'll be able to:

- Handle missing values with `fillna()` and `dropna()`.
- Identify and remove duplicate records.
- Standardize text with `str.strip()` and `str.title()`.
- Convert columns to suitable data types.
- Validate prices and quantities.
- Build a reusable data-cleaning script.

## 1. Prerequisites and setup

Activate your existing Part 7 virtual environment:

```
cd /var/www/html/AI-Learning/python/07-data-science-foundation
source .venv/bin/activate
```

Create the lesson directory:

```
mkdir -p lessons/06-pandas-data-cleaning
cd lessons/06-pandas-data-cleaning
```

Confirm Pandas is installed:

```
python -c "import pandas as pd; print(pd.__version__)"
```

## 2. Create a messy dataset

Create `messy_sales.csv` with the following contents:

```
OrderID,Product,Category,Price,Quantity,Status
201,Laptop,Electronics,55000,1,Completed
202,Mouse,Accessories,500,4,Completed
203, keyboard ,Accessories,1200,2,Pending
204,Monitor,Electronics,,1,Completed
205,Mouse,Accessories,500,3,Pending
205,Mouse,Accessories,500,3,Pending
206,Webcam,Accessories,2200,,Completed
207,Headphones,Accessories,2500,2, completed
208,Monitor,Electronics,-100,1,Pending
```

This dataset contains several issues:

| Problem                     | Example                        |
| --------------------------- | ------------------------------ |
| Extra whitespace            | `" keyboard "`                 |
| Inconsistent capitalization | `" completed"`                 |
| Missing price               | Order 204                      |
| Missing quantity            | Order 206                      |
| Duplicate record            | Order 205 appears twice        |
| Invalid price               | Order 208 has a negative price |

Our goal is to detect these problems and apply appropriate cleaning rules.

## 3. Inspect the original dataset

Create `lesson06_cleaning.py`:

```
import pandas as pddf = pd.read_csv("messy_sales.csv")print("=== ORIGINAL DATA ===")print(df)print("\n=== MISSING VALUES ===")print(df.isna().sum())print("\n=== DUPLICATE ROWS ===")print(df.duplicated().sum())print("\n=== DATA TYPES ===")print(df.dtypes)print("\n=== UNIQUE PRODUCTS ===")print(df["Product"].unique())print("\n=== UNIQUE STATUSES ===")print(df["Status"].unique())
```

Run it:

```
python lesson06_cleaning.py
```

Practice: Before cleaning anything, identify each problem in the output. This is the same inspection process you learned in Lesson 05.

## 4. Clean text values

Text columns often contain inconsistent capitalization and accidental whitespace.

### 4.1 Remove leading and trailing whitespace

```
df["Product"] = df["Product"].str.strip()df["Category"] = df["Category"].str.strip()df["Status"] = df["Status"].str.strip()
```

For example, `" keyboard "` becomes `"keyboard"`.

### 4.2 Standardize capitalization

```
df["Product"] = df["Product"].str.title()df["Category"] = df["Category"].str.title()df["Status"] = df["Status"].str.title()
```

For example, `" completed"` becomes `"Completed"` after stripping and title-casing.

Inspect the results:

```
print(df[["Product", "Category", "Status"]])
```

Useful string methods:

| Method           | Actual use                                   |
| ---------------- | -------------------------------------------- |
| `.str.strip()`   | Removes whitespace at the beginning and end. |
| `.str.lower()`   | Converts text to lowercase.                  |
| `.str.upper()`   | Converts text to uppercase.                  |
| `.str.title()`   | Capitalizes the beginning of each word.      |
| `.str.replace()` | Replaces matching text.                      |

Use consistent formatting that suits the actual data. Title case is not appropriate for every field, such as email addresses or case-sensitive identifiers.

## 5. Handle duplicate records

First, inspect the duplicates:

```
print(df[df.duplicated()])
```

Remove exact duplicate rows:

```
df = df.drop_duplicates()
```

Then verify:

```
print("Duplicate rows remaining:", df.duplicated().sum())
```

The duplicate Order 205 row should be removed.

Important: `drop_duplicates()` checks complete rows by default. If two rows share an `OrderID` but have different values in other columns, they are not necessarily exact duplicates. Investigate such cases before deciding whether to remove them.

## 6. Handle missing values

There are two common approaches: filling missing values and removing records.

### 6.1 Find missing values

```
print(df.isna().sum())
```

### 6.2 Fill a missing value when you have a justified replacement

For example, you may fill a missing category with `"Unknown"`:

```
df["Category"] = df["Category"].fillna("Unknown")
```

For numeric fields, the correct replacement depends on the meaning of the data. Filling a missing price with zero or an average without justification can distort revenue calculations.

### 6.3 Remove records that cannot be reliably analyzed

In this lesson, we'll keep records with missing values in the dataset until we decide which records can be analyzed.

For the sales calculation, a row with missing `Price` or `Quantity` cannot produce reliable revenue. One possible rule is to exclude those rows from the revenue analysis, while retaining the original data for review.

```
valid_sales = df.dropna(subset=["Price", "Quantity"]).copy()print("Rows with valid price and quantity:")print(valid_sales)
```

`dropna(subset=[...])` removes rows missing values in the specified columns. It does not automatically modify the original `df` when used this way.

## 7. Validate and correct data types

Inspect the data types:

```
print(df.dtypes)
```

If a numeric column was imported as text, conversion may be necessary.

```
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
```

- `pd.to_numeric()` converts values to a numeric type where possible.
- `errors="coerce"` converts invalid values to missing values (`NaN`).

Now check the result:

```
print(df[["Price", "Quantity"]].dtypes)print(df[["Price", "Quantity"]].isna().sum())
```

Important: Conversion doesn't validate business rules. A negative price is numeric, but it may still be invalid for this dataset.

## 8. Find invalid prices and quantities

Check for negative values:

```
print("Negative prices:")print(df[df["Price"] < 0])print("\nNegative quantities:")print(df[df["Quantity"] < 0])
```

For this exercise, assume prices must be non-negative and quantities must be positive integers.

Identify invalid rows:

```
invalid_rows = df[    (df["Price"] < 0)    | (df["Quantity"] <= 0)    | (df["Quantity"] % 1 != 0)]print(invalid_rows)
```

Don't silently replace an invalid price with zero. In a real project, investigate the source or flag the row for correction. For this exercise, we'll exclude invalid records from the clean sales analysis and preserve them in a separate report.

## 9. Complete data-cleaning script

Replace the contents of `lesson06_cleaning.py` with this complete script. It preserves the original loaded DataFrame, cleans text, removes exact duplicate rows, converts numeric columns, and separates valid sales from rows that require review.



```
import pandas as pd

# Load the original dataset.
df = pd.read_csv("messy_sales.csv")

print("=== ORIGINAL DATA ===")
print(df)

print("\n=== ORIGINAL DATA QUALITY ===")
print("Shape:", df.shape)
print("Missing values:")
print(df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())

# 1. Standardize text columns.
text_columns = ["Product", "Category", "Status"]

for column in text_columns:
    df[column] = df[column].str.strip()

df["Product"] = df["Product"].str.title()
df["Category"] = df["Category"].str.title()
df["Status"] = df["Status"].str.title()

# 2. Remove exact duplicate records.
df = df.drop_duplicates().copy()

# 3. Convert numeric columns.
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

# 4. Identify invalid prices and quantities.
invalid_mask = (
    (df["Price"] < 0)
    | (df["Quantity"] <= 0)
    | (df["Quantity"] % 1 != 0)
)

invalid_rows = df[invalid_mask].copy()

# 5. Separate rows missing required sales values.
missing_sales_mask = df[["Price", "Quantity"]].isna().any(axis=1)
missing_sales_rows = df[missing_sales_mask].copy()

# 6. Keep rows that have complete, valid sales values.
valid_mask = (
    df["Price"].notna()
    & df["Quantity"].notna()
    & (df["Price"] >= 0)
    & (df["Quantity"] > 0)
    & (df["Quantity"] % 1 == 0)
)

clean_df = df[valid_mask].copy()

# 7. Calculate revenue only for valid rows.
clean_df["Revenue"] = clean_df["Price"] * clean_df["Quantity"]

# 8. Display the cleaning results.
print("\n=== CLEAN DATA ===")
print(clean_df)

print("\n=== REVENUE BY ORDER ===")
print(clean_df[["OrderID", "Product", "Price", "Quantity", "Revenue"]])

print("\n=== TOTAL REVENUE ===")
print(clean_df["Revenue"].sum())

print("\n=== ROWS REQUIRING REVIEW ===")
print(pd.concat([missing_sales_rows, invalid_rows]).drop_duplicates())

print("\n=== CLEANING SUMMARY ===")
print("Rows after removing exact duplicates:", len(df))
print("Rows retained for valid sales analysis:", len(clean_df))
print("Rows with missing price or quantity:", len(missing_sales_rows))
print("Rows with invalid price or quantity:", len(invalid_rows))

# 9. Export results for further analysis.
clean_df.to_csv("clean_sales.csv", index=False)
pd.concat([missing_sales_rows, invalid_rows]).drop_duplicates().to_csv(
    "sales_requiring_review.csv",
    index=False,
)

print("\nSaved clean_sales.csv")
print("Saved sales_requiring_review.csv")
```

Run the script:

```
python lesson06_cleaning.py
```

It produces two files:

- `clean_sales.csv` — rows that meet the stated validation rules.
- `sales_requiring_review.csv` — rows with missing required values or invalid prices/quantities.

A row with both missing and invalid fields may appear in both intermediate groups, but `drop_duplicates()` prevents it from being repeated in the review export when the row is otherwise identical.

## 10. Homework

Create `homework.py` and use the following dataset:

```
import pandas as pddf = pd.DataFrame({    "OrderID": [301, 302, 303, 303, 304, 305],    "Product": [" laptop ", "MOUSE", "Keyboard", "Keyboard", "Monitor", "Webcam"],    "Price": [55000, 500, 1200, 1200, None, -100],    "Quantity": [1, 4, 2, 2, 1, 2],    "Status": [" completed ", "Pending", "Completed", "Completed", "PENDING", "Completed"],})
```

Complete these tasks:

1. Print the original data and its missing-value counts.
2. Remove leading and trailing whitespace from text columns.
3. Standardize product names and status values.
4. Remove exact duplicate rows.
5. Convert `Price` and `Quantity` to numeric types.
6. Identify rows with missing prices.
7. Identify rows with negative prices.
8. Create a DataFrame containing only valid sales rows.
9. Calculate revenue for each valid row.
10. Save the valid records to `homework_clean.csv`.

Before considering the homework complete, explain why replacing a missing price with zero may produce a misleading revenue report.

## 11. Common mistakes

- Dropping all rows with missing values: this may discard useful information from columns unrelated to the calculation.
- Replacing every missing value with zero: zero has a specific meaning and should not be used as a universal substitute.
- Removing duplicates without checking: repeated IDs are not always duplicate transactions.
- Treating numeric conversion as validation: a negative price can be numeric but invalid.
- Overwriting the original dataset: preserve the raw data so cleaning decisions can be reviewed.
- Calculating revenue before validating inputs: missing or invalid prices and quantities can make results unreliable.

## 12. Completion checklist

- Inspected the original dataset.
- Standardized text columns.
- Removed exact duplicate rows.
- Identified missing values.
- Converted numeric columns.
- Identified invalid prices and quantities.
- Separated valid sales from records requiring review.
- Calculated revenue for valid rows.
- Exported the cleaned dataset and review records.
- Completed the homework and committed the files to GitHub.

## 13. Next lesson

Lesson 07 — Pandas Filtering, Sorting and Grouping

You'll learn to filter records with multiple conditions, sort data, group products or categories, and generate useful sales summaries using `groupby()`.