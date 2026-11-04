import pandas as pd

orders = [
    {"OrderID": 101, "Product": "Keyboard", "Amount": 1200},
    {"OrderID": 102, "Product": "Mouse", "Amount": 500},
    {"OrderID": 103, "Product": "Monitor", "Amount": 2500},
    {"OrderID": 104, "Product": "Mobile", "Amount": 3500},
    {"OrderID": 105, "Product": "Power Bank", "Amount": 4500},
    {"OrderID": 106, "Product": "USB-C cable", "Amount": ""},
    {"OrderID": 107, "Product": "Smartwatch", "Amount": 600},
    {"OrderID": 108, "Product": "Adapter", "Amount": 700},
    {"OrderID": 109, "Product": "Iphone", "Amount": 10000},
    {"OrderID": 110, "Product": "Samsung", "Amount": 9000},
]

#df = pd.DataFrame(orders)

#print(df)
# print("Head ",df.head())
# print("Tail ", df.tail())
# print("Info " ,df.info())
# print("Describe ", df.describe())
# print("Random Row ", df.sample())
# print("Missing Values ", df.isna())
# print("Unique Values ", df.nunique())

df = pd.DataFrame({
    "Product": ["Keyboard", "Mouse", "Monitor"],
    "Price": [1200, 500, 8500],
    "Quantity": [5, 10, 2],
})

df["Revenue"] = df["Price"] * df["Quantity"]
df["Discount"] = df["Revenue"] * 0.5

print("Total revenue:", df["Revenue"].sum())
print("Average revenue per product:", df["Revenue"].mean())
print("Maximum revenue:", df["Revenue"].max())
print("Minimum revenue:", df["Revenue"].min())

df.to_csv("product_sales.csv", index=False)

loaded_df = pd.read_csv("product_sales.csv")

print(loaded_df)