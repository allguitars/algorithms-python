'''
lists are quite slow for this purpose because inserting or deleting an element
at the beginning requires shifting all of the other elements by one,
requiring O(n) time.
'''

mylist = []

# enqueue using append()
mylist.append('a')
print(mylist)
mylist.append('b')
print(mylist)
mylist.append('c')
print(mylist)

# dequeue using pop()
front = mylist.pop(0)
print(front)
print(mylist)
front = mylist.pop(0)
print(front)
print(mylist)
front = mylist.pop(0)
print(front)
print(mylist)
