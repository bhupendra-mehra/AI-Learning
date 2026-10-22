# Module 18 – `pyproject.toml`

Modern Python projects commonly use:

```text
pyproject.toml
```

for project metadata and tool configuration.

A basic example:

```toml
[project]
name = "order-processing"
version = "0.1.0"
description = "Order processing application"
requires-python = ">=3.11"
dependencies = [
    "python-dotenv"
]
```

This provides standardized project metadata.

As your Python knowledge grows, `pyproject.toml` will become increasingly important.

---

