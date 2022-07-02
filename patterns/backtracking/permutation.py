'''
Find all permutations for the input list

input: abc
results: abc, acb, bac, bca, cab, cba

There are totally 3! results.

#Backtracking
'''


def find_permutations(lst):
    permutation([], lst)


def permutation(path, lst):

    # base case: when it reaches the null node, the path variable
    # will contain all the decisions made along the path

    if not lst:
        print(path)
        return

    # back up the current state before making decision
    state_backup = lst[:]

    # back up the decision chain
    path_backup = path[:]

    # make decisions: pick a character at a time
    for i in range(len(lst)):
        choice = lst.pop(i)           # choice = 'a', lst = ['b', 'c']
        path.append(choice)           # path = ['a']

        permutation(path, lst)  # permutation(['a'], ['b', 'c'])

        # restore the state after returning from the recursive call

        lst = state_backup[:]         # lst = ['b', 'c']

        # we also need to restore the decision chain so that
        # it will not keep increasing

        path = path_backup[:]         # path = ['a']


SAMPLE = ['a', 'b', 'c']
find_permutations(SAMPLE)
