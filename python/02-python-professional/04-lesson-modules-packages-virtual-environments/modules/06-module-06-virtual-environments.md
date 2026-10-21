# Lesson 14 – Module 6

# Virtual Environments (`venv`)

## Module Objective

In the previous module, you learned how to install Python packages using `pip`.

However, when you tried to install the `rich` package, Ubuntu displayed the following error:

```text
error: externally-managed-environment
```

This is expected on modern Ubuntu and Debian systems because of **PEP 668**, which prevents installing packages directly into the operating system's Python environment.

The professional solution is to use a **Virtual Environment**.

---

# What is a Virtual Environment?

A **Virtual Environment (venv)** is an isolated Python environment created specifically for one project.

Instead of using the operating system's Python installation, each project gets its own:

* Python interpreter
* `pip`
* Installed libraries

This keeps projects independent and avoids dependency conflicts.

---

# Why Do We Need Virtual Environments?

Imagine you have two AI projects.

### Project A

Requires:

```text
openai==1.95
langchain==0.3
```

### Project B

Requires:

```text
openai==2.x
langchain==1.x
```

If both projects use the same system Python, upgrading one project's libraries could break the other.

Using separate virtual environments avoids this problem.

---

# Without Virtual Environment

```text
Ubuntu Python
│
├── openai
├── requests
├── pandas
├── rich
└── numpy
```

Every project shares the same packages.

---

# With Virtual Environment

```text
Chatbot_Project/
│
├── venv/
├── main.py
└── requirements.txt

Magento_AI/
│
├── venv/
├── app.py
└── requirements.txt
```

Each project has its own isolated environment.

---

# What Happened in Our Case?

Initially, you ran:

```bash
python3 -m pip install rich
```

Ubuntu responded:

```text
externally-managed-environment
```

This happened because your Python installation is managed by Ubuntu, and direct package installation into the system environment is restricted.

---

# How We Solved It

### Step 1 – Install Virtual Environment Support

We installed:

```bash
sudo apt update
sudo apt install python3.12-venv
```

This added the missing `venv` and `ensurepip` components.

---

### Step 2 – Create a Virtual Environment

```bash
python3 -m venv testenv
```

Python created:

```text
testenv/
├── bin/
├── include/
├── lib/
└── pyvenv.cfg
```

---

### Step 3 – Activate It

```bash
source testenv/bin/activate
```

Your terminal changed to:

```text
(testenv) ubuntu@...
```

This indicates you're working inside the virtual environment.

---

### Step 4 – Install Packages

Now packages are installed inside the virtual environment instead of the system Python.

Example:

```bash
pip install rich
```

No `externally-managed-environment` error occurs.

---

### Step 5 – Deactivate

When finished:

```bash
deactivate
```

The shell returns to the system Python.

---

# Understanding the Workflow

When the virtual environment is activated:

```text
(testenv)
        │
        ├── python
        ├── pip
        ├── rich
        ├── requests
        └── numpy
```

When it's deactivated:

```text
Ubuntu Python
        │
        ├── system packages
        └── managed by apt
```

Switching between them is as simple as activating or deactivating the environment.

---

# Professional Development Workflow

For every new Python project:

```bash
mkdir my_project
cd my_project

python3 -m venv venv

source venv/bin/activate

python -m pip install requests
python -m pip install rich
```

When you finish:

```bash
deactivate
```

This is the standard workflow used in Python development.

---

# Real AI Project Example

An AI chatbot project might look like:

```text
ai-chatbot/
│
├── venv/
├── app.py
├── requirements.txt
├── prompts/
├── utils/
└── models/
```

The `venv` directory is **not** committed to Git. Instead, the project shares a `requirements.txt` file, which we'll cover next.

---

# Best Practices

### ✅ Create one virtual environment per project.

### ✅ Activate it before installing packages.

### ✅ Use:

```bash
python -m pip install package_name
```

inside the activated environment.

### ✅ Deactivate it when finished.

### ❌ Avoid installing development packages into the system Python.

### ❌ Avoid using:

```bash
--break-system-packages
```

unless you fully understand the implications.

---

# Module 6 Summary

After completing this module, you can:

* ✅ Explain what a virtual environment is.
* ✅ Understand why Ubuntu blocks system-wide `pip` installs.
* ✅ Create a virtual environment.
* ✅ Activate and deactivate it.
* ✅ Install packages safely inside it.
* ✅ Follow the workflow used in professional Python, AI, and web development.

---

# What You've Already Completed

During our troubleshooting, you successfully completed all the practical work for this module:

* ✅ Installed `python3.12-venv`
* ✅ Created a virtual environment
* ✅ Understood why the original error occurred
* ✅ Learned the professional solution

So there are **no additional exercises** for Module 6.

---

## Next Module

**Module 7 – `requirements.txt` & Dependency Management**

This is where you'll learn how teams share project dependencies so that another developer can set up the exact same environment with a single command. It's an essential skill for collaborating on AI, Django, FastAPI, and production Python projects.
