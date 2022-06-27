'''
input: abcde  len: 5
-> abcd, e  [0:4] [4:5]
-> abc, de  [0:3] [3:5]
-> abc, de  [0:3] [3:5]
-> ab, cde  [0:2] [2:5]
-> a, bcde  [0:1] [1:5]

input: ab   len: 2
-> a, b  [0:1] [1:2]   range(1, 0, -1)

input: a   len: 1
-> [0, 0, -1] ->  this does not work
'''

# 印出兩次
for i in range(2, 0, -1):
    print(i)
    print('OK')

# 印出一次
for i in range(1, 0, -1):
    print(i)
    print('OK')

# Compile 不會報錯，但不會印出
for i in range(0, 0, -1):
    print(i)
    print('OK')

# 即使 end 比 start 還要大，也不會報錯。
# 它只會認定條件不符而不執行
for i in range(0, 5, -1):
    print(i)
    print('OK')
