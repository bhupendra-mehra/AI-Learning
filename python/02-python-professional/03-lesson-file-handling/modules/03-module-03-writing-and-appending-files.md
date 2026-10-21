# 📘 Lesson 13 – Module 3

# Writing & Appending Files

**Estimated Time:** 25–30 minutes

---

# Learning Objectives

By the end of this module, you'll understand:

* ✅ `write()`
* ✅ `writelines()`
* ✅ File Modes (`w`, `a`, `x`)
* ✅ Overwriting vs Appending
* ✅ Creating New Files
* ✅ Writing Multiple Lines
* ✅ Common Mistakes
* ✅ Production Best Practices

---

# What is File Writing?

So far we've only **read** files.

Now we'll **store data** into files.

Example:

```text
Program

↓

Write Report

↓

report.txt
```

Real-world examples:

* Saving user data
* Exporting reports
* Creating logs
* Writing AI responses
* Magento product exports

---

# File Modes Recap

| Mode | Purpose | File Exists?  | File Doesn't Exist? |
| ---- | ------- | ------------- | ------------------- |
| `r`  | Read    | ✅ Opens       | ❌ Error             |
| `w`  | Write   | ✅ Overwrites  | ✅ Creates           |
| `a`  | Append  | ✅ Adds at end | ✅ Creates           |
| `x`  | Create  | ❌ Error       | ✅ Creates           |

We'll focus on **w**, **a**, and **x**.

---

# Mode `w` (Write)

The **write mode** opens a file for writing.

If the file exists:

```text
student.txt

Hello
Python
AI
```

After:

```python
file = open("student.txt", "w")
```

Python immediately clears the file.

Result:

```text
student.txt

(empty)
```

This is a very important point.

> **Opening a file in `w` mode erases its existing contents immediately**, even before you call `write()`.

---

# Example

```python
file = open("student.txt", "w")

file.write("Hello World")

file.close()
```

File content:

```text
Hello World
```

---

# `write()`

Syntax

```python
file.write("Python")
```

Returns

```python
number_of_characters_written
```

Example

```python
file = open("student.txt", "w")

count = file.write("Python")

print(count)

file.close()
```

Output

```text
6
```

Because:

```text
Python

P y t h o n

6 characters
```

---

# Writing Multiple Lines

Incorrect

```python
file.write("Python")

file.write("AI")
```

Output

```text
PythonAI
```

---

Correct

```python
file.write("Python\n")

file.write("AI")
```

Output

```text
Python
AI
```

---

# `writelines()`

Used to write multiple strings.

Example

```python
lines = [
    "Python\n",
    "AI\n",
    "Machine Learning\n"
]

file = open("student.txt", "w")

file.writelines(lines)

file.close()
```

Output

```text
Python
AI
Machine Learning
```

---

# Important Interview Point

Many beginners think

```python
file.writelines(lines)
```

adds new lines automatically.

❌ Wrong.

It writes exactly what you provide.

Example

```python
lines = [
    "Python",
    "AI",
    "ML"
]
```

Output

```text
PythonAIML
```

You must include:

```python
"\n"
```

yourself.

---

# Append Mode (`a`)

Suppose

```text
student.txt

Python
```

Now

```python
file = open("student.txt", "a")

file.write("\nAI")

file.close()
```

Result

```text
Python
AI
```

Nothing is deleted.

Append means:

```text
Existing Data

↓

Add New Data

↓

Save
```

---

# Difference Between `w` and `a`

Initial File

```text
Python
AI
```

---

Using

```python
open("student.txt", "w")
```

Result

```text
Hello
```

Old content disappears.

---

Using

```python
open("student.txt", "a")
```

Result

```text
Python
AI
Hello
```

Old content stays.

---

# Create Mode (`x`)

```python
file = open("report.txt", "x")
```

If

```text
report.txt
```

doesn't exist,

Python creates it.

---

If it already exists,

Python raises

```text
FileExistsError
```

This helps avoid accidentally overwriting files.

---

# File Pointer While Writing

When using

```python
"w"
```

pointer starts here:

```text
|
```

When writing

```python
file.write("Python")
```

pointer moves:

```text
Python|
```

In append mode:

Existing file:

```text
Python
AI|
```

New data is added from the end.

---

# Real AI Example

Saving AI output

```python
response = "The capital of France is Paris."

file = open("response.txt", "w")

file.write(response)

file.close()
```

---

# Magento Example

Export Products

```text
products.csv

↓

Write Product Data

↓

Download CSV
```

Magento follows the same pattern.

---

# Common Mistakes

## Mistake 1

```python
open("file.txt", "w")
```

Thinking data is safe.

❌ Wrong.

The file is already emptied.

---

## Mistake 2

Forgetting

```python
close()
```

Can leave resources open and delay writes.

---

## Mistake 3

Expecting

```python
writelines()
```

to insert new lines.

It doesn't.

---

# Best Practices

Instead of

```python
file = open("report.txt", "w")

file.write("Hello")

file.close()
```

Professionals write

```python
with open("report.txt", "w") as file:
    file.write("Hello")
```

We'll learn **why** in Module 6.

---

# Mini Exercise

Create a file named:

```text
notes.txt
```

### Q1

Write

```text
Python
AI
Machine Learning
```

using

```python
write()
```

---

### Q2

Write the same content using

```python
writelines()
```

---

### Q3

Suppose

```text
notes.txt

Python
```

Then execute

```python
file = open("notes.txt", "a")

file.write("\nAI")
```

What will the final file contain?

---

### Q4

What happens if

```python
open("notes.txt", "w")
```

is executed before calling `write()`?

---

# Interview Questions

### Q1

What is the difference between

```python
write()

writelines()
```

---

### Q2

What is the difference between

```python
w

a
```

---

### Q3

Which mode creates a new file only if it does not already exist?

---

### Q4

Does

```python
writelines()
```

automatically insert newline characters?

---

# ⭐ Senior Developer Tip

Choosing the correct file mode is important:

* Use **`w`** when you want to replace the file completely (for example, regenerating a daily report).
* Use **`a`** when you want to preserve existing data and add new entries (for example, application logs).
* Use **`x`** when you want to ensure you don't accidentally overwrite an existing file.

This decision matters in production systems because using the wrong mode can result in accidental data loss.

---

# Lesson Progress

```text
Lesson 13 – File Handling

✅ Module 1 – Introduction
✅ Module 2 – Reading Files
▶ Module 3 – Writing & Appending Files
⏳ Module 4 – CSV Files
⏳ Module 5 – JSON Files
⏳ Module 6 – Best Practices
⏳ Module 7 – Sales Report Generator
⏳ Module 8 – Interview Questions
```

---

## 📝 Your Task

Answer the four mini-exercise questions and, if possible, write the code for **Q1** and **Q2**. After reviewing it, we'll move on to **Module 4 – Working with CSV Files**, where you'll learn one of the most important skills for both Magento development and AI data processing.
