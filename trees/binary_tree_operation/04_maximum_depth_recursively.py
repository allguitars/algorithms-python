'''
https://favtutor.com/blogs/binary-tree-height

LeetCode 上的定義：
A binary tree's maximum depth is the number of 
nodes along the longest path from the root node down to the farthest leaf node.

利用 Recursion 求得樹高是 DFS 的概念
'''


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def height(root):

    # condition to stop the recursive call
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return 1 + max(left_height, right_height)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(height(root))      # 3
