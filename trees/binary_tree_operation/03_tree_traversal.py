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

    def inorder_traversal(self, node):
        '''
        會由小到大印出
        '''
        if node:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.data)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data)


root = Node(27)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print('>>>>>>>> in-order traversal')
root.inorder_traversal(root)             # 10 14 19 27 31 35 42

print('>>>>>>>> pre-order traversal')
root.preorder_traversal(root)            # 27, 14, 10, 19, 35, 31, 42

print('>>>>>>>> post-order traversal')
root.postorder_traversal(root)           # 10, 19, 14, 31, 42, 35, 27
