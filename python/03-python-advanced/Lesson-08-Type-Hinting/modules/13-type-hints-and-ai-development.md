# Module 13 – Type Hints and AI Development

Type hints become particularly useful when working with frameworks such as:

* FastAPI
* Pydantic
* OpenAI SDK
* LangChain
* Data processing libraries

For example, an API function might look like:

```python
def get_order(
    order_id: int
) -> dict[str, str | float]:
    ...
```

The expected input and output are immediately visible.

This improves:

* Readability
* IDE autocomplete
* Error detection
* API documentation
* Refactoring
* Maintainability

---

