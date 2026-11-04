import pandas as pd

# 1. Load the complete dataset
df = pd.read_csv("homework_sales.csv")

print("=== COMPLETE DATASET ===")
print(df)

# 2. Display the first four and last two rows
print("\n=== FIRST FOUR ROWS ===")
print(df.head(4))

print("\n=== LAST TWO ROWS ===")
print(df.tail(2))

# 3. Inspect the dataset structure
print("\n=== DATASET SHAPE ===")
print(df.shape)

print("\n=== COLUMN NAMES ===")
print(df.columns.tolist())

print("\n=== DATA TYPES ===")
print(df.dtypes)

# 4. Check missing values
print("\n=== MISSING VALUES BY COLUMN ===")
print(df.isna().sum())

print("\n=== TOTAL MISSING VALUES ===")
print(df.isna().sum().sum())

# 5. Check duplicate rows
print("\n=== DUPLICATE ROWS ===")
print(df.duplicated().sum())

# 6. Inspect unique products and their frequencies
print("\n=== UNIQUE PRODUCTS ===")
print(df["Product"].unique())

print("\n=== NUMBER OF UNIQUE PRODUCTS ===")
print(df["Product"].nunique())

print("\n=== PRODUCT FREQUENCIES ===")
print(df["Product"].value_counts())

# 7. Load only the required columns
selected_columns = pd.read_csv(
    "homework_sales.csv",
    usecols=["OrderID", "Product", "Price"],
)

print("\n=== SELECTED COLUMNS ===")
print(selected_columns)

# 8. Load only the first three data rows
first_three_rows = pd.read_csv(
    "homework_sales.csv",
    nrows=3,
)

print("\n=== FIRST THREE DATA ROWS ===")
print(first_three_rows)

# 9. Create a data-quality report
print("\n=== DATA-QUALITY REPORT ===")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nMissing values by column:")
print(df.isna().sum())

print("\nTotal missing values:", df.isna().sum().sum())
print("Duplicate rows:", df.duplicated().sum())

print("\nNumerical summary:")
print(df.describe())

# 10. Explain why missing values matter before calculating revenue
print("\n=== WHY CHECK MISSING VALUES? ===")
print(
    "Missing prices or quantities can make revenue calculations "
    "incomplete or misleading. Inspect missing values before "
    "calculating revenue so you can decide how to handle them."
)