# Module 21 – Final Part 3 Project

Now let's combine what you've learned across Part 3.

We'll create a small:

**Order Processing Application**

It will use:

* Type hints
* Dataclasses
* Logging
* `defaultdict`
* `datetime`
* `timedelta`
* Modules
* Packages
* Configuration
* Services

### Project

```text
order-processing/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── order.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── order_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── tests/
│   └── test_orders.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

# `models/order.py`

```python
from dataclasses import dataclass, field
from datetime import datetime
from zoneinfo import ZoneInfo


@dataclass
class Order:

    order_id: str
    customer: str
    amount: float
    category: str
    quantity: int = 1
    status: str = "pending"
    tags: list[str] = field(default_factory=list)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(
            ZoneInfo("Asia/Kolkata")
        )
    )

    def __post_init__(self) -> None:
        self.customer = self.customer.strip()
        self.category = self.category.strip()

    def total_price(self) -> float:
        return self.amount * self.quantity
```

Notice how several previous lessons come together:

```text
Lesson 06 → datetime + ZoneInfo
Lesson 08 → type hints
Lesson 09 → dataclass + field + __post_init__
```

---

# `services/order_service.py`

```python
import logging
from collections import defaultdict

from app.models.order import Order


logger = logging.getLogger(__name__)


def process_order(order: Order) -> bool:

    try:

        logger.info(
            "Processing order %s",
            order.order_id
        )

        if order.amount <= 0:
            logger.warning(
                "Invalid amount for order %s",
                order.order_id
            )

            return False

        order.status = "processed"

        logger.info(
            "Order %s processed successfully",
            order.order_id
        )

        return True

    except Exception:
        logger.exception(
            "Failed to process order %s",
            order.order_id
        )

        return False


def group_by_category(
    orders: list[Order]
) -> dict[str, list[Order]]:

    grouped = defaultdict(list)

    for order in orders:
        grouped[order.category].append(order)

    return dict(grouped)
```

Here we combine:

```text
Lesson 05 → defaultdict
Lesson 07 → logging
Lesson 08 → type hints
Lesson 09 → dataclass
```

---

# `config/settings.py`

```python
import os


class Settings:

    app_name: str = os.getenv(
        "APP_NAME",
        "Order Processing"
    )

    debug: bool = os.getenv(
        "DEBUG",
        "false"
    ).lower() == "true"
```

---

# `utils/helpers.py`

```python
def format_currency(amount: float) -> str:
    return f"₹{amount:,.2f}"
```

---

# `main.py`

```python
import logging

from app.models.order import Order
from app.services.order_service import (
    process_order,
    group_by_category
)
from app.utils.helpers import format_currency


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main() -> None:

    orders: list[Order] = [

        Order(
            order_id="ORD1001",
            customer="Bhupendra Mehra",
            amount=60000.0,
            category="Electronics",
            quantity=2
        ),

        Order(
            order_id="ORD1002",
            customer="Rahul",
            amount=1500.0,
            category="Electronics",
            quantity=1
        ),

        Order(
            order_id="ORD1003",
            customer="Amit",
            amount=2500.0,
            category="Fashion",
            quantity=2
        )
    ]


    for order in orders:
        process_order(order)


    print("\nOrders:")

    for order in orders:

        print(
            order.order_id,
            order.customer,
            format_currency(order.total_price()),
            order.status
        )


    grouped = group_by_category(orders)

    print("\nGrouped by category:")

    for category, category_orders in grouped.items():

        print(
            category,
            "→",
            [order.order_id for order in category_orders]
        )


if __name__ == "__main__":
    main()
```

---

