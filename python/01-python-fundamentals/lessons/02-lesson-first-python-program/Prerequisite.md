Since you're a **Magento developer using WSL**, we'll treat WSL as your **development machine**. This is how many professional developers work.

So from now on:

* ✅ Windows = Operating System
* ✅ WSL (Ubuntu) = Development Environment
* ✅ VS Code = Editor
* ✅ Python = Runs inside WSL
* ✅ AI Programs = Run inside WSL

This is much closer to how you'll eventually deploy AI applications on Linux servers.

---

# Prerequisite (WSL Environment)

## Your Development Architecture

Instead of this:

```text
Windows

↓

Python

↓

OpenAI
```

We'll use:

```text
Windows

↓

WSL (Ubuntu)

↓

Python

↓

OpenAI API

↓

LLM
```

Think of WSL as a small Linux machine running inside Windows.

---

# Compare it with Magento

Today your Magento environment probably looks something like:

```text
Windows

↓

WSL Ubuntu

↓

PHP

↓

Nginx

↓

Magento

↓

MySQL

↓

Redis

↓

OpenSearch
```

We're simply adding Python alongside PHP.

```text
Windows

↓

WSL Ubuntu

↓

PHP
Python

↓

Magento
AI Application

↓

OpenAI API
```

Notice something?

Python is **not replacing PHP**.

It's just another tool available in your development environment.

---

# Step 1 - Open WSL

Open Ubuntu.

Run:

```bash
pwd
```

Tell me what you get.

Example:

```bash
/home/ubuntu
```

---

# Step 2 - Check Python

Inside WSL run:

```bash
python3 --version
```

**Notice it's `python3`, not `python`.**

On Ubuntu/WSL, `python3` is the standard command.

Possible output:

```text
Python 3.12.3
```

---

# Step 3 - Check pip

Run:

```bash
pip3 --version
```

Possible output:

```text
pip 24.x.x
```

---

# Why `python3` and `pip3`?

On Linux:

```bash
python3
pip3
```

are commonly used to avoid conflicts with older Python versions.

You may be able to use `python` and `pip` too, but we'll stick with the Linux convention for now.

---

# Step 4 - Check VS Code Integration

Inside WSL run:

```bash
code .
```

If VS Code opens with a small green or blue indicator showing it's connected to **WSL**, then you're set up correctly.

If it says:

```text
code: command not found
```

We'll fix that.

---
