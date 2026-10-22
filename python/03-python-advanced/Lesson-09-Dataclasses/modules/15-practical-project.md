# Module 15 – Practical Project

Let's combine the concepts into an **Order Dataclass**.

Requirements:

```text
Order
├── order_id: str
├── customer: str
├── amount: float
├── status: str = "pending"
└── tags: list[str] = []
```

Use `default_factory` for `tags`.

Add a method:

```text
apply_discount()
```

that returns the discounted amount.

Also use `__post_init__()` to remove whitespace from the customer name.

---

## Complete Solution

```python
from dataclasses import dataclass, field


@dataclass
class Order:

    order_id: str
    customer: str
    amount: float
    status: str = "pending"
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        self.customer = self.customer.strip()

    def apply_discount(self, percentage: float) -> float:
        return self.amount - (
            self.amount * percentage / 100
        )


order = Order(
    order_id="ORD1001",
    customer="  Bhupendra Mehra  ",
    amount=25000.0
)


print(order)

print("Customer:", order.customer)
print("Status:", order.status)
print("Tags:", order.tags)

print(
    "After 10% discount:",
    order.apply_discount(10)
)
```

Output:

```text
Order(
    order_id='ORD1001',
    customer='Bhupendra Mehra',
    amount=25000.0,
    status='pending',
    tags=[]
)

Customer: Bhupendra Mehra
Status: pending
Tags: []

After 10% discount: 22500.0
```

---

