# Module 10 – Configuration Class

You can centralize configuration into a class.

```python
import os


class Settings:

    app_name: str = os.getenv(
        "APP_NAME",
        "Order Processing"
    )

    debug: bool = os.getenv(
        "DEBUG",
        "false"
    ).lower() == "true"

    api_key: str | None = os.getenv("API_KEY")
```

Then:

```python
from app.config.settings import Settings

settings = Settings()

print(settings.app_name)
print(settings.debug)
```

For larger modern applications, configuration libraries such as Pydantic Settings are also commonly used. You'll encounter this later when working with APIs.

---

