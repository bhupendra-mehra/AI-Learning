# Lesson 14 – Self Assessment (Professional Answers)

### 1. What is the difference between a module and a package?

A **module** is a single Python file (`.py`) that contains related functions, classes, or variables for a specific functionality.

A **package** is a directory that contains multiple related modules (and optionally sub-packages), allowing the project to be organized in a structured way.

---

### 2. Why do we use `__init__.py`?

The `__init__.py` file marks a directory as a Python package (a common and recommended practice). It can also perform package initialization and expose selected modules or functions, making imports simpler and more organized.

---

### 3. What are the different ways to import modules?

Python provides four common ways to import modules:

1. Import the entire module

   ```python
   import calculator
   ```

2. Import specific functions

   ```python
   from calculator import add
   ```

3. Import with an alias

   ```python
   import calculator as calc
   ```

4. Wildcard import

   ```python
   from calculator import *
   ```

---

### 4. Why are wildcard imports generally discouraged?

Wildcard imports bring all public objects from a module into the current namespace. If multiple modules contain functions or variables with the same name, they can overwrite each other, causing naming conflicts and making the code harder to read, debug, and maintain.

---

### 5. What does `pip` do?

`pip` is Python's package manager. It is used to install, upgrade, uninstall, and manage third-party Python packages and their dependencies.

It is similar to **Composer** in PHP or Magento projects.

---

### 6. Why do modern Ubuntu systems block system-wide `pip install`?

Modern Ubuntu systems follow **PEP 668**, which protects the system-managed Python environment. This prevents `pip` from installing packages directly into the operating system's Python installation, reducing the risk of breaking system tools or creating dependency conflicts.

Instead, developers are encouraged to use **virtual environments** or install system packages through `apt` when appropriate.

---

### 7. What is a virtual environment?

A virtual environment is an isolated Python environment created for a specific project. It has its own Python interpreter, `pip`, and installed packages, allowing projects to manage dependencies independently.

---

### 8. Why should each project have its own virtual environment?

Each project may require different package versions or dependencies. Using a separate virtual environment ensures that changes made for one project do not affect another project or the system Python installation.

---

### 9. What is `requirements.txt`?

`requirements.txt` is a file that contains a list of all the project's required Python packages and their versions. It allows anyone to recreate the same environment by running:

```bash
pip install -r requirements.txt
```

---

### 10. Why shouldn't you commit the `venv/` directory to Git?

The `venv/` directory contains the project's local Python interpreter, installed packages, and environment-specific files. These files can be recreated using `requirements.txt` and often consume significant disk space. Therefore, `venv/` should be excluded from version control and added to `.gitignore`.

---

## Interview Tip

For interviews, try to explain the concepts instead of just giving definitions. For example:

* **Module** → "A single Python file containing reusable code."
* **Package** → "A collection of related modules organized inside a directory."

This approach demonstrates that you understand the concepts rather than having memorized definitions.

**I would rate your understanding of Lesson 14 as 9.5/10.** You grasped the concepts well, and with these polished explanations, you're ready to answer interview questions confidently.
