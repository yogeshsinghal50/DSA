# https://www.techiedelight.com/sorted-insert-in-linked-list/

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def sortedInsert(head,newNode):
    if head is None or head.data >= newNode.data:
        newNode.next = head
        head = newNode
        return head
    curr = head
    while curr.next and curr.next.data < newNode.data:
        curr = curr.next
    newNode.next = curr.next
    curr.next = newNode
    return head