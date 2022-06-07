
'''
https://www.stechies.com/python-infinity/

- In Python, there is no way or method to represent infinity as an integer
- Positive infinity number is greatest, and the negative infinity number is 
the smallest of all numbers.
- In comparison, positive infinity is always bigger than every natural number.
- In comparison, negative infinity is smaller than the negative number.
'''

from cmath import inf
import math

# 1. use float()

positive_inf = float('inf')
negative_inf = float('-inf')

print(positive_inf)
print(negative_inf)
inf

# 2. use math module

POSITIVE_INF = math.inf
NEGATIVE_INF = -math.inf

print(POSITIVE_INF)
print(NEGATIVE_INF)


print(999999999999999999999999 < POSITIVE_INF)   # true
print(-999999999999999999999999 > NEGATIVE_INF)  # true

print(999999999999999999999999 < positive_inf)   # true
print(-999999999999999999999999 > negative_inf)  # true
