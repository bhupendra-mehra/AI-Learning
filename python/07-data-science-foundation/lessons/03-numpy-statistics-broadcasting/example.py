import numpy as np

# sales = np.array([100,200,300,400])

# sales = sales * 1.10

# print(sales)

# print(sales + 50)

# print(sales-10)

# print(sales * 2)

# print(sales / 2)

# print(sales ** 2)

prices = np.array([1000, 2000, 3000])
quantities = np.array([2, 3, 1])

revenue = prices * quantities

# print(revenue)

discount = revenue * 0.10

net_before_tax = revenue - discount

tax = net_before_tax * 0.18

total_after_tax = net_before_tax + tax


# print("Revenue:", revenue)
# print("Discount:", discount)
# print("Net before tax:", net_before_tax)
# print("Tax:", tax)
# print("Total after tax:", total_after_tax)


sales = np.array(
    [
        [100, 200, 300],
        [400, 500, 600],
    ]
)

# adjustments = np.array([10, 20, 30])

# print(sales + adjustments)


# monthly_adjustments = np.array([10, 20])

# monthly_adjustments = monthly_adjustments[:, np.newaxis]

# print(monthly_adjustments)


# adjusted_sales = sales + monthly_adjustments[:, np.newaxis]

# print(adjusted_sales)

# print(np.sum(sales))

# print(np.sum(sales, axis=0))

# print(np.sum(sales, axis=1))

sales = np.array([500, 1200, 1800, 2500])

# print(np.cumsum(sales))

categories = np.where(sales >= 1500, "High", "Low")
limited_sales = np.clip(sales, 600, 2000)

print(categories)
print(limited_sales)

# A mix of low, medium, and high numbers
data = np.array([2, 15, 8, 0, 22, -5, 11])

# Keep all numbers strictly between 0 and 10
clipped_data = np.clip(data, a_min=0, a_max=10)

print(clipped_data)
# Output: [ 2 10  8  0 10  0 10]