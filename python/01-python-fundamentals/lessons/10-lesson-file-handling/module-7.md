# 📘 Lesson 13 – Module 7

# Capstone Project – Sales Report Generator

## Estimated Time

| Activity       | Time   |
| -------------- | ------ |
| Project Design | 15 min |
| Coding         | 60 min |
| Testing        | 20 min |
| Refactoring    | 20 min |

**Total:** ~2 hours

---

# Difficulty

⭐⭐⭐☆☆ (Intermediate)

---

# Project Goal

We have a CSV file containing sales data.

Example:

**sales.csv**

```csv
Product,Quantity,Price
Laptop,2,1200
Mouse,5,25
Keyboard,3,80
Monitor,2,300
```

Our program will:

```
sales.csv

↓

Read CSV

↓

Calculate Statistics

↓

Display Summary

↓

Save Report.txt

↓

Save Report.json
```

---

# Final Output

```text
========== SALES REPORT ==========

Total Products : 4

Total Quantity : 12

Total Sales : 3415

Highest Sale : Laptop ($2400)

Lowest Sale : Mouse ($125)

Average Sale : 853.75

=================================
```

---

# What We'll Learn

This project uses:

| Topic              | Used |
| ------------------ | ---- |
| Functions          | ✅    |
| Loops              | ✅    |
| Lists              | ✅    |
| Dictionaries       | ✅    |
| CSV                | ✅    |
| JSON               | ✅    |
| File Handling      | ✅    |
| Exception Handling | ✅    |
| pathlib            | ✅    |

---

# Project Structure

```text
sales_report.py

│

├── SalesReport class

│       __init__()

│       read_sales()

│       calculate_summary()

│       display_report()

│       save_text_report()

│       save_json_report()

│

└── main()
```

---

# Why Use a Class?

Could we write everything as functions?

Yes.

But using a class keeps:

* Sales data
* Summary
* Methods

together in one place.

This follows the OOP principles you learned in Lesson 11.

---

# Project Flow

```text
Start

↓

Read CSV File

↓

Store Sales Data

↓

Calculate Summary

↓

Display Summary

↓

Save TXT Report

↓

Save JSON Report

↓

End
```

---

# Step 1 – Create the Class

```python
from pathlib import Path
import csv
import json


class SalesReport:

    def __init__(self):
        self.sales = []
        self.summary = {}
```

---

# Understanding the Constructor

```python
self.sales = []
```

Stores every row from the CSV.

Example:

```python
[
    {
        "Product": "Laptop",
        "Quantity": 2,
        "Price": 1200
    },
    {
        "Product": "Mouse",
        "Quantity": 5,
        "Price": 25
    }
]
```

---

```python
self.summary = {}
```

Stores calculated results.

Example:

```python
{
    "total_sales": 3415,
    "highest_sale": "Laptop",
    "average_sale": 853.75
}
```

---

# Why Use Two Variables?

Because they have different responsibilities.

## `sales`

Stores **raw data**.

```
Laptop
Mouse
Keyboard
```

---

## `summary`

Stores **processed data**.

```
Total Sales

Average

Highest

Lowest
```

This separation makes the code cleaner and easier to maintain.

---

# Interview Question ⭐

### Why not calculate everything directly while reading the CSV?

Good question.

Because:

* We may need the raw data later.
* We can perform different analyses without reading the file again.
* It separates **data loading** from **data processing**, which is a common design principle.

---

# Mini Exercise 1

Create only this:

```python
from pathlib import Path
import csv
import json


class SalesReport:

    def __init__(self):
        self.sales = []
        self.summary = {}
```

Nothing else yet.

---

# ⭐ Senior Developer Tip

Notice we're importing all required modules at the beginning:

```python
from pathlib import Path
import csv
import json
```

Even though we won't use all of them immediately.

This is common in real projects because it clearly shows the file's dependencies and avoids scattering imports throughout the code.

---
