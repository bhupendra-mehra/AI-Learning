# Part 7 — Data Science Foundation

## Lesson 07: Pandas Filtering, Sorting and Grouping

Folder: `lessons/07-pandas-filtering-sorting-grouping/`

In this lesson, you'll learn how to filter sales records, sort results, group data by product or category, and calculate business metrics using Pandas. These skills will help you build your Sales Data Analysis Dashboard project.

### Learning objectives

By the end of this lesson, you should be able to:

- Filter rows using conditions and multiple criteria.
- Sort data by one or more columns.
- Group records using `groupby()`.
- Calculate total revenue, average price, quantities sold, and order counts.
- Identify top-selling products and best-performing categories.
- Export summary reports to CSV.

## 1. Set up your lesson folder

Open your terminal:

```
cd /var/www/html/AI-Learning/python/07-data-science-foundation
source .venv/bin/activate

mkdir -p lessons/07-pandas-filtering-sorting-grouping
cd lessons/07-pandas-filtering-sorting-grouping
```

Create the lesson file:

```
touch README.md
```

Use your existing Part 7 virtual environment. You don't need to install any additional libraries for this lesson if Pandas is already installed.

## 2. Create the practice dataset

Create a file named `sales.csv` inside this lesson folder.

```
OrderID,Product,Category,Price,Quantity,Status
401,Laptop,Electronics,55000,1,Completed
402,Mouse,Accessories,500,4,Completed
403,Keyboard,Accessories,1200,2,Pending
404,Monitor,Electronics,8500,1,Completed
405,Mouse,Accessories,500,3,Pending
406,Laptop,Electronics,55000,1,Completed
407,Webcam,Accessories,2200,2,Pending
408,Headphones,Accessories,2500,2,Completed
```

Save the file. Each row represents an order, and revenue is calculated as `Price × Quantity`.

## 3. Filtering rows

Filtering allows you to select only records that satisfy a condition.

```
import pandas as pddf = pd.read_csv("sales.csv")# Orders where the price is greater than 1,000print(df[df["Price"] > 1000])# Only completed ordersprint(df[df["Status"] == "Completed"])# Orders with quantity greater than or equal to 2print(df[df["Quantity"] >= 2])
```

### Filtering with multiple conditions

Use `&` for AND and `|` for OR. Put each condition inside parentheses.

```
# Completed orders with price above 1,000result = df[    (df["Status"] == "Completed")    & (df["Price"] > 1000)]print(result)# Orders for either Laptop or Monitorresult = df[df["Product"].isin(["Laptop", "Monitor"])]print(result)
```

Useful filtering patterns:

| Expression                                      | Meaning                           |
| ----------------------------------------------- | --------------------------------- |
| `df["Price"] > 1000`                            | Price above 1,000                 |
| `df["Price"].between(500, 5000)`                | Price within the range, inclusive |
| `df["Status"].isin(["Pending", "Completed"])`   | Match any listed status           |
| `df["Product"].str.contains("top", case=False)` | Case-insensitive text search      |
| `df["Price"].isna()`                            | Find missing prices               |
| `df["Price"].notna()`                           | Find non-missing prices           |

Common mistake: Python uses `and` and `or` for single Boolean expressions, but Pandas Series conditions should normally use `&` and `|` with parentheses.

## 4. Sorting data

Use `sort_values()` to arrange rows.

```
# Highest price firstprint(df.sort_values("Price", ascending=False))# Lowest quantity firstprint(df.sort_values("Quantity"))# Sort by category, then highest price within each categoryprint(    df.sort_values(        ["Category", "Price"],        ascending=[True, False],    ))
```

To get the three most expensive orders:

```
top_3 = df.sort_values("Price", ascending=False).head(3)print(top_3[["OrderID", "Product", "Price"]])
```

Expected result:

```
   OrderID Product  Price
0      401  Laptop  55000
5      406  Laptop  55000
3      404 Monitor   8500
```

The two Laptop orders tie on price, so their relative order can depend on the sorting algorithm. The selected three rows are still the correct top-price records.

## 5. Create a revenue column

Before grouping sales, calculate revenue for each order.

```
df["Revenue"] = df["Price"] * df["Quantity"]print(df[["OrderID", "Product", "Price", "Quantity", "Revenue"]])print("Total revenue:", df["Revenue"].sum())
```

Expected total revenue:

```
Total revenue: 133800
```

For the sample data, each order's revenue is:

| Product    | Quantity | Revenue |
| ---------- | -------- | ------- |
| Laptop     | 1        | 55,000  |
| Mouse      | 4        | 2,000   |
| Keyboard   | 2        | 2,400   |
| Monitor    | 1        | 8,500   |
| Mouse      | 3        | 1,500   |
| Laptop     | 1        | 55,000  |
| Webcam     | 2        | 4,400   |
| Headphones | 2        | 5,000   |

## 6. Grouping with `groupby()`

`groupby()` divides data into groups and lets you calculate summaries for each group.

### Revenue by product

```
product_revenue = df.groupby("Product")["Revenue"].sum()print(product_revenue)
```

Expected result:

```
Product
Headphones      5000
Keyboard        2400
Laptop        110000
Monitor         8500
Mouse           3500
Webcam          4400
Name: Revenue, dtype: int64
```

### Multiple metrics using `agg()`

```
product_summary = df.groupby("Product").agg(    Total_Orders=("OrderID", "count"),    Units_Sold=("Quantity", "sum"),    Total_Revenue=("Revenue", "sum"),    Average_Price=("Price", "mean"),)print(product_summary)
```

This produces one row per product with its order count, units sold, total revenue, and average unit price.

Note that `count` counts non-missing order IDs. If every row is a distinct order, it is an order count; otherwise, you may need to deduplicate or count distinct order IDs.

### Revenue by category

```
category_revenue = (    df.groupby("Category")["Revenue"]    .sum()    .sort_values(ascending=False))print(category_revenue)
```

Expected result:

```
Category
Electronics    118500
Accessories     15300
Name: Revenue, dtype: int64
```

### Group by multiple columns

```
summary = df.groupby(["Category", "Product"]).agg(    Units_Sold=("Quantity", "sum"),    Total_Revenue=("Revenue", "sum"),)print(summary)
```

This gives you a category-and-product breakdown, useful for reporting and dashboards.

## 7. Find the best-performing products

```
# Product with the highest total revenueproduct_revenue = df.groupby("Product")["Revenue"].sum()top_product = product_revenue.idxmax()top_revenue = product_revenue.max()print("Top product:", top_product)print("Revenue:", top_revenue)
```

Expected output:

```
Top product: Laptop
Revenue: 110000
```

To rank all products:

```
ranking = product_revenue.sort_values(ascending=False)print(ranking)
```

To find the largest individual order by revenue:

```
highest_order = df.loc[df["Revenue"].idxmax()]print(highest_order)
```

This identifies an individual order, whereas `groupby("Product")` identifies product-level performance across orders.

## 8. Combine filtering, grouping, and sorting

A realistic business question is: Which products generated the most revenue from completed orders?

```
completed = df[df["Status"] == "Completed"]report = (    completed.groupby("Product")    .agg(        Units_Sold=("Quantity", "sum"),        Total_Revenue=("Revenue", "sum"),    )    .sort_values("Total_Revenue", ascending=False))print(report)
```

Another example: find products with total revenue greater than ₹3,000.

```
product_revenue = df.groupby("Product")["Revenue"].sum()high_revenue_products = product_revenue[product_revenue > 3000]print(high_revenue_products)
```

These patterns combine several common data-analysis operations into a reusable workflow.

## 9. Export your reports

Save the product and category summaries to CSV files.

```
product_report = (    df.groupby("Product")    .agg(        Units_Sold=("Quantity", "sum"),        Total_Revenue=("Revenue", "sum"),    )    .sort_values("Total_Revenue", ascending=False))category_report = (    df.groupby("Category")    .agg(        Units_Sold=("Quantity", "sum"),        Total_Revenue=("Revenue", "sum"),    )    .sort_values("Total_Revenue", ascending=False))product_report.to_csv("product_report.csv")category_report.to_csv("category_report.csv")print("Reports exported successfully.")
```

To include the product and category names as ordinary columns instead of index values, use `.reset_index()` before exporting.

```
product_report.reset_index().to_csv("product_report.csv", index=False)category_report.reset_index().to_csv("category_report.csv", index=False)
```

## 10. Complete practice script

Create `lesson07.py` and run the following complete script:

```
import pandas as pddf = pd.read_csv("sales.csv")# Calculate revenue for each order.df["Revenue"] = df["Price"] * df["Quantity"]print("=== ORIGINAL DATA ===")print(df)print("\n=== COMPLETED ORDERS ===")print(df[df["Status"] == "Completed"])print("\n=== EXPENSIVE ORDERS ===")print(df[df["Price"] > 1000])print("\n=== TOP THREE ORDERS BY PRICE ===")print(df.sort_values("Price", ascending=False).head(3))print("\n=== PRODUCT SUMMARY ===")product_report = df.groupby("Product").agg(    Total_Orders=("OrderID", "count"),    Units_Sold=("Quantity", "sum"),    Total_Revenue=("Revenue", "sum"),)product_report = product_report.sort_values(    "Total_Revenue", ascending=False)print(product_report)print("\n=== CATEGORY SUMMARY ===")category_report = df.groupby("Category").agg(    Units_Sold=("Quantity", "sum"),    Total_Revenue=("Revenue", "sum"),)
```

Run it:

```
python lesson07.py
```

Expected files after execution:

- `product_report.csv`
- `category_report.csv`

## 11. Homework

Use the same `sales.csv` dataset.

1. Filter and display all orders with a price below ₹3,000.
2. Display all Pending orders where quantity is greater than one.
3. Sort all orders by revenue from highest to lowest.
4. Calculate total quantity sold for each product.
5. Calculate total revenue for each category.
6. Find the product with the highest total revenue.
7. Find the average selling price for each category.
8. Create a report containing product, total units sold, order count, and total revenue.
9. Export the report to `homework_product_report.csv`.
10. Explain the difference between finding the highest individual order and finding the product with the highest total revenue.

## 12. Common mistakes

- Forgetting parentheses around multiple filter conditions.
- Using `and` instead of `&` with Pandas Series.
- Sorting a DataFrame but not assigning the result when you need to reuse it.
- Grouping by the wrong column.
- Confusing `count()` with `sum()`: one counts values, the other adds them.
- Calculating revenue from rows with missing or invalid prices or quantities without first handling data quality.
- Forgetting `reset_index()` when you want group names as normal CSV columns.

## 13. Completion checklist

I can filter data using one or multiple conditions.

I can sort by one or more columns.

I can calculate revenue for each order.

I can use groupby() and agg() to create summaries.

I can identify the highest-revenue product and category.

I can export reports to CSV.

I have completed the homework.

7 of 7 completed

## Next lesson

Lesson 08 — Matplotlib Introduction and Data Visualization

You'll learn to create line charts, bar charts, histograms, labels, titles, and legends—the next step toward your Sales Data Analysis Dashboard.