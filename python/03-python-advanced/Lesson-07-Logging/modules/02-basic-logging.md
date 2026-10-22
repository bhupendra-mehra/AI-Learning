# Module 2 – Basic Logging

Python has a built-in `logging` module.

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Application started")
```

Output:

```text
INFO:root:Application started
```

`basicConfig()` configures the basic logging system.

---

