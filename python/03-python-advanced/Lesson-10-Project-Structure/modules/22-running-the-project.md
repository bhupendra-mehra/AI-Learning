# Module 22 – Running the Project

From the project root:

```bash
python -m app.main
```

Using:

```bash
python -m app.main
```

is useful because Python treats `app` as a package and resolves imports consistently.

You should see logs similar to:

```text
INFO - Processing order ORD1001
INFO - Order ORD1001 processed successfully
INFO - Processing order ORD1002
INFO - Order ORD1002 processed successfully
INFO - Processing order ORD1003
INFO - Order ORD1003 processed successfully
```

Then:

```text
Orders:

ORD1001 Bhupendra Mehra ₹120,000.00 processed
ORD1002 Rahul ₹1,500.00 processed
ORD1003 Amit ₹5,000.00 processed

Grouped by category:

Electronics → ['ORD1001', 'ORD1002']
Fashion → ['ORD1003']
```

---

