# Lesson 01: Introduction to Python

## What is Python?

Python is a general-purpose, high-level programming language. Its readable syntax makes it useful for scripting, automation, web development, data work, and building applications. Python is interpreted: the Python runtime executes your source code and reports errors as it runs.

## How a Python program runs

1. Write source code in a file ending in `.py`.
2. Run it with the Python interpreter, for example `python3 app.py` (or `python app.py` when that is the command configured on your system).
3. Python executes the statements and displays output or an error.

You can also start an interactive Python prompt by running `python3` or `python` and try individual expressions there. Use `exit()` to leave it.

```python
print("Hello, Python!")
```

## Important ideas to remember

- **Indentation defines code blocks.** Indent consistently, usually with four spaces. The body of an `if`, loop, function, or class must be indented.
- **Names are case-sensitive.** `name`, `Name`, and `NAME` are different identifiers.
- **Variables are names bound to objects.** Create or update a binding with assignment, such as `count = 3`; Python does not require a separate type declaration.
- **Types matter.** Common built-in types include `int`, `float`, `str`, `bool`, and `None`. Use `type(value)` when learning what a value is.
- **Strings use quotes.** Single and double quotes both work. f-strings such as `f"Hello, {name}"` are a convenient way to insert values into text.
- **Comments begin with `#`.** Comments explain intent; they are ignored when Python runs the program.
- **Input and output are explicit.** `input()` reads text from the user, and `print()` displays values. Convert input when you need a number, for example `age = int(input("Age: "))`.
- **Errors are useful feedback.** Read the exception type and traceback, then inspect the file and line named near the end. Syntax errors prevent parsing; runtime exceptions happen while code executes.
- **The standard library comes with Python.** Import a module before using its functionality, for example `import math`.
- **Third-party packages are installed separately.** Use `pip` in a project-specific virtual environment so project dependencies stay isolated.

## A small example

```python
name = input("What is your name? ")
print(f"Welcome, {name}!")
```

The value returned by `input()` is a string. If you want numeric input, convert it with `int()` or `float()` and handle invalid input as you learn exception handling.

## A practical learning path

The next lessons build on this introduction in order:

1. Writing and running a first Python program
2. Variables and data types
3. Operators and conditions
4. Loops
5. Functions
6. Collections
7. Object-oriented programming
8. Exception handling
9. File handling
10. Modules, packages, and virtual environments

Practice each concept with small programs. Run your code often, change one thing at a time, and use error messages to guide debugging.
