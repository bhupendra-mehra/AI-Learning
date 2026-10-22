# Module 7 — `ChainMap`

`ChainMap` allows you to combine multiple dictionaries and search them as one mapping.

```python
from collections import ChainMap

default_config = {
    "timeout": 30,
    "language": "en"
}

user_config = {
    "timeout": 60
}

config = ChainMap(user_config, default_config)

print(config["timeout"])
print(config["language"])
```

Output:

```text
60
en
```

The first dictionary has priority.

This pattern can be useful for configuration management.

---