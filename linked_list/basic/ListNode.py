class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def append(head, val):
        '''
        append a new node to the end of the list
        '''
        current = head
        # move pointer to the tail node
        while current.next:
            current = current.next

        new_node = ListNode(val)
        current.next = new_node

    @staticmethod
    def append_list(head, lst):
        '''
        spread the list into nodes and append them to end of the linked list
        '''
        for i in lst:
            head.append(head, i)

    @staticmethod
    def display(head):
        '''
        print all values of the nodes
        '''
        current = head
        while current:
            print(current.val)
            current = current.next


if __name__ == '__main__':

    node = ListNode(1)
    list1 = [2, 3, 4, 5]
    list2 = [6, 7, 8, 9]

    ListNode.append_list(node, list1)
    ListNode.append_list(node, list2)

    ListNode.display(node)
