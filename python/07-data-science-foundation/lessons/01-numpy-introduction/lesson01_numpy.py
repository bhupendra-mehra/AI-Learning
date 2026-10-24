import numpy as np

sales = np.array([100, 200, 300, 400,500])

print("Shape:", sales.shape)

monthly_sales = np.array(
    [
        [100, 200, 300],
        [400, 500, 600],
    ]
)

print("Sales:",sales)
print("Monthly sales :")
print(monthly_sales)

print("Dimensions:", monthly_sales.ndim)
print("Shape:", monthly_sales.shape)
print("Total elements:", monthly_sales.size)
print("Data type:", monthly_sales.dtype)

zeros = np.zeros(5)
ones = np.ones(4)
sequence = np.arange(1,11)
evenly_spaced = np.linspace(0,100,5)

print(zeros)
print(ones)
print(sequence)
print(evenly_spaced)


import numpy as np

monthly_sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900],
])

print(monthly_sales[0:2, 1:3])