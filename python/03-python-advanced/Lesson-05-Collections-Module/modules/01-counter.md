# Module 1 — `Counter`

`Counter` is used when you want to **count occurrences of items**.

Instead of:

```python
items = ["apple", "apple", "banana", "apple", "orange"]

counts = {}

for item in items:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

print(counts)
```

You can simply use:

```python
from collections import Counter

items = ["apple", "apple", "banana", "apple", "orange"]

counts = Counter(items)

print(counts)
```

Output:

```text
Counter({'apple': 3, 'banana': 1, 'orange': 1})
```

### Get a specific count

```python
print(counts["apple"])
```

Output:

```text
3
```

### Most common items

```python
print(counts.most_common(2))
```

Output:

```text
[('apple', 3), ('banana', 1)]
```

---

# `Counter` with Text

This is particularly useful for **text processing**, which makes it relevant to AI.

```python
from collections import Counter

text = "python is easy and python is powerful"

words = text.split()

word_count = Counter(words)

print(word_count)
```

Output:

```text
Counter({
    'python': 2,
    'is': 2,
    'easy': 1,
    'and': 1,
    'powerful': 1
})
```

Get the most common word:

```python
print(word_count.most_common(1))
```

Output:

```text
[('python', 2)]
```
