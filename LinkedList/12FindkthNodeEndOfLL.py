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


def getKthFromEnd(head, k):
    i = 0
    firstP = head
    while i < k:
        if firstP is None:
            return Node()
        firstP = firstP.next
        i += 1
    secondP = head
    while firstP:
        secondP = secondP.next
        firstP = firstP.next
    return secondP


if __name__ == '__main__':

    # input keys
    keys = [5, 3, 4, 2, 5, 4, 1, 3]

    # construct a linked list
    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    node = getKthFromEnd(head, 2)

    # print linked list
    printList(node)