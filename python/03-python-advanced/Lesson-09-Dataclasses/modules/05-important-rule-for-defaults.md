# Module 5 – Important Rule for Defaults

Non-default fields must come before default fields.

Correct:

```python
@dataclass
class Product:
    name: str
    price: float
    category: str = "General"
```

Incorrect:

```python
@dataclass
class Product:
    category: str = "General"
    name: str
```

This produces an error because Python cannot have a required field after a field with a default value.

Think:

```text
Required fields
      ↓
Default fields
```

---

