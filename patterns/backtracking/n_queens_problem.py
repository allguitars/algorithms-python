'''
6.1 N Queens Problem using Backtracking - Abdul Bari
https://youtu.be/xFv_Hl4B83A

Input: number of queens
Output: All possible solutions where the queens are not under attack.
        One solution is represented with a list

Every decision is for picking a column
There are four columns for 4 queens

** 其實這個問題一樣是 permutation! 不同的地方在於 base base 是 under attack (diagonal)
以 4 queens 來說，先對 0,1,2,3 找到所有排列方式。再把其中相鄰兩個數字只相差 1 的情況去掉，就是答案。
即:
[1, 3, 0, 2]
[2, 0, 3, 1]
'''

results = []


def solution(num):
    column_pool = list(range(num))  # [0,1,2,3]

    decision_path = []  # to store decisions up to the current node

    n_queens(num, decision_path, column_pool)


def n_queens(num, current_path, current_pool):

    # path which has at least two decisions / cols
    if len(current_path) > 1:
        # compare the last two decisions, check if they are at the same diagonal
        if is_diagonal(current_path[-1], current_path[-2]):
            # kill this path and then go back
            return

        # if they do not form a diagonal, then
        # check if we have reached the end node
        if len(current_path) == num:
            print(current_path)
            results.append(current_path)
            return

    # back up the path
    path_backup = current_path[:]

    # back up the pool (remaining cols)
    pool_backup = current_pool[:]

    for i in range(len(current_pool)):  # pool=[0,2] path=[1,3]
        choice = current_pool.pop(i)    # choice=[0] pool=[2]
        current_path.append(choice)     # [1,3,0] -> safe!

        n_queens(num, current_path, current_pool)

        # before moving on to the next col, we need restore
        # the path and pool.
        current_path = path_backup[:]
        current_pool = pool_backup[:]


def is_diagonal(first_col, second_col):
    '''
    if the difference between their col positions is euqal to 1, then
    the queens are at the same diagonal
    '''
    return abs(first_col - second_col) == 1


NUM_OF_QUEENS = 4
solution(NUM_OF_QUEENS)

print('Results:', results)
