'''
Category:
Find the k'th largest/smallest item in a list/array.
Back to Back SWE: https://youtu.be/hGK_5n81drs
#LeetCode

By QuickSort, this can be solved in O(N log N)
By Heap data structure, this can also be solve in O(N log N)

With this approach, we can solve it in linear time: O(N)
Time 計算方式看筆記
'''


import random


def partition(arr, left, right, pivot_index):
    '''
    Once the partition finishes, the chosen pivot will be sitting at
    the final position in its sorted arrangement.
    '''
    pivot_value = arr[pivot_index]
    print('pivot:', pivot_value)
    lesser_items_tail_index = left

    # swap arr[pivot_index] and arr[right] to temporarily store the PIVOT at the right bound
    swap(arr, pivot_index, right)

    # 這個寫法比我原本用 i and j 兩個 pointer 搭配 while loop 的方式好多了，因為：
    # i in range 就會在每次 iterate 自動＋1，不需要多寫一行。若是用 while loop 則要自己控制 pointer 迭代。
    # the iteration starts from the left and ends before hitting the right bound
    for i in range(left, right):
        # 如果 i 位置的項目小於 pivot，表示他應該放在 pivot 的左邊。而 tail 是最後 pivot 的家，即 sorted position。
        if arr[i] < pivot_value:
            swap(arr, i, lesser_items_tail_index)
            lesser_items_tail_index += 1

    # 此時 tail 左邊的項目都會小於 pivot，故把 pivot 替換到這個位置。
    swap(arr, lesser_items_tail_index, right)

    # 在這個時間點，在 pivot 左邊的項目都會比 pivot 小（即使沒有左半部沒有 sorted）
    # 而在 pivot 右邊的項目都會比 pivot 大
    # ** 意思就是 -- PIVOT 已經位於 SORTED 位置(最終位置)，在整個陣列排序完成之前它都不會再變動位置了。**

    print('partioning finished:', arr, '\n')
    return lesser_items_tail_index  # 回傳分割點（pivot最後所在位置）


def find_kth_largest(arr, k):
    '''
    call partition function recursively
    '''
    n = len(arr)
    left = 0
    right = n-1
    kth_largest_item_index = n - k

    while left <= right:
        chosen_pivot_index = random.randint(left, right)  # randomly pick an item as the pivot

        sorted_position_for_chosen_pivot = partition(arr, left, right, chosen_pivot_index)

        # sorted position 剛好落在 n-k，而 sorted postion 即表示這個位置的項目已在最終位置，
        # 不會再被移動，那這個項目就剛好就是我們要的 item。
        if sorted_position_for_chosen_pivot == kth_largest_item_index:
            return arr[sorted_position_for_chosen_pivot]

        if(sorted_position_for_chosen_pivot > kth_largest_item_index):
            # 如果 sorted pivot 位於 kth_largest_item_index 的右邊，表示我們 overshot!
            # 那就針對 sorted pivot 左半邊去做 partition
            # so we go left by narrowing the right bound
            right = sorted_position_for_chosen_pivot-1

        else:
            # sorted postition 位在 kth_largest_item_index 的左邊，表示接下來要關注右半部。
            left = sorted_position_for_chosen_pivot+1

    # 如果到最後都沒有集中 n-k
    return -1


def swap(arr, first_idx, second_idx):
    '''
    swap two elements in an arr
    '''
    arr[first_idx], arr[second_idx] = arr[second_idx], arr[first_idx]


# lst = [3, 2, 1, 5, 6, 4]
# lst = [2, 3]
lst = [10, 20, 12, 23, 54, 67, 13, 34, 88, 102, 63, 79, 2, 57, 99]
# kth = 2
kth = 4

print('Result:', find_kth_largest(lst, kth))
