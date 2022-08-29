'''
Max Heap:

       50
      /  \
    30    20
   /  \   / \
  15  10 8  16

Min Heap:
  
       10
      /  \
    30    20
   /  \   / \
  35  40 32 25

'''


def left_child_idx(i):
    return i * 2 + 1


def right_child_idx(i):
    return i * 2 + 2


def parent_idx(i):
    return (i-1) // 2


#          0   1   2   3   4   5  6
maxHeap = [50, 30, 20, 15, 10, 8, 16]
minHeap = [10, 30, 20, 35, 40, 32, 25]

# For the Max Heap example
# left child of 30 -> 15
assert maxHeap[left_child_idx(1)] == 15
# right child of 30 -> 10
assert maxHeap[right_child_idx(1)] == 10
# parent of 30 -> 50
assert maxHeap[parent_idx(1)] == 50
# parent of 8 -> 20
assert maxHeap[parent_idx(5)] == 20
