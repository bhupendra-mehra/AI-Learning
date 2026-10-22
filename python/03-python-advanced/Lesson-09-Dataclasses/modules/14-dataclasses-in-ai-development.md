# Module 14 – Dataclasses in AI Development

Dataclasses are useful when representing structured information.

For example:

```python
@dataclass
class Message:
    role: str
    content: str
```

Then:

```python
message = Message(
    role="user",
    content="Explain machine learning"
)
```

Or an AI agent task:

```python
@dataclass
class AgentTask:
    task_id: str
    description: str
    priority: int
    completed: bool = False
```

This gives you a clean structure for representing application data.

You'll encounter similar concepts when working with:

* API request/response models
* AI agent state
* Configuration
* Database records
* Data pipelines
* Structured application data

---

