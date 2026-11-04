
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load sales data
df = pd.read_csv("sales.csv")

# 2. Calculate revenue for each order
df["Revenue"] = df["Price"] * df["Quantity"]

# 3. Line chart: Revenue by order
# This is an order sequence, NOT a monthly trend.
plt.figure(figsize=(10, 5))

plt.plot(
    df["OrderID"],
    df["Revenue"],
    marker="o",
    label="Order Revenue",
)

plt.title("Revenue by Order")
plt.xlabel("Order ID")
plt.ylabel("Revenue (₹)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("sales_homework.png", dpi=150, bbox_inches="tight")
plt.close()

print("Line chart saved: sales_homework.png")


# 4. Bar chart: Total revenue by product
product_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))

plt.bar(product_revenue.index, product_revenue.values)

plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=30, ha="right")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("sales-homework-bar-chart.png", dpi=300, bbox_inches="tight")
plt.close()

print("Bar chart saved: sales-homework-bar-chart.png")


# 5. Histogram: Distribution of order prices
plt.figure(figsize=(10, 5))

plt.hist(df["Price"].dropna(), bins=5, edgecolor="black")

plt.title("Distribution of Order Prices")
plt.xlabel("Price (₹)")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.savefig("sales-histograms-chart.png", dpi=300, bbox_inches="tight")
plt.close()

print("Histogram saved: sales-histograms-chart.png")


# 6. Scatter plot: Quantity versus revenue
plt.figure(figsize=(10, 5))

plt.scatter(df["Quantity"], df["Revenue"])

plt.title("Quantity vs Order Revenue")
plt.xlabel("Quantity")
plt.ylabel("Revenue (₹)")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("sales-quantity-revenue.png", dpi=150, bbox_inches="tight")
plt.close()

print("Scatter plot saved: sales-quantity-revenue.png")


# 7. Print sales statistics
print("\n=== SALES SUMMARY ===")
print("Total Revenue (₹):", df["Revenue"].sum())

print("\n=== TOTAL REVENUE BY PRODUCT ===")
print(product_revenue)

print("\n=== PRODUCT WITH HIGHEST TOTAL REVENUE ===")
print("Product:", product_revenue.idxmax())
print("Revenue (₹):", product_revenue.max())

# Highest individual order is a different metric.
highest_order = df.loc[df["Revenue"].idxmax()]

print("\n=== HIGHEST INDIVIDUAL ORDER ===")
print(highest_order[["OrderID", "Product", "Revenue"]])
