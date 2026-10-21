# Lesson 14 – Module 5

# Installing Libraries with `pip`

## Module Objective

Until now, you've only used Python's built-in modules or modules you've created yourself.

In this module, you'll learn how to install and use **third-party libraries**—code written by other developers that you can use in your own projects.

This is how you'll later install AI libraries such as:

* NumPy
* Pandas
* Scikit-learn
* TensorFlow
* PyTorch
* OpenAI SDK
* LangChain
* FastAPI

---

# What is `pip`?

`pip` stands for **Package Installer for Python**.

It downloads and installs Python packages from the **Python Package Index (PyPI)**.

Think of it this way:

| Technology | Package Manager |
| ---------- | --------------- |
| Python     | `pip`           |
| PHP        | Composer        |
| Node.js    | npm             |
| Java       | Maven / Gradle  |

Since you're a Magento developer, the closest equivalent is **Composer**:

```bash
composer require vendor/package
```

In Python, the equivalent is:

```bash
pip install package_name
```

---

# What is PyPI?

**PyPI (Python Package Index)** is the official repository of Python packages.

It contains hundreds of thousands of open-source libraries.

Instead of writing everything yourself, you install what you need.

Examples:

| Package    | Purpose                     |
| ---------- | --------------------------- |
| requests   | HTTP requests               |
| numpy      | Numerical computing         |
| pandas     | Data analysis               |
| matplotlib | Charts and graphs           |
| flask      | Web applications            |
| fastapi    | REST APIs                   |
| openai     | OpenAI API                  |
| langchain  | AI agents and LLM workflows |

---

# Check Your `pip` Version

Since you're using WSL with Python 3.12, run:

```bash
pip3 --version
```

or

```bash
python3 -m pip --version
```

You should see something similar to:

```text
pip 24.x from /usr/lib/python3/dist-packages/pip (python 3.12)
```

---

# Installing a Package

Let's install one of the most popular Python libraries: `requests`.

Run:

```bash
pip3 install requests
```

Or the recommended approach:

```bash
python3 -m pip install requests
```

### Why is `python3 -m pip` recommended?

It ensures that `pip` belongs to the same Python interpreter you're using, which helps avoid issues when multiple Python versions are installed.

---

# Verify Installation

Run:

```bash
pip3 show requests
```

Example output:

```text
Name: requests
Version: 2.x.x
Location: ...
```

You can also list installed packages:

```bash
pip3 list
```

You'll likely see packages such as:

```text
pip
setuptools
wheel
requests
```

---

# Using an Installed Package

Create `request_example.py`:

```python
import requests

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
```

When you run it:

```bash
python3 request_example.py
```

Expected output:

```text
Status Code: 200
```

> This confirms that the package was successfully installed and imported.

---

# Upgrading a Package

To upgrade to the latest version:

```bash
pip3 install --upgrade requests
```

---

# Uninstalling a Package

If you no longer need it:

```bash
pip3 uninstall requests
```

You'll be asked for confirmation before removal.

---

# Installing a Specific Version

Sometimes projects require a fixed version.

Example:

```bash
pip3 install requests==2.32.3
```

Version pinning is common in production projects because it ensures consistent behavior across different environments.

---

# Viewing Package Information

To inspect a package:

```bash
pip3 show requests
```

Useful details include:

* Name
* Version
* Summary
* Installation path
* Dependencies

---

# Searching for Packages

The old `pip search` command has been removed.

Instead, search on:

**[https://pypi.org](https://pypi.org)**

You'll use this site frequently throughout your AI journey.

---

# Common `pip` Commands

| Command                          | Purpose                                     |
| -------------------------------- | ------------------------------------------- |
| `pip3 install package`           | Install a package                           |
| `pip3 uninstall package`         | Remove a package                            |
| `pip3 list`                      | Show installed packages                     |
| `pip3 show package`              | Show package details                        |
| `pip3 install --upgrade package` | Upgrade a package                           |
| `pip3 freeze`                    | List installed packages with exact versions |

---

# How AI Projects Use `pip`

Suppose you want to build an AI chatbot.

You'll install:

```bash
pip install openai
pip install langchain
pip install chromadb
pip install fastapi
```

Instead of writing those libraries yourself, you install and import them:

```python
from openai import OpenAI
from langchain.chat_models import ChatOpenAI
```

This is the standard workflow for Python development.

---

# Exercise 1

Run these commands one by one:

```bash
python3 -m pip --version
```

```bash
python3 -m pip install requests
```

```bash
python3 -m pip show requests
```

```bash
python3 -m pip list
```

---

# Exercise 2

Create `request_example.py`:

```python
import requests

response = requests.get("https://api.github.com")

print("Status Code:", response.status_code)
print("Server:", response.headers.get("Server"))
```

Run it and confirm you receive a successful response.

---

# Challenge

Install another package, such as:

```bash
python3 -m pip install rich
```

Then create:

```python
from rich import print

print("[bold green]Hello from Rich![/bold green]")
```

This will show how third-party libraries can enhance your applications with very little code.

---

# Common Mistakes

### 1. Running the wrong `pip`

If you have multiple Python versions installed, always prefer:

```bash
python3 -m pip install package_name
```

instead of just:

```bash
pip install package_name
```

---

### 2. `ModuleNotFoundError`

If Python reports:

```text
ModuleNotFoundError: No module named 'requests'
```

the package either wasn't installed or was installed for a different Python interpreter.

---

### 3. Installing as Root

Avoid using:

```bash
sudo pip install ...
```

for regular development. We'll learn a better approach in the next module using **virtual environments**, which isolate dependencies for each project.

---

# Module 5 Summary

After completing this module, you'll be able to:

* ✅ Understand what `pip` is.
* ✅ Install third-party libraries.
* ✅ Upgrade and uninstall packages.
* ✅ Inspect installed packages.
* ✅ Use installed packages in Python programs.
* ✅ Understand how AI projects manage external dependencies.

---

## Your Task

1. Complete both exercises.
2. Install and test the `rich` package in the challenge.
3. Share the output or confirm that everything worked.

After that, we'll move to **Module 6 – Virtual Environments (`venv`)**, where you'll learn one of the most important practices in professional Python development: keeping each project's dependencies isolated. This is essential before we start working with AI frameworks and APIs.
