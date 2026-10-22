# Module 16 – `requirements.txt`

`requirements.txt` records external Python dependencies.

Example:

```text
python-dotenv==1.1.1
requests==2.32.4
```

Install them with:

```bash
pip install -r requirements.txt
```

You can generate a dependency list from an environment with:

```bash
pip freeze > requirements.txt
```

However, `pip freeze` can include packages that your project doesn't actually need, so for production projects it's often better to intentionally manage dependencies rather than blindly committing an entire environment.

---

