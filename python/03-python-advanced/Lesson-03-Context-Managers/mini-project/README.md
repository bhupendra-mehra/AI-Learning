# Lesson 03 Mini Project – Resource-Safe Product Exporter

## Overview

This project extends the **Monitored Product Export Framework** created in Lesson 02.

In Lesson 01, we used generators to process large product datasets efficiently.

In Lesson 02, we added decorators for:

* Logging
* Execution-time monitoring
* Exception handling

In Lesson 03, we will add **context managers** to safely manage the export file lifecycle.

The final application will combine all three concepts:

```text
Generators
    ↓
Memory-efficient product processing
    ↓
Decorators
    ↓
Logging + Timing + Error Handling
    ↓
Context Manager
    ↓
Safe File Resource Management
    ↓
Product Export
```

---

# Project Objective

Build a production-style product export application that:

* Generates a large number of products using generators.
* Filters products without loading everything into memory.
* Uses decorators for logging and execution-time monitoring.
* Handles exceptions consistently.
* Uses a context manager for safe file management.
* Exports the final products to a file.
* Keeps business logic separate from infrastructure logic.

---

# Features

## 1. Product Generation

Products will be generated lazily using a generator.

```python
def generate_products(total):
    ...
    yield product
```

This allows the application to process large datasets without storing all products in memory.

---

## 2. Product Filtering

Products will be filtered as they move through the processing pipeline.

```text
Generate
   ↓
Filter
   ↓
Export
```

The application will continue using generator-based processing.

---

## 3. Logging

The existing `logger` decorator from Lesson 02 will monitor important application functions.

Example:

```text
[LOG] Calling export_products
[LOG] Completed export_products
```

---

## 4. Execution Time Monitoring

The existing `timer` decorator will measure execution time.

Example:

```text
[TIMER] export_products took 0.012345 seconds
```

The exact execution time will vary.

---

## 5. Exception Handling

The existing `handle_errors` decorator will provide centralized exception handling.

Example:

```text
[ERROR] export_products failed: ...
```

Exceptions will not be silently hidden.

---

## 6. Resource Management

A context manager will manage the export file.

Conceptually:

```text
Open File
    ↓
Write Products
    ↓
Close File
```

Even if the export fails:

```text
Open File
    ↓
Write Products
    ↓
Exception
    ↓
Close File
    ↓
Exception Propagates
```

---

# Architecture

```text
                         main.py
                            │
                            ▼
                   generate_products()
                            │
                            ▼
                    filter_products()
                            │
                            ▼
                    export_products()
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
          Logger          Timer      Error Handler
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                     Export Session
                     Context Manager
                            │
                            ▼
                       products.txt
```

---

# Project Flow

```text
Start
  │
  ▼
Generate Products
  │
  ▼
Filter Products
  │
  ▼
Call Export Function
  │
  ├── Logger
  │
  ├── Timer
  │
  └── Error Handler
  │
  ▼
Enter Export Context
  │
  ▼
Open Output File
  │
  ▼
Write Products
  │
  ▼
Exit Export Context
  │
  ▼
Close Output File
  │
  ▼
Display Export Summary
```

---

# Project Structure

```text
mini-project/
│
├── README.md
├── main.py
├── .gitignore
├── requirements.txt
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── generator.py
│   ├── filter.py
│   ├── exporter.py
│   │
│   ├── decorators/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── timer.py
│   │   └── exception_handler.py
│   │
│   └── context_managers/
│       ├── __init__.py
│       └── export_session.py
│
└── output/
```

---

# Components

## `generator.py`

Responsible only for:

```text
Generating Products
```

It should use `yield` so products are generated lazily.

---

## `filter.py`

Responsible only for:

```text
Filtering Products
```

It should continue processing products without unnecessarily creating another large list.

---

## `exporter.py`

Responsible for:

```text
Exporting Products
```

It will use the context manager to safely manage the output file.

---

## `decorators/`

Contains the decorators created in Lesson 02:

```text
logger.py
timer.py
exception_handler.py
```

These provide cross-cutting functionality without putting monitoring code into the business logic.

---

## `context_managers/`

Contains the context manager created in Lesson 03.

```text
export_session.py
```

Its responsibility is:

```text
Open
 ↓
Provide File
 ↓
Cleanup
```

---

# Context Manager Design

We will use `@contextmanager` because the export resource lifecycle is simple.

Conceptually:

```python
@contextmanager
def export_session(filename):

    file = open(filename, "w")

    try:
        yield file

    finally:
        file.close()
```

The actual project implementation will include the required export behavior and error handling.

---

# Decorator Design

The export function will use the decorators learned in Lesson 02:

```python
@logger
@timer
@handle_errors
def export_products(...):
    ...
```

Each decorator has a separate responsibility.

```text
Logger
  ↓
Logging

Timer
  ↓
Performance

Exception Handler
  ↓
Error handling
```

---

# Combined Design

The final export operation will conceptually look like:

```python
@logger
@timer
@handle_errors
def export_products(products, filename):

    with export_session(filename) as file:

        for product in products:
            ...
```

This demonstrates the relationship between decorators and context managers.

```text
Function
   │
   ├── Decorators
   │      ├── Logging
   │      ├── Timing
   │      └── Error Handling
   │
   └── Context Manager
          ├── Open Resource
          ├── Use Resource
          └── Cleanup Resource
```

---

# Memory-Efficient Processing

The application should not do this:

```python
products = list(generate_products(100000))
filtered_products = list(filter_products(products))
```

because large datasets can consume significant memory.

Instead:

```text
Generator
    ↓
Generator Filter
    ↓
Export
```

Products should flow through the pipeline one at a time.

```text
Product 1 → Filter → Export
Product 2 → Filter → Export
Product 3 → Filter → Export
...
```

This preserves the main lesson from Lesson 01.

---

# Expected Output

A successful execution may look like:

```text
[LOG] Calling export_products
Starting export: output/products.txt
Export session closed
[TIMER] export_products took 0.015234 seconds
[LOG] Completed export_products

========================================
Export Summary
========================================
Products Generated : 10000
Products Exported  : 9900
Export Completed Successfully
========================================
```

The exact timing and product count will depend on the implementation.

---

# Error Scenario

The project should also handle an export failure.

For example, if the output operation fails:

```text
[LOG] Calling export_products
Starting export: output/products.txt
[ERROR] export_products failed: ...
Export session closed
[TIMER] export_products took 0.001234 seconds
Traceback ...
```

The important behavior is:

```text
Exception
    ↓
Context Manager Cleanup
    ↓
Timer Records Execution
    ↓
Exception Propagates
```

---

# Production Principles Demonstrated

This mini project demonstrates several important software-development principles.

## Separation of Concerns

Each component has one main responsibility.

```text
Generator
    → Data generation

Filter
    → Data filtering

Exporter
    → Business export logic

Decorators
    → Cross-cutting concerns

Context Manager
    → Resource lifecycle
```

---

## Resource Safety

Resources should always have a predictable lifecycle:

```text
Acquire
   ↓
Use
   ↓
Release
```

---

## Memory Efficiency

Generators allow large datasets to be processed without loading everything into memory.

---

## Reusability

The decorators and context manager can be reused by other parts of the application.

---

# What You Will Implement

We will build the project in the following stages:

```text
Stage 1
Create context manager
        ↓
Stage 2
Integrate context manager with exporter
        ↓
Stage 3
Combine decorators + context manager
        ↓
Stage 4
Integrate generator pipeline
        ↓
Stage 5
Test success + failure scenarios
        ↓
Stage 6
Final cleanup and documentation
```

---

# Completion Criteria

The mini project will be considered complete when:

* [ ] Products are generated using a generator.
* [ ] Products are filtered using generator-based processing.
* [ ] Products are exported successfully.
* [ ] `@contextmanager` manages the output file.
* [ ] File cleanup occurs even when an exception happens.
* [ ] Logger decorator works.
* [ ] Timer decorator works.
* [ ] Exception handler works.
* [ ] Decorators and context manager work together.
* [ ] Large datasets can be processed without creating unnecessary lists.
* [ ] Successful export is tested.
* [ ] Failed export is tested.
* [ ] Project structure is clean.

---

# Final Learning Outcome

After completing this project, you will have combined the major concepts from Part 3 so far:

```text
Lesson 01
Iterators & Generators
        ↓
Memory-efficient data processing
        ↓
Lesson 02
Decorators
        ↓
Logging + Timing + Error Handling
        ↓
Lesson 03
Context Managers
        ↓
Resource-safe processing
        ↓
Production-style Python Application
```

The final application will demonstrate not just individual Python features, but how these features can work together in a real application.

---

# Next Step

After reviewing this README, we will start:

**Stage 1 – Create the `export_session` context manager**

We will use the `@contextmanager` implementation you already created in Module 04 and integrate it into the project structure rather than writing another unrelated example.
