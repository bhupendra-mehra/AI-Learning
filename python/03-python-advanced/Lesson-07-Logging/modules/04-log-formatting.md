# Module 4 – Log Formatting

The default output isn't very useful for production.

We can define our own format:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.warning("Low inventory")
```

Example:

```text
2026-08-23 22:05:10,123 - INFO - Application started
2026-08-23 22:05:10,124 - WARNING - Low inventory
```

### Important format values

| Format          | Meaning     |
| --------------- | ----------- |
| `%(asctime)s`   | Date/time   |
| `%(levelname)s` | Log level   |
| `%(message)s`   | Log message |
| `%(name)s`      | Logger name |
| `%(filename)s`  | File name   |
| `%(lineno)d`    | Line number |

For example:

```python
format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
```

---

