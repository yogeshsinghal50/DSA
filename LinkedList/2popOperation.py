# https://www.techiedelight.com/pop-operation-in-linked-list/

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def pop(head):
    if head is None:
        print('Nothing to pop, LL is empty')
        return None
    result = head.data
    newHead = head.next
    head.next = None
    print('Element popped: ', result)
    return newHead