# Module 1 – Why Project Structure Matters

When learning Python, you may have everything in one file:

```text
app.py
```

For example:

```python
class Product:
    ...


def calculate_total():
    ...


def process_order():
    ...


def send_email():
    ...


# application logic
```

This is fine for small exercises.

But as the application grows, one file becomes difficult to:

* Understand
* Test
* Maintain
* Debug
* Reuse
* Extend

A production application separates responsibilities.

For example:

```text
Application
│
├── Configuration
├── Business Logic
├── Database
├── API
├── Utilities
└── Entry Point
```

---

