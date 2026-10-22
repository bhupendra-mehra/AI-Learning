# Module 6 – Why `Optional` Matters

Consider an API:

```python
def get_customer_email(customer_id: int) -> str | None:
    ...
```

The caller now knows that the function may return:

```text
"customer@example.com"
```

or:

```text
None
```

So you should handle both:

```python
email = get_customer_email(101)

if email is not None:
    print(email)
else:
    print("Email not found")
```

This makes code safer and clearer.

---

