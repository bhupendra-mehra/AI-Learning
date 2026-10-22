# Module 6 – Absolute vs Relative Imports

Suppose we have:

```text
app/
├── models/
│   └── order.py
└── services/
    └── order_service.py
```

An absolute import:

```python
from app.models.order import Order
```

A relative import from inside the `services` package:

```python
from ..models.order import Order
```

For larger applications, absolute imports are often easier to understand:

```python
from app.models.order import Order
```

---

