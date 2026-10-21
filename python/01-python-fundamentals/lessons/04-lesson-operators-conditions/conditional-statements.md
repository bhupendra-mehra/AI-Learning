# 📚 Lesson 7 – Module 3

# Conditional Statements (`if`, `elif`, `else`)

> **Roadmap Note:** As discussed, we're intentionally teaching `if` before logical operators because it creates a smoother learning path. We'll cover `and`, `or`, and `not` in the next module.

---

# 🎯 Goal

By the end of this module, you'll understand:

* What `if` is.
* How `if` works internally.
* What indentation is and why Python uses it.
* `if`
* `else`
* `elif`
* Build your first decision-making program.

---

# Before We Learn `if`

Imagine you're a security guard.

A person arrives at the entrance.

Rule:

```text
Only people aged 18 or above can enter.
```

Person 1:

```text
Age = 20
```

Decision:

```text
Allow Entry
```

Person 2:

```text
Age = 15
```

Decision:

```text
Deny Entry
```

Notice something.

The security guard **doesn't treat everyone the same**.

The decision depends on a condition.

That is exactly what `if` does.

---

# What is `if`?

`if` means:

> **Execute this block of code only if the condition is True.**

Syntax:

```python
if condition:
    statement
```

Read it like English:

```text
IF the condition is true,
THEN execute the code below.
```

---

# Your First `if`

Create:

```text
lesson-7-module3.py
```

Write:

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

---

# Before Running It

Let's think like Python.

Step 1

```python
age = 20
```

Memory:

```text
age = 20
```

---

Step 2

Python reads:

```python
if age >= 18:
```

Internally:

```text
20 >= 18

↓

True
```

---

Step 3

Since the answer is `True`, Python executes the indented code:

```python
print("You are an adult.")
```

Output:

```text
You are an adult.
```

---

# What if the Condition is False?

Change the code:

```python
age = 15

if age >= 18:
    print("You are an adult.")
```

Now think.

Python checks:

```text
15 >= 18

↓

False
```

When the condition is `False`:

Python **skips** the indented block.

Output:

```text
(No output)
```

This surprises many beginners.

Python didn't crash.

It simply had nothing to execute.

---

# The Most Important Python Rule

## Indentation

Look carefully.

Correct:

```python
if age >= 18:
    print("Adult")
```

Notice the spaces before `print()`.

Those spaces tell Python:

> This line belongs to the `if`.

Without indentation:

```python
if age >= 18:
print("Adult")
```

Python raises an error because it doesn't know where the `if` block starts.

Unlike PHP, which uses `{ }`, Python uses indentation to define blocks.

---

# PHP Comparison

PHP:

```php
if ($age >= 18) {
    echo "Adult";
}
```

Python:

```python
if age >= 18:
    print("Adult")
```

Different syntax.

Same logic.

---

# Adding `else`

Now let's handle both possibilities.

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Think like Python.

```text
15 >= 18

↓

False

↓

Skip if block

↓

Run else block

↓

Minor
```

Output:

```text
Minor
```

---

# Adding `elif`

Sometimes there are more than two possibilities.

Example:

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
```

Python checks from top to bottom.

```text
marks >= 90 ?

↓

False

↓

marks >= 75 ?

↓

True

↓

Print Grade B

↓

Stop checking
```

It never reaches the `else` block.

---

# 🧠 Debugger View

Code:

```python
marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")
```

Conceptual execution:

```text
Memory

marks = 75

↓

Check 1

75 >= 90

↓

False

↓

Check 2

75 >= 75

↓

True

↓

Print B

↓

End
```

---

# Magento Connection

Imagine product stock.

```python
stock = 5

if stock > 0:
    print("In Stock")
else:
    print("Out of Stock")
```

This is conceptually similar to how Magento decides which stock message to show.

---

# AI Connection

Suppose your AI assistant receives a question:

> "Track my order."

Your Python application first checks:

```python
if order_exists:
    # Ask the LLM to generate a tracking response.
else:
    # Ask the LLM to explain that the order wasn't found.
```

Again, Python makes the decision.

The LLM writes the response.

---

# Common Beginner Mistakes

## ❌ Mistake 1

Forgetting the colon:

```python
if age >= 18
```

Wrong.

Correct:

```python
if age >= 18:
```

---

## ❌ Mistake 2

Incorrect indentation:

```python
if age >= 18:
print("Adult")
```

Python raises an `IndentationError`.

---

## ❌ Mistake 3

Using `=` instead of `==`:

```python
if age = 18:
```

Wrong.

Comparison uses:

```python
if age == 18:
```

---

# 🧪 Practice Program

Write:

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

Try:

```
17
```

and

```
18
```

Observe how the output changes.

---

# Homework

Create:

```text
lesson-7-module3.py
```

Write the program above and run it with both inputs (`17` and `18`).

Then answer:

### Q1

What happens if the condition is `False` and there is **no** `else` block?

---

### Q2

Why does Python require indentation?

---

### Q3

In your own words, explain the difference between:

* `if`
* `elif`
* `else`

---

# 🎤 Interview Question

**Question:**

Why does Python use indentation instead of braces (`{}`)?

You don't need the historical reason.

Just explain what indentation achieves in a Python program.

---

# 📌 Lesson Status

**Lesson 7 Progress**

* ✅ Module 1 – Arithmetic Operators
* ✅ Module 2 – Comparison Operators
* 🔄 Module 3 – Conditional Statements (`if`, `elif`, `else`)
* ⏳ Module 4 – Logical Operators (`and`, `or`, `not`)
* ⏳ Module 5 – Final Project

---
