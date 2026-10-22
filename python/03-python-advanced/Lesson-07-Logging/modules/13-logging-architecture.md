# Module 13 – Logging Architecture

A production application may look conceptually like:

```text
Application
    |
    +---- Module A ----+
    |                  |
    +---- Module B ----+---- Logger
    |                  |
    +---- Module C ----+
                           |
                    +------+------+
                    |             |
                 Console        File
                    |             |
                  logs          app.log
```

Later, when you work with APIs and AI applications, these logs may also be sent to centralized logging systems.

---

# Final Mini Project – Order Processing Logger

Now combine everything.

Create:

```text
order_logger.py
```

The application should process:

```python
orders = [
    ("ORD1001", 2500),
    ("ORD1002", 0),
    ("ORD1003", 1500),
]
```

Create:

```python
process_order(order_id, amount)
```

### Requirements

For every order:

1. Log that processing started.
2. If amount is greater than `0`, log successful processing.
3. If amount is `0` or negative, log a warning.
4. Write logs to:

```text
orders.log
```

5. Use this format:

```text
timestamp - level - message
```

6. Add exception handling.
7. Use a logger created with:

```python
logger = logging.getLogger(__name__)
```

### Expected type of output

```text
2026-08-23 22:30:01 - INFO - Processing order ORD1001
2026-08-23 22:30:01 - INFO - Order ORD1001 processed successfully
2026-08-23 22:30:01 - INFO - Processing order ORD1002
2026-08-23 22:30:01 - WARNING - Invalid amount for order ORD1002: 0
2026-08-23 22:30:01 - INFO - Processing order ORD1003
2026-08-23 22:30:01 - INFO - Order ORD1003 processed successfully
```

---

# Lesson 07 Summary

You should now understand:

```text
logging
   │
   ├── DEBUG
   ├── INFO
   ├── WARNING
   ├── ERROR
   └── CRITICAL
```

And:

```python
logging.basicConfig()
logging.getLogger()
logger.info()
logger.warning()
logger.error()
logger.exception()
```

Plus:

```text
Console logging
File logging
Log formatting
Exception logging
Production logging practices
```

## Lesson 07 Completion Criteria

* [ ] Understand logging vs `print()`
* [ ] Understand logging levels
* [ ] Configure logging
* [ ] Format log messages
* [ ] Create module-level loggers
* [ ] Write logs to files
* [ ] Log exceptions and tracebacks
* [ ] Log variables/context
* [ ] Follow basic logging best practices
* [ ] Complete the order-processing logger project

**Lesson 07 is designed to be completed in one lesson.** Once you finish the mini-project, we'll move to **Lesson 08 – Type Hinting**.

