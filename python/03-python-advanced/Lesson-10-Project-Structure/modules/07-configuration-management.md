# Module 7 – Configuration Management

Applications usually have configuration such as:

```text
Database URL
API URL
Application environment
Debug mode
API keys
Timeouts
```

Don't scatter configuration throughout your code.

Avoid:

```python
database_url = "mysql://localhost/mydb"
```

inside multiple files.

Instead, centralize configuration.

Example:

```text
app/
└── config/
    └── settings.py
```

---

