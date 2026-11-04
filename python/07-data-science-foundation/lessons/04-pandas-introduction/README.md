# Lesson 04 — Pandas Introduction, Series and DataFrames

## 1. Learning Objectives

By completing this lesson, I will be able to:

- Explain what Pandas is and how it complements NumPy.
- Create a Pandas Series from Python data.
- Create a DataFrame from dictionaries and lists.
- Understand indexes, columns, and data types.
- Select individual columns and rows.
- Inspect DataFrames using common Pandas properties and methods.
- Calculate basic statistics from sales data.
- Export a DataFrame to a CSV file.

## 2. Prerequisites

- Python lists, dictionaries, and functions.
- Lesson 01: NumPy Introduction and Arrays.
- Lesson 02: Array Indexing, Slicing and Shapes.
- Lesson 03: Vectorized Operations, Statistics and Broadcasting.
- Pandas installed in the Part 7 virtual environment.

## 3. What Is Pandas?

Pandas is a Python library used to manipulate and analyze structured data.

It is especially useful for working with:

- CSV files and spreadsheets.
- Product catalogs and order records.
- Sales reports and business metrics.
- Tabular data containing different data types.
- Missing values and inconsistent records.

NumPy is primarily focused on numerical arrays. Pandas provides labeled data structures and convenient operations for working with rows and columns.

### Example

Imagine an e-commerce store with the following data:

| Product  | Price | Quantity |
| -------- | ----: | -------: |
| Keyboard |  1200 |        5 |
| Mouse    |   500 |       10 |
| Monitor  |  8500 |        2 |

Pandas lets us represent this as a table and calculate revenue, filter products, and summarize sales.

## 4. Import Pandas

The conventional import alias is `pd`.

```python
import pandas as pd

print(pd.__version__)
```

The `pd` alias is widely used in Python data analysis projects.

## 5. What Is a Series?

A Series is a one-dimensional labeled array that can hold values of a particular or mixed data type.

### 5.1 Create a Series from a list

```python
import pandas as pd

sales = pd.Series([1200, 1500, 900, 1800])

print(sales)
```

Output:

```text
0    1200
1    1500
2     900
3    1800
dtype: int64
```

By default, Pandas assigns an integer index starting at zero.

### 5.2 Access Series elements

```python
sales = pd.Series([1200, 1500, 900, 1800])

print(sales.iloc[0])
print(sales.iloc[2])
```

Output:

```text
1200
900
```

`.iloc` selects elements by their integer position.

### 5.3 Create a Series with custom labels

```python
monthly_sales = pd.Series(
    [1200, 1500, 1800],
    index=["January", "February", "March"],
)

print(monthly_sales)
```

Output:

```text
January     1200
February    1500
March       1800
dtype: int64
```

Access a value using its label:

```python
print(monthly_sales.loc["February"])
```

Output:

```text
1500
```

Use `.loc` for label-based selection and `.iloc` for position-based selection.

## 6. What Is a DataFrame?

A DataFrame is a two-dimensional labeled data structure with rows and columns.

It is similar to a spreadsheet table or a database query result.

### 6.1 Create a DataFrame from a dictionary

```python
import pandas as pd

products = {
    "Product": ["Keyboard", "Mouse", "Monitor"],
    "Price": [1200, 500, 8500],
    "Quantity": [5, 10, 2],
}

df = pd.DataFrame(products)

print(df)
```

Output:

```text
    Product  Price  Quantity
0  Keyboard   1200         5
1     Mouse    500        10
2   Monitor   8500         2
```

Each dictionary key becomes a column name.

Each list provides the values for that column.

### 6.2 Understand the DataFrame structure

```python
print("Shape:", df.shape)
print("Rows:", len(df))
print("Columns:", df.columns.tolist())
print("Index:", df.index)
print("Data types:")
print(df.dtypes)
```

Expected key results:

```text
Shape: (3, 3)
Rows: 3
Columns: ['Product', 'Price', 'Quantity']
```

The exact index and data-type representations may vary slightly by Pandas version and input data.

| Property     | Actual use                                                      |
| ------------ | --------------------------------------------------------------- |
| `df.shape`   | Returns the number of rows and columns.                         |
| `df.columns` | Returns column labels.                                          |
| `df.index`   | Returns row labels.                                             |
| `df.dtypes`  | Shows the data type of each column.                             |
| `df.size`    | Returns the total number of values across all columns and rows. |

## 7. Create DataFrames from Other Data Structures

### 7.1 From a list of dictionaries

```python
import pandas as pd

orders = [
    {"OrderID": 101, "Product": "Keyboard", "Amount": 1200},
    {"OrderID": 102, "Product": "Mouse", "Amount": 500},
    {"OrderID": 103, "Product": "Monitor", "Amount": 8500},
]

df = pd.DataFrame(orders)

print(df)
```

Each dictionary represents one row.

### 7.2 From a list of lists

```python
data = [
    ["Keyboard", 1200],
    ["Mouse", 500],
    ["Monitor", 8500],
]

df = pd.DataFrame(data, columns=["Product", "Price"])

print(df)
```

Output:

```text
    Product  Price
0  Keyboard   1200
1     Mouse    500
2   Monitor   8500
```

Providing column names makes the table easier to understand.

## 8. Selecting Columns

### 8.1 Select one column

```python
print(df["Product"])
```

Selecting one column by its name returns a Series.

### 8.2 Select multiple columns

```python
print(df[["Product", "Price"]])
```

Selecting multiple columns returns a DataFrame.

### 8.3 Calculate a new column

```python
df["Quantity"] = [5, 10, 2]
df["Revenue"] = df["Price"] * df["Quantity"]

print(df)
```

The `Revenue` column is calculated using vectorized operations.

## 9. Selecting Rows

Use `.iloc` to select rows by integer position.

```python
print(df.iloc[0])
print(df.iloc[1])
```

Select multiple rows:

```python
print(df.iloc[0:2])
```

Use `.loc` to select rows by index label.

```python
print(df.loc[0])
```

With a default integer index, `.loc[0]` and `.iloc[0]` both select the first row. With a custom index, they may select different rows.

### Select a particular value

```python
print(df.loc[0, "Product"])
print(df.iloc[0, 1])
```

Both return the product name in the first row for this DataFrame.

## 10. Inspecting DataFrames

Use these methods when working with a new dataset.

```python
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
```

| Method          | Actual use                                                                                          |
| --------------- | --------------------------------------------------------------------------------------------------- |
| `df.head()`     | Shows the first five rows by default.                                                               |
| `df.tail()`     | Shows the last five rows by default.                                                                |
| `df.info()`     | Displays column names, non-null counts, data types, and memory information.                         |
| `df.describe()` | Summarizes numerical columns with count, mean, standard deviation, minimum, quartiles, and maximum. |
| `df.sample()`   | Selects random rows.                                                                                |
| `df.isna()`     | Identifies missing values.                                                                          |
| `df.nunique()`  | Counts distinct values in each column by default.                                                   |

For example:

```python
print(df.head(2))
print(df.describe())
```

Use `df.info()` to inspect a dataset's structure before performing analysis.

## 11. Basic Calculations with Pandas

Create a product DataFrame:

```python
import pandas as pd

df = pd.DataFrame({
    "Product": ["Keyboard", "Mouse", "Monitor"],
    "Price": [1200, 500, 8500],
    "Quantity": [5, 10, 2],
})

df["Revenue"] = df["Price"] * df["Quantity"]

print("Total revenue:", df["Revenue"].sum())
print("Average revenue per product:", df["Revenue"].mean())
print("Maximum revenue:", df["Revenue"].max())
print("Minimum revenue:", df["Revenue"].min())
```

Expected output:

```text
Total revenue: 18500
Average revenue per product: 6166.666666666667
Maximum revenue: 17000
Minimum revenue: 5000
```

The revenue calculation is:

- Keyboard: 1200 × 5 = 6000
- Mouse: 500 × 10 = 5000
- Monitor: 8500 × 2 = 17000

Total revenue: 28000.

**Important:** Check the calculations when reviewing output. The correct total revenue for these three products is **28000**, and the correct average revenue per product is **9333.333333333334**. This is a useful reminder to verify expected results rather than copy them without checking.

## 12. Export a DataFrame to CSV

Pandas can save a DataFrame as a CSV file.

```python
df.to_csv("product_sales.csv", index=False)
```

The `index=False` argument prevents Pandas from writing the DataFrame's index as an additional CSV column.

Read the file back:

```python
loaded_df = pd.read_csv("product_sales.csv")

print(loaded_df)
```

CSV reading and more complete dataset inspection will be covered in Lesson 05.

## 13. Complete Practical Exercise

Create the file:

`lessons/04-pandas-introduction/lesson04_pandas.py`

```python
import pandas as pd

products = {
    "Product": ["Keyboard", "Mouse", "Monitor", "Webcam"],
    "Price": [1200, 500, 8500, 2200],
    "Quantity": [5, 10, 2, 4],
}

df = pd.DataFrame(products)

print("Product data:")
print(df)

print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())

print("\nFirst two rows:")
print(df.head(2))

print("\nData types:")
print(df.dtypes)

df["Revenue"] = df["Price"] * df["Quantity"]

print("\nRevenue by product:")
print(df[["Product", "Revenue"]])

print("\nTotal revenue:", df["Revenue"].sum())
print("Average product revenue:", df["Revenue"].mean())
print("Highest product revenue:", df["Revenue"].max())

print("\nProducts costing more than 1000:")
print(df[df["Price"] > 1000])

df.to_csv("product_sales.csv", index=False)

print("\nSaved product_sales.csv")
```

Run the script:

```bash
python lessons/04-pandas-introduction/lesson04_pandas.py
```

The generated CSV file will be saved in the current working directory.

## 14. Homework

Create a file named `homework.py`.

Use the following dataset:

```python
import pandas as pd

orders = pd.DataFrame({
    "OrderID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse"],
    "Price": [55000, 500, 1200, 8500, 500],
    "Quantity": [1, 4, 2, 1, 3],
})
```

Complete these tasks:

1. Print the complete DataFrame.
2. Print the number of rows and columns.
3. Print the column names and data types.
4. Display the first three rows.
5. Select the `Product` column.
6. Select the `Product` and `Price` columns.
7. Display the second row using `.iloc`.
8. Calculate revenue for each order.
9. Calculate the total revenue.
10. Find the order with the highest revenue.
11. Filter orders where the price is greater than 1,000.
12. Save the DataFrame to `orders.csv` without the index.

## 15. Common Mistakes

### Confusing Series and DataFrame selection

```python
df["Price"]
```

Returns a Series.

```python
df[["Price"]]
```

Returns a DataFrame with one column.

### Using the wrong row-selection method

- `.iloc[0]` selects by integer position.
- `.loc[0]` selects the row whose index label is `0`.

### Forgetting to assign a new column

This calculates a value but does not save it:

```python
df["Price"] * df["Quantity"]
```

To keep the result, use:

```python
df["Revenue"] = df["Price"] * df["Quantity"]
```

### Exporting the index unintentionally

Use:

```python
df.to_csv("output.csv", index=False)
```

when the DataFrame's index is not intended to be a separate CSV column.

### Assuming all columns contain numbers

Product names are text, while price and quantity are numerical. Inspect data types with `df.dtypes` before performing calculations.

## 16. Completion Checklist

- [x] Installed and imported Pandas.
- [x] Created a Series.
- [x] Created DataFrames from dictionaries and lists.
- [x] Understood indexes, columns, shapes, and data types.
- [x] Selected rows and columns.
- [x] Used `head()`, `tail()`, `info()`, and `describe()`.
- [x] Calculated revenue and basic statistics.
- [x] Exported a DataFrame to CSV.
- [x] Completed the practical exercise.
- [x] Completed the homework.
- [x] Committed the lesson code and documentation to GitHub.

## 17. Next Lesson

**Lesson 05 — Reading CSV and Inspecting Data**

Topics include loading CSV files, inspecting real datasets, understanding column types, examining missing values, and preparing data for analysis.
