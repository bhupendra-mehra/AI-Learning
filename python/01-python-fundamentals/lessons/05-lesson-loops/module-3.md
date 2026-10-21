## Lesson 8 – Module 3: `while` Loop

**Estimated Time:** 30–40 minutes

## Learning Objectives

By the end of this module, you will:

* Know when to use `while` instead of `for`.
* Write `while` loops confidently.
* Avoid infinite loops.
* Build input validation using `while`.

---

# 1. What is a `while` Loop?

A `while` loop repeats **as long as a condition is `True`**.

Unlike a `for` loop, you usually **don't know in advance how many times it will run**.

### Syntax

```python
while condition:
    # Code
```

---

# 2. `for` vs `while`

Use **`for`** when you already know what you're iterating over.

Examples:

* Products
* Students
* Pages
* Characters in a string

```python
for product in products:
    print(product)
```

---

Use **`while`** when repetition depends on a condition.

Examples:

* Login until password is correct.
* Retry API until success.
* ATM PIN validation.
* Menu until user exits.

```python
while password != "1234":
    password = input("Enter Password: ")
```

---

# 3. Basic Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output

```text
1
2
3
4
5
```

---

## Important

This line:

```python
count += 1
```

is called the **update statement**.

Without it...

```python
count = 1

while count <= 5:
    print(count)
```

Output

```text
1
1
1
1
1
...
```

The program never stops.

This is called an **Infinite Loop**.

---

# 4. Infinite Loop

Example

```python
while True:
    print("Running...")
```

This continues forever until the program is stopped.

Sometimes this is intentional.

Example:

* Web servers
* Queue workers
* AI agents waiting for new tasks

---

# 5. Magento Example

Imagine Magento retries an API call.

Conceptually:

```python
success = False

while not success:
    # Call API
```

Keep trying until it succeeds.

---

# 6. AI Agent Example

An AI assistant waits for user messages.

Conceptually:

```python
running = True

while running:
    message = get_message()
    process(message)
```

The assistant keeps listening until it's shut down.

---

# 7. Best Practices

### Always update the condition

```python
count += 1
```

or

```python
password = input(...)
```

Otherwise, the loop may never end.

---

### Keep conditions simple

Good

```python
while count <= 10:
```

Avoid overly complicated conditions unless necessary.

---

# 8. Common Mistakes

### ❌ Forgetting to update the variable

```python
count = 1

while count <= 5:
    print(count)
```

Infinite loop.

---

### ❌ Wrong comparison

```python
count = 5

while count <= 1:
```

Loop never runs because the condition is `False` from the start.

---

### ❌ Using `while` when `for` is simpler

Don't write:

```python
count = 1

while count <= 10:
    print(count)
    count += 1
```

when this is enough:

```python
for i in range(1, 11):
    print(i)
```

Choose the simpler tool.

---

# Mini Project

## Login System

Requirements

* Ask the user for a password.
* Keep asking until the password is:

```text
python123
```

* Print:

```text
Login Successful
```

when the correct password is entered.

---

# Exercises

## Exercise 1

Print numbers from **1 to 10** using a `while` loop.

---

## Exercise 2

Print numbers from **10 to 1**.

---

## Exercise 3

Predict the output.

```python
count = 3

while count > 0:
    print(count)
    count -= 1
```

---

## Exercise 4

Write a program that asks the user to enter a number greater than **100**.

Keep asking until they enter a valid number.

Example:

```text
Enter Number: 25

Invalid

Enter Number: 80

Invalid

Enter Number: 150

Accepted
```

---

## Exercise 5 (Mini Project)

Build the **Login System** described above.

---

# Senior Developer Tips

* Use `for` when the number of iterations is known.
* Use `while` when repetition depends on a changing condition.
* Before writing a `while` loop, always ask yourself:

> **"What changes inside the loop so that it will eventually stop?"**

If the answer is "nothing," you've probably written an infinite loop.

---

# Module Summary

You now know:

* ✅ `while` syntax
* ✅ Difference between `for` and `while`
* ✅ Infinite loops
* ✅ Input validation
* ✅ Best practices
* ✅ Common mistakes

This covers everything you need before moving on to loop control statements.

---

### Complete the five exercises and send me your solutions.

If they're correct, we'll finish **Lesson 8** with **Module 4 (Loop Control Statements)** and **Module 5 (Final Project)**. Those two modules are closely related, so we'll combine them into a single fast-track session to complete the lesson efficiently.
