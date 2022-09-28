class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def append(head, digit):
    if head is None:
        return digit
    carry = append(head.next, digit)
    if carry == 0:
        return 0
    total = carry + head.data
    head.data = total % 10
    return total // 10


def addDigit(head, digit):
    carry = append(head, digit)
    if carry > 0:
        newNode = Node(carry)
        newNode.next = head
        head = newNode
    return head