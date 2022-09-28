class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


def printList(msg, head):
    print(msg, end='')
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')


def reverseMerge(a, b):
    result = None
    while a and b:
        if a.data < b.data:
            newNode = a
            a = a.next
            newNode.next = result
            result = newNode
        else:
            newNode = b
            b = b.next
            newNode.next = result
            result = newNode

    while a:
        newNode = a
        a = a.next
        newNode.next = result
        result = newNode
    while b:
        newNode = b
        b = b.next
        newNode.next = result
        result = newNode

    return result


if __name__ == '__main__':

    a = b = None

    for i in reversed(range(2, 8, 2)):
        a = Node(i, a)

    for i in reversed(range(1, 10, 2)):
        b = Node(i, b)

    # print both lists
    printList('First List: ', a)
    printList('Second List: ', b)

    head = reverseMerge(a, b)
    printList('After Merge: ', head)