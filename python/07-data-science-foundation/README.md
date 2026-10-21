# Part 7 — Data Science Foundation

## Overview

**Goal:** Learn the libraries and techniques used by almost every AI engineer to analyze, manipulate, clean, and visualize data.

This part focuses on practical Python data analysis skills that will prepare me for the upcoming Machine Learning, AI Applications, AI Agents, and Production AI sections of my learning roadmap.

## Learning Objectives

By completing this part, I will be able to:

- Perform numerical operations using NumPy.
- Manipulate and analyze tabular data using Pandas.
- Create meaningful charts using Matplotlib.
- Clean datasets by handling missing values, duplicates, and inconsistent data.
- Perform Exploratory Data Analysis (EDA).
- Extract business insights from data.
- Build a Sales Data Analysis Dashboard project.

## Technologies and Libraries

| Technology | Purpose |
|---|---|
| Python | Data analysis programming |
| NumPy | Numerical computing and array operations |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualization |
| pytest | Testing important calculations and functions |
| Git and GitHub | Version control and project documentation |

## Repository Structure

```text
07-data-science-foundation/
├── README.md
├── ROADMAP.md
├── requirements.txt
├── lessons/
│   ├── 01-numpy-introduction/
│   ├── 02-numpy-array-operations/
│   ├── 03-numpy-statistics-broadcasting/
│   ├── 04-pandas-introduction/
│   ├── 05-reading-and-inspecting-data/
│   ├── 06-filtering-and-transforming-data/
│   ├── 07-grouping-merging-and-aggregation/
│   ├── 08-matplotlib-fundamentals/
│   ├── 09-chart-customization/
│   ├── 10-data-cleaning/
│   ├── 11-exploratory-data-analysis/
│   ├── 12-business-metrics-and-insights/
│   └── 13-sales-analysis-dashboard/
└── projects/
    └── sales-data-analysis-dashboard/
        ├── README.md
        ├── data/
        ├── src/
        ├── tests/
        ├── reports/
        └── outputs/
```

See [ROADMAP.md](ROADMAP.md) for the complete lesson-by-lesson syllabus and project requirements.

## Setup

### 1. Navigate to the Part 7 directory

```bash
cd python/07-data-science-foundation
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on Linux or WSL:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Verify the installation

```bash
python -c "import numpy, pandas, matplotlib; print('Data science libraries installed successfully')"
```

## Final Project — Sales Data Analysis Dashboard

The final project will combine the concepts learned throughout this part to analyze sales data and present useful business insights.

### Expected capabilities

- Load sales data from CSV files.
- Inspect and clean the dataset.
- Calculate total revenue, order counts, and average order value.
- Identify top-performing products and categories.
- Analyze monthly sales trends.
- Create visualizations using Matplotlib.
- Generate a report containing findings and recommendations.
- Test important data-processing and calculation functions.

## Skills Developed

- Data Analysis
- Data Manipulation
- Numerical Computing
- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Business Insight Reporting

## Progress Tracker

- [ ] Lesson 01 — NumPy Introduction and Arrays
- [ ] Lesson 02 — Array Indexing, Slicing and Shapes
- [ ] Lesson 03 — Vectorized Operations, Statistics and Broadcasting
- [ ] Lesson 04 — Pandas Introduction, Series and DataFrames
- [ ] Lesson 05 — Reading CSV and Inspecting Data
- [ ] Lesson 06 — Selecting, Filtering, Sorting and Transforming Data
- [ ] Lesson 07 — Grouping, Aggregation, Merging and Exporting
- [ ] Lesson 08 — Matplotlib Fundamentals
- [ ] Lesson 09 — Chart Customization and Saving
- [ ] Lesson 10 — Data Cleaning
- [ ] Lesson 11 — Exploratory Data Analysis (EDA)
- [ ] Lesson 12 — Business Metrics and Insight Reporting
- [ ] Lesson 13 — Sales Data Analysis Dashboard

## Completion Criteria

Part 7 will be complete when all lessons have been completed, the Sales Data Analysis Dashboard has been built and tested, and the code and documentation have been committed to GitHub.

**Next step:** Start Lesson 01 — NumPy Introduction and Arrays.
