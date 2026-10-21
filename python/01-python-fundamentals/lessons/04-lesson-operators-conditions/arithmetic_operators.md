# **Part 1 – Arithmetic Operators**

We won't move ahead until you fully understand it.

---

# What is an Operator?

An operator tells Python **what action to perform**.

Think of it as a mathematical symbol.

Example:

```text
20 + 10
```

The `+` tells Python:

> Add these two values.

Without operators, Python would simply have values with no instructions about what to do with them.

---

# Real-World Example

Suppose you buy:

* Laptop = ₹50,000
* Mouse = ₹2,000

Your total bill is:

```text
50000 + 2000
```

The `+` operator performs the addition.

Simple.

---

# Magento Example

Suppose a customer buys:

```text
Product Price = ₹1000

Tax = ₹180
```

Python:

```python
total = price + tax
```

Magento does calculations like this all the time for totals, shipping, tax, and discounts.

---

# Arithmetic Operators

| Operator | Meaning        | Example   | Result |
| -------- | -------------- | --------- | -----: |
| `+`      | Addition       | `10 + 5`  |     15 |
| `-`      | Subtraction    | `10 - 5`  |      5 |
| `*`      | Multiplication | `10 * 5`  |     50 |
| `/`      | Division       | `10 / 5`  |    2.0 |
| `%`      | Remainder      | `10 % 3`  |      1 |
| `//`     | Floor Division | `10 // 3` |      3 |
| `**`     | Power          | `2 ** 3`  |      8 |

Don't memorize these yet—we'll understand each one with examples.

---

# Addition (`+`)

```python
a = 20
b = 10

print(a + b)
```

Output:

```text
30
```

---

# Subtraction (`-`)

```python
a = 20
b = 10

print(a - b)
```

Output:

```text
10
```

---

# Multiplication (`*`)

```python
a = 20
b = 10

print(a * b)
```

Output:

```text
200
```

---

# Division (`/`)

```python
a = 20
b = 10

print(a / b)
```

Output:

```text
2.0
```

Notice the result is **2.0**, not **2**.

Why?

Because Python's `/` operator always returns a **float**.

We'll understand why when we discuss numeric types in more depth.

---

# AI Connection

Suppose you're building an AI application that estimates token costs.

```text
Total Tokens = 1500

Price Per 1000 Tokens = ₹0.50
```

You might calculate:

```python
cost = (1500 / 1000) * 0.50
```

Even AI applications use arithmetic every day.

---

# Common Beginner Mistake

Many beginners think:

```python
print(20 / 10)
```

should print:

```text
2
```

But Python prints:

```text
2.0
```

because `/` performs floating-point division.

If you specifically want an integer result, there are other operators (`//`) that we'll learn next.

---

# 🧪 Mini Challenge 1

Without running Python, predict the output.

### Question 1

```python
print(25 + 15)
```

### Question 2

```python
print(50 - 20)
```

### Question 3

```python
print(6 * 8)
```

### Question 4

```python
print(100 / 4)
```

Write only the outputs.

---

# Homework

Create:

```text
lesson-7-part1.py
```

Write:

```python
a = 100
b = 25

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
```

Run it and send me:

1. Your code.
2. The output.
3. The answers to the four mini challenge questions.

---

Perfect! 🚀

We'll continue **Lesson 7**.

> **Current Status**
>
> Lesson 7 → Module 1 → Arithmetic Operators
>
> ✅ Addition
> ✅ Subtraction
> ✅ Multiplication
> ✅ Division
>
> Today we'll complete Module 1.

---

# 📖 Lesson 7 - Module 1 (Continued)

## Remaining Arithmetic Operators

Today we'll learn:

* `%` (Modulus)
* `//` (Floor Division)
* `**` (Power)

These operators may look strange at first, but they're used in real applications much more often than beginners realize.

---

# 1. Modulus Operator (`%`)

## What is Modulus?

The modulus operator returns the **remainder** after division.

Formula:

```text
Dividend % Divisor = Remainder
```

Example:

```python
10 % 3
```

Let's calculate it manually.

```
3 × 3 = 9

10 - 9 = 1
```

Therefore:

```python
10 % 3
```

Result:

```
1
```

---

## Real-World Example

Imagine you have **10 chocolates**.

You want to distribute them equally among **3 children**.

```
Child 1 → 3 chocolates

Child 2 → 3 chocolates

Child 3 → 3 chocolates

Remaining → 1 chocolate
```

That **remaining chocolate** is exactly what `%` returns.

---

# More Examples

```python
print(20 % 5)
```

```
0
```

Why?

Because:

```
20 ÷ 5 = 4

No remainder
```

---

```python
print(17 % 5)
```

```
2
```

Because:

```
5 × 3 = 15

17 - 15 = 2
```

---

# Why is `%` Useful?

Suppose you want to check whether a number is **even**.

A number is even if:

```python
number % 2 == 0
```

Example:

```
8 % 2 = 0
```

Even.

```
7 % 2 = 1
```

Odd.

---

# Magento Example

Suppose you're displaying products.

You want every **4th product** to show a special banner.

```
Product 4

↓

4 % 4 = 0

↓

Show Banner
```

Product 8

```
8 % 4 = 0
```

Show Banner again.

This kind of logic is common in frontend layouts.

---

# AI Connection

Imagine you're processing **100 customer reviews**.

You want to save progress after every 10 reviews.

Python:

```python
if review_number % 10 == 0:
    print("Saving progress...")
```

The `%` operator helps you trigger actions at regular intervals.

---

# Module Challenge 1

Predict:

```python
print(15 % 4)
```

---

```python
print(30 % 6)
```

---

```python
print(19 % 2)
```

---

# 2. Floor Division (`//`)

This operator confuses many beginners.

Let's make it simple.

---

## Normal Division

```python
10 / 3
```

Output:

```
3.3333333333
```

---

## Floor Division

```python
10 // 3
```

Output:

```
3
```

Python removes the decimal part.

It doesn't round up.

It simply keeps the whole-number portion.

---

# Real-World Example

Suppose you have **10 pizzas**.

Each table can hold **3 pizzas**.

Question:

How many completely filled tables do you get?

```
10 // 3
```

Answer:

```
3 tables
```

One pizza is left over.

---

# Magento Example

Suppose:

```
105 products

20 products per page
```

How many completely full pages?

```
105 // 20

↓

5
```

Five full pages.

The remaining products go onto a partially filled page.

---

# AI Connection

Suppose an LLM allows:

```
1000 tokens
```

Each chunk contains:

```
200 tokens
```

How many full chunks?

```python
1000 // 200
```

```
5
```

This kind of calculation appears in chunking documents for RAG applications.

---

# Challenge 2

Predict:

```python
print(25 // 4)
```

---

```python
print(100 // 30)
```

---

# 3. Power Operator (`**`)

This means:

Raise a number to a power.

Example:

```python
2 ** 3
```

means

```
2 × 2 × 2
```

Result:

```
8
```

---

More examples:

```python
print(5 ** 2)
```

```
25
```

---

```python
print(10 ** 3)
```

```
1000
```

---

# AI Connection

Machine learning and AI algorithms often use exponents in mathematical formulas.

You don't need to understand those formulas today.

Just know that Python provides an operator for exponentiation.

---

# Challenge 3

Predict:

```python
print(3 ** 2)
```

---

```python
print(4 ** 3)
```

---

# Common Beginner Mistakes

### Mistake 1

Thinking:

```python
10 // 3
```

equals

```
4
```

❌ Wrong.

Python does **not** round.

It simply removes the decimal portion.

Result:

```
3
```

---

### Mistake 2

Confusing:

```python
/
```

with

```python
//
```

Remember:

```
/

↓

Normal Division

↓

3.333
```

```
//

↓

Floor Division

↓

3
```

---

### Mistake 3

Thinking:

```python
%
```

returns the quotient.

It returns the **remainder**.

---

# Mini Project

Create:

```
lesson-7-module1.py
```

```python
number = int(input("Enter a number: "))

print("Remainder when divided by 2:", number % 2)
print("Whole division by 2:", number // 2)
print("Square:", number ** 2)
```

Try it with:

```
7
```

Expected output:

```
Remainder when divided by 2: 1
Whole division by 2: 3
Square: 49
```

---

# Homework

## Challenge 1

Predict:

```python
15 % 4
30 % 6
19 % 2
```

---

## Challenge 2

Predict:

```python
25 // 4
100 // 30
```

---

## Challenge 3

Predict:

```python
3 ** 2
4 ** 3
```

---

Run the mini project and send me:

1. Your code.
2. The output.
3. Answers to all three challenges.

---

## 🎯 Interview Question

**Question:**

What is the difference between:

```python
/
```

and

```python
//
```

Answer this in your own words, as if an interviewer asked you.

---

# 📌 Lesson Status

**Lesson 7**

Module 1 Progress:

* ✅ Addition
* ✅ Subtraction
* ✅ Multiplication
* ✅ Division
* 🔄 Modulus (`%`)
* 🔄 Floor Division (`//`)
* 🔄 Power (`**`)

After this module is complete, we'll move to **Module 2 – Comparison Operators**, where Python starts making decisions. This is the foundation for `if` statements and, later, for the decision-making logic inside AI agents.

