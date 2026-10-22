# Lesson 4 – Regular Expressions

## Module 9: Validation

Now we'll move from **extracting data** to **validating data**.

Extraction asks:

> "Can I find this value?"

Validation asks:

> "Does this value follow the required format?"

---

## 1. `re.match()` vs `re.fullmatch()`

### `re.match()`

Checks from the **beginning** of the string.

```python
import re

text = "ORD12345"

result = re.match(r"ORD\d+", text)

if result:
    print("Valid")
```

Output:

```text
Valid
```

But `match()` doesn't necessarily guarantee that the **entire string** follows the pattern.

---

### `re.fullmatch()`

Checks the **entire string**.

```python
import re

text = "ORD12345"

result = re.fullmatch(r"ORD\d+", text)

if result:
    print("Valid Order")
else:
    print("Invalid Order")
```

This is generally better when you're validating user input.

---

# 2. Validate Order Number

Suppose our order format must be:

```text
ORD + one or more digits
```

Examples:

```text
ORD12345   ✅
ORD999     ✅
ORDABC     ❌
ABC123     ❌
ORD        ❌
```

Code:

```python
import re

orders = [
    "ORD12345",
    "ORD999",
    "ORDABC",
    "ABC123",
    "ORD"
]

for order in orders:
    if re.fullmatch(r"ORD\d+", order):
        print(order, "→ Valid")
    else:
        print(order, "→ Invalid")
```

Expected:

```text
ORD12345 → Valid
ORD999 → Valid
ORDABC → Invalid
ABC123 → Invalid
ORD → Invalid
```

---

# 3. Validate Phone Number

Our required format is:

```text
+91-9876543210
```

Pattern:

```python
r"\+\d{1,3}-\d{10}"
```

Example:

```python
phones = [
    "+91-9876543210",
    "+1-1234567890",
    "9876543210",
    "+91-12345",
    "+91-98765432101"
]

for phone in phones:
    if re.fullmatch(r"\+\d{1,3}-\d{10}", phone):
        print(phone, "→ Valid")
    else:
        print(phone, "→ Invalid")
```

---

# 4. Validate Email

A commonly used basic email pattern is:

```python
r"[\w.-]+@[\w.-]+\.\w+"
```

Example:

```python
emails = [
    "bhupendra@example.com",
    "user123@gmail.com",
    "test.user@company.co.in",
    "invalid-email",
    "user@",
]

for email in emails:
    if re.fullmatch(r"[\w.-]+@[\w.-]+\.\w+", email):
        print(email, "→ Valid")
    else:
        print(email, "→ Invalid")
```

Expected:

```text
bhupendra@example.com → Valid
user123@gmail.com → Valid
test.user@company.co.in → Valid
invalid-email → Invalid
user@ → Invalid
```

Remember: this checks the **format**, not whether the mailbox actually exists.

---

# 5. `^` and `$`

You'll often see these in Regex.

```text
^   → beginning
$   → end
```

For example:

```python
r"^ORD\d+$"
```

means:

```text
^       Start
ORD     Must start with ORD
\d+     One or more digits
$       Must end there
```

So:

```text
ORD12345     ✅
ORD999       ✅
ABCORD123    ❌
ORD123ABC    ❌
```

For complete validation, `re.fullmatch()` is often clearer, but you should understand `^` and `$` because you'll see them frequently in real Python code.

---

# Module 7: Search & Replace

Now let's learn another important Regex operation.

## `re.sub()`

Syntax:

```python
re.sub(pattern, replacement, text)
```

Example:

```python
import re

text = "My phone is 9876543210"

result = re.sub(r"\d", "X", text)

print(result)
```

Output:

```text
My phone is XXXXXXXXXX
```

We replaced every digit with `X`.

---

## Remove Special Characters

```python
text = "Hello!!! How are you???"

result = re.sub(r"[!?]", "", text)

print(result)
```

Output:

```text
Hello How are you
```

---

## Remove Extra Spaces

```python
text = "Hello     Bhupendra    How   are   you?"

result = re.sub(r"\s+", " ", text)

print(result)
```

Output:

```text
Hello Bhupendra How are you?
```

This is particularly useful for **text preprocessing before sending data to an AI/LLM**.

---

# Module 8 – Mini Project

Now combine everything you've learned.

Given:

```python
import re

text = """
Customer: Bhupendra Mehra
Email: bhupendra@example.com
Phone: +91-9876543210
Order: ORD12345
Amount: ₹25999
"""
```

Build a program that:

### Step 1

Extracts:

```text
Customer
Email
Phone
Order
Amount
```

### Step 2

Validates:

* Email
* Phone
* Order

### Step 3

Cleans the amount so that:

```text
₹25999
```

becomes:

```text
25999
```

### Step 4

Prints:

```text
========== CUSTOMER ORDER ==========

Customer : Bhupendra Mehra
Email    : bhupendra@example.com
Phone    : +91-9876543210
Order    : ORD12345
Amount   : 25999

Email    : Valid
Phone    : Valid
Order    : Valid
```

### Concepts you should use

```text
re.search()
re.fullmatch()
re.sub()

\d
\w
\s
+
*
{n}
()
[]
^
$
```

Try building this yourself first.

Once you complete it, **Lesson 4 – Regular Expressions will be finished**, and we'll move to:

**Lesson 5 – Collections Module**

* `Counter`
* `defaultdict`
* `deque`
* `namedtuple`
* `ChainMap`
