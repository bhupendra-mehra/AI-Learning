# 📘 Lesson 13 – Module 2

# Reading Files

**Estimated Time:** 25–30 minutes

---

# Learning Objectives

By the end of this module, you'll understand:

* ✅ What is `open()`
* ✅ File paths
* ✅ `read()`
* ✅ `readline()`
* ✅ `readlines()`
* ✅ File pointer
* ✅ `close()`
* ✅ Common exceptions
* ✅ Production best practices

---

# What is `open()`?

Before Python can read a file, it must first **open** it.

Think of a file like a book.

```text
Book on Shelf

↓

Open Book

↓

Read Contents

↓

Close Book
```

Python follows the same process.

```text
Open File

↓

Read Data

↓

Close File
```

---

# Syntax

```python
file = open("filename.txt", "r")
```

Let's understand each part.

---

## `file`

```python
file = ...
```

This is a **file object**.

It represents the opened file.

---

## `"filename.txt"`

The file you want to open.

Example

```python
notes.txt

sales.txt

customers.txt
```

---

## `"r"`

Means

```text
Read Mode
```

Python understands several modes.

| Mode | Meaning         |
| ---- | --------------- |
| `r`  | Read            |
| `w`  | Write           |
| `a`  | Append          |
| `x`  | Create New File |

We'll study the others later.

---

# Example

Suppose we have

```
student.txt
```

Contents

```text
Bhupendra
Python
AI Engineering
```

Code

```python
file = open("student.txt", "r")

print(file)
```

Output

```text
<_io.TextIOWrapper name='student.txt' mode='r' encoding='UTF-8'>
```

Notice

Nothing from the file is printed.

Because

We only **opened** it.

We haven't **read** it.

---

# Reading the Entire File

Use

```python
read()
```

Example

```python
file = open("student.txt", "r")

data = file.read()

print(data)
```

Output

```text
Bhupendra
Python
AI Engineering
```

---

# What does `read()` return?

It returns a **single string**.

Example

File

```text
Hello
Python
```

Python sees it as

```python
"Hello\nPython"
```

Notice

The newline character (`\n`) is part of the string.

---

# Checking the Data Type

```python
file = open("student.txt")

data = file.read()

print(type(data))
```

Output

```text
<class 'str'>
```

Very important interview question.

---

# File Pointer

This is one of the most misunderstood concepts.

Imagine reading a book.

```text
Page 1

↓

Page 2

↓

Page 3
```

Your finger moves.

The finger represents the **file pointer**.

---

Initially

```text
Beginning

↓

Bhupendra

Python

AI Engineering
```

---

After

```python
file.read()
```

Pointer moves to the end.

```text
Bhupendra

Python

AI Engineering

             ▲
           Pointer
```

---

Now

```python
print(file.read())
```

Output

```text
```

Nothing.

Why?

Because

Pointer is already at the end.

---

# Example

```python
file = open("student.txt")

print(file.read())

print(file.read())
```

Output

```text
Bhupendra
Python
AI Engineering


```

Second call returns an empty string.

---

# Reading One Line

Use

```python
readline()
```

Example

```python
file = open("student.txt")

print(file.readline())
```

Output

```text
Bhupendra
```

Pointer moves to the next line.

---

Again

```python
print(file.readline())
```

Output

```text
Python
```

Again

```python
print(file.readline())
```

Output

```text
AI Engineering
```

Again

```python
print(file.readline())
```

Output

```text
```

End of file.

---

# Reading All Lines

Use

```python
readlines()
```

Example

```python
file = open("student.txt")

data = file.readlines()

print(data)
```

Output

```python
['Bhupendra\n',
 'Python\n',
 'AI Engineering']
```

Notice

This time

Python returns a

```python
list
```

not a string.

---

# Comparison

| Method        | Returns              |
| ------------- | -------------------- |
| `read()`      | Entire file as `str` |
| `readline()`  | One line as `str`    |
| `readlines()` | List of strings      |

---

# When to Use What?

### `read()`

Small files.

```text
config.txt
```

---

### `readline()`

Read one line at a time.

Useful for very large files.

---

### `readlines()`

When you need each line separately.

---

# Closing the File

Always close it.

```python
file.close()
```

Example

```python
file = open("student.txt")

print(file.read())

file.close()
```

---

# Why Close the File?

Closing a file:

* Releases system resources.
* Flushes pending operations (important when writing).
* Prevents resource leaks.
* Allows other programs to safely access the file.

We'll later learn `with open(...)` which closes the file automatically and is the preferred production approach.

---

# Common Exceptions

## File Not Found

```python
open("abc.txt")
```

Output

```text
FileNotFoundError
```

---

## Permission Error

Trying to open a protected file.

```text
PermissionError
```

---

# Real AI Example

```python
file = open("training_data.csv")

dataset = file.read()
```

---

# Magento Example

```text
products.csv

↓

Read File

↓

Import Products
```

Exactly the same idea.

---

# Best Practice (Preview)

Instead of

```python
file = open("student.txt")

data = file.read()

file.close()
```

Professionals write

```python
with open("student.txt", "r") as file:
    data = file.read()
```

We'll understand **why** in Module 6.

---

# Mini Exercise

Create a file named:

```text
student.txt
```

Contents

```text
Bhupendra
Python
AI Engineering
```

Now answer:

### Q1

What will this print?

```python
file = open("student.txt")

print(file.read())
```

---

### Q2

What will this print?

```python
file = open("student.txt")

print(file.readline())

print(file.readline())
```

---

### Q3

What is the datatype returned by:

```python
file.readlines()
```

---

### Q4

After calling

```python
file.read()
```

where is the file pointer?

---

# Interview Questions

### Q1

What is the difference between:

```python
read()

readline()

readlines()
```

---

### Q2

Why should we close a file?

---

### Q3

What happens if the file does not exist?

---

### Q4

What does `open()` return?

---

# Lesson Progress

```text
Lesson 13

✅ Module 1 – Introduction
▶ Module 2 – Reading Files
⏳ Module 3 – Writing Files
⏳ Module 4 – CSV
⏳ Module 5 – JSON
⏳ Module 6 – Best Practices
⏳ Module 7 – Sales Report Generator
⏳ Module 8 – Interview Questions
```

---

## 💡 Senior Developer Tip

Notice that all our examples currently use:

```python
file = open(...)
```

This is intentional because I want you to understand **how file objects work internally**.

Once you're comfortable with `open()`, `read()`, `readline()`, `readlines()`, and `close()`, we'll switch to the **professional approach** using:

```python
with open("student.txt", "r") as file:
```

By learning both approaches, you'll understand not just **what** to write, but **why** modern Python code is written that way.
