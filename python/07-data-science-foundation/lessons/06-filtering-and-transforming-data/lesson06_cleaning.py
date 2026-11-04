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
missing_sales_mask = df[["Product","Price", "Quantity"]].isna().any(axis=1)
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