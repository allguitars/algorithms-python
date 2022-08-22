'''
2022/06/23

LeetCode: 437. Path Sum III
https://leetcode.com/problems/path-sum-iii/

一個二元樹  每個樹的節點都是數字  數字可以是正數或負數
給定一個數字  找到所有路徑  路徑上所有節點的數字加起來等於這個數字
路徑只能由上往下  不一定從根節點開始
回傳符合這種路徑的數目
target number: 8 (加起來為 8)

         10
        /  \
       5   -3
      / \    \
     3   2    11
    / \
   3  -2

可能路徑：[-3, 11], [5, 3]
'''


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        # left subtree
        if self.left:
            self.left.print_tree()

        # current node
        print(self.data)

        # right subtree
        if self.right:
            self.right.print_tree()


root = Node(10)
root.left = Node(5)
root.right = Node(-3)
root.left.left = Node(3)
root.left.right = Node(2)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)
root.right.right = Node(11)

# root.print_tree()

count = 0
target = 8


# def count_paths(total, node):
#     if node:
#         print('current total:', total)

#         print('current value', node.data)

#         new_total = total + node.data

#         print('new total:', new_total)

#         if new_total == target:
#             count += 1
#             print('count', count)

#         count_paths(node.data, node.left)
#         count_paths(node.data, node.right)

lst = []
res = []


def dfs(node):
    global lst

    if node:
        lst.append(node.data)

        # memoize the current state
        current = []
        for n in lst:
            current.append(n)

        res.append(current)

        if node.left:
            dfs(node.left)

        # after left subtree, restore to the current state
        lst = []
        for n in current:
            lst.append(n)

        if node.right:
            dfs(node.right)


dfs(root)
print(res)


#          10
#         /  \
#        5   -3
#       / \    \
#      3   2    11
#     / \
#    3  -2
