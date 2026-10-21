# 🚀 Module 1 – Introduction to File Handling

**Estimated Time:** 15 minutes

---

# Learning Objectives

By the end of this module, you'll understand:

* ✅ What is a file?
* ✅ Why file handling is needed
* ✅ Types of files
* ✅ File paths
* ✅ File modes overview
* ✅ How Python interacts with files

---

# What is a File?

A **file** is a collection of data stored permanently on a storage device (SSD, HDD, USB, etc.).

Unlike variables:

```python
name = "Bhupendra"
```

which disappear when the program ends, files remain available even after you close the application.

Example:

```text
sales.csv
customers.json
report.txt
error.log
products.csv
```

These files can be read, modified, and reused by different programs.

---

# Memory vs File Storage

```text
Variables (RAM)

Program Starts
      │
      ▼
Store Data
      │
      ▼
Program Ends
      │
      ▼
Data Lost
```

```text
Files (Disk)

Program Starts
      │
      ▼
Read File
      │
      ▼
Program Ends
      │
      ▼
Data Still Exists
```

---

# Why Do We Use Files?

Without files:

* User data disappears.
* Reports cannot be saved.
* AI datasets cannot be loaded.
* Logs cannot be stored.
* Configurations are lost.

Files make data **persistent**.

---

# Types of Files

## 1. Text Files

Human-readable.

Examples:

```text
notes.txt
report.txt
data.csv
config.json
```

---

## 2. Binary Files

Not human-readable.

Examples:

```text
photo.jpg
video.mp4
model.pkl
program.exe
```

We'll focus on **text files** in this lesson.

---

# Common File Extensions

| Extension | Purpose                     |
| --------- | --------------------------- |
| `.txt`    | Plain text                  |
| `.csv`    | Tabular data                |
| `.json`   | Structured data             |
| `.log`    | Logs                        |
| `.xml`    | Configuration/Data exchange |

---

# Real-World Examples

### AI

```text
dataset.csv
```

Stores training data.

---

### Magento

```text
products.csv
```

Used for product import/export.

---

### Banking

```text
transactions.csv
```

Stores transaction history.

---

### E-commerce

```text
orders.json
```

Stores order information.

---

# How Python Works with Files

The general workflow is:

```text
Open File
    ↓
Read / Write Data
    ↓
Close File
```

In later modules, you'll learn how `with open()` automatically handles the closing step.

---

# Preview of File Modes

We'll explore these in detail later:

| Mode | Meaning                  |
| ---- | ------------------------ |
| `r`  | Read                     |
| `w`  | Write (overwrite/create) |
| `a`  | Append                   |
| `x`  | Create new file          |
| `r+` | Read and write           |

---

# Mini Exercise

Without running any code, answer these:

### Q1

Where is variable data stored while a program is running?

---

### Q2

What happens to variables after the program ends?

---

### Q3

Which file type would you use to store:

* Customer names?
* Product list?
* AI training dataset?
* Application logs?

---

# Interview Questions

### Q1. What is file handling?

**Answer:** File handling is the process of creating, reading, writing, updating, and managing files so that data can be stored permanently.

---

### Q2. Why do we need file handling?

**Answer:** Variables exist only while a program is running. File handling allows data to persist after the program ends and enables sharing data between different applications.

---

### Q3. What is the difference between a text file and a binary file?

| Text File                         | Binary File                      |
| --------------------------------- | -------------------------------- |
| Human-readable                    | Not human-readable               |
| Examples: `.txt`, `.csv`, `.json` | Examples: `.jpg`, `.mp4`, `.exe` |

---

## 📈 Lesson Progress

```text
Lesson 13 – File Handling

▶ Module 1 – Introduction
⏳ Module 2 – Reading Files
⏳ Module 3 – Writing & Appending
⏳ Module 4 – CSV
⏳ Module 5 – JSON
⏳ Module 6 – Best Practices
⏳ Module 7 – Sales Report Generator
⏳ Module 8 – Interview Revision
```

### 📝 Your Task

Answer the **Mini Exercise** questions, and then we'll move to **Module 2 – Reading Files**, where you'll start working with actual files using Python.
