# Module 17 – `.gitignore`

`.gitignore` tells Git which files should not be tracked.

A Python project might contain:

```text
__pycache__/
*.pyc
.venv/
.env
.pytest_cache/
.idea/
.vscode/
```

Example `.gitignore`:

```gitignore
# Python
__pycache__/
*.py[cod]

# Virtual environment
.venv/
venv/

# Environment variables
.env

# Testing
.pytest_cache/

# IDE
.vscode/
.idea/

# OS
.DS_Store
```

Most importantly:

```text
.env
```

should normally not be committed when it contains secrets.

---

