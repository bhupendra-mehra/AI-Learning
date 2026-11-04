import pandas as ps

df = ps.read_csv("sales.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

completed = df[df["Status"] == "Completed"]

report = (
    completed.groupby("Product")
    .agg(
        Units_Sold=("Quantity", "sum"),
        Total_Revenue=("Revenue", "sum"),
    )
    .sort_values("Total_Revenue", ascending=False)
)

print(report)

product_revenue = df.groupby("Product")["Revenue"].sum()

high_revenue_products = product_revenue[product_revenue > 3000]

print(high_revenue_products)