'''
https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
'''


class Node:
    '''
    Definition of a node
    '''

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        '''
        Insert a new node recursively
        由 root 代表這個 tree
        每次呼叫都是透過 root
        這裡的實作是以 binary search tree (BST) 為前提，所以才可以每次都透過 root 呼叫。
        '''
        if self.data:
            if data < self.data:
                if self.left is None:
                    # if there is no left subtree, then we create the left child node
                    self.left = Node(data)
                else:
                    # if left subtree is not empty, do recursive insert
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            # current node is null
            self.data = data

    def print_tree(self):
        '''
        In-order traversal: left, current, right
        其實就是將數值由小到大印出
        '''
        # left subtree
        if self.left:
            self.left.print_tree()

        # current node
        print(self.data)

        # right subtree
        if self.right:
            self.right.print_tree()


root = Node(12)

root.insert(6)
root.insert(14)
root.insert(3)
root.insert(1)
root.insert(10)
root.insert(13)
root.insert(20)
root.insert(18)

root.print_tree()

# 1
# 3
# 6
# 10
# 12
# 13
# 14
# 18
# 20
