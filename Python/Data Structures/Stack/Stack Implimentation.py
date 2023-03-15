# If elements are added to a stack in the order [A,B,C,D,E], they will be removed in the order [E,D,C,B,A], assuming all the arrivals happened before the removals started.
# First in, Las out
from collections import deque

data = []

data.append('A')
data.append('B')
data.append('C')
data.append('D')
data.append('E')
# ['A', 'B', 'C', 'D', 'E']

data.pop()
# E removed
data.pop()
# D removed
data.pop()
# C removed
data.pop()
# B removed

print(data)

# OR
myStack = deque()

myStack.append('a')
myStack.append('b')
myStack.append('c')
myStack.append('d')
print(myStack)
#deque(['a', 'b', 'c'])

myStack.pop()
#'c'
myStack.pop()
#'b'
myStack.pop()
#'a'
print(myStack)