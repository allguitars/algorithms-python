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

Time: O(n * k) -- k 為數字的位數
'''


def digit_sum(n):  # Time: O(k) -- k digits
    current = 0
    while n > 0:
        temp = n % 10
        current += temp
        n = n // 10
    return current


def solution(nums):  # Time O(n * k)
    mapping = {}
    res = -1

    for num in nums:
        temp_sum = digit_sum(num)

        # 如果第一次出現這個 digit sum, 將該數字加到 map 中 {digit_sum: num}
        if temp_sum not in mapping:
            mapping[temp_sum] = num
        else:
            # if the digit sum already exists in the hashmap, then add up the
            # two numbers and compare with result
            # update result to a greater one
            # result 負責存放目前最大的數字和  不在乎是屬於哪個位數和
            res = max(res, num + mapping[temp_sum])

            # always keep the maximum number in the map
            # result 永遠會是當下最大的和  又 map 中永遠是目前最大的數字
            # 所以除非出現更大的數字  不然 result 不會被打敗
            mapping[temp_sum] = max(mapping[temp_sum], num)

    return res


nums = [51, 71, 17, 42]
# nums = [42, 33, 60]
# nums = [51, 32, 43]
# nums = []
print(solution(nums))
