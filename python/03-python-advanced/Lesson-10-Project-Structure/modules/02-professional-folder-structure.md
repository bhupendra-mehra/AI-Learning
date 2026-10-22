# Module 2 – Professional Folder Structure

A common Python project can look like:

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
├── README.md
└── requirements.txt
```

Don't worry if this looks complicated.

The important idea is **separation of responsibility**.

---

