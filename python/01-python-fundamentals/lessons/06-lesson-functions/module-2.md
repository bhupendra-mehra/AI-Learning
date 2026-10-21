# Lesson 9 – Module 2

## Parameters, Return Values & Variable Scope

**Estimated Time:** 45–60 minutes

---

# 1. Parameters

Until now, our function always printed the same value.

```python
def greet():
    print("Hello")
```

What if we want to greet different people?

Instead of creating:

```python
def greet_bhupendra():
```

```python
def greet_rohit():
```

We pass the name as a **parameter**.

```python
def greet(name):
    print(f"Hello {name}")
```

Calling:

```python
greet("Bhupendra")
greet("Rohit")
```

Output

```text
Hello Bhupendra
Hello Rohit
```

### Key Point

A **parameter** is the variable inside the function definition.

```python
def greet(name):
```

`name` is the parameter.

---

# 2. Arguments

When calling the function:

```python
greet("Bhupendra")
```

`"Bhupendra"` is called an **argument**.

Remember:

| Parameter                       | Argument                            |
| ------------------------------- | ----------------------------------- |
| Variable in function definition | Actual value passed to the function |

---

# 3. Multiple Parameters

```python
def add(a, b):
    print(a + b)
```

Calling

```python
add(10, 20)
```

Output

```text
30
```

---

# 4. Returning Values

So far we've used `print()`.

But what if another function needs the result?

Use `return`.

Example

```python
def add(a, b):
    return a + b
```

Calling

```python
total = add(10, 20)

print(total)
```

Output

```text
30
```

---

## `print()` vs `return`

### `print()`

Displays the value.

```python
def add(a, b):
    print(a + b)
```

You can't reuse the result easily.

---

### `return`

Sends the value back.

```python
def add(a, b):
    return a + b
```

Now you can do:

```python
total = add(10, 20)

discount = total * 0.1
```

This is how production code works.

---

# 5. Multiple Return Values

Python allows multiple values.

```python
def calculate(a, b):
    return a + b, a - b
```

Calling

```python
sum_value, difference = calculate(10, 5)

print(sum_value)
print(difference)
```

Output

```text
15
5
```

---

# 6. Variable Scope

## Local Variable

```python
def test():
    age = 30
```

`age` exists only inside `test()`.

This will fail:

```python
test()

print(age)
```

Because `age` is local.

---

## Global Variable

```python
name = "Bhupendra"

def greet():
    print(name)
```

Output

```text
Bhupendra
```

The function can read global variables.

---

### Best Practice

Prefer passing values as parameters instead of relying on global variables.

Good

```python
def greet(name):
    print(name)
```

Avoid

```python
name = "Bhupendra"

def greet():
    print(name)
```

This makes functions easier to reuse and test.

---

# 7. Magento Comparison

Instead of

```php
$productName = "Laptop";

echoDiscount();
```

A better approach is

```php
calculateDiscount($price);
```

Python

```python
calculate_discount(price)
```

Exactly the same idea.

---

# 8. AI Example

Instead of writing:

```python
summarize_invoice()

summarize_resume()

summarize_email()
```

We write:

```python
summarize(document)
```

Now the same function works for any document.

This is one of the biggest advantages of functions.

---

# 9. Best Practices

✅ One function should perform one task.

Good

```python
calculate_discount()
```

Bad

```python
calculate_discount_and_send_email_and_save_database()
```

---

Prefer

```python
return
```

over

```python
print()
```

when another part of the program needs the result.

---

# Exercises

## Exercise 1

Create a function

```python
greet(name)
```

Print

```text
Welcome Bhupendra
```

Call it twice with different names.

---

## Exercise 2

Create

```python
multiply(a, b)
```

Return the multiplication.

Example

```python
result = multiply(5, 6)

print(result)
```

Output

```text
30
```

---

## Exercise 3

Predict the output.

```python
def test(a):
    print(a)

test(100)
```

---

## Exercise 4

Predict the output.

```python
name = "Python"

def show():
    print(name)

show()
```

---

## Exercise 5

Predict whether this works.

```python
def show():
    age = 25

show()

print(age)
```

If not, explain why.

---

# Mini Project

## Employee Salary Calculator

Requirements

Create

```python
calculate_salary(hours, rate)
```

Return

```text
hours × rate
```

Then

```python
hours = int(input(...))

rate = int(input(...))

salary = calculate_salary(hours, rate)

print(salary)
```

---

# Senior Developer Tip

One of the biggest differences between junior and senior developers is this:

A junior developer writes code that works.

A senior developer writes **reusable** code.

Functions are the first step toward writing reusable software.

---

## Module Summary

Today you learned:

* ✅ Parameters
* ✅ Arguments
* ✅ Multiple Parameters
* ✅ `return`
* ✅ Multiple Returns
* ✅ Local Variables
* ✅ Global Variables
* ✅ Function Best Practices

---

Complete these exercises, and then we'll move to the **last theory module** of Lesson 9: **Advanced Functions**. After that, we'll build a larger project by refactoring the shopping system into reusable functions, just like a real application.
