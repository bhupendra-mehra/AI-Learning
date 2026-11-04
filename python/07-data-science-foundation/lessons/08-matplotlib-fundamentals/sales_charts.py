import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

# Calculate revenue for each order.
df["Revenue"] = df["Price"] * df["Quantity"]

# Aggregate revenue by product.
product_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
product_revenue.plot(kind="bar")

plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=30, ha="right")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("revenue_by_product.png", dpi=150)
# Close the figure
plt.close()

print("Revenue chart saved successfully: revenue_by_product.png")