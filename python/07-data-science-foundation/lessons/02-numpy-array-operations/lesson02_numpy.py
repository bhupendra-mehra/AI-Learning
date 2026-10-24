import numpy as np

sales = np.array([1200, 1500, 900, 1800, 2100, 2500])

print("First sale:", sales[0])
print("Last sale:", sales[-1])
print("First three sales:", sales[:3])
print("Every second sale:", sales[::2])
print("Reversed sales:", sales[::-1])

print("Sales >= 1500:", sales[sales >= 1500])

monthly_sales = np.array([
    [1200, 1500, 1800],
    [900, 2100, 2500],
])

print("First month:", monthly_sales[0])
print("Second month:", monthly_sales[1])
print("First column:", monthly_sales[:, 0])
print("Shape:", monthly_sales.shape)

values = np.arange(1, 13)
matrix = values.reshape(3, 4)

print("Reshaped array:")
print(matrix)

print("Flattened array:", matrix.flatten())