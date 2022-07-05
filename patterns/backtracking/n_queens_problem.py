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


def solution(n):
    cols_pool = [i for i in range(n)]

    path = []  # store all decisions along the path
    n_queens(path, cols_pool)


def n_queens(path, pool):

    if len(path) > 1:   # path has at least two decisions / cols
        if is_diagonal(path[-1], path[-2]):   # pick the last two decisions
            # kill this path and then go back
            return

        # if the last two decisions do not form a diagonal, then
        # check if we have reached the end of the path
        if len(path) == 4:
            print(path)
            results.append(path)
            return

    # back up the path
    path_backup = path[:]

    # back up the pool (remaining cols)
    pool_backup = pool[:]

    for i in range(len(pool)):  # pool=[0,2] path=[1,3]
        choice = pool.pop(i)  # choice=[0] pool=[2]
        path.append(choice)   # [1,3,0] -> safe!

        n_queens(path, pool)

        # before moving on to the next col, we need restore
        # the path and pool.
        path = path_backup[:]
        pool = pool_backup[:]


def is_diagonal(first_col, second_col):
    '''
    if the difference between their col positions is euqal to 1, then
    the queens are at the same diagonal
    '''
    return abs(first_col - second_col) == 1


NUM_OF_QUEENS = 4
solution(NUM_OF_QUEENS)

print('Results:', results)
