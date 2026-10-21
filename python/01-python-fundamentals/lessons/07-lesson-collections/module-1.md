# Module 1 – Lists

**Estimated Time:** 30–40 minutes

---

## 1. What is a List?

A **list** stores multiple values in a single variable.

Instead of:

```python
product1 = "Laptop"
product2 = "Mouse"
product3 = "Keyboard"
```

Use:

```python
products = ["Laptop", "Mouse", "Keyboard"]
```

---

## 2. List Properties

* Ordered ✅
* Mutable (can be changed) ✅
* Allows duplicate values ✅

Example:

```python
products = ["Laptop", "Mouse", "Laptop"]
```

This is valid because lists allow duplicates.

---

## 3. Creating Lists

```python
products = ["Laptop", "Mouse", "Keyboard"]
```

```python
prices = [100, 200, 300]
```

```python
is_available = [True, False, True]
```

Mixed data types are possible:

```python
data = ["Laptop", 50000, True]
```

But in real projects, keep similar data types together whenever possible.

---

## 4. Accessing Items

Python indexing starts from **0**.

```python
products = ["Laptop", "Mouse", "Keyboard"]

print(products[0])
print(products[1])
print(products[2])
```

Output:

```text
Laptop
Mouse
Keyboard
```

Negative indexing:

```python
print(products[-1])
```

Output:

```text
Keyboard
```

`-1` always refers to the last item.

---

## 5. Updating Items

```python
products[1] = "Monitor"

print(products)
```

Output:

```text
['Laptop', 'Monitor', 'Keyboard']
```

---

## 6. Adding Items

```python
products.append("Speaker")
```

Result:

```text
['Laptop', 'Mouse', 'Keyboard', 'Speaker']
```

---

## 7. Removing Items

Remove by value:

```python
products.remove("Mouse")
```

Remove by index:

```python
products.pop(1)
```

---

## 8. List Length

```python
print(len(products))
```

Returns the number of items in the list.

---

## 9. Loop Through a List

```python
products = ["Laptop", "Mouse", "Keyboard"]

for product in products:
    print(product)
```

---

## 10. Most Common Methods

| Method      | Purpose         |
| ----------- | --------------- |
| `append()`  | Add an item     |
| `remove()`  | Remove by value |
| `pop()`     | Remove by index |
| `len()`     | Count items     |
| `sort()`    | Sort items      |
| `reverse()` | Reverse order   |

These cover most day-to-day list operations.

---

# Exercises

### Exercise 1

Create a list of **5 fruits** and print the entire list.

---

### Exercise 2

Print:

* First fruit
* Last fruit

---

### Exercise 3

Replace the **third fruit** with `"Mango"` and print the updated list.

---

### Exercise 4

Add `"Orange"` to the list, remove the **first fruit**, and print the final list.

---

### Exercise 5

Create a list of **5 numbers** and print each number using a `for` loop.

---

## Where You'll Use This in AI Agent Development

Lists are one of the most frequently used data structures in AI:

* Store chat history.
* Hold retrieved documents for RAG.
* Process API results.
* Keep tool outputs.
* Manage batches of embeddings.

You'll use lists in almost every AI project we build from here onward.

---

This is the exact structure I'll follow from now on:

1. **Complete lesson structure** (for your roadmap).
2. **Start Module 1**.
3. Complete one module in one sitting.
4. Review.
5. Move to the next module.

This keeps the roadmap organized and avoids surprises as we progress.
