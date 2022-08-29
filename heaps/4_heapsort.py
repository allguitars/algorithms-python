'''
Heap Sort is achieved with the insertion and removal process
'''


def get_bigger_child_idx(heap, i, j):
    if heap[i] > heap[j]:
        return i
    return j


def get_parent_idx(i):
    return (i-1) // 2


def get_left_child_idx(i):
    return i * 2 + 1


def get_right_child_idx(i):
    return i * 2 + 2


def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


def insert(heap, elem):
    heap.append(elem)

    if len(heap) > 1:
        current = len(heap) - 1
        parent = get_parent_idx(current)

        while parent >= 0:
            if heap[parent] < heap[current]:
                swap(heap, parent, current)
                current = parent
                parent = get_parent_idx(current)
            else:
                break


def pop(heap):
    if len(heap) == 1:
        return heap.pop()

    popped = heap[0]
    heap[0] = heap.pop()

    current = 0
    left = get_left_child_idx(current)
    right = get_right_child_idx(current)

    while left < len(heap) or right < len(heap):
        if left < len(heap) and right < len(heap):
            bigger_child_idx = get_bigger_child_idx(heap, left, right)
            if heap[current] < heap[bigger_child_idx]:
                swap(heap, current, bigger_child_idx)
                current = bigger_child_idx
                left = get_left_child_idx(current)
                right = get_right_child_idx(current)
            else:
                break

        if left < len(heap):
            if heap[left] > heap[current]:
                swap(heap, current, left)
            break

    return popped


unsorted_arr = [10, 20, 15, 30, 40]
heap = []

# First, insert these elements into the heap and adjust one by one
# Time: O(N log N)
for n in unsorted_arr:
    insert(heap, n)

# Second, pop the top element one by one followed by adjustment
# Time: O(N log N)
ascending = []
descending = []
while len(heap) > 0:
    elem = pop(heap)
    descending.append(elem)
    ascending.insert(0, elem)

print(ascending)
print(descending)
