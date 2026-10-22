# Module 13 – Dataclass vs Namedtuple

We learned `namedtuple` in Lesson 05.

### `namedtuple`

```python
from collections import namedtuple

Product = namedtuple(
    "Product",
    ["name", "price"]
)
```

### Dataclass

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
```

For modern application development, dataclasses are generally more flexible.

| Feature             |        `namedtuple` |   `dataclass` |
| ------------------- | ------------------: | ------------: |
| Named fields        |                   ✅ |             ✅ |
| Type hints          |             Limited |             ✅ |
| Default values      |             Limited |             ✅ |
| Mutable             |                   ❌ |  ✅ by default |
| Immutable option    | Naturally immutable | `frozen=True` |
| Methods             |             Limited |             ✅ |
| Field customization |             Limited |             ✅ |
| `__post_init__()`   |                   ❌ |             ✅ |

You don't need to stop using `namedtuple`; just understand when a dataclass is more appropriate.

---

