This is actually **very good**. More importantly, I can see you're **thinking like a programmer instead of just copying my solution**, which is exactly the goal of this course.

If I were reviewing this in a code review (similar to a senior developer reviewing your PR), here's my feedback.

---

# Overall Rating

| Category        | Rating      |
| --------------- | ----------- |
| Logic           | ⭐⭐⭐⭐⭐ (5/5) |
| Python Syntax   | ⭐⭐⭐⭐⭐ (5/5) |
| Problem Solving | ⭐⭐⭐⭐⭐ (5/5) |
| Readability     | ⭐⭐⭐⭐☆ (4/5) |
| Best Practices  | ⭐⭐⭐⭐☆ (4/5) |

**Overall: 9/10**

This is definitely **your own implementation**, which is much better than memorizing mine.

---

# Things you did really well

## ✅ 1. Login Validation

I like this.

```python
is_logged_in = False

if username == 'user' and password == '1234':
    is_logged_in = True
```

Many beginners write

```python
if username == 'user':
    if password == '1234':
```

Your approach is cleaner.

Even shorter:

```python
is_logged_in = username == "user" and password == "1234"
```

Both are correct.

---

## ✅ 2. Used `not`

```python
if not is_logged_in:
```

Excellent.

This is exactly why we learned `not`.

---

## ✅ 3. Didn't ask unnecessary questions

You only ask

```python
cart_value
```

after login succeeds.

Real applications work this way.

Imagine Amazon.

If login fails,

they don't ask

> What's your payment method?

Good thinking.

---

## ✅ 4. Nested flow

Your program naturally flows like this

```
Login?

↓

Stock?

↓

Discount?

↓

Place Order?
```

This is how backend systems are usually written.

---

## ✅ 5. Discount Logic

Works perfectly.

```python
if cart_value >=10000:
```

```
20%
```

```python
elif cart_value >=5000:
```

```
10%
```

Correct.

---

# Improvements

---

## 1. You don't actually need `is_in_stock`

Currently

```python
qty = int(input(...))

is_in_stock = False

if qty > 0:
    is_in_stock = True
```

This works.

But you're creating an extra variable.

Instead

```python
qty = int(input("Qty: "))

if qty <= 0:
    print("Out of Stock")
else:
    ...
```

Cleaner.

---

## 2. This condition

```python
elif cart_value >=5000 and cart_value <=9999:
```

Python already knows.

Because the first condition failed.

So

```python
elif cart_value >=5000:
```

is enough.

Example

```
12000

↓

First if already executed

↓

Python never reaches elif
```

Likewise,

```
7000

↓

First if false

↓

Must be below 10000 already

↓

Only check >=5000
```

---

## 3. This condition is unnecessary

```python
if is_logged_in and is_in_stock and cart_value > 0:
```

You're already inside

```
Login successful

↓

Stock available
```

Therefore

```python
is_logged_in == True
```

already.

and

```python
is_in_stock == True
```

already.

So only

```python
total = cart_value - discount
```

is enough.

---

## 4. Better error messages

Current

```python
Either total is 0 or you are minor
```

The user doesn't know which one happened.

Instead

```python
if age < 18:
    print("You must be 18 or older.")

elif total <= 0:
    print("Invalid cart value.")

else:
    print("Order Placed")
```

Much more user-friendly.

---

## 5. Initialize variables

I would initialize

```python
discount = 0
total = 0
```

at the top.

Suppose later someone edits your code.

It avoids accidental "variable referenced before assignment" issues.

---

# How a Senior Developer Might Simplify It

One thing you'll learn as you gain experience is to reduce unnecessary state.

For example:

Instead of

```python
is_logged_in = False

if username == "user" and password == "1234":
    is_logged_in = True
```

you can write

```python
is_logged_in = username == "user" and password == "1234"
```

The expression itself already evaluates to `True` or `False`.

The same idea applies to stock:

```python
is_in_stock = qty > 0
```

This is concise and still very readable.

---

# If This Were an Interview

If you wrote this in a Python interview for an entry-level or junior role, I'd be satisfied because it shows you can:

* Take user input.
* Validate credentials.
* Apply business rules.
* Use nested decision-making.
* Calculate values.
* Structure a complete flow.

Those are the core skills the exercise was meant to test.

---

# One Small Challenge

Can you modify your program so it asks:

```text
Are you a premium customer? (yes/no)
```

If the answer is **yes**, give an **additional 5% discount** after the existing discount is calculated.

For example:

* Cart = ₹12,000
* Regular discount = 20% → ₹2,400
* Premium discount = 5% of the original cart (₹600)
* Final discount = ₹3,000
* Final amount = ₹9,000

This is a realistic extension of your program and will prepare you for the next lessons where we'll start introducing loops and more complex logic.
