'''
Using insertion process to create a new heap takes O(N log N) time.
If we just heapify the original array without needing another memory space, it 
will take only O(N) time.

heapq - Heap queue algorithm
This module provides an implementation of the heap queue algorithm, also 
known as the priority queue algorithm.

'''

import heapq as hq

lst = [10, 20, 15, 30, 40]

# 預設是轉換成 min heap
hq.heapify(lst)

print(lst)  # [10, 20, 15, 30, 40]

# push a new element
hq.heappush(lst, 13)
print(lst)  # [10, 20, 13, 30, 40, 15] <- auto adjusted to maintain a min heap

# Heap elements can be tuples. This is useful for assigning comparison values
# (such as task priorities) alongside the main record being tracked
h = []
hq.heappush(h, (5, 'write code'))
hq.heappush(h, (7, 'release product'))
hq.heappush(h, (1, 'write spec'))
hq.heappush(h, (3, 'create tests'))
print(hq.heappop(h))  # (1, 'write spec')

lst = [10, 20, 15, 30, 40]


# The following two functions perform best for smaller values of n.
# For larger values, it is more efficient to use the sorted() function.
# Note: 以下函式不需要先將 list heapify

# Return a list with the n largest elements
print(hq.nlargest(2, lst))  # [40, 30]
# Return a list with the n smallest elements
print(hq.nsmallest(3, lst))  # [10, 15, 20]
