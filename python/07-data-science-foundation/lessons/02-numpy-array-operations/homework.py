import numpy as np

prices = np.array([499, 799, 1299, 1599, 2499, 999, 1899, 299])

print("First ",prices[0])
print("Last ",prices[-1])
print("Last Three", prices[-3::])
print("Every Second Price", prices[0::2])
print("Reverse the array", prices[::-1])
print("Greater than 1000",prices[prices > 1000])
print("Greater than 1000",prices[prices > 1000])
print("Greater between 500 and 1500",prices[(prices >= 500) & (prices <= 1500)])


matrix = prices.reshape(2,4)

print(matrix)
print(matrix[1])
print(matrix[:,2])
print(matrix.flatten())

copy_prices = prices[1:3].copy()
copy_prices[0] = 999

# copied_sales = sales[1:3].copy()
# copied_sales[0] = 999

print(prices)
print(copy_prices)