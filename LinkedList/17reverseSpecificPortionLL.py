
# https://www.techiedelight.com/reverse-specified-portion-linked-list/

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Utility function to print a linked list
def printList(msg, head):
    print(msg, end=': ')
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')

def reverse(head, m, n):
    prev = None
    curr = head
    i = 1
    while curr and i < m:
        prev = curr
        curr = curr.next
        i += 1
    start = curr
    end = None
    while curr and i <= n:
        temp = curr.next
        curr.next = end
        end = curr
        curr = temp
        i += 1
    start.next = curr
    if prev is None:
        head = end
    else:
        prev.next = end
    return head



if __name__ == '__main__':

    head = None
    for i in reversed(range(7)):
        head = Node(i + 1, head)

    (m, n) = (0, 5)

    printList('Original linked list:', head)
    head = reverse(head, m, n)
    printList('Reversed linked list', head)