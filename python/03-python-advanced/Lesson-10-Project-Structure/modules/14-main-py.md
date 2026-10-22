# Module 14 – `main.py`

`main.py` is commonly used as an application entry point.

For example:

```python
from app.models.order import Order
from app.services.order_service import process_order


def main() -> None:

    order = Order(
        order_id="ORD1001",
        customer="Bhupendra",
        amount=25000.0
    )

    process_order(order)

    print(order)


if __name__ == "__main__":
    main()
```

The important part is:

```python
if __name__ == "__main__":
    main()
```

It means:

> Run `main()` when this file is executed directly.

But don't automatically run it when another module imports `main.py`.

---

