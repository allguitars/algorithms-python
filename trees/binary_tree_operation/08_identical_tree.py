'''
Check if two trees are identical
'''


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def is_identical(root1, root2):
    # 如果兩個都是空的，表示比到最底了，之前都是一樣的。
    if (not root1) and (not root2):
        return True

    # 兩個都有內容，則看值是否一樣，若值相同，則遞迴檢查左右子樹。
    if root1 and root2:
        if root1.data == root2.data:
            is_left_identical = is_identical(root1.left, root2.left)
            is_right_identical = is_identical(root1.right, root2.right)

            return is_left_identical and is_right_identical

    # 一個有值一個為空
    return False


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)

# only one node
root3 = Node(10)
root4 = Node(10)

# one tree is empty
root5 = Node(10)
root6 = None

# both trees are empty
root7 = None
root8 = None

print(is_identical(root1, root2))  # True
print(is_identical(root3, root4))  # True
print(is_identical(root5, root6))  # False
print(is_identical(root7, root8))  # True
