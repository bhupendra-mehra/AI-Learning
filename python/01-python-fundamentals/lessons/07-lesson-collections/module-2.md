# Lesson 10 – Module 2

## Tuples & Sets

**Estimated Time:** 25–30 minutes

---

# Part 1 – Tuples

## What is a Tuple?

A **Tuple** stores multiple values just like a list.

The difference is:

> **A Tuple cannot be modified after it is created (Immutable).**

---

## Creating a Tuple

```python
fruits = ("Apple", "Banana", "Mango")
```

---

## Accessing Items

```python
print(fruits[0])
print(fruits[-1])
```

Output

```text
Apple
Mango
```

---

## Tuple Properties

* Ordered ✅
* Immutable (Cannot change values) ✅
* Allows Duplicates ✅

---

## Example

```python
coordinates = (25.276987, 55.296249)
```

Coordinates should never change, so a tuple is a good choice.

---

## What is NOT Allowed?

```python
fruits = ("Apple", "Banana")

fruits[0] = "Orange"
```

Output

```text
TypeError
```

Because tuples are immutable.

---

# When to Use Tuples

Use a tuple when the data **should not change**.

Examples:

* Coordinates
* RGB Colors
* Database IDs
* Fixed configuration values

---

# Part 2 – Sets

## What is a Set?

A **Set** stores **unique values only**.

Duplicates are removed automatically.

---

## Creating a Set

```python
fruits = {"Apple", "Banana", "Apple", "Mango"}

print(fruits)
```

Output

```text
{'Apple', 'Banana', 'Mango'}
```

Notice:

The duplicate `"Apple"` is removed.

---

## Set Properties

* Unordered ✅
* Mutable ✅
* No Duplicates ✅

---

## Adding Items

```python
fruits.add("Orange")
```

---

## Removing Items

```python
fruits.remove("Banana")
```

---

## Union

Combine two sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)
```

Output

```text
{1, 2, 3, 4, 5}
```

---

## Intersection

Common values.

```python
print(set1 & set2)
```

Output

```text
{3}
```

---

# Tuple vs List vs Set

| Feature    | List | Tuple | Set |
| ---------- | ---- | ----- | --- |
| Ordered    | ✅    | ✅     | ❌   |
| Mutable    | ✅    | ❌     | ✅   |
| Duplicates | ✅    | ✅     | ❌   |

---

# Best Practices

### Use List

When data changes frequently.

Example:

```python
shopping_cart = []
```

---

### Use Tuple

When values should remain fixed.

Example:

```python
database_config = ("localhost", 3306)
```

---

### Use Set

When uniqueness matters.

Example:

```python
visited_pages = set()
```

---

# AI Example

Suppose an AI extracts keywords.

```python
keywords = {
    "python",
    "ai",
    "python",
    "machine learning"
}
```

The duplicate `"python"` is removed automatically.

---

# Magento Example

Product tags:

```python
tags = {
    "Sale",
    "Electronics",
    "Sale"
}
```

Only unique tags remain.

---

# Exercises

## Exercise 1

Create a tuple of **5 cities**.

Print:

* First city
* Last city

---

## Exercise 2

Try changing the first city.

Observe the error and tell me why it occurs.

---

## Exercise 3

Create a set:

```python
{"Apple", "Banana", "Apple", "Orange"}
```

Print the result.

---

## Exercise 4

Add `"Mango"` to the set.

Remove `"Banana"`.

Print the final set.

---

## Exercise 5

Create:

```python
A = {1, 2, 3, 4}

B = {3, 4, 5, 6}
```

Print:

* Union
* Intersection

---

# Mini Project

## Student Registration System

Requirements

Create a set containing student names.

```text
Rahul
Amit
Rahul
Priya
Amit
```

Print the final set.

Observe that duplicate names are automatically removed.

---

# Where You'll Use This in AI Agent Development

### Tuples

* Fixed coordinates
* Constant configuration
* Function return values

### Sets

* Remove duplicate search results
* Unique keywords
* Unique document IDs
* Unique product SKUs

---

# Module Outcome

After this module, you'll be able to:

* ✅ Choose between List, Tuple, and Set.
* ✅ Store immutable data using tuples.
* ✅ Remove duplicates using sets.
* ✅ Perform union and intersection operations.

---

**Estimated completion time:** **20–25 minutes**.

Once you complete these exercises, we'll move to **Lesson 10 – Module 3 (Dictionaries)**.

> **Note:** Dictionaries are one of the most important topics in Python for AI. Nearly every API response (OpenAI, Magento REST, GraphQL, JSON) is dictionary-based, so we'll spend a little more time there than we did on lists or sets.
