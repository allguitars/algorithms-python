from basic.ListNode import ListNode

node = ListNode(1)
lst = [2, 3, 4]
ListNode.append_list(node, lst)
ListNode.display(node)  # 1,2,3,4


def reverse_list(head):
    prev_node = None  # THE TRICK
    current = head

    while current:
        # 1. backup the original next pointer so we won't lose the trace
        old_next = current.next

        # 2. reverse the pointer
        current.next = prev_node

        # 3. move forward
        prev_node = current
        current = old_next

    # by the end, the prev_node will be pointing to the new head
    return prev_node


new_head = reverse_list(node)
ListNode.display(new_head)  # 4,3,2,1
