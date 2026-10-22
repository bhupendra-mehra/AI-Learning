# Module 12 – Models

Models represent application data.

For example:

```text
app/
└── models/
    └── order.py
```

Use the dataclass concept from Lesson 09:

```python
from dataclasses import dataclass


@dataclass
class Order:

    order_id: str
    customer: str
    amount: float
    status: str = "pending"

    def total_with_tax(
        self,
        tax: float
    ) -> float:

        return self.amount + tax
```

Now your model has a clear responsibility:

> Represent an order and its related behavior.

---

