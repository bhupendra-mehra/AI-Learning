# Review

**Score: 10/10 ⭐**

---

# Exercise 1

```python
cities = ("Bhopal", "Indore", "Gwalior", "Jabalpur", "Ujjain")

print(cities[0])
print(cities[-1])
```

✅ Correct

Output

```text
Bhopal
Ujjain
```

---

# Exercise 2

```python
cities[0] = "Raipur"
```

✅ Correct

This will raise:

```text
TypeError: 'tuple' object does not support item assignment
```

**Reason:** Tuples are **immutable** (cannot be modified after creation).

---

# Exercise 3

```python
fruits = {"Apple", "Banana", "Apple", "Orange"}

print(fruits)
```

✅ Correct

Output will contain only unique values.

Example:

```text
{'Apple', 'Banana', 'Orange'}
```

> **Note:** Sets are **unordered**, so the display order may differ every time. Don't expect `"Apple"` to always appear first.

This is an important difference from lists and tuples.

---

# Exercise 4

```python
fruits.add("Mango")
fruits.remove("Banana")

print(fruits)
```

✅ Perfect

---

# Exercise 5

```python
A = {1, 2, 3, 4}

B = {3, 4, 5, 6}

print(A | B)

print(A & B)
```

✅ Perfect

Output

```text
{1, 2, 3, 4, 5, 6}

{3, 4}
```

---

# Mini Project

```python
students = {"Rahul", "Amit", "Rahul", "Priya", "Amit"}

print(students)
```

✅ Perfect

Result

```text
{'Rahul', 'Amit', 'Priya'}
```

Duplicate names are removed automatically.

---

# Senior Developer Tip

Here's a rule you'll use throughout your career:

| Use                    | Collection   |
| ---------------------- | ------------ |
| Ordered, editable data | `list`       |
| Fixed data             | `tuple`      |
| Unique values          | `set`        |
| Key-value data         | `dictionary` |

If you remember this table, you'll make the right choice most of the time.

---

# Module 2 Status

```
✅ Module 1 – Lists
✅ Module 2 – Tuples & Sets
⏳ Module 3 – Dictionaries
⏳ Module 4 – Inventory Management Project
```

---

# Important Note About Module 3

This is the **first module where we'll intentionally slow down a little.**

### Why?

Because almost everything in AI uses dictionaries.

For example:

OpenAI Response

```python
{
    "id": "...",
    "model": "...",
    "choices": [...],
    "usage": {...}
}
```

Magento REST API

```python
{
    "sku": "ABC123",
    "name": "Laptop",
    "price": 50000
}
```

JSON

```python
{
    "name": "Bhupendra",
    "age": 37
}
```

Every one of these is represented as a **dictionary** in Python.

So while we'll still keep it within **30–40 minutes**, this is one topic where I don't want to rush because it will make the upcoming API and AI phases much easier.

I think this is one of the highest-return topics in the entire Python phase. Once you're comfortable with dictionaries, working with APIs, JSON, and AI SDKs becomes much more natural.
