# Module 7 – Logging Exceptions

This is one of the most important parts of logging.

Suppose:

```python
number = 10
result = number / 0
```

This generates:

```text
ZeroDivisionError
```

We can log it:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    number = 10
    result = number / 0

except Exception:
    logging.exception("An error occurred")
```

`logging.exception()` automatically includes the traceback.

Example:

```text
ERROR - An error occurred
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
```

This is much more useful than:

```python
print("Something went wrong")
```

because the traceback tells you **where and why** the error happened.

---

