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
        in-order traversal 用這個寫法沒有問題
        會由小到大印出
        '''
        if node:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        '''
        用這個寫法印出來的結果才會正確
        [27, 14, 10, 19, 35, 31, 42]
        '''
        res = []
        if node:
            res.append(node.data)
            res = res + self.preorder_traversal(node.left)
            res = res + self.preorder_traversal(node.right)

        return res

    def postorder_traversal(self, node):
        '''
        如果用跟 inorder traversal 一樣的寫法，印出來的順序不正確。
        執行結果為 10 14 19 31 35 42 27
        正確順序應該是 [10, 19, 14, 31, 42, 35, 27] <- 我用手寫演練也是這個結果
        '''
        # TODO: find out why the order is not right
        if node:
            self.inorder_traversal(node.left)
            self.inorder_traversal(node.right)
            print(node.data)


root = Node(27)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print('>>>>>>>> in-order traversal')
root.inorder_traversal(root)

print('>>>>>>>> pre-order traversal')
print(root.preorder_traversal(root))

print('>>>>>>>> post-order traversal')
root.postorder_traversal(root)
