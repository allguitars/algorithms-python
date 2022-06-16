'''
Back to Back SWE: https://youtu.be/suj1ro8TIVY
'''

from collections import deque


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def preorder_traversal(node):
    if node:
        print(node.data)
        preorder_traversal(node.left)
        preorder_traversal(node.right)


def serialize(root):
    if root is None:
        return 'X'

    left_serialized = serialize(root.left)
    right_serialized = serialize(root.right)

    return str(root.data) + ',' + left_serialized + ',' + right_serialized


def deserialize(s):
    queue = deque(s.split(','))

    return deserializeHelper(queue)


def deserializeHelper(queue):
    value = queue.popleft()

    if value == 'X':
        return None

    node = Node(value)
    node.left = deserializeHelper(queue)
    node.right = deserializeHelper(queue)

    return node


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print('>>> the original tree:')
preorder_traversal(root)             # 1, 2, 4, 3

# serialization
serialized_string = serialize(root)  # 1,2,4,X,X,X,3,X,X

# deserialization
new_root = deserialize(serialized_string)

print('>>> after serialization and deserialization')
preorder_traversal(new_root)
