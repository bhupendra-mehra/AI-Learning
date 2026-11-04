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
