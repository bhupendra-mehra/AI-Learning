# Part 7 — Lesson 05: Reading CSV and Inspecting Data

Path: `python/07-data-science-foundation/lessons/05-pandas-csv-inspection/README.md`

In this lesson, you'll learn how to load a CSV file into Pandas, inspect its structure, identify missing values, check data types, and perform initial data-quality checks. These are essential skills before analyzing real-world datasets.

## 1. Learning objectives

By the end of this lesson, you will be able to:

- Read CSV files using `pd.read_csv()`.
- Inspect rows, columns, and data types.
- Understand the difference between missing values and duplicate records.
- Identify missing values using `isna()` and `isnull()`.
- Count duplicate rows using `duplicated()`.
- Inspect unique values and value frequencies.
- Read CSV files with common formatting issues.
- Perform an initial data-quality assessment.

## 2. Prerequisites and setup

You should have completed Lesson 04 — Pandas Introduction, Series and DataFrames.

From your repository, activate the existing Part 7 virtual environment:

```
cd /var/www/html/AI-Learning/python/07-data-science-foundation
source .venv/bin/activate
```

Verify Pandas is available:

```
python -c "import pandas as pd; print(pd.__version__)"
```

Create the lesson directory:

```
mkdir -p lessons/05-pandas-csv-inspection
```

## 3. What is a CSV file?

CSV stands for Comma-Separated Values. It stores tabular data as text, usually with one record per line and commas separating fields.

Example `sales.csv`:

```
OrderID,Product,Price,Quantity
101,Laptop,55000,1
102,Mouse,500,4
103,Keyboard,1200,2
104,Monitor,8500,1
```

CSV files are commonly used for sales reports, exports from databases, spreadsheets, and data analysis projects.

## 4. Read a CSV file with Pandas

Create a file named `sales.csv` inside the lesson directory using the example above.

Now create `lesson05_csv.py`:

```
import pandas as pddf = pd.read_csv("sales.csv")print(df)
```

Run it from the lesson directory:

```
cd lessons/05-pandas-csv-inspection
python lesson05_csv.py
```

Expected output:

```
   OrderID   Product  Price  Quantity
0      101    Laptop  55000         1
1      102     Mouse    500         4
2      103  Keyboard   1200         2
3      104   Monitor   8500         1
```

Important: `pd.read_csv("sales.csv")` looks for the file relative to your current working directory, not necessarily the Python script's location. Run the command from the lesson directory as shown above.

## 5. Inspect the dataset

When you receive a new dataset, don't start calculations immediately. First inspect its structure.

```
import pandas as pddf = pd.read_csv("sales.csv")print("First five rows:")print(df.head())print("\nLast five rows:")print(df.tail())print("\nDataset shape:")print(df.shape)print("\nColumn names:")print(df.columns.tolist())print("\nData types:")print(df.dtypes)print("\nDataset information:")df.info()print("\nNumerical summary:")print(df.describe())
```

### Common inspection methods

| Method or property | Actual use                                                                 |
| ------------------ | -------------------------------------------------------------------------- |
| `df.head(3)`       | Displays the first three rows.                                             |
| `df.tail(3)`       | Displays the last three rows.                                              |
| `df.shape`         | Returns `(number_of_rows, number_of_columns)`.                             |
| `df.columns`       | Lists the column labels.                                                   |
| `df.dtypes`        | Shows each column's data type.                                             |
| `df.info()`        | Shows non-null counts, data types, and memory information.                 |
| `df.describe()`    | Summarizes numerical columns.                                              |
| `df.sample(2)`     | Displays two randomly selected rows, when at least two rows are available. |

## 6. Check missing values

Real datasets may have missing prices, quantities, product names, or other fields.

Create a file called `messy_sales.csv`:

```
OrderID,Product,Price,Quantity
101,Laptop,55000,1
102,Mouse,500,4
103,,1200,2
104,Monitor,,1
105,Keyboard,1200,
```

Load and inspect it:

```
import pandas as pddf = pd.read_csv("messy_sales.csv")print(df)print("\nMissing values by column:")print(df.isna().sum())print("\nTotal missing values:")print(df.isna().sum().sum())
```

Expected missing-value counts:

```
OrderID     0
Product     1
Price       1
Quantity    1
```

The total number of missing values is `3`.

### Useful missing-value methods

| Method                  | Actual use                                        |
| ----------------------- | ------------------------------------------------- |
| `df.isna()`             | Returns `True` for missing values.                |
| `df.isnull()`           | An equivalent alias for `isna()`.                 |
| `df.isna().sum()`       | Counts missing values in each column.             |
| `df.isna().sum().sum()` | Counts missing values across the whole DataFrame. |
| `df.notna()`            | Returns `True` for values that are not missing.   |

At this stage, identify missing values; don't automatically delete them. In later data-cleaning lessons, you'll learn when to fill, remove, or otherwise handle missing data.

## 7. Check duplicate records

A duplicate record is a row that repeats another row. Duplicates can cause incorrect totals if they represent accidental repeated transactions.

```
import pandas as pddf = pd.DataFrame({    "OrderID": [101, 102, 102, 103],    "Product": ["Laptop", "Mouse", "Mouse", "Keyboard"],    "Price": [55000, 500, 500, 1200],})print("Duplicate row flags:")print(df.duplicated())print("\nNumber of duplicate rows:")print(df.duplicated().sum())
```

Expected output:

```
0    False
1    False
2     True
3    False
```

There is one fully duplicated row.

Useful methods:

| Method                       | Actual use                                                      |
| ---------------------------- | --------------------------------------------------------------- |
| `df.duplicated()`            | Identifies rows that duplicate earlier rows across all columns. |
| `df.duplicated().sum()`      | Counts fully duplicated rows.                                   |
| `df.drop_duplicates()`       | Returns a DataFrame with duplicate rows removed by default.     |
| `df["OrderID"].duplicated()` | Checks repeated order IDs specifically.                         |
| `df["OrderID"].nunique()`    | Counts distinct non-missing order IDs.                          |

Important: Two orders can have the same product and price without being duplicates. Always decide what defines a duplicate for your business data before removing records.

## 8. Inspect unique values and frequencies

Sometimes a column contains unexpected categories, inconsistent spelling, or invalid values.

```
import pandas as pddf = pd.DataFrame({    "Product": ["Laptop", "Mouse", "Mouse", "Keyboard", "Mouse"],    "Status": ["Completed", "Pending", "Completed", "Pending", "Completed"],})print("Unique products:")print(df["Product"].unique())print("\nNumber of unique products:")print(df["Product"].nunique())print("\nProduct frequencies:")print(df["Product"].value_counts())print("\nOrder status frequencies:")print(df["Status"].value_counts())
```

Actual uses:

- `unique()` shows the distinct values present in a column.
- `nunique()` counts distinct non-missing values by default.
- `value_counts()` counts how often each value occurs.

These methods help you find unexpected labels, inconsistent statuses, and unusual category distributions.

## 9. Read CSV files with common formatting issues

CSV files are not always formatted consistently. Pandas provides options for handling common cases.

### 9.1 Read a file with a different separator

Some files use semicolons instead of commas.

Example `regional_sales.csv`:

```
OrderID;Product;Price
101;Laptop;55000
102;Mouse;500
```

Read it with:

```
df = pd.read_csv("regional_sales.csv", sep=";")print(df)
```

Use the `sep` parameter to specify the delimiter.

### 9.2 Read only selected columns

For a large dataset, you may need only a few columns.

```
df = pd.read_csv(    "sales.csv",    usecols=["OrderID", "Product", "Price"],)print(df)
```

This reads only the specified columns.

### 9.3 Read only a limited number of rows

```
df = pd.read_csv("sales.csv", nrows=2)print(df)
```

This reads the first two data rows, which is useful when quickly testing a large file.

### 9.4 Handle spaces in column names

A CSV may contain headers such as `" Product "` or `" Price "`.

```
df = pd.read_csv("sales.csv")df.columns = df.columns.str.strip()print(df.columns.tolist())
```

This removes leading and trailing whitespace from column labels.

### 9.5 Specify an identifier column's data type

Identifiers such as order numbers or postal codes may need to remain strings rather than numbers.

```
df = pd.read_csv(    "sales.csv",    dtype={"OrderID": "string"},)print(df.dtypes)
```

Use a string type when you need to preserve identifiers as text, especially when leading zeros matter.

## 10. Build a data-quality report

Let's combine the main inspection methods into one reusable report.

Create `data_quality_report.py`:

```
import pandas as pddf = pd.read_csv("messy_sales.csv")print("=== DATASET OVERVIEW ===")print("Rows:", df.shape[0])print("Columns:", df.shape[1])print("Column names:", df.columns.tolist())print("\n=== DATA TYPES ===")print(df.dtypes)print("\n=== MISSING VALUES ===")print(df.isna().sum())print("Total missing values:", df.isna().sum().sum())print("\n=== DUPLICATE ROWS ===")print("Duplicate rows:", df.duplicated().sum())print("\n=== UNIQUE VALUES ===")for column in df.columns:    print(f"{column}: {df[column].nunique()} unique values")print("\n=== NUMERICAL SUMMARY ===")print(df.describe())
```

Run this script from the directory containing `messy_sales.csv`:

```
python data_quality_report.py
```

This report doesn't clean or change the data. It helps you understand the dataset before deciding what to do next.

## 11. Complete practical exercise

Create this file:

`lessons/05-pandas-csv-inspection/lesson05_csv.py`

Use the following complete code:



```
import pandas as pd

# Load the sales dataset.
df = pd.read_csv("sales.csv")

# 1. Display the dataset.
print("=== SALES DATA ===")
print(df)

# 2. Inspect the dataset.
print("\n=== FIRST THREE ROWS ===")
print(df.head(3))

print("\n=== SHAPE ===")
print(df.shape)

print("\n=== COLUMNS ===")
print(df.columns.tolist())

print("\n=== DATA TYPES ===")
print(df.dtypes)

# 3. Check missing values.
print("\n=== MISSING VALUES ===")
print(df.isna().sum())

# 4. Check duplicate rows.
print("\n=== DUPLICATES ===")
print("Duplicate rows:", df.duplicated().sum())

# 5. Inspect distinct products.
print("\n=== UNIQUE PRODUCTS ===")
print(df["Product"].unique())

print("\n=== PRODUCT COUNTS ===")
print(df["Product"].value_counts())

# 6. Calculate revenue after inspection.
df["Revenue"] = df["Price"] * df["Quantity"]

print("\n=== REVENUE BY ORDER ===")
print(df[["OrderID", "Product", "Revenue"]])

print("\n=== TOTAL REVENUE ===")
print(df["Revenue"].sum())
```



Use the `sales.csv` file from Section 4. Run the script:

```
python lesson05_csv.py
```

Expected results for this dataset:

- Shape before adding `Revenue`: `(4, 4)`
- Missing values: `0` in each column
- Duplicate rows: `0`
- Total revenue: `64900`

## 12. Homework

Create `homework.py` inside the same lesson directory.

First create a file called `homework_sales.csv`:

```
OrderID,Product,Category,Price,Quantity,Status
201,Laptop,Electronics,55000,1,Completed
202,Mouse,Accessories,500,4,Completed
203,Keyboard,Accessories,1200,2,Pending
204,Monitor,Electronics,8500,1,Completed
205,Mouse,Accessories,500,3,Pending
206,Laptop,Electronics,55000,1,Completed
207,Webcam,Accessories,,2,Pending
208,Headphones,Accessories,2500,,Completed
```

Complete these tasks:

1. Load the CSV file into a DataFrame.
2. Display the first four rows and the last two rows.
3. Print the dataset shape, column names, and data types.
4. Count missing values in each column and across the entire dataset.
5. Count fully duplicated rows.
6. Display all unique products and count the distinct products.
7. Display the frequency of each product.
8. Read the same file again, but load only the `OrderID`, `Product`, and `Price` columns.
9. Read only the first three data rows.
10. Create a data-quality report containing the row count, column count, missing-value counts, duplicate count, and numerical summary.
11. Explain why you should inspect missing values before calculating revenue.

Expected checks: The dataset has 8 rows and 6 columns. There are 2 missing values in total, both in different columns. The dataset contains no fully duplicated rows.

## 13. Common mistakes

### File not found

Error:

```
FileNotFoundError: [Errno 2] No such file or directory: 'sales.csv'
```

Check your current directory and confirm the file exists there:

```
pwd
ls
```

If the file is elsewhere, provide its correct relative or absolute path.

### Treating missing values as zero without checking

A missing price is not necessarily a price of zero. Replacing missing data with zero can distort business calculations.

### Assuming repeated values mean duplicate rows

Several orders can contain the same product. A duplicate check across all columns is different from checking whether one column contains repeated values.

### Forgetting to assign the result of a DataFrame operation

For example:

```
df.drop_duplicates()
```

returns a DataFrame without duplicates, but does not normally modify `df` in place. To keep the result, assign it:

```
df = df.drop_duplicates()
```

Only do this after confirming that removing those rows is appropriate.

### Ignoring data types

An identifier may be stored as an integer, while prices should generally be numeric. Check `df.dtypes` before calculations or transformations.

## 14. Completion checklist

- Read a CSV file using `pd.read_csv()`.
- Inspected rows, shape, columns, and data types.
- Used `info()` and `describe()`.
- Counted missing values.
- Checked duplicate rows.
- Inspected unique values and frequencies.
- Used `sep`, `usecols`, and `nrows`.
- Built the data-quality report.
- Completed the homework.
- Committed the lesson code and documentation to GitHub.

## 15. Next lesson

Lesson 06 — Data Cleaning with Pandas

You'll learn how to handle missing values, remove duplicates when appropriate, standardize text, correct data types, and prepare a dataset for reliable analysis.

## 16. How to organize and run Lesson 05

Your lesson folder should look like this:

```
05-pandas-csv-inspection/
├── README.md
├── sales.csv
├── messy_sales.csv
├── regional_sales.csv
├── homework_sales.csv
├── lesson05_csv.py
├── data_quality_report.py
└── homework.py
```

You don't need to create every file immediately. Start with `README.md`, `sales.csv`, and `lesson05_csv.py`, then work through the sections in order.

After completing the exercises, update the checklist in your README based on what you've actually completed.

Key takeaway: Before analyzing a dataset, first understand its structure, data types, missing values, duplicates, and unique values. This makes your later calculations and conclusions more reliable.