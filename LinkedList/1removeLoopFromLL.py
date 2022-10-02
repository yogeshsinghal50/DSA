# https://www.techiedelight.com/remove-loop-linked-list/

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#using hashing


def removeCycle(head):
    prev = None
    curr = head
    s = set()
    while curr:
        if curr in s:
            prev.next = None
            return
        s.add(curr)
        prev = curr
        curr = curr.next

#Floyd’s Cycle Detection Algorithm


