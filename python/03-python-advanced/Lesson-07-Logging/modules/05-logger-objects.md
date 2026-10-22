# Module 5 – Logger Objects

For production applications, don't normally use only:

```python
logging.info(...)
```

Instead, create a logger:

```python
import logging

logger = logging.getLogger(__name__)

logger.info("Application started")
```

Why?

`__name__` identifies the current Python module.

For example, if your file is:

```text
order_service.py
```

the logger can identify messages as coming from that module.

This becomes extremely useful in larger applications.

---

