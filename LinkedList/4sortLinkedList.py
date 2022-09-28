class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next



def sortInsert(head,newNode):
    curr = temp = Node()
    temp.next = head

    while curr.next and curr.next.data < newNode.data:
        curr = curr.next
    newNode.next = curr.next
    curr.next = newNode
    return temp.next

def insertSort(head):
    result = None
    curr = head

    while curr:
        temp = curr.next
        result = sortInsert(result,curr)
        curr = temp
    return result