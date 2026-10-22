# Module 1 – What Is Logging?

Logging means recording information about what your application is doing.

Instead of:

```python
print("Order processed")
```

you can use:

```python
import logging

logging.info("Order processed")
```

The difference is that logging gives you:

* Severity levels
* Timestamps
* Structured messages
* File output
* Exception details
* Configuration
* Production-friendly debugging

For example:

```text
2026-08-23 22:00:15 - INFO - Order ORD12345 processed
```

---

