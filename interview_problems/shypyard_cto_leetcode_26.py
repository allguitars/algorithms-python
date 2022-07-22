'''
Interview with the CTO at Shypyard
LeetCode: 26. Remove Duplicates from Sorted Array

Given a sorted array *nums*, remove the duplicates in-place such that each element
appears only *once* and returns the new length.

Do not allocate extra space for another array, you must do this by **modifying the
input array in-place with O(1) extra memory.

Note that the return value is a number. And the array is simply modified in-place.
Only the first N numbers are un-duplicated, and the rest of the array does not matter.

Example:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,...] (it doens't matter what numbers are after the first 5)

for the for N numbers, they will be unique
'''


def unduplicate(arr):
    l = 1

    for r in range(1, len(arr)):
        if arr[r] != arr[r-1]:
            arr[l] = arr[r]
            l += 1

    return l


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums = [1, 2, 3, 4, 5]
print(unduplicate(nums))
