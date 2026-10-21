# Code Review

## ✅ 1. Excellent Project Structure

You naturally separated the logic into:

```python
add_product()

show_products()

search_product()

update_quantity()

main_menu()
```

⭐⭐⭐⭐⭐

Exactly what I wanted.

---

## ✅ 2. Inventory Design

This is excellent.

```python
inventory = [
    {
        "sku": "...",
        "name": "...",
        "price": ...,
        "qty": ...
    }
]
```

This is almost identical to how you'll receive Magento REST API responses.

---

## ✅ 3. Looping

Very good.

```python
for product in inventory:
```

This is exactly the correct approach.

---

## ✅ 4. Dictionary Usage

Excellent.

You used

```python
product.get("name")
```

instead of

```python
product["name"]
```

Good habit.

---

# Improvements

Now let's review it like a senior developer reviewing a pull request.

---

# 1. Never Return append()

Current

```python
return inventory.append(product)
```

The problem:

`append()` always returns **None**.

So this function returns:

```python
None
```

Better:

```python
inventory.append(product)
print("Product added successfully.")
```

or

```python
inventory.append(product)
return True
```

This is standard practice.

---

# 2. search_product()

Current

```python
for key, value in product.items():

    if key == "sku" and value == sku:
```

This works...

But it is unnecessary.

You already know the key name.

Instead of looping through every key:

Use

```python
if product["sku"] == sku:
```

Much simpler.

Instead of

```python
for product in inventory:

    for key, value in product.items():
```

Use

```python
for product in inventory:

    if product["sku"] == sku:
```

Cleaner.

Faster.

More readable.

---

# 3. Same Issue in update_quantity()

Instead of

```python
for key, value in product.items():
```

Just write

```python
if product["sku"] == sku:
```

Again,

you already know the key.

---

# 4. is_product_found

You created

```python
is_product_found = False
```

but never changed it to

```python
True
```

Actually,

you don't even need it.

Because

```python
return
```

already exits the function.

Simply write

```python
for product in inventory:

    if product["sku"] == sku:

        ...

        return product

print("Product Not Found")
return None
```

Much simpler.

---

# 5. Exit Menu

Current

```python
else:

    is_show_menu = False
```

This means

```
7

10

99
```

also exits.

Instead

```python
elif selected_option == 5:

    is_show_menu = False

else:

    print("Invalid Option")
```

Much safer.

---

# 6. Show Products

Instead of

```python
for key, value in product.items():
```

I'd write

```python
print(f"SKU   : {product['sku']}")
print(f"NAME  : {product['name']}")
print(f"PRICE : {product['price']}")
print(f"QTY   : {product['qty']}")
```

Reason?

Inventory has a fixed structure.

This is easier to read.

---

# ⭐ Optional Challenge

When adding a product,

check whether SKU already exists.

Example

```python
for product in inventory:

    if product["sku"] == sku:

        print("SKU already exists")

        return
```

This is exactly what Magento does.

---

# Updated Production Version

This is how I'd write it after refactoring while using **only the concepts you've learned so far** (no classes, no exceptions, no advanced features).

```python
inventory = []


def add_product():
    sku = input("Enter SKU: ")

    for product in inventory:
        if product["sku"] == sku:
            print("SKU already exists.")
            return

    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    qty = int(input("Enter Quantity: "))

    inventory.append({
        "sku": sku,
        "name": name,
        "price": price,
        "qty": qty
    })

    print("Product added successfully.")


def show_products():
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n========= INVENTORY =========")

    for product in inventory:
        print(f"SKU   : {product['sku']}")
        print(f"NAME  : {product['name']}")
        print(f"PRICE : {product['price']}")
        print(f"QTY   : {product['qty']}")
        print("-----------------------------")


def search_product():
    sku = input("Enter SKU to search: ")

    for product in inventory:
        if product["sku"] == sku:
            print("\nProduct Found")
            print(f"Name  : {product['name']}")
            print(f"Price : {product['price']}")
            print(f"Qty   : {product['qty']}")
            return product

    print("Product Not Found.")
    return None


def update_quantity():
    sku = input("Enter SKU: ")
    qty = int(input("Enter New Quantity: "))

    for product in inventory:
        if product["sku"] == sku:
            product["qty"] = qty
            print("Quantity updated successfully.")
            return

    print("Product Not Found.")


def main_menu():
    while True:
        print("\n========= MENU =========")
        print("1. Add Product")
        print("2. Show Products")
        print("3. Search Product")
        print("4. Update Quantity")
        print("5. Exit")

        option = int(input("Select an option: "))

        if option == 1:
            add_product()

        elif option == 2:
            show_products()

        elif option == 3:
            search_product()

        elif option == 4:
            update_quantity()

        elif option == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid Option")


main_menu()
```

---

# 🎉 Lesson 10 Completed

## What You've Learned

* ✅ Lists
* ✅ Tuples
* ✅ Sets
* ✅ Dictionaries
* ✅ Combining collections
* ✅ Building a CRUD-style console application

---

# Progress Report

We have now completed **10 lessons** of Python.

At this point, you can build small console applications from scratch without referring back to earlier lessons. That's a strong indicator that the fundamentals are becoming second nature.

## Updated Roadmap Progress

```
Phase 1 – Python Foundation

██████████░░░░░░░░░░░░░░ 45%

✅ Lessons 1–10 Completed
⏳ Lesson 11 – Object-Oriented Programming
⏳ Lesson 12 – File Handling
⏳ Lesson 13 – Exception Handling
⏳ Lesson 14 – Modules & Packages
⏳ Phase 1 Capstone Project
```

One last observation: I noticed you naturally designed functions first and then connected them with a menu. That's the same mindset you'll use later when building AI agents—small, focused functions coordinated by a central workflow. That's a very encouraging sign for the next phases of the roadmap.
