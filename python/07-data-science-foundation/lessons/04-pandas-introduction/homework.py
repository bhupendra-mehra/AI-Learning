import pandas as pd

# 1. Create the orders DataFrame
orders = pd.DataFrame(
    {
        "OrderID": [101, 102, 103, 104, 105],
        "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Mouse"],
        "Price": [55000, 500, 1200, 8500, 500],
        "Quantity": [1, 4, 2, 1, 3],
    }
)

# 2. Display the complete DataFrame
print("Complete Orders Data:")
print(orders)

# 3. Display the number of rows and columns
print("\nDataFrame Shape:")
print(orders.shape)

# 4. Display column names and data types
print("\nColumn Names:")
print(orders.columns.tolist())

print("\nData Types:")
print(orders.dtypes)

# 5. Display the first three rows
print("\nFirst Three Rows:")
print(orders.head(3))

# 6. Select the Product column
print("\nProduct Column:")
print(orders["Product"])

# 7. Select Product and Price columns
print("\nProduct and Price Columns:")
print(orders[["Product", "Price"]])

# 8. Display the second row
print("\nSecond Row:")
print(orders.iloc[1])

# 9. Calculate revenue for each order
orders["Revenue"] = orders["Price"] * orders["Quantity"]

print("\nRevenue for Each Order:")
print(orders[["OrderID", "Product", "Revenue"]])

# 10. Calculate total revenue
print("\nTotal Revenue:", orders["Revenue"].sum())

# 11. Calculate the highest revenue
print("Highest Revenue:", orders["Revenue"].max())

# 12. Find the order with the highest revenue
highest_revenue_order = orders.loc[orders["Revenue"].idxmax()]

print("\nOrder with Highest Revenue:")
print(highest_revenue_order)

# 13. Filter orders where price is greater than 1000
print("\nOrders Where Price > 1000:")
print(orders[orders["Price"] > 1000])

# 14. Save the DataFrame to a CSV file without the index
orders.to_csv("sales.csv", index=False)

print("\nData successfully saved to sales.csv")