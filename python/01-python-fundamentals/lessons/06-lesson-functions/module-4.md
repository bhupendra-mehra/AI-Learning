# Lesson 9 – Module 4: Final Project

## Project: Shopping System v2 (Functions)

### Objective

Refactor a shopping program using functions.

Until now, you've written everything in one file.

Now you'll organize it into reusable functions.

---

# Requirements

Create the following functions.

## 1. `login()`

Ask for:

* Username
* Password

Valid credentials:

```text
Username : admin
Password : 1234
```

Return:

```python
True
```

if login succeeds.

Otherwise

```python
False
```

---

## 2. `calculate_discount(cart_value)`

Rules

| Cart Value | Discount |
| ---------- | -------- |
| >=10000    | 20%      |
| >=5000     | 10%      |
| otherwise  | 0%       |

Return only the **discount amount**.

---

## 3. `premium_discount(cart_value, premium_customer)`

If premium customer

Extra discount

```text
5%
```

Otherwise

```text
0
```

Return the premium discount.

---

## 4. `checkout()`

Ask

```text
Cart Value
Premium Customer (yes/no)
```

Call

```python
calculate_discount()
```

Call

```python
premium_discount()
```

Calculate

```text
Final Amount
```

Return it.

---

## 5. `show_summary(total)`

Print

```text
====================
ORDER SUMMARY
====================

Final Amount : xxxx
```

---

# Main Program

```text
Program Starts

↓

login()

↓

Failed?

↓

Exit

↓

Success

↓

checkout()

↓

show_summary()

↓

End
```

---

# Rules

Use:

* Functions
* Parameters
* Return
* if/elif/else
* Input
* Variables

Don't use:

* Lists
* Dictionaries
* Classes

We'll learn those next.

---

# Expected Structure

Something similar to:

```python
def login():
    ...

def calculate_discount():
    ...

def premium_discount():
    ...

def checkout():
    ...

def show_summary():
    ...

# Main Program
```

---

# Challenge (Optional ⭐)

If login fails,

Ask

```text
Retry Login? (yes/no)
```

If

```text
yes
```

Try again.

Otherwise exit.

> **Don't worry if you can't do this yet.** It combines loops and functions, so it's slightly harder.

---

# What You'll Practice

By completing this project, you'll naturally use:

* ✅ Functions
* ✅ Parameters
* ✅ Return values
* ✅ Boolean values
* ✅ Conditions
* ✅ Loops
* ✅ Variables
* ✅ Code organization

---

## Where You'll Use This in AI Agent Development

This project mirrors how AI systems are structured.

Instead of writing one huge script:

```python
# 500 lines
```

AI applications are built from small reusable functions:

```python
authenticate_user()

load_documents()

search_vector_db()

generate_response()

save_chat_history()
```

The architecture is the same—you've just replaced shopping logic with AI logic.

---

### ⏱️ Estimated Time

**20–30 minutes**

Take your time and build it yourself. Try not to look back at previous solutions. Once you share your code, I'll review it like a senior developer, and if it's solid, we'll officially mark **Lesson 9 as completed** and move on to **Lesson 10 – Collections**.
