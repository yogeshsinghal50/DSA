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

def deleteNodes(head, m, n):
    curr = head
    while curr:
        i = 1
        while i < m:
            if curr:
                curr = curr.next
            i += 1
        skip = curr.next
        j = 0
        while j < n:
            if skip:
                skip = skip.next
            j += 1
        curr.next = skip
        curr = skip
    return head


if __name__ == '__main__':

    head = None
    for i in reversed(range(10)):
        head = Node(i + 1, head)

    head = deleteNodes(head, 1, 6)
    printList(head)