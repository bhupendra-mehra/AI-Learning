## Review of Your Answers

### 1. Why does `handle_errors` need `raise`?

Your answer:

> will return None

That's actually the result **if you don't use `raise`**.

Better answer:

> `raise` re-raises the caught exception so the caller can still detect and handle the error. Without `raise`, if the `except` block has no return value, the decorator returns `None`.

---

### 2. What happens if we replace `raise` with `return None`?

Your answer:

> Then it will not show trace

✅ **Mostly correct.**

More precisely:

> The exception is swallowed by the decorator, the caller receives `None`, and the original exception traceback is not propagated to the caller.

So:

```python
except Exception as error:
    print(error)
    return None
```

results in:

```text
Error: division by zero
None
```

Whereas:

```python
except Exception as error:
    print(error)
    raise
```

allows the exception to propagate.

---

### 3. Which decorator executes first at runtime?

Your answer:

> logger

✅ Correct.

For:

```python
@logger
@timer
@handle_errors
def divide():
```

the runtime flow starts with:

```text
logger
   ↓
timer
   ↓
handle_errors
   ↓
divide()
```

This distinction is important:

**Decoration order:**

```text
handle_errors
      ↓
timer
      ↓
logger
```

**Runtime execution:**

```text
logger
   ↓
timer
   ↓
handle_errors
   ↓
divide
```

---

### 4. Why should each decorator return the wrapped function's result?

Your answer:

> because then only we can bind all decorator with function

The idea is close, but the important reason is **preserving the original function's behavior**.

Better answer:

> Each decorator should return the wrapped function's result so that the decorated function continues to produce the same output as the original function. This also allows multiple decorators to be chained correctly.

For example:

```python
result = function(*args, **kwargs)
return result
```

---

### 5. What is the purpose of `@wraps`?

Your answer:

> to provide the exact function used

You're thinking in the right direction, but let's make it precise.

Better answer:

> `@wraps` preserves the original function's metadata, such as its name, docstring, module, and other attributes, instead of replacing them with the wrapper's metadata.

Without it:

```python
print(add.__name__)
```

could give:

```text
wrapper
```

With it:

```text
add
```

---

# Lesson 02 — Knowledge Status

```text
Lesson 02 – Decorators

✅ Module 01 – Why Decorators
✅ Module 02 – Nested Functions
✅ Module 03 – Closures
✅ Module 04 – Building Decorators
✅ Module 05 – Advanced Decorators
✅ Module 06 – Production Decorators
✅ Practical Exercise
```

You've now covered the complete decorator concept from **basic → advanced → production usage**.

---

# Now: Lesson 02 Mini Project

As we agreed earlier, we'll now take your **Lesson 01 Large Product Export Simulator** and improve it rather than creating an unrelated project.

The project will become:

## Function Monitoring Framework

We'll add:

```text
Large Product Export Simulator
          │
          ├── Logging
          │
          ├── Execution Timing
          │
          ├── Exception Handling
          │
          └── Function Monitoring
```

Before we start coding, following our agreed workflow, I'll first give you the **Mini Project README** containing:

* Project overview
* Objectives
* Features
* Architecture
* Folder structure
* Implementation stages
* Expected output
* Concepts demonstrated

Then we'll build it module by module without unnecessary exercises.
