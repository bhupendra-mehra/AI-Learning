import pandas as pd

# df = pd.read_csv("messy_sales.csv")

# print("Missing Values by column:")
# print(df.isna().sum())

# print("\nTotal missing values:")
# print(df.isna().sum().sum())

# df = pd.DataFrame({
#     "OrderID": [101, 102, 103, 102],
#     "Product": ["Laptop", "Mouse", "Keyboard","Mouse"],
#     "Price": [55000, 500, 1200, 500],
# })


# print(df)

# print("Duplicate row flags:")
# print(df.duplicated())

# print("\nNumber of duplicate rows:")
# print(df.duplicated().sum())

# 1. Group by all columns and find the index positions for each unique group
# grouped_indices = df.groupby(list(df.columns)).indices

# 2. Filter out groups that only have 1 unique row (not duplicates)
# duplicates_mapping = {val[0]: list(val) for val in grouped_indices.values() if len(val) > 1}

# print("Original Row Index -> List of all duplicate row indices:")
# print(duplicates_mapping)

df = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Mouse", "Keyboard", "Mouse"],
    "Status": ["Completed", "Pending", "Completed", "Pending", "Completed"],
})

print("Unique products:")
print(df["Product"].unique())

print("\nNumber of unique products:")
print(df["Product"].nunique())

print("\nProduct frequencies:")
print(df["Product"].value_counts())

print("\nOrder status frequencies:")
print(df["Status"].value_counts())