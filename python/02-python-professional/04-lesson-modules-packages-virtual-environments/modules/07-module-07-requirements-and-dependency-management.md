# Lesson 14 – Module 7

# `requirements.txt` & Dependency Management

## Module Objective

Imagine you've spent three months building an AI chatbot.

You've installed:

* OpenAI
* LangChain
* FastAPI
* Pandas
* NumPy
* Rich

Now another developer joins your team.

How will they know **which packages** and **which versions** to install?

That's the purpose of `requirements.txt`.

---

# What is `requirements.txt`?

`requirements.txt` is a plain text file that contains a list of all the Python packages required by your project.

Example:

```text
requests==2.32.3
rich==14.1.0
numpy==2.3.1
pandas==2.3.1
```

Instead of installing each package manually, another developer can install everything with one command.

---

# Why is it Important?

Suppose your project uses:

```text
openai==1.95.0
```

A teammate installs:

```text
openai==2.1.0
```

Some APIs may have changed, causing your code to fail.

By sharing the exact versions, everyone works with the same environment.

---

# Real-World Example

Imagine a team of five developers.

```
Developer A
↓

Creates project

↓

Installs packages

↓

Generates requirements.txt

↓

Pushes code to GitHub
```

Later:

```
Developer B

↓

Clones the repository

↓

Creates a virtual environment

↓

Runs:

pip install -r requirements.txt

↓

Ready to work
```

No guessing. No missing packages.

---

# Creating `requirements.txt`

Inside an activated virtual environment, run:

```bash
pip freeze
```

Example output:

```text
markdown-it-py==4.0.0
mdurl==0.1.2
Pygments==2.19.2
rich==14.1.0
requests==2.32.3
```

To save this list:

```bash
pip freeze > requirements.txt
```

Now your project contains:

```text
project/

main.py
requirements.txt
venv/
```

---

# Installing from `requirements.txt`

On another machine (or after creating a new virtual environment):

```bash
pip install -r requirements.txt
```

Python reads the file and installs every package automatically.

---

# Updating Dependencies

Suppose you install another package:

```bash
pip install pandas
```

Your `requirements.txt` won't update automatically.

Run:

```bash
pip freeze > requirements.txt
```

again to refresh it.

---

# Real AI Project Structure

A professional AI project typically looks like this:

```text
ai-chatbot/

├── venv/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── prompts/
├── models/
├── utils/
└── tests/
```

Notice:

* `requirements.txt` is committed to Git.
* `venv/` is **not** committed.

---

# Why Don't We Commit `venv/`?

A virtual environment contains:

* Python binaries
* Installed packages
* Temporary files

It can easily be hundreds of megabytes.

Instead, Git stores only:

```text
requirements.txt
```

Anyone can recreate the environment.

---

# `.gitignore`

A typical `.gitignore` file contains:

```text
venv/
__pycache__/
*.pyc
.env
```

This prevents unnecessary or machine-specific files from being committed.

---

# Common Commands

### Save dependencies

```bash
pip freeze > requirements.txt
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### View installed packages

```bash
pip list
```

### Show package details

```bash
pip show requests
```

---

# Professional Workflow

Every new project follows roughly this sequence:

```bash
mkdir project
cd project

python3 -m venv venv

source venv/bin/activate

pip install requests
pip install rich

pip freeze > requirements.txt
```

Later, another developer does:

```bash
git clone <repository>

cd project

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

The environments are now identical.

---

# AI Example

When we build an AI Agent later in this roadmap, our `requirements.txt` might contain:

```text
openai==1.95.0
langchain==0.3.x
fastapi==0.116.x
uvicorn==0.35.x
chromadb==1.x
python-dotenv==1.1.x
```

A new developer only needs:

```bash
pip install -r requirements.txt
```

and the project is ready.

---

# Difference Between `pip list` and `pip freeze`

| `pip list`                 | `pip freeze`                    |
| -------------------------- | ------------------------------- |
| Human-readable             | Machine-readable                |
| Shows installed packages   | Generates version-pinned output |
| Good for checking packages | Best for `requirements.txt`     |

---

# Best Practices

### ✅ Create one `requirements.txt` per project.

### ✅ Update it after adding or removing packages.

### ✅ Commit it to Git.

### ✅ Install dependencies only inside a virtual environment.

### ❌ Never commit the `venv/` directory.

---

# Module 7 Summary

After completing this module, you can:

* ✅ Explain the purpose of `requirements.txt`.
* ✅ Generate it using `pip freeze`.
* ✅ Install dependencies with `pip install -r requirements.txt`.
* ✅ Understand why version pinning matters.
* ✅ Follow the dependency management workflow used by professional Python and AI teams.

---

# 🎉 Lesson 14 Completed

## What You Learned

| Module                                     | Status |
| ------------------------------------------ | ------ |
| Introduction to Modules                    | ✅      |
| Creating Your Own Modules                  | ✅      |
| Different Import Styles                    | ✅      |
| Packages (`__init__.py`)                   | ✅      |
| Installing Libraries with `pip`            | ✅      |
| Virtual Environments (`venv`)              | ✅      |
| `requirements.txt` & Dependency Management | ✅      |

---

# Knowledge Check

You should now be able to answer these questions confidently:

1. What is the difference between a **module** and a **package**?
2. Why do we use `__init__.py`?
3. What are the different ways to import modules?
4. Why are wildcard imports generally discouraged?
5. What does `pip` do?
6. Why do modern Ubuntu systems block system-wide `pip install`?
7. What is a virtual environment?
8. Why should each project have its own virtual environment?
9. What is `requirements.txt`?
10. Why shouldn't you commit the `venv/` directory to Git?

If you can answer these without looking back, you've mastered the core Python project organization concepts.

---

## Next Lesson

We'll move to **Lesson 15 – Object-Oriented Programming (OOP)**.

Since you're a Magento developer, you'll notice many familiar concepts:

* Classes
* Objects
* Constructors
* Inheritance
* Polymorphism
* Encapsulation
* Abstraction

We'll connect every concept to both **Magento 2** and **Python**, making it easier to transfer your existing knowledge instead of learning OOP from scratch. This lesson is particularly important because nearly every major AI framework is object-oriented.
