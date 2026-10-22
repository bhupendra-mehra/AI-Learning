# Module 11 – Utilities

Utilities contain small reusable functions that don't belong to a particular business domain.

For example:

```text
app/
└── utils/
    └── helpers.py
```

`helpers.py`:

```python
def format_currency(amount: float) -> str:
    return f"₹{amount:,.2f}"
```

Then:

```python
from app.utils.helpers import format_currency

print(format_currency(25999))
```

Output:

```text
₹25,999.00
```

Don't put every function into `utils`.

A function should go into a utility module only when it is genuinely generic and reusable.

---

