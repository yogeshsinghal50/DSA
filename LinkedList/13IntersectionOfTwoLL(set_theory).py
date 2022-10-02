# https://www.techiedelight.com/find-intersection-point-of-two-linked-lists

# A Linked List Node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



def findIntersection(first, second):
    nodes = set()
    while first:
        nodes.add(first)
        first = first.next

    while second:
        if second in nodes:
            return second
        second = second.next
    return None

