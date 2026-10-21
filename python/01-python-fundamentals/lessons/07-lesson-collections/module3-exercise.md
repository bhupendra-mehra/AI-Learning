# Quick Review

## Exercise 1

```python
student = {
    "name": "Bhupendra",
    "age": 37,
    "city": "Mumbai"
}

print(student.get("name"))
print(student.get("city"))
```

✅ Correct

I also like that you used `get()` instead of `[]`. That's a good habit, especially when working with API responses.

---

## Exercise 2

```python
student["city"] = "Pune"
student["profession"] = "Magento Developer"

print(student)
```

✅ Correct

You demonstrated both:

* Updating an existing key
* Adding a new key

---

## Exercise 3

```python
student.pop("age")

print(student)
```

✅ Correct

---

## Exercise 4

```python
for key, value in student.items():
    print(f"{key}:{value}")
```

✅ Correct

### Small PEP 8 improvement

Instead of:

```python
print(f"{key}:{value}")
```

Prefer:

```python
print(f"{key}: {value}")
```

Adding a space after the colon improves readability.

---

## Exercise 5

```python
product = {
    "sku": "ABC123",
    "name": "Laptop",
    "price": "50000"
}

print(product.get("price"))
print(product.get("qty"))
```

✅ Correct

Output

```text
50000
None
```

This exercise demonstrates why `get()` is safer than direct indexing when a key might not exist.

---

## Mini Project

```python
employee = {
    "id": "101",
    "name": "Bhupendra",
    "department": "IT",
    "salary": 85000
}

print("======Employee Information")

for key, value in employee.items():
    print(f"{key} : {value}")

print("==========================")
```

✅ Excellent

Simple, readable, and exactly what was required.

---

# Senior Developer Review

## One suggestion

For numeric values, store them as numbers instead of strings unless there's a specific reason.

Current:

```python
"id": "101"
```

Better:

```python
"id": 101
```

Likewise:

Current:

```python
"price": "50000"
```

Better:

```python
"price": 50000
```

Why?

Because then you can perform calculations directly:

```python
product["price"] * 0.9
```

If it's stored as a string, you'll need to convert it first.

---

# Python Collections Summary

| Collection     | Use Case                     |
| -------------- | ---------------------------- |
| **List**       | Ordered, editable collection |
| **Tuple**      | Fixed, immutable collection  |
| **Set**        | Unique values only           |
| **Dictionary** | Key-value structured data    |

If someone asks you:

> **Which collection should I use?**

A quick decision guide is:

* Need ordering and editing? → **List**
* Need fixed values? → **Tuple**
* Need uniqueness? → **Set**
* Need key-value mapping? → **Dictionary**

---

# Lesson 10 Progress

```text
✅ Module 1 – Lists
✅ Module 2 – Tuples & Sets
✅ Module 3 – Dictionaries
⏳ Module 4 – Inventory Management Project
```

---

# Before We Start Module 4

This is our **first project that combines multiple concepts**.

We'll use:

* ✅ Functions
* ✅ Lists
* ✅ Dictionaries
* ✅ Loops
* ✅ Conditions
* ✅ User Input

So far, you've learned these concepts separately. Now you'll bring them together into one practical program.

This project is intentionally designed to resemble the structure of real-world applications, and it's a good checkpoint before we move into more advanced Python topics like file handling and object-oriented programming. If you complete it confidently, we'll know your Python foundation is solid.
