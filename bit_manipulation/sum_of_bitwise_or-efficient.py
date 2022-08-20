'''
Sum of Bitwise OR of all pairs in a given array
https://www.geeksforgeeks.org/sum-of-bitwise-or-of-all-pairs-in-a-given-array/

It can solve this problem in O(n) time.

The assumption here is that integers are represented using 32 bits.
The idea is to count number of set bits at every i'th position (i>=0 && i<=31).

Let k1 be the count of set bits at i'th position.
Total number of pairs with i'th set bit would be
k1C2 = k1*(k1-1)/2 (Count k1 means there are k1 numbers that have i'th set bit).
(C k1 取 2)

Every such pair adds 2i to total sum.
Similarly, there are total k0 values that don't have set bits at i'th position.
Now each element (which have not set the bit at the i'th position can make pair
with k1 elements (ie., those elements which have set bits at the i'th position), So
there are total k1 * k0 pairs and every such pair also adds 2i to total sum.

# Time: O(n * 32)
'''


def pair_or_sum(arr):
    n = len(arr)
    res = 0

    for i in range(0, 32):
        k0 = 0
        k1 = 0

        # count 1 and 0 for each number on bit i
        for j in range(0, n):
            if arr[j] & (1 << i):
                k1 += 1
            else:
                k0 += 1

        res = res + (1 << i) * (k1*(k1-1)//2) + (1 << i) * (k1*k0)

    return res


assert pair_or_sum([1, 2, 3, 4]) == 27
assert pair_or_sum([5, 10, 6, 4]) == 61
print('all tests have passed')
