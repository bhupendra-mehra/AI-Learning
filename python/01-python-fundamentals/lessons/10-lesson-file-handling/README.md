# 📘 Lesson 13 Overview – File Handling

> **Estimated Time:** 2–3 Hours

**Difficulty:** ⭐⭐⭐☆☆ (Intermediate)

**Prerequisites:**

* ✅ Functions
* ✅ Loops
* ✅ OOP
* ✅ Exception Handling

---

# Why This Lesson Matters

Until now, every program you've written stored data only in **memory (RAM)**.

Example:

```python
name = "Bhupendra"
balance = 5000
```

When the program ends:

```text
Program Closed
↓

All Data Lost
```

That's not how real applications work.

Examples:

* Magento stores product information in files.
* AI models load datasets from CSV and JSON.
* Applications generate logs.
* Reports are exported to CSV or PDF.
* Configuration is often stored in JSON.

To make data **persistent**, we use **files**.

---

# AI Connection 🎯

Every AI project uses files.

Examples:

```text
dataset.csv
model.json
config.json
logs.txt
training_data.csv
```

Without file handling, you cannot:

* Load datasets.
* Save trained models.
* Read prompts.
* Store AI responses.
* Process logs.

---

# Magento Connection 🛒

Magento uses file handling extensively:

* Product Import (CSV)
* Customer Export (CSV)
* Order Export
* System Logs
* Exception Logs
* JSON Configuration
* Media Files
* Report Generation

---

# Estimated Time

| Activity | Time       |
| -------- | ---------- |
| Modules  | 2 Hours    |
| Practice | 30 Minutes |
| Project  | 45 Minutes |
| Revision | 15 Minutes |

**Total:** **2.5–3 Hours**

---

# Lesson Modules

| Module   | Topic                          | Time   |
| -------- | ------------------------------ | ------ |
| Module 1 | Introduction to File Handling  | 15 min |
| Module 2 | Reading Files                  | 25 min |
| Module 3 | Writing & Appending Files      | 25 min |
| Module 4 | Working with CSV Files         | 30 min |
| Module 5 | Working with JSON Files        | 30 min |
| Module 6 | File Handling Best Practices   | 20 min |
| Module 7 | Sales Report Generator Project | 45 min |
| Module 8 | Interview Questions & Revision | 20 min |

---

# Module Details

## Module 1 – Introduction

You'll learn:

* What is a file?
* Why files are used
* File paths
* File modes
* Text vs Binary files

---

## Module 2 – Reading Files

Topics:

* `open()`
* `read()`
* `readline()`
* `readlines()`
* Closing files

---

## Module 3 – Writing Files

Topics:

* `write()`
* `writelines()`
* Append mode
* Overwriting files
* Creating new files

---

## Module 4 – CSV Files

Topics:

* `csv.reader`
* `csv.writer`
* Reading CSV
* Writing CSV
* Processing tabular data

---

## Module 5 – JSON Files

Topics:

* `json.load()`
* `json.dump()`
* `json.loads()`
* `json.dumps()`
* Python Dictionary ↔ JSON

---

## Module 6 – Best Practices

Topics:

* `with open()`
* Context Managers
* File Exceptions
* Path Handling
* Production Coding Standards

---

## Module 7 – Project

### 📊 Sales Report Generator

We'll build a project that:

* Reads sales data from a CSV file.
* Calculates:

  * Total Sales
  * Highest Sale
  * Lowest Sale
  * Average Sale
* Generates a text report.
* Exports summary as JSON.
* Uses exception handling throughout.

---

## Module 8 – Interview Preparation

We'll cover:

* Common interview questions.
* Coding exercises.
* Best practices.
* Real-world scenarios.

---

# What You'll Learn

By the end of this lesson you'll be able to:

* Read files.
* Write files.
* Append data.
* Process CSV files.
* Process JSON files.
* Build report generators.
* Handle file-related exceptions.

---

# Learning Outcome

After completing this lesson you'll be able to build:

* Log Reader
* CSV Import Tool
* Report Generator
* Configuration Loader
* AI Dataset Reader
* Magento CSV Import/Export Utilities

---

# Interview Preparation

Topics include:

* Difference between `read()`, `readline()`, and `readlines()`.
* File modes (`r`, `w`, `a`, `x`, `r+`).
* Why use `with open()`?
* CSV vs JSON.
* `json.load()` vs `json.loads()`.
* Common file-related exceptions.

---

# Lesson Completion Checklist

By the end of Lesson 13, you should be able to:

* ⬜ Open and close files.
* ⬜ Read text files.
* ⬜ Write and append data.
* ⬜ Work with CSV files.
* ⬜ Work with JSON files.
* ⬜ Use `with open()` correctly.
* ⬜ Handle file exceptions.
* ⬜ Complete the Sales Report Generator project.

---

# 📚 Resources (Optional)

We'll rely primarily on the lesson itself, but the official Python documentation on `open()`, `csv`, and `json` modules is a good reference as you progress.

---

# Lesson Summary

| Item                 | Details                   |
| -------------------- | ------------------------- |
| Lesson               | Lesson 13 – File Handling |
| Modules              | 8                         |
| Estimated Time       | 2.5–3 Hours               |
| Difficulty           | ⭐⭐⭐☆☆                     |
| Project              | Sales Report Generator    |
| AI Relevance         | ⭐⭐⭐⭐⭐                     |
| Magento Relevance    | ⭐⭐⭐⭐⭐                     |
| Interview Importance | ⭐⭐⭐⭐⭐                     |

---
