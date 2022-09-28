class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def frontBackSplit(head):
    if head is None or head.next is None:
        return head, None
    slow = head
    fast = head.next
    while fast:
        fast = fast.next
        if fast:
            slow = slow.next
            fast = fast.next
    backLL = slow.next
    slow.next = None
    return head, backLL