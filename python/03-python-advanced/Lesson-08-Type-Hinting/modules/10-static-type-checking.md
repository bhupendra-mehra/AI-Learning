# Module 10 – Static Type Checking

Python itself generally doesn't enforce type hints at runtime.

Static type checkers analyze your code **before execution**.

A popular tool is:

```text
mypy
```

For example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Then:

```python
result = add("10", "20")
```

Python may run this code depending on what the function does, but a static type checker can identify that you're passing strings where integers were expected.

---

## Install mypy

```bash
pip install mypy
```

Then:

```bash
mypy app.py
```

It analyzes the code and reports type-related problems.

---

