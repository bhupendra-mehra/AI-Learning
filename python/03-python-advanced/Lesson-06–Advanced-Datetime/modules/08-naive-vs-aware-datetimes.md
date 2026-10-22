# Module 8 – Naive vs Aware Datetimes

This is an important professional concept.

## Naive Datetime

A naive datetime doesn't contain timezone information.

```python
from datetime import datetime

now = datetime.now()

print(now)
print(now.tzinfo)
```

Output:

```text
2026-08-22 18:30:25.123456
None
```

---

## Timezone-Aware Datetime

```python
from datetime import datetime
from zoneinfo import ZoneInfo

now = datetime.now(
    ZoneInfo("Asia/Kolkata")
)

print(now)
print(now.tzinfo)
```

The datetime now contains timezone information.

For applications involving:

* Users
* Orders
* APIs
* Logs
* Distributed systems
* Scheduled jobs

timezone-aware datetimes are generally safer.

---

