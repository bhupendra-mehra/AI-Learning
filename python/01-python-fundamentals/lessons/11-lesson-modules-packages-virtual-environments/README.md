# Lesson 14 — Modules, Packages & Virtual Environments

## Lesson Objective

By the end of this lesson, you will understand how Python projects are organized into reusable files and folders, how to use code written by yourself or others, how to install external libraries, and how to isolate project dependencies using virtual environments.

This lesson is one of the most important foundations for AI development because virtually every AI project relies on external packages such as NumPy, Pandas, PyTorch, TensorFlow, LangChain, FastAPI, and the OpenAI SDK.

After completing this lesson, you'll be able to create structured Python projects similar to real-world AI applications.

---

# Why This Lesson Is Important

Until now, every program you've written has been in a single file. That works for small examples, but real applications may contain hundreds or even thousands of Python files.

For example:

```
AI Chatbot
│
├── main.py
├── config.py
├── database.py
├── prompts.py
├── models.py
├── utils.py
├── api.py
├── requirements.txt
└── venv/
```

Imagine keeping all of that code in one file—it would quickly become difficult to read, maintain, and debug.

Modules and packages solve this problem by letting you organize related functionality into separate, reusable components.

---

# Real-World Examples

### Magento

Instead of writing everything in one file, Magento is organized into modules such as:

```
Magento_Catalog
Magento_Checkout
Magento_Customer
Magento_Sales
```

Each module has its own responsibilities.

---

### Python AI Project

Similarly, an AI project might look like:

```
chatbot/

main.py
config.py
llm.py
database.py
memory.py
utils.py
```

Each file has a specific responsibility, making the project easier to maintain.

---

# Learning Outcomes

After completing Lesson 14, you will be able to:

* Create reusable Python modules.
* Import modules in different ways.
* Organize code into packages.
* Install third-party libraries using `pip`.
* Create and use virtual environments.
* Understand `requirements.txt`.
* Build a small multi-file Python project.

These skills are prerequisites for working with AI frameworks later in the roadmap.

---

# Lesson Structure

This lesson contains **7 modules**.

| Module   | Topic                                              | Difficulty | Estimated Time |
| -------- | -------------------------------------------------- | ---------- | -------------- |
| Module 1 | Introduction to Modules                            | ⭐          | 20 min         |
| Module 2 | Creating Your Own Modules                          | ⭐          | 30 min         |
| Module 3 | Packages & `__init__.py`                           | ⭐⭐         | 30 min         |
| Module 4 | Installing Libraries with `pip`                    | ⭐          | 20 min         |
| Module 5 | Virtual Environments (`venv`)                      | ⭐⭐         | 40 min         |
| Module 6 | Project Dependency Management (`requirements.txt`) | ⭐⭐         | 20 min         |
| Module 7 | Mini Project – Build a Modular Calculator          | ⭐⭐⭐        | 45 min         |

**Estimated total lesson time:** 3–4 hours

---

# Skills You'll Gain

By the end of Lesson 14, you'll understand:

* What a Python module is.
* The difference between modules and packages.
* How Python searches for imported modules.
* Different import styles (`import`, `from`, aliases).
* How to organize a multi-file project.
* How to install external libraries.
* Why virtual environments are essential.
* How dependency management works in professional projects.

---

# Where This Fits in the AI Roadmap

Everything after this lesson depends on it.

For example:

* **NumPy** → Imported as a module.
* **Pandas** → Installed using `pip`.
* **OpenAI SDK** → Installed in a virtual environment.
* **LangChain** → Imported from installed packages.
* **FastAPI** → Runs inside a virtual environment with managed dependencies.

Without these concepts, working on real AI applications becomes much harder.

---

# Prerequisites

You should already know:

* ✅ Variables
* ✅ Data types
* ✅ Operators
* ✅ Conditions
* ✅ Loops
* ✅ Functions
* ✅ File handling

Since you've completed those lessons, you're ready for Lesson 14.

---

# What We'll Build in This Lesson

By the end, you'll have a small project like this:

```
calculator_project/
│
├── calculator/
│   ├── __init__.py
│   ├── arithmetic.py
│   └── advanced.py
│
├── main.py
├── requirements.txt
└── venv/
```

This mirrors the structure of professional Python and AI projects.

---
