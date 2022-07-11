'''
Category:
Find the k'th largest/smallest item in a list/array.
Back to Back SWE: https://youtu.be/hGK_5n81drs

By QuickSort, this can be solved in O(N log N)
By Heap data structure, this can also be solve in O(N log N)

With this approach, we can solve it in linear time: O(N)
'''


def partition(lst, l, r):
    '''
    Once the partition finishes, the chosen pivot will be sitting at
    the final position in its sorted arrangement.
    '''
    # select the most left item as PIVOT
    pivot = lst[l]
    print('pivot:', pivot)
    # swap lst[l] and lst[r] to place the PIVOT on the right
    lst[l], lst[r] = lst[r], lst[l]

    # the iteration starts form the left
    i = j = l

    # r is where the pivot initially sits, we do not touch it
    while j < r:
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1  # only when swap happens do we need to advance i

        j += 1  # always advance j

    # i is now at the tail of the "less than pivot" section
    # so we place the pivot to i
    # - every item on the left hand side of the pivot is less than the pivot
    # - every item on the right hand side of the pivot is greater than the pivot
    lst[i], lst[r] = lst[r], lst[i]
    print('partioning finished:', lst)

    return i


def find(lst, l, r):
    '''
    As we are looking for the kth "largest" item, we do not
    care the items on the left hand side.
    Therefore, we just keep partitioning the right hand side.
    '''
    if l < r:
        p = partition(lst, l, r)
        find(lst, p+1, r)  # keep partitioning right hand side


def find_kth_largest(lst, k):
    '''
    client interface
    '''
    # the position where we pick the k'th largest item
    final_position = len(lst) - k  # the position of the kth largest item

    # initial partitioning range
    l, r = 0, len(lst)-1

    find(lst, l, r)

    # once the recursion ends, the result will be at the final_position
    return lst[final_position]


# lst = [3, 2, 1, 5, 6, 4]
# lst = [2, 3]
lst = [10, 20, 12, 23, 54, 67, 13, 34, 88, 102, 63, 79, 2, 57, 99]
k = 2
# k = 4

print(find_kth_largest(lst, k))

# TODO: this solutio does not handle the case where k is less than
# n-k
# 目前的方法都一直針對每一回合的右半邊做 partition
# 所以只要 k 夠大，n-k 可能就會落在沒有被排序好的那一邊。
# 例如：當 k=4 時，必須要回傳第4大的項目，最後一輪的 partition 為
# pivot: 102
# partioning finished: [2, 10, 12, 20, 13, 23, 34, 54, 67, 63, 79, 57, 88, 99, 102]
# 57

# 因為有一次 pivot 挑的是 88，pivot 擺定之後，88 左邊確實都比 88小，
# 但其實沒有排序，如 57 仍擺在 79 的右邊，位於 n-k 的位置。
# 結果會回傳 57，但 57 不是第 4 大的項目。
