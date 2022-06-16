from collections import deque

mylist = [1, 2, 3, ]

q = deque(mylist)
print(q)

print(q.popleft())
print(q)

print(q.popleft())
print(q)

print(q.popleft())
print(q)
