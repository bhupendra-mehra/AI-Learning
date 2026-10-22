# Module 10 – Practical Example

Let's create a small order-processing system.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def process_order(order_id, amount):

    logger.info(
        "Processing order %s",
        order_id
    )

    if amount <= 0:
        logger.warning(
            "Invalid amount for order %s: %s",
            order_id,
            amount
        )
        return False

    logger.info(
        "Order %s processed successfully",
        order_id
    )

    return True


process_order("ORD12345", 25999)
process_order("ORD12346", 0)
```

You'll get messages similar to:

```text
INFO - Processing order ORD12345
INFO - Order ORD12345 processed successfully
INFO - Processing order ORD12346
WARNING - Invalid amount for order ORD12346: 0
```

---

