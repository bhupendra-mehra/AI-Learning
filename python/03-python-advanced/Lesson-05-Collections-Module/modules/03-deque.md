# Module 5 — `deque`

`deque` means **double-ended queue**.

It allows efficient insertion and removal from both ends.

```python
from collections import deque

queue = deque()

queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

print(queue)
```

Output:

```text
deque(['Task 1', 'Task 2', 'Task 3'])
```

Remove from the left:

```python
task = queue.popleft()

print(task)
print(queue)
```

Output:

```text
Task 1
deque(['Task 2', 'Task 3'])
```

Add to the left:

```python
queue.appendleft("Urgent Task")

print(queue)
```

Output:

```text
deque(['Urgent Task', 'Task 2', 'Task 3'])
```

### Why `deque` matters

It's useful for:

* Queues
* Task processing
* Request processing
* Sliding windows
* BFS algorithms
* AI agent task queues

---