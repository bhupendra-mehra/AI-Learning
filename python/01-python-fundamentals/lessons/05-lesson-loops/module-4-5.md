# Lesson 8 – Module 4 & 5

* ✅ Module 4 – Loop Control Statements
* ✅ Module 5 – Final Project

## Loop Control Statements + Final Project

**Estimated Time:** 30–40 minutes

---

# 1. `break`

`break` immediately exits the loop.

### Syntax

```python
while condition:
    if some_condition:
        break
```

### Example

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

Output

```text
1
2
3
4
```

Once `i` becomes `5`, the loop ends completely.

### Use Cases

* Product found
* User chooses Exit
* API returned expected result
* AI agent found the required document

---

# 2. `continue`

`continue` skips the current iteration and moves to the next one.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output

```text
1
2
4
5
```

Notice:

The loop **doesn't stop**.

It only skips `3`.

---

# 3. `pass`

`pass` does nothing.

It's simply a placeholder.

Example

```python
if True:
    pass
```

or

```python
for i in range(5):
    pass
```

Useful when you're writing the structure of a program but haven't implemented the logic yet.

---

# Difference

| Statement  | Action                 |
| ---------- | ---------------------- |
| `break`    | Exit loop completely   |
| `continue` | Skip current iteration |
| `pass`     | Do nothing             |

---

# Magento Examples

### break

```text
Search Product

↓

Found Product

↓

Stop Searching
```

---

### continue

```text
Loop Products

↓

Out of Stock?

↓

Skip Product

↓

Continue Next Product
```

---

### pass

```python
if feature_enabled:
    pass
```

Feature will be implemented later.

---

# AI Examples

### break

AI searches documents.

Once the answer is found:

```text
Stop searching.
```

---

### continue

Skip corrupted documents.

Continue processing remaining documents.

---

### pass

Placeholder while building a workflow.

---

# Common Mistakes

### Mistake 1

Using `break` instead of `continue`

Remember:

```text
break

↓

Entire loop stops
```

---

```text
continue

↓

Only current iteration skipped
```

---

### Mistake 2

Using `pass` expecting it to skip iterations.

It won't.

It literally does nothing.

---

# Mini Project

## Shopping Menu

Requirements

```
========= MENU =========

1. Browse Products

2. Checkout

3. Exit
```

Keep showing the menu until user selects:

```
3
```

When user chooses:

```
3
```

Use

```python
break
```

to exit.

For invalid options:

```
Invalid Choice
```

Continue showing the menu.

---

# Exercises

## Exercise 1

Predict the output

```python
for i in range(5):

    if i == 2:
        break

    print(i)
```

---

## Exercise 2

Predict the output

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

---

## Exercise 3

Write a loop that prints numbers **1–10** but skips **5**.

---

## Exercise 4

Write a loop that prints numbers **1–10** but stops at **7**.

---

## Exercise 5 (Final Project)

Build the menu system described above.

Requirements:

```
========= MENU =========

1. Browse Products

2. Checkout

3. Exit
```

* Keep showing the menu.
* Exit only when user selects **3**.
* Show **Invalid Choice** for anything else.

Use:

* `while`
* `break`
* `if-elif-else`

---

# Senior Developer Tips

Before writing a loop, ask yourself:

1. **Should it stop early?**
   → Use `break`.

2. **Should it ignore some values?**
   → Use `continue`.

3. **Am I only creating the structure?**
   → Use `pass`.

This simple checklist will help you choose the right statement.

---

# Lesson 8 Summary

Congratulations! 🎉

You've completed everything related to loops.

You now know:

* ✅ `for`
* ✅ `range()`
* ✅ String iteration
* ✅ Nested loops
* ✅ `while`
* ✅ Infinite loops
* ✅ `break`
* ✅ `continue`
* ✅ `pass`

---

# Roadmap Progress

## ✅ Lesson 8 Completed

Next lesson:

## Lesson 9 – Functions

This is the first topic where we'll slow down slightly because **functions are fundamental to writing maintainable Python code and are used extensively in AI applications**. We'll review the structure first, as per our new workflow, before starting the lesson.

---

Complete the five exercises, and then we'll officially close Lesson 8 and move on to the Lesson 9 structure.
