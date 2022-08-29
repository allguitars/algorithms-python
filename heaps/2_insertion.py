'''
This is an insertion demo for Max Heap

Input array: [10, 20, 15, 30, 40]
Insert these elements into the heap one by one:
    10

    20
   /
  10

   20
  /  \
 10  15
  
    30
   /  \
  20  15
 /
10

    40
   /  \
  30  15
 / \
10 20


有 N 個元素必須 insert 到 heap
每 insert 一次需要花 log N 時間做調整
故整體時間 O(N log N)
'''


def insert(heap, elem):
    # new element is always appended to the end
    heap.append(elem)

    # if there is more than one elements, then do Adjustment
    if len(heap) > 1:
        current = len(heap) - 1               # index of the new element
        parent = get_parent_idx(current)      # parent index

        while parent >= 0:
            if heap[parent] < heap[current]:
                swap(heap, parent, current)

                # do not forget to update the current index since we have "lifted"
                # the new element
                current = parent
                parent = get_parent_idx(current)
            else:
                break


def get_parent_idx(i):
    return (i-1) // 2


def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


arr = [10, 20, 15, 30, 40]
heap = []

for n in arr:
    insert(heap, n)
    print(heap)
