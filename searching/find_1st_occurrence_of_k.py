'''
Search Sorted Array For First Occurrence Of K
Principles of Binary Search & Reducing Search Space
#LeetCode

Back to Back SWE: https://youtu.be/gOkNq8Co6B8
'''


def first_occurrence_of_k(arr, k):
    left = 0
    right = len(arr)-1

    while left <= right:
        middle = (left + right) // 2

        # ** TRICK **
        # if hit, we need to look at the elem to the left as
        # this array is already sorted
        # there can be more the same elems
        if arr[middle] == k:
            # the neightbor to the left is also k
            # also check if the index is out of bound
            if middle-1 >= 0 and arr[middle-1] == k:
                right = middle - 1
            else:
                # the neightbor to the left is not k or it does not exist (out of bound)
                # meaning arr[middle] is the first occurrence
                # return the index
                return middle

        # below: normal binary search

        if arr[middle] < k:  # k is on the right hand side
            left = middle + 1

        if arr[middle] > k:  # k is on the left hand side
            right = middle - 1

    # if left and right have crossed each other
    return -1


# SAMPLE = [1, 1, 1, 1, 1, 5, 5, 6, 7, 11]
# k = 1
SAMPLE = [1, 1, 1, 1, 2, 5, 5, 6, 7, 11]
k = 2
print(first_occurrence_of_k(SAMPLE, k))
