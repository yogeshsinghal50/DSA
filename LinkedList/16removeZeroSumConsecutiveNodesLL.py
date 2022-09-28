def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prefix_sum = 0
    dict_map = {}
    dict_map[0] = mainHead = ListNode()
    mainHead.next = head
    while head:
        prefix_sum += head.val
        dict_map[prefix_sum] = head
        head = head.next
    head = mainHead
    prefix_sum = 0
    while head:
        prefix_sum += head.val
        head.next = dict_map[prefix_sum].next
        head = head.next
    return mainHead.next