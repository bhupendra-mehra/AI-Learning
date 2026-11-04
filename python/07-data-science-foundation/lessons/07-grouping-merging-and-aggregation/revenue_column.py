import pandas as ps

df = ps.read_csv("sales.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

# print(df[["OrderID", "Product", "Price", "Quantity", "Revenue"]])
# print("Total revenue:", df["Revenue"].sum())


# product_revenue = df.groupby("Product")["Revenue"].sum()
# print(product_revenue)

#Multiple metrics using agg()
product_summary = df.groupby("Product").agg(
    Total_Orders=("OrderID", "count"),
    Units_Sold=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum"),
    Average_Price=("Price", "mean"),
)

print(product_summary)

category_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(category_revenue)

summary = df.groupby(["Category", "Product"]).agg(
    Units_Sold=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum"),
)

print(summary)

# Product with the highest total revenue
product_revenue = df.groupby("Product")["Revenue"].sum()

top_product = product_revenue.idxmax()
top_revenue = product_revenue.max()

print("Top product:", top_product)
print("Revenue:", top_revenue)
ranking = product_revenue.sort_values(ascending=False)
print(ranking)

highest_order = df.loc[df["Revenue"].idxmax()]

print(highest_order)