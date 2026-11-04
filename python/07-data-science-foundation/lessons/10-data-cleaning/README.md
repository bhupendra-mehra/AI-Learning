# Lesson 10 — Data Cleaning with Python and Pandas

**Part:** 7 — Data Science Foundation
**Folder:** `10-data-cleaning`
**Project connection:** Sales Data Analysis Dashboard

## Objective

Learn to clean, standardize, and validate business records before using them for reporting, API integrations, or AI-powered automation.

## Learning outcomes

By completing this lesson, you should be able to:

- Identify and handle missing values.
- Detect and remove duplicate records.
- Standardize text, whitespace, and category values.
- Convert malformed dates and numeric values safely.
- Detect invalid prices, quantities, emails, and statuses.
- Separate valid records from records requiring review.
- Validate cleaned data before an API or AI workflow.
- Export and verify cleaned CSV and JSON files.

## Files

```text
10-data-cleaning/
├── README.md
├── messy_orders.csv
└── lesson10.py
```

## Setup

From the Part 7 directory:

```bash
cd /var/www/html/AI-Learning/python/07-data-science-foundation
source .venv/bin/activate
cd lessons/10-data-cleaning
```

Required libraries: Pandas. Use the existing Part 7 virtual environment.

## Practical topics

### 1. Missing values

Use:

```python
df.isna().sum()
df["Price"].isna()
df.dropna(subset=["Price"])
df["Price"].fillna(0)
```

**Important:** `fillna(0)` is appropriate only when zero has a valid business meaning. A missing price usually means the value is unknown, not free. Inspect missing values before deciding how to handle them.

### 2. Duplicate records

Use:

```python
df.duplicated().sum()
df.drop_duplicates()
df.duplicated(subset=["OrderID"], keep="first")
```

Exact duplicates and repeated business identifiers are different checks. Confirm the business rules before removing records based on an identifier.

### 3. Text standardization

Use:

```python
df["Product"] = df["Product"].str.strip().str.title()
df["CustomerEmail"] = df["CustomerEmail"].str.strip().str.lower()
df["Status"] = df["Status"].str.strip().str.title()
```

Standardization makes filtering, grouping, matching, and reporting more reliable.

### 4. Numeric and date conversion

Use:

```python
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

df["OrderDate"] = pd.to_datetime(
    df["OrderDate"],
    errors="coerce",
    format="mixed",
)
```

Malformed values become missing values for investigation. Check conversion failures before exporting the data.

### 5. Business validation

Examples of practical rules:

- Order ID must be present and unique.
- Customer email must match the expected format.
- Product and category must be present.
- Order date must be valid.
- Price must be non-negative.
- Quantity must be a positive whole number.
- Status must belong to the approved list.

Business rules should be confirmed with the system owner. For example, a zero price might be legitimate for a promotional item.

### 6. Prepare data for automation

A reliable workflow should:

1. Load the source data.
2. Standardize formats.
3. Identify missing, duplicate, malformed, and invalid records.
4. Separate valid records from records requiring review.
5. Validate required fields and business rules.
6. Export the results.
7. Validate the final payload before sending it to another system.

Do not silently discard records or invent missing business values. Keep rejected records and their reasons for investigation.

## Run the exercise

```bash
python lesson10.py
```

Expected summary for the supplied sample dataset:

```text
Rows loaded: 9
Exact duplicate rows found: 1
Repeated order IDs removed: 0
Valid rows: 3
Rows requiring review: 5
Total valid revenue: 65500
```

Expected output files:

- `clean_orders.csv`
- `orders_requiring_review.csv`
- `clean_orders.json`

The three valid orders have a combined revenue of ₹65,500.

## Exercises

1. Add a row with a missing customer email. Verify that it is rejected.
2. Add a row with a negative quantity. Verify that it is rejected.
3. Add an unknown order status and confirm that it requires review.
4. Add a valid product category with inconsistent capitalization and verify that it is standardized.
5. Add a malformed price and verify that it is not silently converted to zero.
6. Reload `clean_orders.csv` and confirm that order IDs are unique.
7. Reload `clean_orders.json` and validate the required fields.
8. Explain why invalid records should be reviewed rather than automatically deleted.
9. Explain why an AI workflow should validate both its input data and its generated output.

## Common errors

- Treating missing values as zero without a business justification.
- Removing repeated IDs without confirming the uniqueness rule.
- Converting malformed values without checking the conversion failures.
- Treating string formatting as proof that an email address is valid.
- Exporting data without verifying the saved file.
- Sending invalid or unnecessary customer information to an external service.
- Assuming that a successful CSV export means the data is ready for an API.

## Completion checklist

- [x] I can identify missing values and duplicates.
- [x] I can standardize text and category values.
- [x] I can convert numeric values and dates safely.
- [x] I can detect invalid business records.
- [x] I can separate valid and rejected records.
- [x] I can validate the cleaned dataset.
- [x] I can export and reload CSV and JSON files.
- [x] I have completed the exercises.

## Next step

Continue with the existing Part 7 roadmap. Lesson 09 — Chart Customization remains pending, and the next data-analysis topic should be selected according to the existing roadmap rather than renumbering completed lessons.
