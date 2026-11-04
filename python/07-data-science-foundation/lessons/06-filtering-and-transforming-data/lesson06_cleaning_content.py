import pandas as pd

df = pd.read_csv("messy_sales.csv")

print("=== ORIGINAL DATA ===")
print(df)

print("\n=== MISSING VALUES ===")
print(df.isna().sum())

print("\n=== DUPLICATE ROWS ===")
print(df.duplicated().sum())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== UNIQUE PRODUCTS ===")
print(df["Product"].unique())

print("\n=== UNIQUE STATUSES ===")
print(df["Status"].unique())