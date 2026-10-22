# Module 6 – File Logging

Instead of displaying logs only in the terminal, we can save them to a file.

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.warning("Low inventory")
logging.error("Payment failed")
```

Python creates:

```text
app.log
```

with entries similar to:

```text
2026-08-23 22:10:01,123 - INFO - Application started
2026-08-23 22:10:02,123 - WARNING - Low inventory
2026-08-23 22:10:03,123 - ERROR - Payment failed
```

---

