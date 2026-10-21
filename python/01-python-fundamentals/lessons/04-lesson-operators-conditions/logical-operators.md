# Module 4 – Logical Operators (`and`, `or`, `not`)

Welcome back! We have already covered:

* ✅ Module 1 – Arithmetic Operators
* ✅ Module 2 – Comparison Operators
* ✅ Module 3 – Boolean (`True` & `False`)
* ✅ **Today:** Module 4 – Logical Operators

This lesson follows your roadmap: **Concept → Why → Analogy → Magento/PHP Comparison → Syntax → Execution Flow → AI Connection → Mini Examples → Common Mistakes → Homework.**

---

# 1. What are Logical Operators?

Logical operators combine multiple conditions into one decision.

Imagine your program asks:

> "Should I execute this code?"

Sometimes checking one condition isn't enough.

Example:

* Age > 18
* User has ID

Both must be true.

Logical operators solve this.

Python has only **3 logical operators**:

| Operator | Meaning                               |
| -------- | ------------------------------------- |
| `and`    | Both conditions must be True          |
| `or`     | At least one condition must be True   |
| `not`    | Reverse True to False (or vice versa) |

Logical operators combine or negate Boolean conditions. ([DataCamp][1])

---

# 2. Real Life Analogy

## ATM Withdrawal

You can withdraw money only if:

* Card inserted
* PIN correct

Both are required.

```
Card Inserted  → True
PIN Correct    → True

Result → Allow Withdrawal
```

If either is False:

```
Card Inserted → True
PIN Correct → False

Result → Denied
```

This is exactly how `and` works.

---

# 3. AI Agent Analogy

Suppose you build a Magento AI Agent.

Customer asks:

> "Track my order"

Agent checks:

* Customer logged in
* Order exists

Only then respond.

```
if logged_in and order_exists:
    show_tracking()
```

Without logical operators, AI agents couldn't combine multiple checks.

---

# 4. Operator 1 — `and`

Meaning:

**Both conditions must be True.**

Syntax

```python
condition1 and condition2
```

Example

```python
age = 20
has_license = True

print(age >= 18 and has_license)
```

Output

```
True
```

---

Another example

```python
age = 16
has_license = True

print(age >= 18 and has_license)
```

Output

```
False
```

Because the first condition failed.

---

Truth Table

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

---

# 5. Operator 2 — `or`

Meaning:

Only one condition needs to be True.

Syntax

```python
condition1 or condition2
```

Example

```python
is_admin = False
is_manager = True

print(is_admin or is_manager)
```

Output

```
True
```

---

Another example

```python
is_admin = False
is_manager = False

print(is_admin or is_manager)
```

Output

```
False
```

---

Truth Table

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

# 6. Operator 3 — `not`

`not` reverses the Boolean value.

Syntax

```python
not condition
```

Example

```python
logged_in = True

print(not logged_in)
```

Output

```
False
```

---

Another example

```python
logged_in = False

print(not logged_in)
```

Output

```
True
```

---

Truth Table

| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

---

# 7. Combining Operators

Example

```python
age = 25
salary = 50000

print(age > 18 and salary > 30000)
```

Output

```
True
```

---

Another example

```python
temperature = 40

print(temperature < 0 or temperature > 35)
```

Output

```
True
```

---

Example with `not`

```python
logged_in = False

print(not logged_in)
```

Output

```
True
```

---

# 8. Execution Flow

Consider

```python
age = 25
citizen = True

print(age >= 18 and citizen)
```

Python evaluates:

Step 1

```
age >=18

25 >=18

True
```

Step 2

```
citizen

True
```

Step 3

```
True and True

Result → True
```

---

# 9. Short-Circuit Evaluation (Very Important)

Python avoids unnecessary work using **short-circuit evaluation**.

Example

```python
False and print("Hello")
```

Output

```
False
```

`print("Hello")` never runs because the first condition is already `False`.

Similarly:

```python
True or print("Hello")
```

Output

```
True
```

Python stops because `or` already has one `True`.

This makes programs faster and avoids unnecessary operations. ([Runestone Academy][2])

---

# 10. Magento Comparison (PHP vs Python)

### PHP

```php
if ($customerLoggedIn && $productInStock) {
    echo "Buy Now";
}
```

Python

```python
if customer_logged_in and product_in_stock:
    print("Buy Now")
```

---

PHP

```php
if ($isAdmin || $isManager)
```

Python

```python
if is_admin or is_manager:
```

---

PHP

```php
if (!$loggedIn)
```

Python

```python
if not logged_in:
```

---

# 11. AI Connection

Every AI Agent uses logical operators.

Example:

Customer:

> "Cancel my order"

Agent checks:

```
Is customer logged in?

AND

Does order exist?

AND

Has order shipped?
```

Logic

```python
if logged_in and order_exists and not shipped:
    cancel_order()
```

Without logical operators:

* AI cannot validate permissions.
* AI cannot combine business rules.
* AI cannot make reliable decisions.

---

# 12. Mini Project

## Loan Eligibility Checker

```python
age = 28
salary = 40000

eligible = age >= 21 and salary >= 30000

print(eligible)
```

Output

```
True
```

---

Another example

```python
age = 19
salary = 50000

eligible = age >= 21 and salary >= 30000

print(eligible)
```

Output

```
False
```

---

# 13. Common Beginner Mistakes

### ❌ Mistake 1

```python
if age > 18 & salary > 30000
```

Wrong.

Use

```python
if age > 18 and salary > 30000:
```

---

### ❌ Mistake 2

```python
if age >18 or 21
```

Wrong.

Correct

```python
if age > 18 or age == 21:
```

Every side of `or` must be a complete condition. ([Runestone Academy][2])

---

### ❌ Mistake 3

```python
not age >18
```

Works, but this is clearer:

```python
not (age > 18)
```

---

# 14. Homework

### Exercise 1

Print whether a customer can place an order.

Variables

```python
logged_in = True
product_available = True
```

Expected

```
Order Allowed
```

---

### Exercise 2

Check if someone is eligible for a driving license.

Conditions

* Age ≥ 18
* Has ID

---

### Exercise 3

Create a simple login checker.

Variables

```python
username = "admin"
password = "1234"
```

Only print:

```
Login Successful
```

when both are correct.

---

# Lesson Summary

You learned:

* ✅ `and`
* ✅ `or`
* ✅ `not`
* ✅ Truth Tables
* ✅ Combining Conditions
* ✅ Short-Circuit Evaluation
* ✅ Magento vs Python syntax
* ✅ AI Agent decision making using logical operators

