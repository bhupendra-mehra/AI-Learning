# Module 20 – Recommended Project Structure

For the level you're currently reaching, use this as a practical structure:

```text
order-processing/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── order.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── order_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── tests/
│   ├── __init__.py
│   └── test_orders.py
│
├── .env
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── README.md
```

The important separation is:

```text
config   → configuration
models   → data structures
services → business logic
utils    → reusable generic helpers
tests    → tests
main.py  → application entry point
```

---

