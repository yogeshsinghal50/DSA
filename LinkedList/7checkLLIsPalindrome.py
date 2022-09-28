class Node:
    def __init__(self, ch):
        self.data = ch
        self.next = None


def construct(head,s1='',s2=''):
    if head is None:
        return s1,s2
    s1 += head.data
    s1, s2 = construct(head.next,s1=s1,s2=s2)
    s2 += head.data
    return s1,s2

def isPalindrome(head):
    (s1,s2) = construct(head)
    return s1 == s2

def isPalindromeRecursive(left,right):
    if right is None:
        return True, left
    val, left = isPalindromeRecurcise(left,right.next)
    if not val:
        return False, left
    return left.data == right.data, left.next


isPalindromeRecurcise(head,head)