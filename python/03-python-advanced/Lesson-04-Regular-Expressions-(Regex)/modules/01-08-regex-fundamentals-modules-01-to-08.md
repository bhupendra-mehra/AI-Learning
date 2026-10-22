# Part 3 – Advanced Python

## Lesson 04 – Regular Expressions (Regex)

We’ll start directly from **Lesson 4**. Since you already completed the earlier lessons, I’ll keep this practical and focused on concepts you'll actually use in **AI, APIs, data processing, and backend development**.

### What you'll learn

1. What Regex is
2. Pattern matching
3. Character classes
4. Quantifiers
5. Groups
6. Validation
7. Search & replace
8. Practical mini-project

---

## Module 1 — What is Regular Expression?

A **Regular Expression (Regex)** is a pattern used to find, extract, validate, or replace text.

For example, suppose you have:

```python
text = "My email is bhupendra@example.com"
```

You could use Regex to find the email address automatically.

```python
import re

text = "My email is bhupendra@example.com"

result = re.search(r"\S+@\S+\.\S+", text)

print(result.group())
```

Output:

```text
bhupendra@example.com
```

### Why Regex matters for AI

Regex is still useful even when working with AI/LLMs.

For example:

* Extract an email from user input
* Validate phone numbers
* Find URLs
* Extract order numbers
* Clean text before sending it to an LLM
* Detect specific patterns in logs
* Extract structured information from unstructured text

---

# Module 2 — The `re` Module

Python provides Regex through the built-in `re` module.

```python
import re
```

The most important functions are:

| Function        | Purpose                 |
| --------------- | ----------------------- |
| `re.search()`   | Find a pattern anywhere |
| `re.match()`    | Match from beginning    |
| `re.findall()`  | Find all matches        |
| `re.finditer()` | Iterate through matches |
| `re.sub()`      | Replace matches         |
| `re.split()`    | Split using a pattern   |

### `re.search()`

```python
import re

text = "My order number is ORD12345"

result = re.search(r"ORD\d+", text)

if result:
    print(result.group())
```

Output:

```text
ORD12345
```

---

# Module 3 — Character Classes

Character classes define **what characters can match**.

### `\d` — digit

```python
\d
```

Matches:

```text
0 1 2 3 4 5 6 7 8 9
```

Example:

```python
text = "Order 12345"

print(re.findall(r"\d", text))
```

Output:

```text
['1', '2', '3', '4', '5']
```

---

### `\w` — word character

```python
\w
```

Matches letters, numbers and underscore.

```python
text = "hello_123"

print(re.findall(r"\w", text))
```

---

### `\s` — whitespace

```python
\s
```

Matches spaces, tabs and newlines.

---

### Opposite versions

Add uppercase:

```text
\d  → digit
\D  → non-digit

\w  → word character
\W  → non-word character

\s  → whitespace
\S  → non-whitespace
```

These are extremely common in Regex.

---

# Module 4 — Quantifiers

Quantifiers tell Regex **how many times something should occur**.

### `+` — one or more

```python
\d+
```

Matches:

```text
123
45678
99
```

Example:

```python
text = "There are 25 products and 100 orders"

print(re.findall(r"\d+", text))
```

Output:

```text
['25', '100']
```

---

### `*` — zero or more

```python
a*
```

Matches zero or more `a` characters.

---

### `?` — zero or one

```python
colou?r
```

Matches both:

```text
color
colour
```

---

### `{n}` — exactly n

```python
\d{4}
```

Matches exactly four digits.

Example:

```python
text = "2026 123 45678"

print(re.findall(r"\d{4}", text))
```

Output:

```text
['2026', '4567']
```

Notice that `45678` contains a four-digit sequence.

---

### `{n,m}` — between n and m

```python
\d{2,4}
```

Matches between 2 and 4 digits.

---

# Module 5 — Groups

Groups allow you to capture parts of a pattern.

Example:

```python
text = "Date: 11-08-2026"

result = re.search(r"(\d{2})-(\d{2})-(\d{4})", text)

print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))
```

Output:

```text
11-08-2026
11
08
2026
```

So:

```text
group()   → complete match
group(1)  → first group
group(2)  → second group
group(3)  → third group
```

This becomes very useful when extracting structured information from text.

---

# Module 6 — Validation

Regex can validate whether input follows a particular format.

For example, a simple email validation:

```python
import re

email = "user@example.com"

pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

if re.fullmatch(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
```

Output:

```text
Valid email
```

### Important

Regex validation is good for checking **format**, but it doesn't prove that an email address actually exists.

---

# Module 7 — Search and Replace

This is another very useful feature.

```python
import re

text = "Python is difficult. Python is powerful."

new_text = re.sub(r"Python", "AI Python", text)

print(new_text)
```

Output:

```text
AI Python is difficult. AI Python is powerful.
```

### Cleaning text

This is particularly useful before processing text with an LLM.

```python
text = "Hello!!!   How are you???"

cleaned = re.sub(r"[!?]+", "", text)
cleaned = re.sub(r"\s+", " ", cleaned)

print(cleaned)
```

Output:

```text
Hello How are you
```

---

# Module 8 — Practical Exercise

Create a Python program that extracts information from this text:

```python
text = """
Customer: Bhupendra Mehra
Email: bhupendra@example.com
Phone: +91-9876543210
Order: ORD12345
Amount: ₹25999
"""
```

Your program should extract:

```text
Customer: Bhupendra Mehra
Email: bhupendra@example.com
Phone: +91-9876543210
Order: ORD12345
Amount: 25999
```

### Hints

Email:

```python
r"[\w.-]+@[\w.-]+\.\w+"
```

Order:

```python
r"ORD\d+"
```

Amount:

```python
r"\d+"
```

For the phone number, try creating the Regex yourself.

---

## Lesson 4 — What you need to remember

The most important Regex concepts for your AI journey are:

```text
\d       digit
\w       word character
\s       whitespace

+        one or more
*        zero or more
?        zero or one
{n}      exactly n
{n,m}    n to m

()       group
^        beginning
$        end

search() find pattern
findall() find all
sub()    replace
```

**Don't try to memorize every Regex syntax.** The goal is to understand the patterns and become comfortable reading/writing them.

### Next

Complete the **Customer Information extraction exercise** above. Send me your code and output, and we'll quickly check it before moving to **Module 9 / Lesson 4 validation + mini-project**, then **Lesson 5 – Collections Module**.
