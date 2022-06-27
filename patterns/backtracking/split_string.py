'''
將 abcde 分成數堆，每堆的字元數目不固定，但字元的順序保持固定。
例如分成 1, 4 -> 'a', 'bcde'
分成 2, 3 -> 'ab', 'cde'
或是 1, 2, 2 -> 'a', 'bc', 'de'
將所有可能性列出。

可以用 decision tree 配合 backtracking 紀錄每個結點的狀態

Slicing the string into two parts:

>> 由大切到小
input: abcde  len: 5 -> range(4, 0, -1) -> 有四種切法
-> abcd, e  [0:4] [4:5]
-> abc, de  [0:3] [3:5]
-> ab, cde  [0:2] [2:5]
-> a, bcde  [0:1] [1:5]

>> 由小切到大
input: abcde  len: 5 -> range(1, 5) -> 有四種切法
-> a, bcde  [0:1] [1:5]
-> ab, cde  [0:2] [2:5]
-> abc, de  [0:3] [3:5]
-> abcd, e  [0:4] [4:5]

input: ab   len: 2 -> range(1, 2) -> 只有一種切法
-> a, b  [0:1] [1:2]

input: a   len: 1
-> [0, 0, -1] ->  this does not work
so we need to handle special case for the string with length one

'''

results = []


def split_string(s):
    split_helper([], s)


def split_helper(previous_slicing_chain, current):

    # print the path so far
    path = []

    for item in previous_slicing_chain:
        path.append(item)

    # add the end node to create the whole path
    # this end node could be in the middle of the decision tree
    path.append(current)

    # append the path to the result (a list of list)
    results.append(path)

    # >>> BACKTRACKING:
    # create a copy of the chain to store the chain for current node for restoring later
    # For the first round, it would be an empty list as we haven't made any decision
    previous_chain_backup = []
    for item in previous_slicing_chain:
        previous_chain_backup.append(item)

    # *** Split the string into two parts gradually ***

    if len(current) > 1:
        for cut_point in range(1, len(current)):
            # Split the string into two parts
            slicing = current[0:cut_point]            # next slicing decision
            rest = current[cut_point:len(current)]    # rest string -> value for the child node

            previous_slicing_chain.append(slicing)    # chain for the child node

            split_helper(previous_slicing_chain, rest)   # continue to the next level

            # >>> BACKTRACKING:
            # restore the backup for the preivous slicing chain so that
            # we can make a new starting point for the next subtree
            previous_slicing_chain = []
            for item in previous_chain_backup:
                previous_slicing_chain.append(item)


SAMPLE = 'abcde'
split_string(SAMPLE)

for result in results:
    print(result)
