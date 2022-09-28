class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def removeDuplicates(head):
    if head is None:
        return head
    curr = head
    while curr.next:
        if curr.data == curr.next.data:
            temp = curr.next.next
            curr.next.next = None
            curr.next = temp
        else:
            curr = curr.next    # only advance if no deletion
    return head

