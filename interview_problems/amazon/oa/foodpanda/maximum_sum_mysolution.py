'''
My solution: It does no

Question1: Given an array A consisting of N integers, returns the maximum sum of
"two" numbers whose digits add up to an equal sum.
if there are not two numbers whose digits have an equal sum, the function should
return -1.
Constraints: N is integer within the range [1, 200000]
each element of array A is an integer within the range [1, 1000000000]

Example1:
Input:
A = [51, 71, 17, 42]
Output: 93
Explanation: There are two pairs of numbers whose digits add up to an
equal sum: (51, 42) and (17, 71), The first pair sums up to 93

Example2:
Input:
A = [42, 33, 60]
Output: 102
Explanation: The digits of all numbers in A add up the same sum, 6, and
choosing to add 42 and 60 gives the result 102

Example3:
Input:
A = [51, 32, 43]
Output: -1
Explanation: All numbers in A have digits that add up to different, unique sums

我的 solution 沒有考慮到三位以上的數字，只能針對二位數。

'''
from collections import defaultdict


def solution(nums):
    mapping = defaultdict(list)
    res = -1

    for n in nums:
        digit_sum = (n // 10) + (n % 10)
        mapping[digit_sum].append(n)

    for sum, lst in mapping.items():
        if len(lst) >= 2:
            lst.sort()
            sum = lst[-1] + lst[-2]
            res = max(res, sum)

    return res


# nums = [51, 71, 17, 42]
# nums = [42, 33, 60]
# nums = [51, 32, 43]
nums = []
print(solution(nums))
