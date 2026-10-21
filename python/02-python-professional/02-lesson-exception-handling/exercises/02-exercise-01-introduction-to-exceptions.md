# Answers Review

## Q1

```python
print(10 / 0)
```

Your Answer:

```text
ZeroDivisionError
```

✅ Correct

Reason:

Division by zero is mathematically impossible, so Python raises:

```text
ZeroDivisionError: division by zero
```

---

## Q2

```python
numbers = [1,2,3]

print(numbers[10])
```

Your Answer:

```text
KeyError
```

❌ Incorrect

Correct Answer:

```text
IndexError
```

### Why?

Lists use **indexes**.

```
Index
0 → 1
1 → 2
2 → 3
```

There is no index `10`.

Hence,

```text
IndexError: list index out of range
```

---

### Remember this trick

**List → Index → IndexError**

---

## Q3

```python
age = int("hello")
```

Your Answer:

```text
ValueError
```

✅ Correct

Reason:

`int()` expects something like

```
10
20
35
```

But

```
hello
```

cannot be converted to an integer.

---

## Q4

```python
student = {
    "name":"John"
}

print(student["age"])
```

Your Answer:

```text
KeyError
```

✅ Correct

Reason:

Dictionary doesn't contain the key

```
age
```

---

### Easy way to remember

Dictionary

```
Key → Value
```

Wrong Key

↓

```
KeyError
```

---

## Q5

```python
print(10 + "20")
```

Your Answer

```
TypeError
```

✅ Correct

Reason:

```
int + str
```

Different data types.

Python doesn't know how to add them.

---

# Score

| Question | Result |
| -------- | ------ |
| Q1       | ✅      |
| Q2       | ❌      |
| Q3       | ✅      |
| Q4       | ✅      |
| Q5       | ✅      |

**Score: 4/5 (80%)**

Excellent. Only one small confusion between **IndexError** and **KeyError**.

---

# Quick Memory Trick

| Data Structure | Wrong Access | Exception      |
| -------------- | ------------ | -------------- |
| List           | Wrong Index  | **IndexError** |
| Tuple          | Wrong Index  | **IndexError** |
| Dictionary     | Wrong Key    | **KeyError**   |
| String         | Wrong Index  | **IndexError** |

### Visual Memory

```
List
-----
0
1
2
3

Wrong Number
↓

IndexError
```

```
Dictionary
-----------
"name"
"age"
"city"

Wrong Key
↓

KeyError
```

This distinction is a very common interview question.

---

# Interview Tip ⭐

If an interviewer asks:

> **Why doesn't a dictionary throw IndexError?**

A good answer is:

> "Because dictionaries are not index-based collections. They are key-based mappings. Accessing a missing key raises `KeyError`, while accessing an invalid position in an index-based collection like a list raises `IndexError`."

That answer demonstrates a deeper understanding than simply naming the exception.

---

## Module 1 Status

```
Lesson 12
│
├── ✅ Module 1 (Completed)
├── ▶ Module 2 (try & except)
├── ⏳ Module 3 (else & finally)
├── ⏳ Module 4 (raise)
├── ⏳ Module 5 (Custom Exceptions)
├── ⏳ Module 6 (Best Practices)
└── ⏳ ATM Banking Project
```

You have a solid understanding of the different exception types now.

**Next**, we'll move to **Module 2 – `try` & `except`**, where you'll learn how to catch and handle these exceptions so your programs don't crash. This module includes plenty of hands-on coding because exception handling is best learned through practice.
