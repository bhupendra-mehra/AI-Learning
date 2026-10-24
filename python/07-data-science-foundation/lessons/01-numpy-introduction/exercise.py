
import numpy as np

sales = np.array([1200, 1500, 900, 1800, 2100])

print("Number of values:", sales.size)
print("Shape:", sales.shape)
print("Dimensions:", sales.ndim)
print("Total sales:", np.sum(sales))
print("Average sales:", np.mean(sales))
print("Sales after 15% increase:", sales * 1.15)
print("Min", np.min(sales))
print("Max", np.max(sales))
