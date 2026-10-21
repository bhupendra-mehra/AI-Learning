# Lesson 7 – Module 5: Final Project

Congratulations! You've reached the **first milestone project** in the roadmap.

This project is designed to use **everything you've learned so far**. Instead of introducing new concepts, we'll apply them together in a realistic scenario—similar to how you'll build logic inside an AI agent or a Magento backend.

---

# What We've Learned So Far

Before starting, let's review the tools available:

| Concept                | Example                          |
| ---------------------- | -------------------------------- |
| Variables              | `age = 25`                       |
| Data Types             | `int`, `float`, `str`, `bool`    |
| User Input             | `input()`                        |
| Type Conversion        | `int()`, `float()`               |
| Arithmetic Operators   | `+`, `-`, `*`, `/`               |
| Comparison Operators   | `>`, `<`, `==`, `!=`, `>=`, `<=` |
| Conditional Statements | `if`, `elif`, `else`             |
| Logical Operators      | `and`, `or`, `not`               |

Today's goal is to combine all of them.

---

# Project Scenario

Imagine you're developing the backend logic for an online shopping website.

When a customer places an order, the system needs to answer questions like:

* Is the customer old enough?
* Is the customer logged in?
* Is the product in stock?
* Is the cart value eligible for a discount?
* What is the final payable amount?

This is exactly the type of decision-making logic you'll later build into AI agents.

---

# Project Requirements

The program should:

1. Ask the customer's name.
2. Ask the customer's age.
3. Ask if they are logged in.
4. Ask if the product is in stock.
5. Ask the cart value.
6. Calculate any discount.
7. Decide whether the order can be placed.
8. Display the final result.

---

# Step 1 – Collect User Input

```python
name = input("Enter your name: ")

age = int(input("Enter your age: "))

logged_in = input("Are you logged in? (yes/no): ")

stock = input("Is the product in stock? (yes/no): ")

cart = float(input("Enter cart amount: "))
```

---

# Step 2 – Convert User Input

Currently:

```python
logged_in = "yes"
```

is a string.

Convert it into a Boolean.

```python
logged_in = logged_in.lower() == "yes"

stock = stock.lower() == "yes"
```

Now:

If user enters:

```
yes
```

Python stores:

```python
True
```

If user enters:

```
no
```

Python stores:

```python
False
```

---

# Step 3 – Calculate Discount

Business Rule

```
₹10,000 or more → 20%

₹5,000–9,999 → 10%

Otherwise → No discount
```

Code

```python
discount = 0

if cart >= 10000:
    discount = cart * 0.20
elif cart >= 5000:
    discount = cart * 0.10
```

Calculate final amount

```python
final_amount = cart - discount
```

---

# Step 4 – Check Order Eligibility

Business Rule

Customer can order only if:

* Age ≥ 18
* Logged in
* Product available

Code

```python
if age >= 18 and logged_in and stock:
    order_allowed = True
else:
    order_allowed = False
```

---

# Step 5 – Display Result

```python
print("\n===== ORDER SUMMARY =====")

print("Customer:", name)

print("Discount:", discount)

print("Final Amount:", final_amount)

if order_allowed:
    print("Order Status: Approved")
else:
    print("Order Status: Rejected")
```

---

# Complete Program

```python
name = input("Enter your name: ")

age = int(input("Enter your age: "))

logged_in = input("Are you logged in? (yes/no): ")

stock = input("Is the product in stock? (yes/no): ")

cart = float(input("Enter cart amount: "))

logged_in = logged_in.lower() == "yes"

stock = stock.lower() == "yes"

discount = 0

if cart >= 10000:
    discount = cart * 0.20
elif cart >= 5000:
    discount = cart * 0.10

final_amount = cart - discount

if age >= 18 and logged_in and stock:
    order_allowed = True
else:
    order_allowed = False

print("\n===== ORDER SUMMARY =====")

print("Customer:", name)
print("Discount:", discount)
print("Final Amount:", final_amount)

if order_allowed:
    print("Order Status: Approved")
else:
    print("Order Status: Rejected")
```

---

# Sample Run 1

### Input

```
Enter your name: Bhupendra

Enter your age: 30

Are you logged in? yes

Is the product in stock? yes

Enter cart amount: 12000
```

### Output

```
===== ORDER SUMMARY =====

Customer: Bhupendra

Discount: 2400.0

Final Amount: 9600.0

Order Status: Approved
```

---

# Sample Run 2

### Input

```
Name: Rahul

Age: 17

Logged In: yes

Stock: yes

Cart: 8000
```

### Output

```
===== ORDER SUMMARY =====

Customer: Rahul

Discount: 800.0

Final Amount: 7200.0

Order Status: Rejected
```

Reason:

```
Age < 18
```

---

# Sample Run 3

### Input

```
Age: 28

Logged In: no

Stock: yes
```

Output

```
Order Status: Rejected
```

Reason:

```
Customer not logged in
```

---

# How an AI Agent Uses Similar Logic

Imagine a customer asks:

> "Cancel my order."

An AI agent won't immediately cancel it. It first evaluates conditions.

```python
if (
    logged_in
    and order_exists
    and payment_received
    and not shipped
):
    cancel_order()
else:
    show_reason()
```

This is the same decision-making process you've practiced in this project.

---

# Magento Example

In Magento, you'll often see similar logic written in PHP.

```php
if (
    $customer->getId()
    && $product->isSaleable()
) {
    // Allow checkout
}
```

The Python equivalent is:

```python
if customer_logged_in and product_available:
    print("Proceed to Checkout")
```

The language changes, but the decision-making pattern remains the same.

---

# Challenge Exercise

Enhance the program with these rules:

1. Add **Premium Member** (`yes/no`).
2. Premium members get an **additional 5% discount**.
3. If the customer is **under 18**, print the reason:

   ```
   Rejected: Customer must be at least 18 years old.
   ```
4. If the product is out of stock, print:

   ```
   Rejected: Product is currently unavailable.
   ```
5. If the customer is not logged in, print:

   ```
   Rejected: Please log in before placing an order.
   ```

Try implementing these changes yourself before looking for help.

---

# What You Have Accomplished

By completing this project, you've written a program that uses:

* ✅ Variables
* ✅ User input
* ✅ Type conversion
* ✅ Strings
* ✅ Numbers
* ✅ Arithmetic operators
* ✅ Comparison operators
* ✅ Conditional statements
* ✅ Logical operators
* ✅ Business rules
* ✅ Real-world workflow

This is your first complete program that resembles the logic used in production software.

---

# Roadmap Progress

## ✅ Lesson 7 Completed

You can now:

* Use variables confidently.
* Accept and process user input.
* Perform calculations.
* Compare values.
* Make decisions with `if`, `elif`, and `else`.
* Combine conditions with `and`, `or`, and `not`.
* Build small business logic programs.

---
