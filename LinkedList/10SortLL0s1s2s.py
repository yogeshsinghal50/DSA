# https://www.techiedelight.com/sort-linked-list-containing-0s-1s-2s/

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')


def sortList(head):
    if head is None or head.next is None:
        return head
    zero = Node()
    one = Node()
    two = Node()

    z = zero
    o = one
    t = two
    curr = head
    while curr:
        if curr.data == 0:
            z.next = curr
            z = z.next
        elif curr.data == 1:
            o.next = curr
            o = o.next
        elif curr.data == 2:
            t.next = curr
            t = t.next
        curr = curr.next
    z.next = one.next if one else two.next
    o.next = two.next
    t.next = None

    return zero.next


if __name__ == '__main__':

    # input keys
    keys = [1, 2, 0, 0, 1, 2, 1, 2, 1,1,1,1,1,0,0,0]

    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    head = sortList(head)
    printList(head)