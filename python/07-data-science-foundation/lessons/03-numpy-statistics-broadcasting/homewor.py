import numpy as np

sales = np.array([
    [1200, 1500, 1800, 2000],
    [900, 2100, 2500, 2300],
    [700, 1100, 1600, 1900],
])

print("Total:", np.sum(sales))
print("Average:", np.mean(sales))
print("Minimum:", np.min(sales))
print("Maximum:", np.max(sales))

monthly_totals = np.sum(sales, axis=0)
product_totals = np.sum(sales, axis=1)

print("Monthly totals:", monthly_totals)
print("Product totals:", product_totals)

print("After 15% discount:", sales * 0.85)

monthly_adjustments = np.array([100, 200, 300, 400])
print("Monthly adjustments:", sales + monthly_adjustments)

product_adjustments = np.array([50, 100, 150])
print(
    "Product adjustments:",
    sales + product_adjustments[:, np.newaxis],
)

print("Cumulative monthly totals:", np.cumsum(monthly_totals))
print("Monthly differences:", np.diff(monthly_totals))

print("Sales categories:", np.where(sales >= 1800, "High", "Low"))
print("75th percentile:", np.percentile(sales, 75))