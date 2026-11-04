# Part 7 — Data Science Foundation

## Lesson 08: Matplotlib Fundamentals

Folder: `python/07-data-science-foundation/lessons/08-matplotlib-fundamentals/`

In this lesson, you'll learn how to visualize sales data using Matplotlib, one of the most widely used Python libraries for data visualization. You'll create line charts, bar charts, histograms, and customized plots that will later support your Sales Data Analysis Dashboard project.

### Learning objectives

By the end of this lesson, you should be able to:

- Create and save charts using Matplotlib.
- Plot data using line, bar, and histogram charts.
- Add chart titles, axis labels, legends, and grid lines.
- Visualize Pandas DataFrames and grouped sales data.
- Choose an appropriate chart for a business question.

## 1. Set up your lesson folder

Open your terminal:

```
cd /var/www/html/AI-Learning/python/07-data-science-foundation
source .venv/bin/activate

mkdir -p lessons/08-matplotlib-fundamentals
cd lessons/08-matplotlib-fundamentals
touch README.md
```

You should already have Matplotlib installed from the Part 7 dependencies. If it isn't installed, run:

```
python -m pip install matplotlib
```

Verify the installation:

```
python -c "import matplotlib; print(matplotlib.__version__)"
```

Keep using your existing Part 7 `.venv`; there's no need to modify your Magento environment.

## 2. Understand Matplotlib

Matplotlib is a Python library for creating visualizations from numerical and tabular data.

The most common interface is `matplotlib.pyplot`, usually imported as `plt`.

```
import matplotlib.pyplot as pltx = [1, 2, 3, 4, 5]y = [100, 150, 120, 200, 250]plt.plot(x, y)plt.show()
```

What happens here?

- `plt.plot()` creates a line chart.
- `plt.show()` displays the chart.
- `x` represents the horizontal-axis values.
- `y` represents the vertical-axis values.

## 3. Create your first chart

Create a file named `lesson08.py` in your lesson folder.

```
import matplotlib.pyplot as pltdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]sales = [1200, 1800, 1500, 2200, 2800]plt.plot(days, sales)plt.title("Daily Sales")plt.xlabel("Day")plt.ylabel("Sales (₹)")plt.show()
```

Run the script:

```
python lesson08.py
```

A chart window should appear with days on the horizontal axis and sales on the vertical axis.

## 4. Line charts

[Day 32 — Data Visualization Day 3: Line & Bar Charts in Matplotlib | by Ratnesh | Medium](https://images.openai.com/static-rsc-4/q4jWFvcW30BzSUpWzASkhlm_WWH8TleOIa91Ww-oriIZ9Ple_Aw54LHFYlAxgYMruXXyiVIUK2Pn4BeyhtypE9ZmPPD6IxRBPYnhLrM_0oiGUtuUMZVzqNj6-LlGH_BvI7ZwSSU2GNC-4QuEH_PiI-Hrz81lRfmsXRafS2vVsSQ?purpose=inline)

[medium.com](https://medium.com/%40ratnesh3345/day-32-data-visualization-day-3-line-bar-charts-in-matplotlib-a0353005f430?utm_source=chatgpt.com)

A line chart is useful for showing trends over time, such as daily sales, monthly revenue, or website traffic.

```
import matplotlib.pyplot as pltmonths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]revenue = [45000, 52000, 48000, 61000, 70000, 68000]plt.plot(    months,    revenue,    marker="o",    linestyle="-",    label="Revenue",)plt.title("Monthly Revenue")plt.xlabel("Month")plt.ylabel("Revenue (₹)")plt.legend()plt.grid(True)plt.tight_layout()plt.show()
```

Important parameters:

| Parameter            | Purpose                                    |
| -------------------- | ------------------------------------------ |
| `marker="o"`         | Shows a circular marker at each data point |
| `linestyle="-"`      | Connects points with a solid line          |
| `label="Revenue"`    | Provides a name for the legend             |
| `plt.legend()`       | Displays the legend                        |
| `plt.grid(True)`     | Adds grid lines                            |
| `plt.tight_layout()` | Helps prevent labels from being cut off    |

## 5. Bar charts

[Bar Label Demo — Matplotlib 3.8.3 documentation](https://images.openai.com/static-rsc-4/thBxJSaPMdsNT0wgMAy7jBprys0FHaPauAbmlO-YbCbmCqxcvtXvA6Ysvt9xqQvqb4HMLJVlqZsIwqEaAxmSmXvm78ZJkfGAJK9hqxZe_r2HrJEaZXLkN3tAdWPfy9UPdtGW1sjNhiygLWQkaWD3UWSWfPXtqZDs4BKX61vlnNo?purpose=inline)

[matplotlib.org](https://matplotlib.org/3.8.3/gallery/lines_bars_and_markers/bar_label_demo.html?utm_source=chatgpt.com)

Bar charts help compare values across categories, such as revenue by product or sales by region.

```
import matplotlib.pyplot as pltproducts = ["Laptop", "Mouse", "Keyboard", "Monitor"]revenue = [110000, 3500, 2400, 8500]plt.bar(products, revenue)plt.title("Revenue by Product")plt.xlabel("Product")plt.ylabel("Revenue (₹)")plt.tight_layout()plt.show()
```

### Horizontal bar chart

When product names are long, horizontal bars can be easier to read.

```
plt.barh(products, revenue)plt.title("Revenue by Product")plt.xlabel("Revenue (₹)")plt.ylabel("Product")plt.tight_layout()plt.show()
```

Use `plt.bar()` for vertical bars and `plt.barh()` for horizontal bars.

## 6. Histograms

[EDA. Exploratory Data Analysis (EDA): A… | by Anuj Agrawal | Medium](https://images.openai.com/static-rsc-4/0XY_FtOD4EZcdcJLXlFlrxA8kcGIRpdH2mxAr9jMfHz04jZ-_gnXe8xpxhUTJMGzZuLQGaASfESloiXRhDqcC6sURUpn4YU-JUp-9LKw9PVdOc6n1W5kbEeI7YGLFjeN-xOPV2-kjCheiVdtDbs0cvedgE0hQi8gKolbbQd7sFg?purpose=inline)

[medium.com](https://medium.com/%40anujagrawal359/eda-cd4344a5fd4b?utm_source=chatgpt.com)

A histogram shows how numerical values are distributed across ranges, called bins.

For example, you can examine how many products have prices in different ranges.

```
import matplotlib.pyplot as pltprices = [    300, 450, 500, 650, 800,    1200, 1500, 2200, 2500,    5000, 8500, 12000, 25000, 55000,]plt.hist(prices, bins=5, edgecolor="black")plt.title("Distribution of Product Prices")plt.xlabel("Price Range (₹)")plt.ylabel("Number of Values")plt.tight_layout()plt.show()
```

Important distinction: A bar chart compares separate categories. A histogram groups numerical observations into ranges. Its bars usually touch because the ranges are continuous.

## 7. Scatter plots

A scatter plot helps explore the relationship between two numerical variables.

For example, does quantity tend to increase with order revenue?

```
import matplotlib.pyplot as pltquantity = [1, 4, 2, 1, 3, 1, 2, 2]revenue = [55000, 2000, 2400, 8500, 1500, 55000, 4400, 5000]plt.scatter(quantity, revenue)plt.title("Quantity vs Order Revenue")plt.xlabel("Quantity")plt.ylabel("Revenue (₹)")plt.tight_layout()plt.show()
```

Scatter plots help reveal patterns, clusters, and unusual observations. They do not, by themselves, prove that one variable causes changes in another.

## 8. Work with Pandas sales data

Use the `sales.csv` file from Lesson 07. If you don't have it, create it with this data:

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

Create `sales_charts.py`:

```
import pandas as pdimport matplotlib.pyplot as pltdf = pd.read_csv("sales.csv")# Calculate revenue for each order.df["Revenue"] = df["Price"] * df["Quantity"]# Aggregate revenue by product.product_revenue = (    df.groupby("Product")["Revenue"]    .sum()    .sort_values(ascending=False))plt.figure(figsize=(10, 6))product_revenue.plot(kind="bar")plt.title("Total Revenue by Product")plt.xlabel("Product")plt.ylabel("Revenue (₹)")plt.xticks(rotation=30, ha="right")plt.grid(axis="y", alpha=0.3)plt.tight_layout()plt.savefig("revenue_by_product.png", dpi=150)plt.show()
```

Run:

```
python sales_charts.py
```

This script creates `revenue_by_product.png` in the current directory. You can use the image in a report or dashboard.

## 9. Customize and save charts

You can customize figure size, titles, axis labels, and legends to make charts clearer.

```
import matplotlib.pyplot as pltmonths = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]actual = [45000, 52000, 48000, 61000, 70000, 68000]target = [50000, 50000, 55000, 60000, 65000, 70000]plt.figure(figsize=(10, 5))plt.plot(months, actual, marker="o", label="Actual Revenue")plt.plot(months, target, marker="s", linestyle="--", label="Target Revenue")plt.title("Actual vs Target Revenue")plt.xlabel("Month")plt.ylabel("Revenue (₹)")plt.legend()plt.grid(True, alpha=0.3)plt.tight_layout()plt.savefig("actual_vs_target.png", dpi=150, bbox_inches="tight")plt.show()
```

Useful functions:

| Function                      | Purpose                        |
| ----------------------------- | ------------------------------ |
| `plt.figure(figsize=(10, 5))` | Sets figure size in inches     |
| `plt.title()`                 | Adds a chart title             |
| `plt.xlabel()`                | Labels the horizontal axis     |
| `plt.ylabel()`                | Labels the vertical axis       |
| `plt.legend()`                | Displays series names          |
| `plt.xticks(rotation=30)`     | Rotates horizontal-axis labels |
| `plt.savefig()`               | Saves the chart to a file      |
| `plt.close()`                 | Closes a figure after saving   |

## 10. Choosing the right chart

| Business question                                     | Suitable chart                  |
| ----------------------------------------------------- | ------------------------------- |
| How did revenue change each month?                    | Line chart                      |
| Which product generated the most revenue?             | Bar chart                       |
| How are product prices distributed?                   | Histogram                       |
| Is there a relationship between quantity and revenue? | Scatter plot                    |
| How do actual sales compare with targets over time?   | Line chart with multiple series |

Choose a chart based on the question you want to answer, not just on appearance.

## 11. Mini project: Sales visualization report

Create a script named `sales_visualization_report.py` that:

1. Reads `sales.csv` using Pandas.
2. Calculates `Revenue = Price × Quantity`.
3. Creates a line chart of monthly revenue using a suitable monthly dataset.
4. Creates a bar chart of revenue by product.
5. Creates a histogram of order prices.
6. Saves each chart as a separate PNG file.
7. Prints total revenue and the product with the highest total revenue.

For the current eight-row dataset, the monthly chart needs a separate date or month column. Do not invent monthly trends from data that has no dates.

Expected output files:

- `revenue_by_product.png`
- `price_distribution.png`
- `monthly_revenue.png` — after adding appropriate date/month data.

## 12. Common mistakes

- Forgetting `plt.show()` when you expect a chart window to appear.
- Forgetting `plt.savefig()` when you need a permanent image file.
- Using a histogram to compare named product categories.
- Forgetting axis labels and units.
- Using too many categories in a crowded chart.
- Calculating revenue before checking for missing or invalid price and quantity values.
- Trying to plot monthly trends when the dataset has no date information.

## 13. Homework

Use the provided `sales.csv` dataset.

- Create a vertical bar chart of revenue by product.
- Create a horizontal bar chart of units sold by product.
- Create a histogram of product prices.
- Create a scatter plot comparing quantity and revenue.
- Add meaningful chart titles, axis labels, and grid lines where useful.
- Save all four charts as PNG files.
- Explain why a histogram is different from a bar chart.
- Explain which chart you would use to compare product revenue and why.

## 14. Completion checklist

I can create a line chart.

I can create vertical and horizontal bar charts.

I can create a histogram and scatter plot.

I can add titles, labels, legends, and grid lines.

I can visualize Pandas groupby() results.

I can save charts as PNG files.

I have completed the homework.

7 of 7 completed

## Next lesson

Lesson 09 — Data Cleaning and Exploratory Data Analysis (EDA)

You'll learn to investigate data quality, identify patterns and outliers, summarize distributions, and prepare datasets for meaningful analysis. This will bring together the NumPy, Pandas, and visualization skills developed so far.