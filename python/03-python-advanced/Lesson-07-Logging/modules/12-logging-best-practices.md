# Module 12 – Logging Best Practices

These are the practices you should remember for professional Python development.

### 1. Don't use `print()` for application logging

Instead of:

```python
print("Payment failed")
```

use:

```python
logger.error("Payment failed")
```

`print()` is fine for quick scripts and learning exercises, but production applications generally use logging.

---

### 2. Use appropriate levels

Don't do:

```python
logger.error("Application started")
```

Use:

```python
logger.info("Application started")
```

And:

```python
logger.error("Payment processing failed")
```

---

### 3. Don't log sensitive information

Never log things such as:

```text
Passwords
API keys
Access tokens
Credit card numbers
Private credentials
```

For example, don't do:

```python
logger.info("API key: %s", api_key)
```

---

### 4. Include useful context

Instead of:

```python
logger.error("Failed")
```

prefer:

```python
logger.error(
    "Payment failed for order %s",
    order_id
)
```

The second message tells you what failed and which order was affected.

---

### 5. Use `logger.exception()` for exceptions

Instead of:

```python
except Exception:
    logger.error("Something went wrong")
```

use:

```python
except Exception:
    logger.exception("Something went wrong")
```

when you want the traceback.

---

