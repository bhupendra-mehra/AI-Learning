# Part 7 — Data Science Foundation

Goal: Learn the libraries and data analysis techniques used by almost every AI engineer.

We'll follow your original roadmap: NumPy, Pandas, Matplotlib, data cleaning, and Exploratory Data Analysis (EDA), finishing with a practical Sales Data Analysis Dashboard project.

The lessons will be hands-on and build on your existing Python knowledge. We won't introduce machine learning or AI agent topics into this part; those belong later in your roadmap.

## 1. Complete lesson roadmap

### Module 1 — NumPy

Lessons 01–03 · Numerical computing

Learn to work efficiently with numerical data and arrays.

### Module 2 — Pandas

Lessons 04–07 · Data manipulation

Load, inspect, filter, transform, group and summarize tabular data.

### Module 3 — Matplotlib

Lessons 08–09 · Data visualization

Turn data into charts that reveal trends and comparisons.

### Module 4 — Data Cleaning and EDA

Lessons 10–12 · Data quality and insights

Handle missing and duplicate records, explore distributions and identify patterns.

### Module 5 — Final Project

Lesson 13 · Sales Data Analysis Dashboard

Combine the libraries and techniques into one complete analysis project.

## 2. Lesson-by-lesson syllabus

### Module 1 — NumPy

Purpose: Learn efficient numerical operations in Python.

| Lesson | Topic                                              | Practical outcome                                                                  |
| ------ | -------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 01     | NumPy Introduction and Arrays                      | Create arrays and understand NumPy vs Python lists                                 |
| 02     | Array Indexing, Slicing and Shapes                 | Select values, reshape arrays and inspect dimensions                               |
| 03     | Vectorized Operations, Statistics and Broadcasting | Perform calculations, sums, means, minimums and maximums without unnecessary loops |

### Module 2 — Pandas

Purpose: Work with real-world datasets stored in CSV files and tables.

| Lesson | Topic                                               | Practical outcome                                                          |
| ------ | --------------------------------------------------- | -------------------------------------------------------------------------- |
| 04     | Pandas Introduction, Series and DataFrames          | Create tables and understand rows, columns and indexes                     |
| 05     | Reading CSV and Inspecting Data                     | Load sales data and use `head()`, `info()`, `describe()` and `shape`       |
| 06     | Selecting, Filtering, Sorting and Transforming Data | Filter sales by date, category and revenue; create calculated columns      |
| 07     | Grouping, Aggregation, Merging and Exporting        | Calculate category totals, monthly sales, join datasets and export reports |

### Module 3 — Matplotlib

Purpose: Visualize information and communicate business findings.

| Lesson | Topic                          | Practical outcome                                                      |
| ------ | ------------------------------ | ---------------------------------------------------------------------- |
| 08     | Matplotlib Fundamentals        | Create line, bar, scatter and histogram charts                         |
| 09     | Chart Customization and Saving | Add titles, labels, legends, formatting and save charts as image files |

### Module 4 — Data Cleaning and EDA

Purpose: Make data reliable before analyzing it.

| Lesson | Topic                                  | Practical outcome                                                                                                          |
| ------ | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 10     | Data Cleaning                          | Handle missing values, duplicates, incorrect data types and inconsistent categories                                        |
| 11     | Exploratory Data Analysis (EDA)        | Examine distributions, outliers, relationships and trends                                                                  |
| 12     | Business Metrics and Insight Reporting | Calculate revenue, order counts, average order value, top products and monthly growth; write conclusions supported by data |

### Module 5 — Final Project

Lesson 13 — Sales Data Analysis Dashboard

Build a complete analysis workflow using NumPy, Pandas and Matplotlib.

The dashboard/report should answer questions such as:

- What is the total revenue and number of orders?
- Which products and categories generate the most revenue?
- Which months have the highest and lowest sales?
- What is the average order value?
- Are there missing records, duplicates or unusual values?
- What business recommendations can be supported by the analysis?

Expected deliverables:

- A sample sales dataset in CSV format.
- Python analysis code organized into reusable functions.
- A cleaned dataset and analysis summary.
- Charts for monthly trends, category performance and top products.
- A saved dashboard/report with business insights.
- Tests for important calculations and data-cleaning functions.

## 3. Recommended repository structure

Use this structure in your existing `AI-Learning` repository, following the numbered lesson convention you've been using.

```

python/
└── 07-data-science-foundation/
    ├── README.md
    ├── ROADMAP.md
    ├── requirements.txt
    ├── lessons/
    │   ├── 01-numpy-introduction/
    │   │   └── README.md
    │   ├── 02-numpy-array-operations/
    │   │   └── README.md
    │   ├── 03-numpy-statistics-broadcasting/
    │   │   └── README.md
    │   ├── 04-pandas-introduction/
    │   │   └── README.md
    │   ├── 05-reading-and-inspecting-data/
    │   │   └── README.md
    │   ├── 06-filtering-and-transforming-data/
    │   │   └── README.md
    │   ├── 07-grouping-merging-and-aggregation/
    │   │   └── README.md
    │   ├── 08-matplotlib-fundamentals/
    │   │   └── README.md
    │   ├── 09-chart-customization/
    │   │   └── README.md
    │   ├── 10-data-cleaning/
    │   │   └── README.md
    │   ├── 11-exploratory-data-analysis/
    │   │   └── README.md
    │   ├── 12-business-metrics-and-insights/
    │   │   └── README.md
    │   └── 13-sales-analysis-dashboard/
    │       └── README.md
    └── projects/
        └── sales-data-analysis-dashboard/
            ├── README.md
            ├── data/
            │   └── raw/
            ├── src/
            ├── tests/
            ├── reports/
            └── outputs/

```

## 4. Dependencies

Keep the initial dependencies simple:

```
numpy
pandas
matplotlib
pytest
```

Install them inside a dedicated virtual environment for this part. Keep your Magento environment and completed API project untouched.

## 5. Completion criteria

By the end of Part 7, you should be able to:

- Perform numerical calculations with NumPy.
- Read, filter, transform and aggregate data using Pandas.
- Create and save charts with Matplotlib.
- Clean messy datasets and validate data quality.
- Perform EDA and explain findings using evidence.
- Complete the Sales Data Analysis Dashboard project.
- Commit the code and documentation to GitHub.

Recommended next step: Start Lesson 01 — NumPy Introduction and Arrays. Each lesson should include the concepts, practical examples, a comparison to familiar PHP/Magento concepts where useful, hands-on exercises, homework and a code review before moving on.