# 📚 Lesson 7 – Module 2

# Comparison Operators

---

# 🎯 Goal

By the end of this module, you'll understand:

* What comparison operators are.
* Why they return `True` or `False`.
* How they're used in Magento.
* How they're used in AI.
* How Python internally evaluates comparisons.

---

# Why Do We Need Comparison Operators?

Let's think like software developers.

Suppose a customer logs into your Magento store.

Before showing the **Wholesale Dashboard**, Magento asks:

```text
Is this customer a wholesale customer?
```

Possible answers:

```text
Yes

or

No
```

Not:

* Maybe
* Almost
* Around 70%

Just:

```text
True

False
```

This is exactly what comparison operators do.

---

# Real-World Example

Imagine a security guard at an office.

Rule:

```text
Age >= 18
```

Visitor 1

```text
Age = 20
```

Security Guard:

```text
20 >= 18

↓

True

↓

Allow Entry
```

Visitor 2

```text
Age = 16
```

Security Guard:

```text
16 >= 18

↓

False

↓

Deny Entry
```

The security guard is simply evaluating a condition.

---

# What Does Python Do?

Suppose Python sees:

```python
age = 37

print(age > 18)
```

Conceptually:

```text
Read variable age

↓

age = 37

↓

Compare

37 > 18 ?

↓

True

↓

Print True
```

Notice:

Python is **not calculating**.

It is **comparing**.

---

# Comparison Operators

| Operator | Meaning               | Example    | Result |
| -------- | --------------------- | ---------- | ------ |
| `==`     | Equal to              | `10 == 10` | `True` |
| `!=`     | Not equal to          | `10 != 5`  | `True` |
| `>`      | Greater than          | `20 > 10`  | `True` |
| `<`      | Less than             | `5 < 10`   | `True` |
| `>=`     | Greater than or equal | `18 >= 18` | `True` |
| `<=`     | Less than or equal    | `15 <= 20` | `True` |

---

# Operator 1 – Equal (`==`)

Example:

```python
print(10 == 10)
```

Python asks:

```text
Is 10 equal to 10?
```

Answer:

```text
True
```

---

Another example:

```python
print(10 == 20)
```

Python asks:

```text
Is 10 equal to 20?
```

Answer:

```text
False
```

---

# Common Beginner Mistake

Many beginners write:

```python
age = 20

print(age = 20)
```

❌ Wrong.

Remember:

```python
=
```

means:

> Store a value.

Whereas:

```python
==
```

means:

> Compare two values.

---

# Easy Trick to Remember

Think of it this way:

```text
=

Put something into a box.
```

```text
==

Ask a question about what's inside the box.
```

---

# Magento Example

PHP:

```php
$productStatus = 1;
```

Assignment.

Later:

```php
if ($productStatus == 1)
```

Comparison.

The same idea exists in Python.

---

# Operator 2 – Not Equal (`!=`)

Example:

```python
print(10 != 20)
```

Python asks:

```text
Are these NOT equal?
```

Answer:

```text
True
```

Another example:

```python
print(10 != 10)
```

Answer:

```text
False
```

---

# Operator 3 – Greater Than (`>`)

```python
print(25 > 20)
```

Python asks:

```text
Is 25 greater than 20?
```

Result:

```text
True
```

---

# Operator 4 – Less Than (`<`)

```python
print(15 < 20)
```

Result:

```text
True
```

---

# Operator 5 – Greater Than or Equal (`>=`)

Example:

```python
print(18 >= 18)
```

Question:

```text
Is 18 greater than OR equal to 18?
```

Answer:

```text
True
```

---

# Operator 6 – Less Than or Equal (`<=`)

```python
print(10 <= 20)
```

Answer:

```text
True
```

---

# 🧠 Debugger View

Let's see what happens conceptually.

Code:

```python
age = 37

print(age >= 18)
```

Execution:

```text
Step 1

Variable created

age = 37

↓

Step 2

Comparison starts

37 >= 18

↓

Step 3

Result

True

↓

Step 4

Print

True
```

---

# Magento Connection

Suppose a product has:

```text
Quantity = 15
```

Before showing the Add to Cart button:

```python
quantity > 0
```

Result:

```text
True
```

Show:

```text
Add to Cart
```

If:

```text
Quantity = 0
```

Then:

```python
quantity > 0
```

Result:

```text
False
```

Show:

```text
Out of Stock
```

This is exactly how business rules are implemented.

---

# AI Connection

Imagine you're building a Magento AI Assistant.

A user asks:

> "Can I buy this product?"

Your application checks:

```python
stock > 0
```

If `True`:

The AI replies:

> "Yes, the product is currently in stock."

If `False`:

The AI replies:

> "This product is currently out of stock."

Notice something important:

The **LLM didn't check the stock**.

Your **Python application** checked the stock using a comparison operator, then used that result to decide what information to send to the user.

This distinction is fundamental in AI engineering.

---

# Practice Program

Create:

```text
lesson-7-module2.py
```

Write:

```python
age = 37

print(age == 37)
print(age != 37)
print(age > 18)
print(age < 18)
print(age >= 37)
print(age <= 40)
```

Before running it, try to predict every output.

---

# 🧪 Mini Challenge

Without running Python, answer these:

### Q1

```python
print(50 == 50)
```

---

### Q2

```python
print(100 != 50)
```

---

### Q3

```python
print(25 < 20)
```

---

### Q4

```python
print(30 >= 30)
```

---

### Q5

```python
print(18 <= 17)
```

---

# 🎤 Interview Question

Explain the difference between:

```python
=
```

and

```python
==
```

Imagine you're answering in an interview.

---

# Homework

1. Create `lesson-7-module2.py`.
2. Run it.
3. Paste:

   * Your code.
   * The output.
4. Answer all five mini challenge questions.
5. Answer the interview question in your own words.

---

## 📌 Lesson Status

**Lesson 7**

* ✅ Module 1 – Arithmetic Operators
* 🔄 Module 2 – Comparison Operators (**In Progress**)
* ⏳ Module 3 – Logical Operators
* ⏳ Module 4 – `if`, `elif`, `else`
* ⏳ Module 5 – Final Project

---
