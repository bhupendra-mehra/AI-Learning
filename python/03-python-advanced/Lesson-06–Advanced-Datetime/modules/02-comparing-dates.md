# Module 2 – Comparing Dates

`datetime` objects can be compared directly.

```python
from datetime import datetime

date1 = datetime(2026, 8, 20)
date2 = datetime(2026, 8, 22)

print(date1 < date2)
print(date1 > date2)
print(date1 == date2)
```

Output:

```text
True
False
False
```

This is useful for:

* Order dates
* Expiry dates
* Appointment dates
* Token expiration
* Scheduled jobs
* API timestamps

---

