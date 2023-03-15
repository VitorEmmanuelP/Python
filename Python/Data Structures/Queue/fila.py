#In a line (or queue) at a bank, the first person to arrive is the first person to be served. When using a queue to store data, the first elements in are the first elements out.
# First in, First Out
from collections import deque
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
# ['a', 'b', 'c','d']
print(queue)

# Removing elements from the queue
# Elements dequeued from queue")
queue.pop(0)
queue.pop(0)
queue.pop(0)

# Queue after removing elements")
print(queue)

# Or

q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
q.append('d')
# deque(['a', 'b', 'c','d'])

print(q)

# Removing elements from a queue
# Elements dequeued from the queue"
q.popleft()
q.popleft()
q.popleft()

print("\nQueue after removing elements")
print(q)