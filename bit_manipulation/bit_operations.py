# & operator

# 3: 011
# 7: 111
# 3 & 7: 011
print('3 & 7:', 3 & 7)  # 3

# 4: 100
# 2: 010
# 4 & 2: 000
print('2 & 4:', 2 & 4)  # 0

# | operator

# 3: 011
# 7: 111
# 3 | 7: 111
print('3 | 7:', 3 | 7)  # 111-> 7

# 4: 100
# 2: 010
# 4 | 2: 110
print('2 | 4:', 2 | 4)  # 110 -> 6


# "and" is a logical operator
# The expression x and y first evaluates x; if x is false,
# its value is returned; otherwise, y is evaluated and
# the resulting value is returned.

print('3 and 7:', 3 and 7)  # 7
print('0 and 7:', 0 and 7)  # 0 <- 0 means false

# the "or" operator works opposite from the "and" operator
# x is true -> return x
# x is false -> return y
print('1 or 5:', 1 or 5)  # 1
print('0 or 5:', 0 or 5)  # 5
print('False or 5:', False or 5)  # 5

# "<<" operator
# 每 shift 一位元就像是乘以 2

print('1 << 1:', 1 << 1)  # 001 -> 010: 2
print('2 << 2:', 2 << 2)  # 010 -> 1000: 8
print('2 << 3:', 2 << 3)  # 010 -> 10000: 16
print('3 << 1:', 3 << 1)  # 011 -> 110: 6
print('7 << 1:', 7 << 1)  # 111 -> 1110: 14

# >>

print('4 >> 2:', 4 >> 2)  # 100 -> 001: 1

# ~ <- bitwise NOT: returns one’s complement

print('~1:', ~1)  # -(0001 + 1) = -(0010) = -2
print('~10:', ~10)  # ~1010 = -(1010 + 1) = -1011 = -11

# ^ <- bitwise XOR

print('10 ^ 4:', 10 ^ 4)  # 1010 XOR 0100 = 1110 = 14


# count set bits of an integer
# assume integers are represented using 32 bits
num = 75
print(bin(num).replace('0b', ''))  # 1001011: 4 1s and 28 0s

k1 = 0  # count of set bits
k0 = 0  # count of non-set bits

for i in range(0, 32):
    if num & (1 << i):
        k1 += 1
    else:
        k0 += 1

print(f'{k1} 1s and {k0} 0s')


# Bitwise OR multiple elements

# 001 | 001 | 011 -> 011
print('1 | 1 | 3:', 1 | 1 | 3)  # 3
# 0100 | 0101 | 1000 -> 1101
print('4 | 5 | 8:', 4 | 5 | 8)  # 13
