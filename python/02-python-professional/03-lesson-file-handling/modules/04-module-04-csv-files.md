# 📘 Lesson 13 – Module 4

# Working with CSV Files

**Estimated Time:** 30–35 minutes

---

# Learning Objectives

By the end of this module, you'll understand:

* ✅ What is a CSV file?
* ✅ Why CSV is widely used
* ✅ `csv` module
* ✅ `csv.reader()`
* ✅ `csv.writer()`
* ✅ Reading CSV files
* ✅ Writing CSV files
* ✅ Processing CSV data
* ✅ Magento & AI use cases
* ✅ Production best practices

---

# What is CSV?

CSV stands for:

```text
Comma Separated Values
```

It stores **tabular data** (rows and columns).

Example:

```text
Name,Age,City
Bhupendra,37,Mumbai
Rahul,28,Delhi
Priya,30,Pune
```

Think of it as a simple spreadsheet without formatting.

---

# Why Use CSV?

Suppose you have 10,000 products.

Instead of:

```text
Product 1

Product 2

Product 3
```

CSV organizes them neatly.

```text
Name,Price,Qty

Laptop,1200,5

Mouse,25,100

Keyboard,80,50
```

---

# Real-World Uses

## Magento

```text
products.csv
customers.csv
orders.csv
```

Used for:

* Product Import
* Product Export
* Customer Export
* Inventory Updates

---

## AI

```text
dataset.csv
```

Used for:

* Training data
* Data preprocessing
* Machine Learning datasets

---

# Python CSV Module

Python provides a built-in module:

```python
import csv
```

No installation is required.

---

# Sample CSV File

Create:

```text
students.csv
```

Contents

```csv
Name,Age,Course
Bhupendra,37,Python
Rahul,25,AI
Priya,28,Data Science
```

---

# Reading CSV

```python
import csv

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output

```python
['Name', 'Age', 'Course']
['Bhupendra', '37', 'Python']
['Rahul', '25', 'AI']
['Priya', '28', 'Data Science']
```

---

# Understanding `reader`

```python
reader = csv.reader(file)
```

This does **not** return the entire file immediately.

It creates an **iterator**.

Remember Lesson 8?

An iterator produces one row at a time.

---

# Why Use a Loop?

```python
for row in reader:
```

Each iteration returns one row.

Iteration 1

```python
['Name', 'Age', 'Course']
```

Iteration 2

```python
['Bhupendra', '37', 'Python']
```

Iteration 3

```python
['Rahul', '25', 'AI']
```

---

# Data Type

What is

```python
row
```

?

Answer:

```python
list
```

Example

```python
['Bhupendra', '37', 'Python']
```

---

# Accessing Columns

Suppose

```python
row = ['Bhupendra', '37', 'Python']
```

Then

```python
print(row[0])
```

Output

```text
Bhupendra
```

---

```python
print(row[1])
```

Output

```text
37
```

---

```python
print(row[2])
```

Output

```text
Python
```

---

# Skipping Header

Most CSV files contain a header.

Example

```text
Name,Age,Course
```

We usually don't process it as data.

Use:

```python
next(reader)
```

Example

```python
import csv

with open("students.csv") as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)
```

Output

```python
['Bhupendra', '37', 'Python']
['Rahul', '25', 'AI']
['Priya', '28', 'Data Science']
```

---

# Writing CSV

```python
import csv

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Course"])

    writer.writerow(["Bhupendra", 37, "Python"])

    writer.writerow(["Rahul", 25, "AI"])
```

---

# Why `newline=""`?

This is a common interview question.

Without:

```python
newline=""
```

some operating systems (especially Windows) may insert extra blank lines.

So the recommended practice is:

```python
with open("students.csv", "w", newline="")
```

Always include it when writing CSV files.

---

# Writing Multiple Rows

Instead of

```python
writer.writerow(...)
writer.writerow(...)
writer.writerow(...)
```

Use

```python
writer.writerows([
    ["Name", "Age", "Course"],
    ["Bhupendra", 37, "Python"],
    ["Rahul", 25, "AI"],
    ["Priya", 28, "Data Science"]
])
```

Cleaner and easier to maintain.

---

# Reading Example

Suppose

```csv
Product,Price,Qty
Laptop,1200,5
Mouse,25,100
Keyboard,80,50
```

Code

```python
import csv

with open("products.csv") as file:

    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(f"Product : {row[0]}")
        print(f"Price : {row[1]}")
        print(f"Quantity : {row[2]}")
        print("----------------")
```

---

# Magento Example

Magento Product Import

```text
sku,name,price,qty

ABC001,Laptop,1200,5
```

Magento reads one row at a time.

Exactly like

```python
for row in reader:
```

---

# AI Example

Training Data

```csv
Question,Answer

Hi,Hello

Bye,Goodbye
```

Python reads

each row

↓

converts it into data

↓

sends it to the AI model.

---

# Common Mistakes

## Forgetting

```python
import csv
```

Results in:

```text
NameError
```

---

## Forgetting

```python
next(reader)
```

Header is treated as data.

---

## Using

```python
row[5]
```

when only three columns exist.

Results in:

```text
IndexError
```

---

# Best Practices

* Use `with open()`.
* Skip headers with `next(reader)` when appropriate.
* Use meaningful column indexes.
* Validate data before processing.
* Handle exceptions for missing files and malformed rows.

---

# Mini Exercise

Create:

```text
employees.csv
```

Contents:

```csv
Name,Department,Salary
John,IT,5000
Alice,HR,4500
Bob,Finance,6000
```

Then answer:

### Q1

What is the datatype of:

```python
row
```

inside

```python
for row in reader:
```

---

### Q2

Why do we use:

```python
next(reader)
```

---

### Q3

Write code to print only employee names.

---

### Q4

Which method writes a **single** row?

---

### Q5

Which method writes **multiple** rows?

---

# Interview Questions

### Q1

What does CSV stand for?

---

### Q2

Why is CSV commonly used?

---

### Q3

What is the difference between:

```python
writer.writerow()
```

and

```python
writer.writerows()
```

---

### Q4

Why do we use:

```python
newline=""
```

while writing CSV?

---

# ⭐ Senior Developer Tip

You already know lists and loops.

A CSV reader simply gives you:

```python
['John', 'IT', '5000']
```

Everything you've learned about list indexing, loops, conditionals, and exception handling now applies directly.

That's why Python fundamentals are so important—they carry over into real-world tasks like CSV processing.

---

# Lesson Progress

```text
Lesson 13 – File Handling

✅ Module 1 – Introduction
✅ Module 2 – Reading Files
✅ Module 3 – Writing & Appending
▶ Module 4 – CSV Files
⏳ Module 5 – JSON Files
⏳ Module 6 – Best Practices
⏳ Module 7 – Sales Report Generator
⏳ Module 8 – Interview Questions
```

---

## 📝 Your Task

Answer the five mini-exercise questions. For **Q3**, write the actual Python code to print only the employee names. After I review it, we'll move to **Module 5 – Working with JSON Files**, which is another essential skill for both Magento integrations and AI development.
