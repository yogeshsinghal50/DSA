# https://www.techiedelight.com/remove-duplicates-linked-list/

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

def removeDuplicates(head):
    curr = head
    prev = None
    s = set()
    while curr:
        if curr.data in s:
            prev.next = curr.next
        else:
            s.add(curr.data)
            prev = curr
        curr = curr.next
    return head


if __name__ == '__main__':

    # input keys
    keys = [5, 3, 4, 2, 5, 4, 1, 3]

    # construct a linked list
    head = None
    for i in reversed(range(len(keys))):
        head = Node(keys[i], head)

    removeDuplicates(head)

    # print linked list
    printList(head)

