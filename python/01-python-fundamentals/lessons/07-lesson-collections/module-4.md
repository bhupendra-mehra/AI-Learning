# Lesson 10 – Module 4

## Final Project – Inventory Management System

**Estimated Time:** 25–30 minutes

**Difficulty:** ⭐⭐

---

# Objective

Build a simple Inventory Management System using everything you've learned so far.

This is **not** about writing hundreds of lines of code—it's about organizing your logic properly.

---

# Concepts Covered

* ✅ Functions
* ✅ Lists
* ✅ Dictionaries
* ✅ Loops
* ✅ Conditions
* ✅ User Input
* ✅ Return Values

---

# Requirements

Create an inventory where each product is stored as a **dictionary** inside a **list**.

Example inventory:

```python
inventory = [
    {
        "sku": "P001",
        "name": "Laptop",
        "price": 50000,
        "qty": 10
    },
    {
        "sku": "P002",
        "name": "Mouse",
        "price": 500,
        "qty": 50
    }
]
```

---

# Functions to Create

## 1. `add_product()`

Ask the user for:

* SKU
* Product Name
* Price
* Quantity

Create a dictionary and add it to the inventory list.

---

## 2. `show_products()`

Display all products.

Example:

```text
========= INVENTORY =========

SKU : P001
Name : Laptop
Price : 50000
Qty : 10

----------------------------

SKU : P002
Name : Mouse
Price : 500
Qty : 50
```

---

## 3. `search_product()`

Ask the user for a SKU.

If found:

```text
Product Found

Laptop
50000
10
```

Otherwise:

```text
Product Not Found
```

**Hint:**

```python
for product in inventory:
```

---

## 4. `update_quantity()`

Ask:

* SKU
* New Quantity

Update only the quantity if the product exists.

---

## 5. `main_menu()`

Display:

```text
========= MENU =========

1. Add Product

2. Show Products

3. Search Product

4. Update Quantity

5. Exit
```

Keep showing the menu until the user selects **5**.

Use:

* `while`
* `if-elif-else`
* Function calls

---

# Suggested Structure

```python
inventory = []

def add_product():
    ...

def show_products():
    ...

def search_product():
    ...

def update_quantity():
    ...

def main_menu():
    ...

main_menu()
```

---

# Rules

Use only the concepts we've covered so far.

Do **not** use:

* Classes
* Files
* Exception handling
* Advanced Python features

We'll learn those later.

---

# Challenge ⭐ (Optional)

When adding a product, check if the SKU already exists.

If it does:

```text
SKU already exists.
```

Don't add the duplicate product.

This is optional because it combines searching and validation.

---

# Where You'll Use This in AI Agent Development

This project teaches the same pattern you'll use in AI:

```text
User Input
      ↓
Function
      ↓
Search Data
      ↓
Update Data
      ↓
Display Result
```

Replace **Inventory** with:

* Chat History
* Retrieved Documents
* Tool Results
* Knowledge Base

The structure remains almost the same.

---

# Lesson 10 Outcome

After completing this project, you'll have learned:

* ✅ Lists
* ✅ Tuples
* ✅ Sets
* ✅ Dictionaries
* ✅ Combining multiple collections
* ✅ Organizing logic with functions

This marks the completion of your Python collections foundation.

---

## ⏱️ Target Time

**25–30 minutes**

---

### My Suggestion

Try to build it **without looking back at previous lessons**.

If you get stuck for more than **5–10 minutes**, ask me about that specific part rather than looking up the full solution. That's the fastest way to strengthen your problem-solving skills while still keeping our overall pace high.
