SIZE = 4

# create the game board
board = [['' for i in range(SIZE)] for j in range(SIZE)]

symbols = {
    'A': 'x',
    'B': 'o'
}


def move(player, coor):
    if is_valid(coor):
        # place the symbol
        board[coor['x']][coor['y']] = symbols[player]
        # print the new board
        print_board(board)
    else:
        print('This coor is not valid')

    # conditions for diagnols

    if coor['x'] == coor['y']:
        if check_left_diagonal(symbols[player]):
            print(player, 'wins')

    if coor['x'] + coor['y'] == SIZE - 1:
        if check_right_diagonal(symbols[player]):
            print(player, 'wins')

    # conditions for vertical and horizontal lines

    if check_horizontal(coor, symbols[player]) or check_vertical(coor, symbols[player]):
        print(player, 'wins')


def is_valid(coor):
    if board[coor['x']][coor['y']] != '':
        return False
    return True


def print_board(game_board):
    for i in range(SIZE):
        print(game_board[i])

    print('-----------------')


def check_horizontal(coor, symbol):
    for i in range(SIZE):
        if board[coor['x']][i] != symbol:
            return False

    return True


def check_vertical(coor, symbol):
    for i in range(SIZE):
        if board[i][coor['y']] != symbol:
            return False

    return True


def check_left_diagonal(symbol):
    for i in range(SIZE):
        if board[i][i] != symbol:
            return False
    return True


def check_right_diagonal(symbol):
    # (3,0) (2,1) (1,2) (0,3)
    for i in range(SIZE):
        if board[SIZE-1-i][i] != symbol:
            return False
    return True


move('B', {'x': 0, 'y': 3})
move('B', {'x': 1, 'y': 2})
move('B', {'x': 2, 'y': 1})
move('B', {'x': 3, 'y': 0})

# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)
# (3,0) (3,1) (3,2) (3,3)
