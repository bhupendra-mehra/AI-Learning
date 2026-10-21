# Review
---

# Exercise 1

```python
fruits = ['Apple','Banana','Cherry','Papaya','Watermelon']

print(fruits)
```

### ✅ Correct

Output

```text
['Apple', 'Banana', 'Cherry', 'Papaya', 'Watermelon']
```

---

# Exercise 2

```python
print(fruits[0])
print(fruits[-1])
```

### ✅ Correct

Output

```text
Apple
Watermelon
```

You correctly used **negative indexing**.

---

# Exercise 3

```python
fruits[2] = "Mango"

print(fruits)
```

### ✅ Correct

Result

```text
['Apple', 'Banana', 'Mango', 'Papaya', 'Watermelon']
```

---

# Exercise 4

```python
fruits.append("Orange")

fruits.remove("Apple")

print(fruits)
```

### ✅ Correct

Final List

```text
['Banana', 'Mango', 'Papaya', 'Watermelon', 'Orange']
```

Perfect use of `append()` and `remove()`.

---

# Exercise 5

```python
numbers = [1,2,3,4,5]

for number in numbers:
    print(number)
```

### ✅ Perfect

---

# Overall Score

| Exercise | Result |
| -------- | ------ |
| 1        | ✅      |
| 2        | ✅      |
| 3        | ✅      |
| 4        | ✅      |
| 5        | ✅      |

# ⭐ Score: 10/10

---

# Senior Developer Review

I noticed another improvement.

Earlier you used to write:

```python
for i in numbers:
```

Now you're naturally writing:

```python
for number in numbers:
```

This is much more readable.

Professional Python code favors meaningful variable names.

---

## One New Best Practice

When creating collections, add a space after commas.

Instead of:

```python
fruits = ['Apple','Banana','Cherry']
```

Prefer:

```python
fruits = ['Apple', 'Banana', 'Cherry']
```

or

```python
numbers = [1, 2, 3, 4, 5]
```

This follows **PEP 8**, Python's official style guide.

It's a small formatting habit, but it's worth adopting now.

---

# Lesson 10 Progress

```
✅ Module 1 – Lists
⏳ Module 2 – Tuples & Sets
⏳ Module 3 – Dictionaries
⏳ Module 4 – Inventory Management Project
```

---

## One Small Improvement to the Course

I've noticed that you're consistently finishing modules with very few mistakes. Starting from the next module, I'll spend even less time reviewing code unless there's something important to discuss.

The new pattern will be:

* ✅ Quick review (1–2 minutes)
* ✅ Mention any best practice
* ✅ Move to the next module

This will help us maintain the **20–30 minute per module** target while still giving you meaningful feedback.

We'll now continue with **Module 2 – Tuples & Sets** in Fast Track mode.
