# 📘 Lesson 13 – Module 5

# Working with JSON Files

**Estimated Time:** 35–40 minutes

---

# Learning Objectives

By the end of this module, you'll understand:

* ✅ What is JSON?
* ✅ JSON vs Python Dictionary
* ✅ `json` module
* ✅ `json.load()`
* ✅ `json.loads()`
* ✅ `json.dump()`
* ✅ `json.dumps()`
* ✅ Reading JSON files
* ✅ Writing JSON files
* ✅ Magento & AI use cases
* ✅ Best Practices

---

# What is JSON?

JSON stands for:

```text
JavaScript Object Notation
```

Don't let the name confuse you.

Although it originated from JavaScript, **JSON is language-independent**.

Python, Java, PHP, C#, Go, Node.js—all support JSON.

---

# Why JSON?

Suppose we need to store customer information.

Instead of

```text
Bhupendra
37
Mumbai
```

JSON stores data with meaningful keys.

```json
{
    "name": "Bhupendra",
    "age": 37,
    "city": "Mumbai"
}
```

This makes the data self-describing and easy to exchange between systems.

---

# JSON vs Dictionary

This is one of the most common interview questions.

Python Dictionary

```python
student = {
    "name": "Bhupendra",
    "age": 37,
    "course": "Python"
}
```

JSON

```json
{
    "name": "Bhupendra",
    "age": 37,
    "course": "Python"
}
```

Looks similar.

But they are **not** the same.

---

# Difference

| Python Dictionary | JSON                                 |
| ----------------- | ------------------------------------ |
| Python object     | Text format                          |
| Uses Python types | Used for data exchange               |
| Exists in memory  | Stored in files or sent over network |

---

# JSON File

Create:

```text
student.json
```

Contents

```json
{
    "name": "Bhupendra",
    "age": 37,
    "course": "Python"
}
```

---

# Python JSON Module

```python
import json
```

Built into Python.

No installation required.

---

# Reading JSON File

```python
import json

with open("student.json", "r") as file:

    data = json.load(file)

print(data)
```

Output

```python
{
    'name': 'Bhupendra',
    'age': 37,
    'course': 'Python'
}
```

Notice:

The result is a

```python
dict
```

---

# Data Type

```python
print(type(data))
```

Output

```python
<class 'dict'>
```

Very important interview question.

---

# Access Values

```python
print(data["name"])
```

Output

```text
Bhupendra
```

---

```python
print(data["age"])
```

Output

```text
37
```

---

# Writing JSON

Suppose

```python
student = {
    "name": "Rahul",
    "age": 25,
    "course": "AI"
}
```

Write it to a file.

```python
import json

with open("student.json", "w") as file:

    json.dump(student, file)
```

File becomes

```json
{"name": "Rahul", "age": 25, "course": "AI"}
```

---

# Pretty Printing

By default

```python
json.dump()
```

writes everything on one line.

Better

```python
json.dump(student, file, indent=4)
```

Now

```json
{
    "name": "Rahul",
    "age": 25,
    "course": "AI"
}
```

Much more readable.

---

# `load()` vs `loads()`

This confuses many beginners.

## `load()`

Reads JSON **from a file**.

```python
with open("student.json") as file:
    data = json.load(file)
```

Think:

> **load = file**

---

## `loads()`

Reads JSON **from a string**.

```python
import json

text = '{"name":"Rahul","age":25}'

data = json.loads(text)
```

Output

```python
{
    'name': 'Rahul',
    'age': 25
}
```

Think:

> **loads = string**

Notice the extra **"s"**.

---

# `dump()` vs `dumps()`

Again,

very common interview question.

---

## `dump()`

Writes JSON to a file.

```python
json.dump(student, file)
```

Think:

> dump → file

---

## `dumps()`

Converts a dictionary into a JSON string.

```python
text = json.dumps(student)
```

Output

```python
'{"name": "Rahul", "age": 25, "course": "AI"}'
```

Notice:

Nothing is written to a file.

Only a string is returned.

---

# Easy Memory Trick

| Method    | Works With      |
| --------- | --------------- |
| `load()`  | File → Python   |
| `loads()` | String → Python |
| `dump()`  | Python → File   |
| `dumps()` | Python → String |

---

# Visual Flow

```text
JSON File

↓

json.load()

↓

Python Dictionary
```

---

```text
Python Dictionary

↓

json.dump()

↓

JSON File
```

---

```text
JSON String

↓

json.loads()

↓

Python Dictionary
```

---

```text
Python Dictionary

↓

json.dumps()

↓

JSON String
```

---

# Magento Example

Magento REST API

Response

```json
{
    "id": 10,
    "sku": "ABC001",
    "price": 1200
}
```

Python

```python
response = requests.get(...)

product = response.json()
```

Internally,

JSON becomes a Python dictionary.

---

# AI Example

ChatGPT API Response

```json
{
    "choices": [
        {
            "message": {
                "content": "Hello"
            }
        }
    ]
}
```

Python

```python
response["choices"][0]["message"]["content"]
```

This works because JSON has been converted into dictionaries and lists.

---

# Common Mistakes

## Forgetting

```python
import json
```

Results in

```text
NameError
```

---

## Confusing

```python
load()
```

with

```python
loads()
```

Remember:

**File vs String**

---

## Forgetting

```python
indent=4
```

The file still works,

but it becomes harder to read.

---

# Best Practices

* Always use `with open()`.
* Use `indent=4` for readability.
* Validate JSON before processing.
* Catch `json.JSONDecodeError` when reading untrusted JSON.

---

# Mini Exercise

Create:

```text
employee.json
```

Contents

```json
{
    "name": "John",
    "department": "IT",
    "salary": 5000
}
```

Then answer:

### Q1

What datatype does

```python
json.load(file)
```

return?

---

### Q2

What is the difference between

```python
load()
```

and

```python
loads()
```

---

### Q3

What is the difference between

```python
dump()
```

and

```python
dumps()
```

---

### Q4

Write code to print only:

```text
John
```

from

```python
employee.json
```

---

### Q5

Why do we use

```python
indent=4
```

---

# Interview Questions

### Q1

What does JSON stand for?

---

### Q2

Why is JSON widely used?

---

### Q3

What is the difference between a Python dictionary and JSON?

---

### Q4

Explain:

```python
load()

loads()

dump()

dumps()
```

---

# ⭐ Senior Developer Tip

When you start learning **APIs** (coming in a later lesson), you'll notice something important:

You almost never manually parse API responses.

For example:

```python
response = requests.get(url)

data = response.json()
```

Even though it looks simple, behind the scenes the JSON response is being converted into Python dictionaries and lists—exactly the concepts you're learning in this module.

This is why understanding JSON now will make API programming much easier later.

---

# Lesson Progress

```text
Lesson 13 – File Handling

✅ Module 1 – Introduction
✅ Module 2 – Reading Files
✅ Module 3 – Writing & Appending
✅ Module 4 – CSV Files
▶ Module 5 – JSON Files
⏳ Module 6 – Best Practices
⏳ Module 7 – Sales Report Generator
⏳ Module 8 – Interview Questions
```

---

## 📝 Your Task

Answer the five mini-exercise questions.

For **Q4**, write the actual Python code to read `employee.json` and print only the employee's name.

Once I review it, we'll move to **Module 6 – File Handling Best Practices**, where you'll learn professional techniques such as context managers, path handling, and robust file error handling that you'll use in real-world Python applications.
