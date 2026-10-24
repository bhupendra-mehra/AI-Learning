import numpy as np

sales = np.array(
    [
        [1200, 1500, 1800],
        [900, 2100, 2500],
        [700, 1100, 1600],
    ]
)


#print("Sales Data : ", sales)

discounted_sales = sales * 0.90

print("\nSales after discount : ")
print(discounted_sales)

print("\nTotal Sales", np.sum(sales))
print("Average Sales", np.mean(sales))
print("Minium Sales", np.min(sales))
print("Maximum Sales", np.max(sales))

#monthyl total
print("\nMonthly Total",np.sum(sales,axis=0))
print("Product Total ",np.sum(sales,axis=1))

# Broadcasting: apply a separate adjustment to each product.
adjustments = np.array([100, 200, 300])
adjusted_sales = sales + adjustments[:, np.newaxis]

print("\nAdjusted sales:")
print(adjusted_sales)

# Cumulative calculations.
monthly_totals = np.sum(sales, axis=0)

print("\nCumulative monthly sales:", np.cumsum(monthly_totals))
print("Month-to-month differences:", np.diff(monthly_totals))

# Classify individual sales values.
categories = np.where(sales >= 1500, "High", "Low")

print("\nSales categories:")
print(categories)
