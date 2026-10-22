# Mini Project – Function Monitoring Framework

## Overview

This project enhances the **Large Product Export Simulator** created in Lesson 01 by adding a reusable function monitoring layer using Python decorators.

The application will continue to generate, filter, and export products, but decorators will now provide additional functionality such as logging, execution-time measurement, and centralized exception handling without modifying the core business logic.

This demonstrates how decorators can be used in a production-style Python application.

---

# Objectives

By completing this project, you will learn how to:

* Apply decorators to an existing application.
* Separate monitoring logic from business logic.
* Log function execution.
* Measure execution time.
* Handle exceptions centrally.
* Stack multiple decorators.
* Preserve function metadata.
* Build reusable infrastructure components.

---

# Features

## 1. Function Logging

The application will log:

```text
[LOG] Calling generate_products
[LOG] Completed generate_products
```

This allows developers to understand which functions are being executed.

---

## 2. Execution Time Monitoring

The application will measure how long important operations take.

Example:

```text
[TIMER] generate_products took 0.002341 seconds
```

This can help identify performance bottlenecks.

---

## 3. Centralized Exception Handling

Errors occurring inside monitored functions can be captured and logged consistently.

Example:

```text
[ERROR] export_products failed: File not found
```

---

## 4. Decorator Stacking

Multiple decorators can be applied to the same function:

```python
@logger
@timer
@handle_errors
def export_products():
    ...
```

This demonstrates how decorators can work together.

---

## 5. Business Logic Remains Clean

The product-generation logic will remain focused on generating products.

Instead of adding:

```python
print(...)
timer...
try...
except...
```

inside every function, decorators handle those concerns externally.

---

# Architecture

```text
                    main.py
                       │
                       ▼
              generate_products()
                       │
                ┌──────┴──────┐
                │             │
              Logger         Timer
                │             │
                └──────┬──────┘
                       ▼
                 filter_products()
                       │
                       ▼
                 export_products()
                       │
                       ▼
                  Output File
```

Decorators provide monitoring around the application's business functions.

---

# Project Flow

```text
Start
  │
  ▼
Generate Products
  │
  ├── Logging
  └── Timing
  │
  ▼
Filter Products
  │
  ├── Logging
  └── Timing
  │
  ▼
Export Products
  │
  ├── Logging
  ├── Timing
  └── Error Handling
  │
  ▼
Display Statistics
  │
  ▼
Complete
```

---

# Folder Structure

```text
mini-project/
│
├── README.md
├── main.py
│
├── src/
│   │
│   ├── generator.py
│   ├── filter.py
│   ├── exporter.py
│   ├── statistics.py
│   │
│   └── decorators/
│       ├── __init__.py
│       ├── logger.py
│       ├── timer.py
│       └── exception_handler.py
│
├── output/
│   └── products.txt
│
└── requirements.txt
```

---

# Decorator Components

## logger.py

Responsible for:

* Logging function start.
* Logging function completion.
* Identifying the function name.

---

## timer.py

Responsible for:

* Recording start time.
* Recording end time.
* Calculating execution duration.

---

## exception_handler.py

Responsible for:

* Catching exceptions.
* Logging errors.
* Re-raising exceptions when appropriate.

---

# Example

Without decorators:

```python
def export_products(products):

    print("[LOG] Starting export")

    start = time.perf_counter()

    try:
        # Export logic
        ...
    except Exception as error:
        print(error)

    end = time.perf_counter()

    print(f"Time: {end - start}")
```

The business function becomes cluttered.

With decorators:

```python
@logger
@timer
@handle_errors
def export_products(products):
    ...
```

The function contains only its actual export logic.

---

# Expected Output

Example:

```text
[LOG] Calling generate_products
[TIMER] generate_products took 0.004321 seconds
[LOG] Completed generate_products

[LOG] Calling filter_products
[TIMER] filter_products took 0.001245 seconds
[LOG] Completed filter_products

[LOG] Calling export_products
[TIMER] export_products took 0.008731 seconds
[LOG] Completed export_products

==================================================
Export Summary
==================================================
Products Generated : 10000
Products Exported  : 782

Export Completed Successfully
==================================================
```

Execution times and exported counts will vary.

---

# Concepts Demonstrated

This project combines the concepts learned in Lesson 02:

* Functions as first-class objects
* Nested functions
* Closures
* Decorators
* Wrapper functions
* `*args`
* `**kwargs`
* `functools.wraps`
* Decorator stacking
* Exception handling
* Performance measurement
* Separation of concerns

---

# Production Concepts

This project introduces an important software engineering principle:

## Separation of Concerns

Business logic:

```text
Generate
Filter
Export
```

Infrastructure logic:

```text
Logging
Timing
Error Handling
```

Decorators keep these responsibilities separate.

---

# Future Improvements

This framework can later be extended with:

* File-based logging.
* Log levels.
* Retry decorators.
* Authentication decorators.
* Permission decorators.
* Caching decorators.
* Metrics collection.
* Database monitoring.
* API request monitoring.
* Async function support.

These concepts will become particularly useful when we reach FastAPI and AI application development.

---

# Completion Criteria

The mini project is complete when:

* Logging decorator works.
* Timer decorator works.
* Exception handling decorator works.
* Decorators are applied to project functions.
* Multiple decorators work together.
* Function metadata is preserved.
* Product export still works.
* Output is generated successfully.
* Monitoring logic is separated from business logic.

---

# Final Outcome

The Lesson 01 application:

```text
Large Product Export Simulator
```

will become:

```text
Monitored Product Export Framework
```

The application will still perform the same business operations, but it will now have reusable monitoring capabilities implemented using Python decorators.
