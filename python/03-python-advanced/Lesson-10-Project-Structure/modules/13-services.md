# Module 13 – Services

Services contain business logic.

For example:

```text
app/
└── services/
    └── order_service.py
```

```python
from app.models.order import Order


def process_order(order: Order) -> bool:

    if order.amount <= 0:
        return False

    order.status = "processed"

    return True
```

Now the responsibilities are separated:

```text
Order
 ↓
models/order.py

Processing logic
 ↓
services/order_service.py
```

This separation becomes extremely important in larger applications.

---

