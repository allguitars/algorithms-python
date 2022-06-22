# 面試的時候被問到 tic tac toe 的問題

size = 3

board = [['' for i in range(size)] for j in range(size)]

print(board)


arr = []

for i in range(3):         # 3 rows
    row = []

    for j in range(5):     # 5 cols for each row
        row.append('')

    arr.append(row)

print(arr)
