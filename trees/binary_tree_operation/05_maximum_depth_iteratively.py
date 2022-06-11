'''
https://favtutor.com/blogs/binary-tree-height

BFS -- using Level order traversal without using recursion.

Time:
The time complexity of the algorithm is O(n) as we iterate through
node of the binary tree calculating the height of the binary tree
only once.

Space:
And the space complexity is also O(n) as we are using an extra space for the queue.

Where n is the number of nodes in the binary tree.
'''

import collections


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def height(node):
    result = 0
    queue = collections.deque()

    if node is None:
        return result

    # inital step
    queue.append(node)    # 把根節點加入 queue

    while queue:
        # 每一輪都是處理新的一層
        current_level_size = len(queue)

        while current_level_size > 0:
            current_node = queue.popleft()
            current_level_size -= 1

            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)

        # current_level_size 減為 0 表示這一層已經結束
        result += 1

    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print(height(root))      # 3
