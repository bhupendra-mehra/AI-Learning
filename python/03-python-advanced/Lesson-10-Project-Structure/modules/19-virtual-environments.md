# Module 19 – Virtual Environments

Each project should ideally have its own environment.

Create one:

```bash
python -m venv .venv
```

Activate on Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Then install dependencies:

```bash
pip install python-dotenv
```

The benefit is that different projects can use different package versions without interfering with each other.

---

