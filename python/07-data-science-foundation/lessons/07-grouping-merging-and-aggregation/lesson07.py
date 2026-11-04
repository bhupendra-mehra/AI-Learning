
import pandas as pd

df = pd.read_csv("sales.csv")

# Calculate revenue for each order.
df["Revenue"] = df["Price"] * df["Quantity"]

print("=== ORIGINAL DATA ===")
print(df)

print("\n=== COMPLETED ORDERS ===")
print(df[df["Status"] == "Completed"])

print("\n=== EXPENSIVE ORDERS ===")
print(df[df["Price"] > 1000])

print("\n=== TOP THREE ORDERS BY PRICE ===")
print(df.sort_values("Price", ascending=False).head(3))

print("\n=== PRODUCT SUMMARY ===")
product_report = df.groupby("Product").agg(
    Total_Orders=("OrderID", "count"),
    Units_Sold=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum"),
)
product_report = product_report.sort_values(
    "Total_Revenue", ascending=False
)
print(product_report)

print("\n=== CATEGORY SUMMARY ===")
category_report = df.groupby("Category").agg(
    Units_Sold=("Quantity", "sum"),
    Total_Revenue=("Revenue", "sum"),
)
print(category_report)

print("\n=== TOP PRODUCT ===")
product_revenue = df.groupby("Product")["Revenue"].sum()
print(product_revenue.idxmax(), product_revenue.max())

# Export reports.
product_report.reset_index().to_csv(
    "product_report.csv", index=False
)
category_report.reset_index().to_csv(
    "category_report.csv", index=False
)

print("\nReports saved successfully.")
