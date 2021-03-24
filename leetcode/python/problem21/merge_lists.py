class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# O(n + m) where n and m are sizes of sub lists
def merge_lists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    head = ListNode()
    if l1.val < l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next
    orig = head
    while l1 is not None or l2 is not None:
        if l1 is None:
            head.next = l2
            l2 = head.next.next
        elif l2 is None:
            head.next = l1
            l1 = head.next.next
        else:
            if l1.val < l2.val:
                head.next = l1
                l1 = head.next.next
            else:
                head.next = l2
                l2 = head.next.next
        head = head.next
    return orig