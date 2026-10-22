# Module 9 – Logging Variables

You can include variables in log messages.

Preferred approach:

```python
import logging

logger = logging.getLogger(__name__)

order_id = "ORD12345"
amount = 25999

logger.info(
    "Order %s processed with amount %s",
    order_id,
    amount
)
```

Output:

```text
Order ORD12345 processed with amount 25999
```

You can also use f-strings:

```python
logger.info(f"Order {order_id} processed")
```

but the logging-style placeholder approach is generally preferred because logging can defer string formatting until the message actually needs to be emitted.

---

