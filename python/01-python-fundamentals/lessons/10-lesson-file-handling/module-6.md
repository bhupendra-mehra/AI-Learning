# 📘 Lesson 13 – Module 6

# File Handling Best Practices

**Estimated Time:** 20–25 minutes

---

# Learning Objectives

By the end of this module, you'll understand:

* ✅ Why `with open()` is preferred
* ✅ Context Managers
* ✅ Automatic file closing
* ✅ File-related exceptions
* ✅ Relative vs Absolute paths
* ✅ `pathlib` basics
* ✅ Production coding standards
* ✅ Common interview questions

---

# Why Best Practices Matter

Suppose you write:

```python
file = open("student.txt", "r")

data = file.read()

print(data)

file.close()
```

This works.

But what if an exception occurs before `close()`?

Example:

```python
file = open("student.txt", "r")

print(10 / 0)

file.close()
```

Output:

```text
ZeroDivisionError
```

Did Python execute:

```python
file.close()
```

❌ No.

The file remains open until Python cleans it up later.

---

# The Professional Solution

Use a **Context Manager**.

```python
with open("student.txt", "r") as file:

    data = file.read()

    print(data)
```

No `close()` needed.

---

# What Happens Internally?

Think of it like this:

```text
Enter with block

↓

Open File

↓

Execute Code

↓

Exception?

↓

Yes or No

↓

Close File Automatically
```

Whether the code succeeds or fails, the file is closed.

---

# Comparison

### Traditional

```python
file = open("student.txt")

data = file.read()

file.close()
```

---

### Professional

```python
with open("student.txt") as file:

    data = file.read()
```

Cleaner.

Safer.

Less code.

---

# Why is it Called a Context Manager?

The `with` statement creates a **context**.

Inside the block:

```python
with open(...) as file:
```

the file is available.

Outside the block:

```python
print(file.read())
```

❌ Error.

Because the file has already been closed.

---

# Demonstration

```python
with open("student.txt") as file:
    print(file.closed)
```

Output

```text
False
```

After the block:

```python
print(file.closed)
```

Output

```text
True
```

A nice interview question.

---

# File Exceptions

---

## FileNotFoundError

```python
with open("abc.txt") as file:
    pass
```

Output

```text
FileNotFoundError
```

Handle it

```python
try:
    with open("abc.txt") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")
```

---

## PermissionError

Trying to access a protected file.

```text
PermissionError
```

---

## JSONDecodeError

Suppose

```json
{
"name":"John",
age:25
}
```

Invalid JSON.

Reading it

```python
json.load(file)
```

raises

```text
JSONDecodeError
```

---

# Relative Path

Example

```python
open("student.txt")
```

Python searches in the **current working directory**.

Example

```text
project/

│

├── main.py

├── student.txt
```

Works.

---

# Absolute Path

```python
open("C:/Users/Bhupendra/Documents/student.txt")
```

Contains the complete path.

---

# Which Should We Use?

| Relative  | Absolute                |
| --------- | ----------------------- |
| Portable  | Machine-specific        |
| Preferred | Rarely used in projects |

Most real projects use **relative paths**.

---

# `pathlib`

Python's modern way of handling paths.

```python
from pathlib import Path

path = Path("student.txt")

print(path.exists())
```

Output

```text
True
```

---

# Check File Exists

Instead of

```python
try:
    open("student.txt")
except FileNotFoundError:
    ...
```

You can do

```python
from pathlib import Path

path = Path("student.txt")

if path.exists():
    print("File exists")
```

---

# Production Example

```python
from pathlib import Path
import json

path = Path("config.json")

if path.exists():

    with open(path) as file:

        config = json.load(file)

else:

    print("Configuration file missing.")
```

This is much closer to production-quality code.

---

# Best Practices Checklist

Always:

✅ Use `with open()`

✅ Handle exceptions

✅ Prefer relative paths

✅ Validate file existence

✅ Use meaningful filenames

✅ Close files automatically

Avoid:

❌ Leaving files open

❌ Hardcoding machine-specific paths

❌ Ignoring exceptions

❌ Using `"w"` carelessly

---

# Magento Example

Magento log files

```text
var/log/system.log
```

Before reading:

* Check if the file exists.
* Handle permission issues.
* Read safely.

---

# AI Example

Dataset loading

```python
from pathlib import Path

dataset = Path("training.csv")

if dataset.exists():

    print("Ready for training")

else:

    print("Dataset missing")
```

Almost every AI project performs these checks.

---

# Common Interview Questions

### Q1

Why is

```python
with open()
```

better than

```python
open()
```

?

**Answer:**

Because it automatically closes the file, even if an exception occurs.

---

### Q2

What is a Context Manager?

**Answer:**

An object that automatically manages resources like files by handling setup and cleanup.

---

### Q3

Why use relative paths?

**Answer:**

They make the application portable across different computers and operating systems.

---

### Q4

What does

```python
Path.exists()
```

return?

**Answer:**

`True` if the file or directory exists, otherwise `False`.

---

# Mini Exercise

Answer these questions.

---

### Q1

What is the output?

```python
with open("student.txt") as file:
    print(file.closed)

print(file.closed)
```

---

### Q2

Which is better?

```python
open()

or

with open()
```

Why?

---

### Q3

What exception is raised when:

```python
open("abc.txt")
```

and the file does not exist?

---

### Q4

What does this return?

```python
Path("student.txt").exists()
```

---

### Q5

Why are relative paths preferred in production applications?

---

# Interview Challenge ⭐⭐⭐

Suppose the interviewer asks:

```python
with open("student.txt") as file:
    pass

print(file.closed)
```

What is the output?

Think carefully.

Many beginners answer incorrectly.

(Hint: The `file` variable still exists after the `with` block, but the underlying file has been closed.)

---

# Lesson Progress

```text
Lesson 13 – File Handling

✅ Module 1 – Introduction
✅ Module 2 – Reading Files
✅ Module 3 – Writing & Appending
✅ Module 4 – CSV Files
✅ Module 5 – JSON Files
▶ Module 6 – Best Practices
⏳ Module 7 – Sales Report Generator
⏳ Module 8 – Interview Revision
```

---

# ⭐ Senior Developer Tip

You've probably noticed a pattern throughout the course:

* Variables
* Loops
* Functions
* OOP
* Exception Handling
* File Handling

All of these now come together.

A real program often looks like this:

```python
from pathlib import Path
import json

path = Path("config.json")

if path.exists():
    try:
        with open(path, "r") as file:
            config = json.load(file)
            print(config)
    except json.JSONDecodeError:
        print("Invalid JSON configuration.")
```

This single example uses concepts from multiple lessons you've already completed. That's exactly how professional Python development works—small concepts combine to solve real-world problems.

---

## 📝 Your Task

Answer the five mini-exercise questions. After I review them, we'll begin **Module 7 – Sales Report Generator**, where we'll build a complete project using:

* File Handling
* CSV
* JSON
* OOP
* Exception Handling

This project will serve as the capstone for Lesson 13.
