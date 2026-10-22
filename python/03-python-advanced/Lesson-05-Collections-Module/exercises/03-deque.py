from collections import deque

queue = deque()

queue.append("Task 1")
queue.append("Task 2")
queue.append("Task 3")

print(queue)


task = queue.popleft()
print(f"Removing queue: {task}")    
print(f"Update queue: {queue}")

newleft = queue.appendleft("Task 0") #will return None
print(f"Adding to left: {newleft}")    
print(f"Update queue: {queue}")     

newright = queue.append("Task 4") #will return None
print(f"Adding to right: {newright}")
print(f"Update queue: {queue}")

task = queue.pop()
print(f"Removing from right: {task}")
print(f"Update queue: {queue}")