# Module 11 – Practical Example with `mypy`

Create:

```text
type_check.py
```

```python
def calculate_total(
    price: float,
    quantity: int
) -> float:

    return price * quantity


total = calculate_total(
    1000.0,
    3
)

print(total)
```

This is valid.

Now intentionally introduce an error:

```python
total = calculate_total(
    "1000",
    3
)
```

A static type checker can flag:

```text
Expected float
Got str
```

The important concept is:

```text
Python
  ↓
runs code

mypy
  ↓
checks type consistency
```

They serve different purposes.

---

