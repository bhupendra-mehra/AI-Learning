# Lesson 03 – Context Managers

## Overview

Context Managers are an important Python feature used for safely managing resources and ensuring that required cleanup operations are performed automatically.

You have already used context managers in earlier lessons:

```python
with open("products.txt", "r") as file:
    data = file.read()
```

The `with` statement automatically handles opening and closing the file.

In this lesson, we will understand what happens behind the `with` statement and learn how to create our own context managers.

The concepts learned here are widely used in file handling, database connections, network connections, locks, transactions, and other resource-management scenarios.

---

# Why This Lesson Is Important

Without proper resource management, applications can leave resources open or in an inconsistent state.

For example:

```python
file = open("products.txt", "r")

data = file.read()

file.close()
```

If an exception occurs before `file.close()`, the file may not be closed properly.

A context manager solves this problem:

```python
with open("products.txt", "r") as file:
    data = file.read()
```

Python ensures that the required cleanup happens automatically.

---

# Learning Objectives

After completing this lesson, you will be able to:

* Understand what a context manager is.
* Understand how the `with` statement works.
* Explain why resource management is important.
* Understand `__enter__()` and `__exit__()`.
* Create custom context managers using classes.
* Handle exceptions inside context managers.
* Use `contextlib`.
* Create context managers using `@contextmanager`.
* Understand when context managers should be used.
* Apply context managers to practical applications.

---

# Prerequisites

Before starting this lesson, you should understand:

* Functions
* Classes and Objects
* Exception Handling
* File Handling
* Modules and Packages
* Decorators

These topics have already been covered in previous lessons.

---

# Lesson Modules

## Module 01 – Understanding Context Managers

### Topics

* What is a Context Manager?
* Why Context Managers Exist
* Resource Management
* The `with` Statement
* Automatic Cleanup
* Real-World Use Cases
* Context Manager Execution Flow

---

## Module 02 – How the `with` Statement Works

### Topics

* `__enter__()`
* `__exit__()`
* Context Manager Protocol
* Entering a Context
* Exiting a Context
* Exception Handling During Context Execution
* Execution Flow

---

## Module 03 – Creating Custom Context Managers

### Topics

* Context Manager Using a Class
* Implementing `__enter__()`
* Implementing `__exit__()`
* Returning Values from `__enter__()`
* Handling Exceptions
* Suppressing Exceptions
* Re-raising Exceptions
* Practical Examples

---

## Module 04 – Context Managers with `contextlib`

### Topics

* Introduction to `contextlib`
* `@contextmanager`
* `yield`
* Before and After `yield`
* Exception Handling
* Resource Cleanup
* Comparing Class-Based and Function-Based Context Managers

---

## Module 05 – Production Usage

### Topics

* File Resource Management
* Database Connections
* Temporary Resources
* Locks
* Transactions
* Logging and Monitoring
* Resource Cleanup
* Best Practices
* Common Mistakes

---

# Practical Examples

During this lesson, examples will include:

### File Management

```python
with open("products.txt") as file:
    ...
```

### Database-Style Resource Management

```python
with database_connection() as connection:
    ...
```

### Temporary Resource Management

```python
with temporary_resource() as resource:
    ...
```

### Lock Management

```python
with lock:
    ...
```

---

# Context Manager Execution Flow

The basic flow is:

```text
Enter Context
      ↓
__enter__()
      ↓
Execute Code
      ↓
Exception?
   ↙       ↘
 Yes       No
  ↓         ↓
__exit__() __exit__()
      ↓
Cleanup
      ↓
Exit Context
```

Understanding this execution flow will be one of the most important parts of this lesson.

---

# Context Managers vs Manual Cleanup

### Manual Approach

```python
resource = acquire_resource()

try:
    use_resource(resource)
finally:
    release_resource(resource)
```

### Context Manager

```python
with acquire_resource() as resource:
    use_resource(resource)
```

The second approach is cleaner, safer, and easier to maintain.

---

# Mini Project

## Project Name

**Resource-Safe Product Exporter**

We will enhance the existing **Function Monitoring Framework** from Lesson 02.

The project will introduce context managers for safely managing resources used during product export.

The project will demonstrate:

* Safe file handling
* Automatic cleanup
* Export session management
* Error handling
* Logging
* Combining decorators and context managers
* Clean resource management

The existing project will continue evolving rather than being discarded.

---

# Progressive Project Evolution

```text
Lesson 01
Large Product Export Simulator
        ↓
Lesson 02
Monitored Product Export Framework
        ↓
Lesson 03
Resource-Safe Product Exporter
```

This allows every new Python concept to improve an existing application.

---

# Repository Structure

```text
Lesson-03-Context-Managers/
│
├── README.md
├── notes.md
│
├── modules/
│   ├── module-01.md
│   ├── module-02.md
│   ├── module-03.md
│   ├── module-04.md
│   └── module-05.md
│
├── exercises/
│   ├── exercise-01.py
│   ├── exercise-02.py
│   └── ...
│
├── mini-project/
│   ├── README.md
│   ├── main.py
│   │
│   └── src/
│       ├── config.py
│       ├── generator.py
│       ├── filter.py
│       ├── exporter.py
│       │
│       ├── decorators/
│       │   ├── logger.py
│       │   ├── timer.py
│       │   └── exception_handler.py
│       │
│       └── context_managers/
│           └── ...
│
└── resources/
    ├── cheatsheet.md
    └── references.md
```

---

# Exercise Strategy

Following our updated learning workflow:

### Theory-only modules

We will use:

* Concept explanation
* Examples
* Interview questions
* Short knowledge-check questions

No unnecessary coding exercises.

### Practical modules

We will provide:

* Practical examples
* Coding exercises
* Code review
* Real-world implementation

This keeps the course focused and avoids spending time on repetitive exercises.

---

# Interview Topics

By the end of this lesson, you should be able to answer:

* What is a context manager?
* Why do we use the `with` statement?
* What are `__enter__()` and `__exit__()`?
* What is the context manager protocol?
* How do context managers handle exceptions?
* Can `__exit__()` suppress an exception?
* How do you create a custom context manager?
* What is `contextlib`?
* What does `@contextmanager` do?
* What is the purpose of `yield` in a context manager?
* When should you use a context manager?

---

# Real-World Applications

Context managers are commonly used for:

* File handling
* Database connections
* Transactions
* Locks
* Temporary directories
* Network connections
* Resource allocation
* Testing resources
* Session management

They are especially important in backend and production applications where resources must always be released correctly.

---

# Best Practices Covered

* Always release acquired resources.
* Prefer context managers over manual cleanup when appropriate.
* Keep context managers focused on resource lifecycle management.
* Handle exceptions carefully.
* Avoid hiding unexpected exceptions.
* Use `contextlib` when a class-based context manager would be unnecessarily complex.
* Keep resource acquisition and cleanup clearly separated.

---

# Expected Outcome

After completing this lesson, you should be able to look at:

```python
with something() as resource:
    ...
```

and understand exactly what Python is doing behind the scenes.

You will also be able to create your own context managers and use them to safely manage resources in production applications.

---

# Estimated Completion Time

**5–7 Hours**

The time is shorter than some previous lessons because we will focus on the concepts that are actually important for practical Python development.

---

# Lesson Completion Criteria

The lesson will be considered complete when you can:

* Explain the purpose of context managers.
* Explain the `with` statement.
* Explain `__enter__()` and `__exit__()`.
* Create a class-based context manager.
* Create a function-based context manager using `@contextmanager`.
* Handle exceptions correctly.
* Explain when to use each approach.
* Complete the Resource-Safe Product Exporter mini project.
* Answer the core interview questions confidently.


