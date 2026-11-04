import pandas as pd

products = {
    "Product": ["Keyboard", "Mouse", "Monitor", "Webcam"],
    "Price": [1200, 500, 8500, 2200],
    "Quantity": [5, 10, 2, 4],
}

df = pd.DataFrame(products)

print("Product data:")
print(df)

print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())

print("\nFirst two rows:")
print(df.head(2))

print("\nData types:")
print(df.dtypes)

df["Revenue"] = df["Price"] * df["Quantity"]

print("\nRevenue by product:")
print(df[["Product", "Revenue"]])

print("\nTotal revenue:", df["Revenue"].sum())
print("Average product revenue:", df["Revenue"].mean())
print("Highest product revenue:", df["Revenue"].max())

print("\nProducts costing more than 1000:")
print(df[df["Price"] > 1000])

df.to_csv("product_sales.csv", index=False)

print("\nSaved product_sales.csv")