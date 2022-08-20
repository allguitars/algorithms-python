'''
Sum of Bitwise OR of all pairs in a given array
https://www.geeksforgeeks.org/sum-of-bitwise-or-of-all-pairs-in-a-given-array/

Given an array “arr[0..n-1]” of integers. The task is to calculate the
sum of Bitwise OR of all pairs, i.e. calculate the sum of “arr[i] | arr[j]”
for all the pairs in the given array where i < j.
Here | is a bitwise OR operator.

The expected time complexity is O(n).
'''


def pair_or_sum(arr):
    n = len(arr)
    res = 0

    for i in range(0, n):
        for j in range(i+1, n):
            res = res + (arr[i] | arr[j])

    return res


assert pair_or_sum([1, 2, 3, 4]) == 27
assert pair_or_sum([5, 10, 6, 4]) == 61
print('all tests have passed')
