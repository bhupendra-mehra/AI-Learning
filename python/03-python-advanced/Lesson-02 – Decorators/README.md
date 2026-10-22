# Lesson 02 – Decorators

## Overview

Decorators are one of Python's most powerful and widely used features. They allow you to extend or modify the behavior of functions without changing their original implementation. Instead of placing repetitive logic such as logging, timing, validation, authentication, or error handling inside every function, decorators let you write that logic once and reuse it wherever needed.

Although decorators initially seem difficult, they are built on concepts you already know, including functions, nested functions, closures, and returning functions. By the end of this lesson, decorators will become one of your most valuable tools for writing clean, reusable, and production-ready Python code.

---

# Why This Lesson Is Important

As applications grow, many functions require the same additional behavior.

For example:

* Logging function execution
* Measuring execution time
* Validating inputs
* Checking permissions
* Handling exceptions
* Caching results
* Counting function calls

Without decorators, these tasks are repeated inside every function, leading to duplicated code and making applications harder to maintain.

Decorators solve this problem by separating reusable infrastructure logic from business logic.

---

# Real-World Applications

Decorators are used extensively in:

* FastAPI
* Django
* Flask
* PyTest
* Click
* Celery
* AI Frameworks
* Data Engineering Pipelines
* Magento Backend Integrations

Examples include:

* API route registration
* Authentication
* Authorization
* Logging
* Rate limiting
* Retry mechanisms
* Caching
* Performance monitoring
* Exception handling

---

# Prerequisites

Before starting this lesson, you should understand:

* Functions
* Function arguments
* Return values
* Variable scope
* Object-Oriented Programming
* Modules & Packages
* Iterators & Generators

---

# Learning Objectives

After completing this lesson, you will be able to:

* Explain why decorators exist.
* Understand nested functions.
* Understand closures.
* Create custom decorators.
* Decorate functions with and without parameters.
* Pass arguments using `*args` and `**kwargs`.
* Preserve function metadata using `functools.wraps`.
* Stack multiple decorators.
* Build reusable production-ready decorators.
* Read and understand decorator-based code in modern Python frameworks.

---

# Lesson Modules

## Module 01 – Why Decorators?

### Topics

* What Problem Do Decorators Solve?
* Code Duplication
* Cross-Cutting Concerns
* Real-World Examples
* Advantages of Decorators

---

## Module 02 – Nested Functions

### Topics

* Functions Inside Functions
* Scope
* Calling Inner Functions
* Returning Functions
* Practical Examples

---

## Module 03 – Closures

### Topics

* What Is a Closure?
* Variable Capture
* Preserving State
* Practical Use Cases
* Relationship Between Closures and Decorators

---

## Module 04 – Building Decorators

### Topics

* Creating Your First Decorator
* Wrapping Functions
* `*args`
* `**kwargs`
* Returning Values
* Decorating Multiple Functions

---

## Module 05 – Advanced Decorators

### Topics

* Decorators with Parameters
* Stacking Decorators
* `functools.wraps`
* Preserving Metadata
* Class-Based Decorators (Introduction)

---

## Module 06 – Production Decorators

### Topics

* Logging Decorator
* Execution Time Decorator
* Exception Handling Decorator
* Retry Decorator
* Input Validation
* Real-World Project Integration

---

# Mini Project

## Project Name

**Function Monitoring Framework**

During this lesson, you'll enhance the **Large Product Export Simulator** built in Lesson 01.

Instead of creating a separate project, you'll improve the existing application by adding reusable decorators.

Features include:

* Logging every function call.
* Measuring execution time.
* Counting function executions.
* Handling exceptions gracefully.
* Validating function inputs.
* Applying multiple decorators to the same function.

By extending an existing project, you'll learn how decorators are applied in real software rather than in isolated examples.

---

# Repository Structure

```text
Lesson-02-Decorators/
│
├── README.md
├── notes.md
│
├── modules/
│   ├── module-01.md
│   ├── module-02.md
│   ├── module-03.md
│   ├── module-04.md
│   ├── module-05.md
│   └── module-06.md
│
├── exercises/
│   ├── exercise-01.py
│   ├── exercise-02.py
│   └── ...
│
├── mini-project/
│   ├── README.md
│   ├── main.py
│   └── src/
│
├── interview/
│   └── interview-questions.md
│
└── resources/
    ├── cheatsheet.md
    ├── references.md
    └── images/
```

---

# Interview Skills You'll Gain

By the end of this lesson, you'll confidently answer questions such as:

* What is a decorator?
* Why are decorators used?
* What problem do decorators solve?
* What is the relationship between closures and decorators?
* What are `*args` and `**kwargs` in decorators?
* Why is `functools.wraps` important?
* How do multiple decorators execute?
* Give real-world examples of decorators.

---

# Estimated Completion Time

**6–8 Hours**

---

# Expected Outcome

After completing this lesson, you'll be able to understand and write decorator-based code used in FastAPI, Django, Flask, PyTest, and production Python applications. You'll also upgrade your previous mini project into a cleaner, more maintainable application using reusable decorators.

---

# Lesson Summary

Decorators are a core feature of professional Python development. They eliminate duplicated code, improve maintainability, and make applications easier to extend. Mastering decorators will prepare you for backend development, AI frameworks, FastAPI, and production software engineering.



