'''
https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
'''


class Node:
    '''definition of a tree node'''

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        '''for this example, we just print the root'''
        print(self.data)


root = Node(10)
root.print_tree()
