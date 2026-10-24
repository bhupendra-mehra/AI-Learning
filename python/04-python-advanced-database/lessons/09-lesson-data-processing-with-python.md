# Lesson 09 — Data Processing with Python

Practical project

Python + SQLAlchemy + MySQL + Pandas

Project: `advanced-python-database/ecommerce-db`

In this lesson, we'll use your e-commerce database to learn how to extract data, transform it, analyze it, clean it, and export it into useful formats. We'll finish with a small ETL pipeline similar to the kind used in real data engineering projects.

## What you'll learn

### 01

Read database data

Query MySQL using SQLAlchemy

### 02

Transform data

Clean and reshape product records

### 03

Aggregation

Calculate counts, totals and averages

### 04

CSV and JSON

Export data for other tools

### 05

Pandas fundamentals

Use DataFrames for analysis

### 06

Data cleaning

Handle missing values and duplicates

### 07

Build a mini ETL pipeline

Extract → Transform → Load

## Step 0 — Prepare your local environment

Use your local WSL development environment, not the live GCP VM.

```
cd /var/www/html/advanced-python-database/ecommerce-db
```

Activate your existing virtual environment, then check:

```
python --version
python -m pytest -v
ruff check .
```

Install the data-processing libraries in that environment:

```
python -m pip install pandas
```

If you want to record this dependency for the project, add `pandas` to `requirements.txt` only if the application or project scripts will actually use it. Otherwise, you can keep it in a separate data-processing dependency file.

### Create a workspace

From the `ecommerce-db` project root:

```
mkdir -p scripts/data
```

We'll put the lesson scripts under `scripts/` and generated CSV/JSON files under `scripts/data/`. Keep generated exports out of Git if they contain real customer or order data.

## 1. Reading database data with SQLAlchemy

Your application already uses Flask and SQLAlchemy, so we'll use SQLAlchemy to read records from the database rather than connecting with a separate database driver.

### Example: Read products

Create `scripts/read_products.py`:

```
from sqlalchemy import select# Adjust this import to your project's existing database setup.from app import dbfrom app.models import Productdef main():    stmt = select(Product.id, Product.name, Product.price).limit(10)    with db.engine.connect() as connection:        rows = connection.execute(stmt).mappings().all()    for row in rows:        print(dict(row))if __name__ == "__main__":    main()
```

Important: The imports depend on how your application initializes Flask, SQLAlchemy, and models. This is a teaching template, not a guaranteed drop-in script. If your project uses an application factory, initialize the Flask app and execute database operations within its application context. Also check your actual model module and column names.

For a Flask application factory, the general pattern is:

```
from app.web import create_appfrom app import dbapp = create_app()with app.app_context():    # Execute SQLAlchemy queries here.    ...
```

Use whichever setup matches your current codebase.

### What the query does

```
select(Product.id, Product.name, Product.price).limit(10)
```

- `select(...)` defines the fields to retrieve.
- `.limit(10)` restricts the result to at most 10 rows.
- `connection.execute(...)` runs the query.
- `.mappings().all()` returns rows that can be accessed by column name.

For example, a row might look like:

```
{    "id": 1,    "name": "Wireless Mouse",    "price": 799.0,}
```

Those values are illustrative; your database may contain different records.

### When to read using SQLAlchemy

Use SQLAlchemy when your script needs to query your existing application database, apply filters, join related tables, or reuse your existing connection configuration.

## 2. Transforming data with Python

Transformation means converting raw data into a useful format for analysis or reporting.

Suppose a product record contains a name with extra spaces and a price stored as text. We can normalize the name and convert the price to a number.

Create `scripts/transform_products.py`:

```
def transform_product(product):    """Clean and normalize a product dictionary."""    name = str(product.get("name") or "").strip()    try:        price = float(product["price"])    except (TypeError, ValueError, KeyError):        price = None    return {        "id": product.get("id"),        "name": name,        "price": price,    }sample = {    "id": 1,    "name": "  Wireless Mouse  ",    "price": "799.00",}print(transform_product(sample))
```

Output:

```
{'id': 1, 'name': 'Wireless Mouse', 'price': 799.0}
```

### What happened?

- `.strip()` removes spaces at the beginning and end.
- `float()` converts a numeric string to a number.
- `try/except` handles invalid or missing price values.
- The returned dictionary contains only the fields needed for this task.

Notice that we use `None` for a missing or invalid price rather than silently treating it as zero. A missing price and a free product are not the same thing.

### Where is this useful?

- Standardizing product names.
- Normalizing categories.
- Converting date strings into date objects.
- Preparing order records for reporting.
- Removing unwanted fields before exporting data.

## 3. Aggregation — turn rows into useful information

Aggregation summarizes many records into fewer results.

For an e-commerce business, useful questions include:

- How many products are available?
- What is the average product price?
- How many products belong to each category?
- What is the total value of completed orders?

### Option A: Aggregate inside MySQL

Use SQL when the database can perform the calculation efficiently.

```
SELECT
    COUNT(*) AS product_count,
    AVG(price) AS average_price,
    MIN(price) AS lowest_price,
    MAX(price) AS highest_price
FROM products;
```

For category-level counts:

```
SELECT
    category_id,
    COUNT(*) AS product_count
FROM products
GROUP BY category_id
ORDER BY product_count DESC;
```

`GROUP BY` combines rows with the same category ID. `COUNT(*)` counts the rows in each group.

### Option B: Aggregate in Python

If you've already loaded a small set of product dictionaries:

```
products = [    {"name": "Mouse", "price": 799.0},    {"name": "Keyboard", "price": 1499.0},    {"name": "USB Cable", "price": 199.0},]prices = [    product["price"]    for product in products    if product["price"] is not None]if prices:    print("Product count:", len(prices))    print("Average price:", sum(prices) / len(prices))    print("Total price:", sum(prices))
```

Output:

```
Product count: 3
Average price: 832.3333333333334
Total price: 2497.0
```

These numbers are based on the sample records, not your actual database.

### Which approach should you use?

| SQL aggregation                  | Python aggregation                      |
| -------------------------------- | --------------------------------------- |
| Best for large database datasets | Useful when data is already loaded      |
| Transfers fewer rows to Python   | Gives you flexible Python processing    |
| Uses database query capabilities | Can use Python libraries such as pandas |

Rule of thumb: If the database can calculate a count, sum, or average without sending every row to Python, prefer SQL for large datasets.

### Example: Order totals

An order total can be calculated from order-item quantities and prices, depending on how your application stores prices:

```
SELECT
    order_id,
    SUM(quantity * price) AS order_total
FROM order_items
GROUP BY order_id;
```

This assumes the `order_items` table has `order_id`, `quantity`, and `price` columns. Verify your actual schema before running the query. If the stored price field has a different name, adjust it accordingly.

## 4. Export data to CSV and JSON

Data exports allow your application data to be used by spreadsheets, analytics tools, APIs, and other systems.

We'll use sample product data first so you can practice without exporting real customer information.

Create `scripts/export_products.py`:

```
import csvimport jsonfrom pathlib import Pathproducts = [    {"id": 1, "name": "Wireless Mouse", "price": 799.0},    {"id": 2, "name": "Keyboard", "price": 1499.0},    {"id": 3, "name": "USB Cable", "price": 199.0},]output_dir = Path("scripts/data")output_dir.mkdir(parents=True, exist_ok=True)# CSV exportcsv_path = output_dir / "products.csv"with csv_path.open("w", newline="", encoding="utf-8") as file:    writer = csv.DictWriter(        file,        fieldnames=["id", "name", "price"],    )    writer.writeheader()    writer.writerows(products)# JSON exportjson_path = output_dir / "products.json"with json_path.open("w", encoding="utf-8") as file:    json.dump(products, file, indent=2, ensure_ascii=False)print(f"CSV saved to {csv_path}")print(f"JSON saved to {json_path}")
```

Run:

```
python scripts/export_products.py
```

### CSV output

`products.csv`:

```
id,name,price
1,Wireless Mouse,799.0
2,Keyboard,1499.0
3,USB Cable,199.0
```

CSV is convenient for Excel and many data tools. It represents rows and columns, but it does not preserve rich nested structures.

### JSON output

`products.json`:

```
[
  {
    "id": 1,
    "name": "Wireless Mouse",
    "price": 799.0
  },
  {
    "id": 2,
    "name": "Keyboard",
    "price": 1499.0
  },
  {
    "id": 3,
    "name": "USB Cable",
    "price": 199.0
  }
]
```

JSON supports nested objects and arrays, making it useful for APIs and exchanging structured data.

### When to use each format

- CSV: tabular reports, spreadsheet analysis, bulk imports.
- JSON: API responses, nested records, structured data exchange.

For financial data, remember that Python `float` can introduce precision issues. For real monetary calculations, use appropriate decimal handling and your application's existing money conventions.

## 5. Pandas fundamentals

Pandas is a Python library for working with tabular data. Its main data structure is a DataFrame, similar to a spreadsheet table.

You can load data from a database query or a CSV file, clean it, group it, and export the results.

### Step 5.1 — Create a DataFrame

Create `scripts/pandas_basics.py`:

```
import pandas as pdproducts = [    {"id": 1, "name": "Mouse", "category": "Accessories", "price": 799},    {"id": 2, "name": "Keyboard", "category": "Accessories", "price": 1499},    {"id": 3, "name": "USB Cable", "category": "Accessories", "price": 199},    {"id": 4, "name": "Monitor", "category": "Electronics", "price": 8999},]df = pd.DataFrame(products)print(df)print("\nFirst two rows:")print(df.head(2))print("\nColumn names:")print(df.columns.tolist())print("\nData types:")print(df.dtypes)
```

Run:

```
python scripts/pandas_basics.py
```

### Step 5.2 — Filter rows

Get products priced above ₹1,000:

```
expensive_products = df[df["price"] > 1000]print(expensive_products)
```

Select specific columns:

```
print(df[["name", "price"]])
```

Sort by price:

```
print(df.sort_values("price", ascending=False))
```

These operations are useful when preparing product reports or identifying expensive and inexpensive items.

### Step 5.3 — Aggregate with pandas

```
print("Average price:", df["price"].mean())print("Total product count:", df["id"].count())category_summary = (    df.groupby("category")    .agg(        product_count=("id", "count"),        average_price=("price", "mean"),    )    .reset_index())print(category_summary)
```

This groups products by category and calculates a count and average price for each category.

### Step 5.4 — Read data from SQLAlchemy

You can pass the result of a database query into a DataFrame.

Conceptually:

```
import pandas as pdfrom sqlalchemy import textwith engine.connect() as connection:    df = pd.read_sql(        text("""            SELECT id, name, price            FROM products            ORDER BY id            LIMIT 1000        """),        connection,    )print(df.head())
```

Here, `engine` must be your project's existing configured SQLAlchemy engine. Don't create another engine with hardcoded credentials. For large tables, extract data in batches or aggregate inside MySQL rather than loading the entire database into memory.

## 6. Data cleaning — prepare reliable data

Real datasets often contain missing values, duplicate records, inconsistent text, and invalid numbers.

Data cleaning helps make the resulting report trustworthy.

### Step 6.1 — Create deliberately messy data

Create `scripts/data_cleaning.py`:

```
import pandas as pddf = pd.DataFrame(    [        {"id": 1, "name": " Mouse ", "price": "799"},        {"id": 2, "name": "Keyboard", "price": "1499"},        {"id": 3, "name": "mouse", "price": "799"},        {"id": 4, "name": "USB Cable", "price": None},        {"id": 4, "name": "USB Cable", "price": None},        {"id": 5, "name": "Monitor", "price": "invalid"},    ])print("Original data:")print(df)print("\nMissing values:")print(df.isna().sum())
```

This dataset includes whitespace, inconsistent capitalization, missing values, duplicate rows, and an invalid price.

### Step 6.2 — Normalize text

```
df["name"] = df["name"].astype("string").str.strip()df["name"] = df["name"].str.title()
```

This removes surrounding whitespace and normalizes capitalization. Title casing is only an example; product names with brand-specific capitalization may need custom rules.

### Step 6.3 — Convert numeric values safely

```
df["price"] = pd.to_numeric(df["price"], errors="coerce")
```

`errors="coerce"` converts invalid values to missing values (`NaN`) rather than stopping the script with a conversion error.

Inspect the result:

```
print(df.dtypes)print(df[df["price"].isna()])
```

### Step 6.4 — Remove duplicates

```
df = df.drop_duplicates()
```

This removes identical rows. If you need to enforce unique product IDs, you may instead use:

```
df = df.drop_duplicates(subset=["id"], keep="first")
```

Choose the rule carefully. If duplicate IDs have conflicting data, inspect and resolve those conflicts instead of automatically discarding records.

### Step 6.5 — Decide how to handle missing values

To exclude records without a valid price from a price report:

```
valid_prices = df.dropna(subset=["price"])
```

To fill missing prices with zero:

```
# Usually inappropriate for product prices.df["price"] = df["price"].fillna(0)
```

The second example is technically valid, but a missing price should not normally be interpreted as a free product. In most cases, flag missing prices for review or exclude those records from price calculations.

### Step 6.6 — Validate the final data

```
assert df["id"].notna().all()assert (df["price"].dropna() >= 0).all()print(df)
```

Assertions should reflect your actual business rules. If your dataset legitimately contains records without IDs or if negative prices have a specific meaning, adjust the checks.

Checkpoint: You can identify data-quality issues, normalize values, convert types, remove duplicates carefully, and validate the cleaned output.

## 7. ETL — build a complete data-processing pipeline

ETL stands for:

- E — Extract: Read data from a source, such as MySQL.
- T — Transform: Clean, validate, filter, or aggregate the data.
- L — Load: Save the results to a destination, such as CSV, JSON, another database, or a data warehouse.

Let's build a small ETL pipeline for product reporting.

Extract

Read products from MySQL

Transform

Clean names, convert prices, validate rows

Load

Export cleaned products and a category summary

Below is the complete ETL script for your existing `ecommerce-db` project. It reuses the SQLAlchemy `engine` defined in `app/database/database.py`, reads product data from MySQL, cleans it with pandas, and exports three files.

## 1. Create the script

From your project directory:

```
cd /var/www/html/advanced-python-database/ecommerce-db
mkdir -p scripts
touch scripts/__init__.py
nano scripts/product_etl.py
```

Paste the complete code below into `scripts/product_etl.py`.

```
from pathlib import Pathimport pandas as pdfrom sqlalchemy import textfrom app.database.database import engine# Output directory relative to the project root.OUTPUT_DIR = Path("scripts/data")def extract_products(db_engine):    """Extract product records from the MySQL database."""    query = text("""        SELECT id, name, category_id, price        FROM products        ORDER BY id    """)    with db_engine.connect() as connection:        df = pd.read_sql(query, connection)    return dfdef transform_products(df):    """Clean product data and flag invalid prices."""    df = df.copy()    # Clean product names.    df["name"] = df["name"].astype("string").str.strip()    # Convert prices to numeric values; invalid values become NaN.    df["price"] = pd.to_numeric(df["price"], errors="coerce")
```

## 2. Install required packages

Activate your virtual environment if it isn't already active:

```
source .venv/bin/activate
```

Check the dependencies:

```
python -m pip show pandas sqlalchemy mysql-connector-python python-dotenv
```

If any are missing, install them:

```
python -m pip install pandas sqlalchemy mysql-connector-python python-dotenv
```

Your existing `app/database/database.py` uses these packages to configure the MySQL connection. Keep your existing `.env` configuration; don't put database passwords in this script.

## 3. Run the ETL script

Make sure you're in the `ecommerce-db` project root:

```
cd /var/www/html/advanced-python-database/ecommerce-db
python -m scripts.product_etl
```

Expected output will look similar to this; the counts will depend on your database:

```
Starting product ETL...
Extracted rows: 100
Transformed rows: 98
Products flagged with invalid prices: 2
Category summary rows: 5
Output directory: /var/www/html/advanced-python-database/ecommerce-db/scripts/data
ETL completed successfully.
```

## 4. Verify the generated files

```
ls -lh scripts/data/
```

You should see these files:

| File                    | Purpose                                               |
| ----------------------- | ----------------------------------------------------- |
| `cleaned_products.csv`  | Cleaned product records for spreadsheets and analysis |
| `cleaned_products.json` | Cleaned product records in JSON format                |
| `category_summary.csv`  | Product count and average valid price per category    |

To preview the CSV:

```
head scripts/data/cleaned_products.csv
```

To preview the category summary:

```
cat scripts/data/category_summary.csv
```

## 5. Important notes

- Database safety: This script only executes a `SELECT` query. It doesn't insert, update, or delete database records.
- Invalid prices: Products with invalid or negative prices remain in the cleaned output but are flagged with `price_valid=False`; they are excluded from the category summary.
- Duplicates: `drop_duplicates()` removes rows identical across all columns, not every repeated product ID.
- Output location: Run the script from the project root so `scripts/data/` is created in the expected location.

If the script reports a MySQL connection error, check that your `.env` values and database service are correct before changing the connection code.

### Step 7.3 — Understand why ETL matters

The same pattern is useful for:

- Daily sales reports.
- Product inventory summaries.
- Customer analytics.
- Data migration between systems.
- Preparing clean data for machine learning.
- Creating datasets for dashboards.

For large production datasets, add batching, structured logging, validation reports, failure handling, and a strategy for incremental extraction. Don't load millions of records into one DataFrame without considering memory limits.

## 8. Final exercise — run the full workflow

Use this checklist to track your progress through Lesson 09.

## Lesson 09 checklist

0/8 complete

Read database records

Run a SQLAlchemy query against your local development database.

Transform product data

Normalize names and convert prices safely.

Aggregate records

Calculate product counts and average prices using SQL or Python.

Export CSV and JSON

Generate files under scripts/data/.

Use pandas

Filter, sort, group, and summarize a DataFrame.

Clean data

Handle invalid values, missing data, and duplicates.

Run the ETL pipeline

Extract, transform, validate, and export product data.

Verify project quality

Run pytest and Ruff after changes.

### Final verification

Run these from your local `ecommerce-db` directory:

```
python -m pytest -v
ruff check .
```

If you added pandas as a project dependency, review the dependency file and make sure the new package is installed in the environment used by your scripts.

If you generated reports from real database records, inspect them locally and make sure they do not contain sensitive customer information before committing anything to Git.

## 9. Interview questions and answers

1\. What is ETL?

ETL stands for Extract, Transform, Load. Data is extracted from a source, transformed into the required structure, and loaded into a destination.

2\. What is the difference between a list and a pandas DataFrame?

A list is a general Python collection. A DataFrame is a tabular structure with labeled rows and columns and built-in filtering, aggregation, and data-cleaning capabilities.

3\. When should you aggregate in SQL rather than pandas?

When the database can efficiently filter or aggregate a large dataset, doing it in SQL reduces the amount of data transferred to Python. Pandas is useful for more complex analysis after extracting a manageable dataset.

4\. What is data cleaning?

Identifying and handling missing values, duplicates, invalid types, inconsistent formats, and other data-quality issues.

5\. What is the difference between CSV and JSON?

CSV is primarily tabular, while JSON can represent nested objects and arrays.

6\. Why is `errors="coerce"` useful in pandas?

It converts values that cannot be parsed into missing values instead of raising a conversion error. Those missing values must still be handled appropriately.

7\. Why should an ETL pipeline be repeatable?

A repeatable pipeline can be rerun after a failure or on a schedule without unintentionally corrupting the source data or producing inconsistent results.

## Lesson 09 — Completion criteria

You've completed the lesson when you can:

- Read your e-commerce data with SQLAlchemy.
- Transform and validate records using Python.
- Perform aggregation in SQL and pandas.
- Export CSV and JSON.
- Use DataFrames for filtering, sorting, and grouping.
- Clean missing, duplicate, and invalid data.
- Build a small ETL pipeline that produces useful reports.

One important distinction: The code examples above teach the complete workflow, but the database imports in the reading and ETL examples need to be connected to your project's actual Flask application factory and SQLAlchemy configuration before they can run unchanged.

## What's next in your AI roadmap?

Lessons 08 and 09 cover the remaining database-performance and data-processing topics under `advanced-python-database`. These skills provide a practical foundation for later AI work because data needs to be queried efficiently, cleaned, transformed, and prepared before it can be used for analysis or model training.

I recommend your next practical milestone be a small e-commerce sales analytics report using your own database schema, with a CSV export and pandas summary—without modifying the live GCP database.
