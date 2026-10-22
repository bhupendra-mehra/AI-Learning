# Module 8 – Environment Variables

Sensitive configuration should generally come from environment variables.

For example:

```text
DATABASE_URL=...
API_KEY=...
DEBUG=false
```

Instead of hardcoding:

```python
API_KEY = "my-secret-key"
```

use:

```python
import os

API_KEY = os.getenv("API_KEY")
```

Now the secret doesn't need to be written directly into your source code.

---

