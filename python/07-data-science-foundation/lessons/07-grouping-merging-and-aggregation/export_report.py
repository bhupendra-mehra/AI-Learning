import pandas as ps

df = ps.read_csv("sales.csv")

df["Revenue"] = df["Price"] * df["Quantity"]

product_report = (
    df.groupby("Product")
    .agg(
        Units_Sold=("Quantity", "sum"),
        Total_Revenue=("Revenue", "sum"),
    )
    .sort_values("Total_Revenue", ascending=False)
)

category_report = (
    df.groupby("Category")
    .agg(
        Units_Sold=("Quantity", "sum"),
        Total_Revenue=("Revenue", "sum"),
    )
    .sort_values("Total_Revenue", ascending=False)
)

product_report.to_csv("product_report.csv")
category_report.to_csv("category_report.csv")

print("Reports exported successfully.")