# Module 8 – `logger.exception()`

If you're using a logger:

```python
import logging

logger = logging.getLogger(__name__)

try:
    result = 10 / 0

except Exception:
    logger.exception("Failed to calculate result")
```

Use `logger.exception()` **inside an exception handler**.

It automatically logs the exception traceback.

---

