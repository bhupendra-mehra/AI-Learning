import pandas as pd
df = pd.read_csv("regional_sales.csv", sep=";")
print(df)

df = pd.read_csv(
    "sales.csv",
    usecols=["OrderID", "Product", "Price"],
)

print(df)

df = pd.read_csv("sales.csv", nrows=2)

print(df)

df.columns = df.columns.str.strip()

print(df.columns.tolist())


df = pd.read_csv(
    "sales.csv",
    dtype={"OrderID": "string"},
)

print(df.dtypes)