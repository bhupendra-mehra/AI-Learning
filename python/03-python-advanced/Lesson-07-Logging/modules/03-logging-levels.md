# Module 3 – Logging Levels

Python provides several standard logging levels.

| Level      | Purpose                                           |
| ---------- | ------------------------------------------------- |
| `DEBUG`    | Detailed information for debugging                |
| `INFO`     | Normal application events                         |
| `WARNING`  | Something unexpected but application can continue |
| `ERROR`    | An operation failed                               |
| `CRITICAL` | Serious failure                                   |

Example:

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug information")
logging.info("Application started")
logging.warning("Low disk space")
logging.error("Payment failed")
logging.critical("Database unavailable")
```

Output will contain all five levels because we configured:

```python
level=logging.DEBUG
```

---

## Logging Level Hierarchy

Think of the levels like this:

```text
DEBUG
  ↓
INFO
  ↓
WARNING
  ↓
ERROR
  ↓
CRITICAL
```

If you configure:

```python
logging.basicConfig(level=logging.WARNING)
```

you won't see:

```text
DEBUG
INFO
```

but you'll see:

```text
WARNING
ERROR
CRITICAL
```

---

