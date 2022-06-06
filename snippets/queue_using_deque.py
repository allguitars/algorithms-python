'''
Deque is preferred over list in the cases where we need quicker append and
pop operations from both the ends of container, as deque provides an O(1) time
complexity for append and pop operations as compared to list which provides O(n)
time complexity.
'''

from collections import deque

# initialization
q = deque()

# addig elements
q.append('a')
print(q)
q.append('b')
print(q)
q.append('c')
print(q)

print(len(q))

# removing elements
front = q.popleft()
print(front)
print(q)
front = q.popleft()
print(front)
print(q)
front = q.popleft()
print(front)
print(q)

print(len(q))
