# Lesson 8 – Module 2: `for` Loop

**Estimated Time:** 60–75 Minutes

## Learning Objectives

By the end of this module, you will be able to:

* Understand what a `for` loop is.
* Write your own `for` loops.
* Understand the loop variable.
* Understand how `range()` works.
* Predict the output of a `for` loop.
* Compare Python `for` loops with PHP `foreach`.
* Understand where AI agents use `for` loops.

---

# 1. What is a `for` Loop?

A `for` loop is used when Python needs to perform the **same task for every item in a collection** or **repeat a task a known number of times**.

Think of it as telling Python:

> "Do this once for each item."

Examples:

* Print numbers from 1 to 10.
* Print every product in Magento.
* Read every line in a file.
* Process every page of a PDF.
* Summarize every customer review.

Notice something common?

We already know **how many items** (or at least what collection) we're working with.

That's where `for` is the best choice.

---

# 2. Basic Syntax

```python
for variable in sequence:
    # code to repeat
```

Let's understand each part.

```python
for
```

This tells Python:

> "Start a loop."

---

```python
variable
```

This is called the **loop variable**.

It stores the current value during each iteration.

Example:

```python
for i in range(5):
```

Here,

```python
i
```

changes automatically.

First iteration

```text
i = 0
```

Second

```text
i = 1
```

Third

```text
i = 2
```

until the loop finishes.

---

# 3. What is `range()`?

`range()` is a built-in Python function that generates a sequence of numbers.

For now, remember these two forms:

```python
range(5)
```

Produces:

```text
0 1 2 3 4
```

Notice:

It **starts at 0**.

It **stops before 5**.

---

Another example:

```python
range(1, 6)
```

Produces:

```text
1 2 3 4 5
```

Rule:

```text
range(start, stop)

Start → Included

Stop → Excluded
```

This "stop is excluded" rule is one of the most important things to remember in Python.

---

# 4. First Example

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

# 5. How Python Executes This

Imagine Python running:

```python
for i in range(5):
    print(i)
```

Internally, it's similar to:

```text
Iteration 1

i = 0

↓

print(0)

-----------------

Iteration 2

i = 1

↓

print(1)

-----------------

Iteration 3

i = 2

↓

print(2)

-----------------

Iteration 4

i = 3

↓

print(3)

-----------------

Iteration 5

i = 4

↓

print(4)

Loop Ends
```

Python automatically updates `i` for each iteration.

You don't have to do it manually.

---

# 6. Printing Something Multiple Times

Suppose you want:

```text
Welcome
Welcome
Welcome
```

Code:

```python
for i in range(3):
    print("Welcome")
```

Output:

```text
Welcome
Welcome
Welcome
```

Notice that `i` isn't used.

We'll discuss the `_` convention later as a Python best practice.

For now, using `i` is perfectly fine while you're learning.

---

# 7. Printing 1 to 10

```python
for i in range(1, 11):
    print(i)
```

Output:

```text
1
2
3
4
5
6
7
8
9
10
```

Again,

`11` isn't printed because the stop value is excluded.

---

# 8. Magento Comparison

PHP:

```php
foreach ($products as $product) {
    echo $product->getName();
}
```

Python:

```python
for product in products:
    print(product.name)
```

Notice the similarity:

* One product at a time.
* Same block of code.
* Loop ends automatically after the last product.

---

# 9. AI Agent Example

Suppose an AI agent receives 100 customer reviews.

Conceptually:

```python
for review in reviews:
    analyze(review)
```

Execution:

```text
Review 1

↓

Analyze

↓

Review 2

↓

Analyze

↓

...

↓

Review 100

↓

Analyze

↓

Done
```

This is one of the most common patterns in AI systems.

---

# 10. Common Beginner Mistakes

### Mistake 1

Expecting:

```python
range(5)
```

to produce

```text
1 2 3 4 5
```

It doesn't.

It produces:

```text
0 1 2 3 4
```

---

### Mistake 2

Thinking the stop value is included.

Example:

```python
range(1,5)
```

Many beginners expect:

```text
1 2 3 4 5
```

Actual output:

```text
1 2 3 4
```

The stop value is **always excluded**.

---

### Mistake 3

Trying to change the loop variable manually.

Example:

```python
for i in range(5):
    i = 100
```

Python will still control the next iteration.

The loop variable is managed by the loop itself.

---

# Senior Developer Tip

Don't memorize `range()`.

Understand its behavior.

If you know:

> **Start is included, stop is excluded**

you can predict almost every `range()` result correctly.

---

# Exercises

Now we'll practice **only what we've learned in this module**.

### Exercise 1

Print:

```text
Python
```

exactly **5 times**.

---

### Exercise 2

Print numbers from **1 to 20**.

---

### Exercise 3

Print numbers from **0 to 9**.

---

### Exercise 4

Without running the code, predict the output:

```python
for i in range(2, 6):
    print(i)
```

---

### Exercise 5

Without running the code, predict the output:

```python
for i in range(3):
    print("AI")
```

---

# Module Summary

Today you learned:

* ✅ What a `for` loop is.
* ✅ Loop syntax.
* ✅ Loop variable.
* ✅ `range(start, stop)`.
* ✅ Why the stop value is excluded.
* ✅ Python execution flow.
* ✅ Magento `foreach` comparison.
* ✅ AI agent usage.

---

**Complete these five exercises and send me your answers.**

If you solve them correctly, we'll move directly to the next part of Module 2, where we'll extend `for` loops to work with **strings** and then introduce **nested `for` loops** before moving on to the module's mini project. This keeps everything within Module 2 without introducing concepts from later modules.


Perfect. Since **Module 2** is not a large topic, we'll **finish it completely in one go** instead of splitting it further.

---

# Lesson 8 – Module 2 (Part 2): Iterating Over Strings, Nested Loops & Mini Project

**Goal:** Complete everything related to the `for` loop before moving to `while`.

---

# 1. Iterating Over Strings

Until now, we've used `range()` to generate numbers.

A `for` loop can also iterate directly over a string.

Example:

```python
name = "Bhupendra"

for ch in name:
    print(ch)
```

### Output

```text
B
h
u
p
e
n
d
r
a
```

---

## How Python Executes It

Python internally thinks like this:

```text
name = "Bhupendra"

↓

First Character

↓

B

↓

Second Character

↓

h

↓

Third Character

↓

u

↓

...

↓

Last Character

↓

a

↓

End
```

Each iteration stores one character in the loop variable.

Here:

```python
ch
```

contains

```
Iteration 1 → B
Iteration 2 → h
Iteration 3 → u
...
```

---

## Magento Comparison

PHP

```php
$name = "Magento";

foreach(str_split($name) as $char){
    echo $char;
}
```

Python

```python
for ch in "Magento":
    print(ch)
```

Python is simpler because strings are already iterable.

---

## AI Example

Suppose an AI validates a coupon code.

```python
coupon = "SAVE20"

for ch in coupon:
    print(ch)
```

The AI can inspect each character one by one.

---

# 2. Nested `for` Loops

A nested loop means:

> A loop inside another loop.

Syntax

```python
for i in range(...):

    for j in range(...):

        print(i, j)
```

---

## Example

```python
for i in range(3):

    for j in range(2):

        print(i, j)
```

Output

```text
0 0
0 1
1 0
1 1
2 0
2 1
```

---

## Execution Flow

```text
Outer Loop → i = 0

      ↓

Inner Loop

j = 0

j = 1

↓

Outer Loop → i = 1

↓

Inner Loop

j = 0

j = 1

↓

Outer Loop → i = 2

↓

Inner Loop

j = 0

j = 1
```

**Important Rule**

The **inner loop completes all its iterations** before the outer loop moves to the next value.

---

## Real-Life Example

Imagine a classroom.

3 rows

Each row has 4 students.

```text
Row 1

Student 1

Student 2

Student 3

Student 4

↓

Row 2

Student 1

Student 2

Student 3

Student 4
```

Rows = Outer Loop

Students = Inner Loop

---

## Magento Example

Categories

```
Electronics

    Laptop

    Mobile

Fashion

    Shirt

    Shoes
```

Conceptually:

```python
for category in categories:

    for product in category.products:

        print(product)
```

Nested loops are very common when dealing with hierarchical data.

---

## AI Example

Imagine an AI processes multiple documents.

Each document contains multiple pages.

```text
Document 1

Page 1

Page 2

↓

Document 2

Page 1

Page 2

↓

Document 3

...
```

Conceptually:

```python
for document in documents:

    for page in document.pages:

        analyze(page)
```

This is a real-world use of nested loops.

---

# 3. Common Mistakes

### Mistake 1

Confusing the outer and inner loop variables.

Bad:

```python
for i in range(3):

    for i in range(2):
        print(i)
```

Correct:

```python
for i in range(3):

    for j in range(2):
        print(i, j)
```

Always use different variable names for different loops.

---

### Mistake 2

Expecting the inner loop to continue where it left off.

It **starts from the beginning every time** the outer loop changes.

---

### Mistake 3

Using nested loops unnecessarily.

If one loop is enough, don't add another.

Nested loops increase complexity and can slow programs when processing large amounts of data.

---

# Senior Developer Tips

### 1.

Choose meaningful variable names.

Instead of:

```python
for i in products:
```

Prefer:

```python
for product in products:
```

Much easier to read.

---

### 2.

When iterating over characters:

```python
for character in word:
```

is more descriptive than:

```python
for c in word:
```

---

### 3.

Don't use nested loops unless the data naturally has multiple levels.

Example:

```
Orders

↓

Order Items
```

is a natural fit for nested loops.

---

# Mini Project

## Student Attendance System

Requirements

1. Ask how many students are present.

2. Print:

```
Student 1 Present

Student 2 Present

...
```

3. Ask for a classroom name.

4. Print each character of the classroom name on a new line.

This project combines:

* `for`
* `range()`
* String iteration
* User input

No new concepts beyond this module.

---

# Exercises

### Exercise 1

Print every character of your name on a separate line.

---

### Exercise 2

Predict the output without running:

```python
for ch in "AI":
    print(ch)
```

---

### Exercise 3

Predict the output:

```python
for i in range(2):

    for j in range(3):

        print(i, j)
```

---

### Exercise 4

Write a program that asks the user for a word and prints each letter on a new line.

---

### Exercise 5 (Mini Project)

Implement the **Student Attendance System** described above.

---

# Module 2 Summary

You have now learned everything related to the **`for` loop**:

* ✅ `for` loop syntax
* ✅ Loop variables
* ✅ `range()`
* ✅ Iterating over strings
* ✅ Nested loops
* ✅ Python best practices
* ✅ Magento use cases
* ✅ AI agent use cases

---

## Roadmap Progress

* ✅ Lesson 8 – Module 1: Completed
* 🔄 Lesson 8 – Module 2: **Awaiting exercises**
* ⏭️ Next: **Lesson 8 – Module 3: `while` Loop** (we'll cover it in one complete session, as per our new course format).

