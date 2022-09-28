# A Linked List Node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def identifyCycle(second):
    slow = fast = second
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return slow
    return None

def removeCycle(slow, second):
    head = second
    while head is not slow:
        slow = slow.next
        head = head.next
    return head

def findIntersection(first, second):
    prev = None
    curr = first
    while curr:
        prev = curr
        curr = curr.next
    if prev:
        prev.next = first
    slow = identifyCycle(second)
    addr = None
    if slow:
        addr = removeCycle(slow, second)
    return addr

if __name__ == '__main__':

    # construct the first linked list (1 —> 2 —> 3 —> 4 —> 5 —> None)
    first = None
    for i in reversed(range(1, 10)):
        first = Node(i, first)

    # construct the second linked list (1 —> 2 —> 3 —> None)
    second = None
    for i in reversed(range(1, 4)):
        second = Node(i, second)

    # link tail of the second list to the fourth node of the first list
    second.next.next.next = first.next.next.next

    addr = findIntersection(first, second)
    if addr:
        print('The intersection point is', addr.data)
    else:
        print('The lists do not intersect.')

