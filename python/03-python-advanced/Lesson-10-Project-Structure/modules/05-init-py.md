# Module 5 – `__init__.py`

You will frequently see:

```text
__init__.py
```

inside Python packages.

For example:

```text
app/
├── __init__.py
└── models/
    ├── __init__.py
    └── order.py
```

Historically, `__init__.py` was required for Python to recognize a directory as a regular package.

Modern Python also supports namespace packages without it, but including `__init__.py` remains common and useful for explicit package structure.

It can be empty:

```python
# app/models/__init__.py
```

Or it can expose selected objects:

```python
from .order import Order
```

Then you may be able to write:

```python
from app.models import Order
```

instead of:

```python
from app.models.order import Order
```

---

