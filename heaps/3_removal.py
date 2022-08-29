'''
This is an removal demo for Max Heap

    40
   /  \
  30  15
 / \
10 20

每次都必須取走最頂端的元素 -> 故每一次從 Max heap pop out 的都是最大元素  Min heap 則是最小元素
取走之後，把最後一個元素放到最頂端的位置。
然後再 heapify。

每次 adjust time: O(log N)
'''


def get_bigger_child_idx(heap, i, j):
    if heap[i] > heap[j]:
        return i
    return j


def get_left_child_idx(i):
    return i * 2 + 1


def get_right_child_idx(i):
    return i * 2 + 2


def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]


def pop(heap):
    if len(heap) == 1:
        return heap.pop()

    # >>> 以下是 heap 剩餘兩個元素以上的處理

    # 先取出頂端的元素，最後要用來 return
    popped = heap[0]

    # 將最後一個元素放到頂端，然後再做調整。
    heap[0] = heap.pop()

    current = 0
    left = get_left_child_idx(current)
    right = get_right_child_idx(current)

    # >>> 開始做調整

    # 至少有一個 child -> 表示還沒到達底部
    while left < len(heap) or right < len(heap):
        # 有左右兩個 child  跟比較大的 child 對調
        if left < len(heap) and right < len(heap):
            bigger_child_idx = get_bigger_child_idx(heap, left, right)  # 找比較大的 child
            if heap[current] < heap[bigger_child_idx]:
                swap(heap, current, bigger_child_idx)
                # update indexes to the deeper level
                current = bigger_child_idx
                left = get_left_child_idx(current)
                right = get_right_child_idx(current)
            else:
                break  # 沒有互換，則不需要在往底部調整。

        # 只有一個 child (因為是 complete binary tree, 所以一定是 left child)
        if left < len(heap):
            if heap[left] > heap[current]:
                swap(heap, current, left)

            # 已經到底了  所以也不需要再更新 index 往下探尋
            break

    return popped


heap = [40, 30, 15, 10, 20]

while len(heap) > 0:
    elem = pop(heap)
    print(elem)
