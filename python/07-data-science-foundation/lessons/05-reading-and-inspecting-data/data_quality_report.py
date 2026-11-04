import pandas as pd

df = pd.read_csv("messy_sales.csv")

print("=== DATASET OVERVIEW ===")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Column names:", df.columns.tolist())

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== MISSING VALUES ===")
print(df.isna().sum())
print("Total missing values:", df.isna().sum().sum())

print("\n=== DUPLICATE ROWS ===")
print("Duplicate rows:", df.duplicated().sum())

print("\n=== UNIQUE VALUES ===")
for column in df.columns:
    print(f"{column}: {df[column].nunique()} unique values")

print("\n=== NUMERICAL SUMMARY ===")
print(df.describe())