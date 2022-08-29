'''
Magic equation
'''

import math


def height(N):
    return math.ceil(math.log2(N + 1)) - 1


# number of nodes
N = 6
print(height(N))
