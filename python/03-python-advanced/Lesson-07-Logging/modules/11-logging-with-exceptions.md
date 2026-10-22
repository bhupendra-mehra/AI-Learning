# Module 11 – Logging With Exceptions

Now make the function handle unexpected errors.

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def calculate_total(price, quantity):

    try:
        total = price * quantity

        logger.info(
            "Calculated total: %s",
            total
        )

        return total

    except Exception:
        logger.exception(
            "Failed to calculate total"
        )

        return None


calculate_total(1000, 3)
calculate_total(1000, "invalid")
```

The second call generates an exception, and the logger records the traceback.

---

