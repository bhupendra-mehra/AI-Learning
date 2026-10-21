# Exercise 1

```python
for i in range(5):
    if i == 2:
        break
    print(i)
```

Your answer:

```text
1
```

### ❌ Incorrect

Let's trace it.

| i | Condition    | Printed |
| - | ------------ | ------- |
| 0 | False        | 0       |
| 1 | False        | 1       |
| 2 | True → break | Stop    |

Output:

```text
0
1
```

The important thing is that `break` happens **before** `print()`.

---

# Exercise 2

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

Your answer:

```text
1
3
4
5
```

### ❌ Incorrect

Remember:

```python
range(5)
```

produces:

```text
0
1
2
3
4
```

When `i == 2`, `continue` skips only that iteration.

Output:

```text
0
1
3
4
```

You made the same observation mistake as Exercise 1—you forgot that `range(5)` starts at `0`.

---

# Exercise 3

```python
for i in range(1,11):
    if i == 5:
        continue
    print(i)
```

### ✅ Perfect

Output:

```text
1
2
3
4
6
7
8
9
10
```

---

# Exercise 4

```python
for i in range(1,11):
    if i == 7:
        break
    print(i)
```

### ✅ Perfect

Output:

```text
1
2
3
4
5
6
```

---

# Exercise 5

```python
option = 0

while option != 3:
    print("========= MENU =========")
    print("1. Browse Products")
    print("2. Checkout")
    print("3. Exit")

    option = int(input("Select menu option : "))

    if option == 3:
        break
    elif option == 1:
        print("Browse Products")
    else:
        print("Checkout")
```

## ⭐ Good implementation

But there is **one logical bug**.

Requirement:

> Show **Invalid Choice** for anything other than `1`, `2`, or `3`.

Suppose user enters:

```text
7
```

Your program prints:

```text
Checkout
```

which isn't correct.

A better version would be:

```python
if option == 3:
    break
elif option == 1:
    print("Browse Products")
elif option == 2:
    print("Checkout")
else:
    print("Invalid Choice")
```

Now every input is handled correctly.

---

# Overall Score

| Exercise | Result                      |
| -------- | --------------------------- |
| 1        | ❌                           |
| 2        | ❌                           |
| 3        | ✅                           |
| 4        | ✅                           |
| 5        | ✅ (small logic improvement) |

**Overall:** **8.8/10**

---

# Why did you make mistakes in 1 & 2?

I don't think you misunderstood `break` or `continue`.

I think you answered from memory instead of mentally executing the code.

For every loop question, I want you to follow this habit:

```text
Iteration 1

↓

What's i?

↓

Condition?

↓

Print?

↓

Next Iteration
```

It takes 10 seconds and catches these mistakes.

---

# Senior Developer Observation

Here's something I noticed across the last few modules.

### Your strengths

* ✅ Writing code
* ✅ Translating requirements into logic
* ✅ Input validation
* ✅ Choosing `for` vs `while`
* ✅ Naming variables

### The area to improve

You're occasionally rushing through **output prediction** questions.

That's normal, but these questions train you to mentally execute code, which becomes very important later for debugging.

---

# 🎉 Lesson 8 Completed

Congratulations!

You've completed one of the core programming topics.

## Skills Unlocked

* ✅ `for`
* ✅ `range()`
* ✅ String iteration
* ✅ Nested loops
* ✅ `while`
* ✅ Infinite loops
* ✅ `break`
* ✅ `continue`
* ✅ `pass`

At this point, you can already write many console-based programs with loops and conditions.

---

# Roadmap Update (v2.2)

* ✅ **Lesson 8 – Loops: Completed**
* ⏭️ **Next:** **Lesson 9 – Functions**

---

## My Plan for Lesson 9

Unlike loops, **Functions** are a foundational concept that will be used in almost every AI project we build.

However, I still think we can keep it efficient.

Instead of spending days on it, we'll structure it as:

* Module 1 – Why Functions? + Basic Functions
* Module 2 – Parameters & Return Values
* Module 3 – Variable Scope
* Module 4 – Advanced Parameters (`*args`, `**kwargs`, defaults, keyword arguments)
* Module 5 – Mini Project

This is one of the few topics where I recommend slowing down a bit because almost every AI SDK (OpenAI, LangChain, FastAPI, MCP servers, etc.) revolves around defining and calling functions. A solid understanding here will save you time throughout the rest of the course.
