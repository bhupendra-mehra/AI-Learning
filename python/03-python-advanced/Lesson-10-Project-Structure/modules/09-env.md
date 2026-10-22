# Module 9 – `.env`

During local development, you may use a `.env` file:

```text
API_KEY=my-development-key
DATABASE_URL=mysql://localhost/orders
DEBUG=true
```

A popular package for loading `.env` values is:

```text
python-dotenv
```

Install:

```bash
pip install python-dotenv
```

Then:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
```

Important:

**Do not commit real secrets to Git.**

Your `.env` should normally be included in `.gitignore`.

---

