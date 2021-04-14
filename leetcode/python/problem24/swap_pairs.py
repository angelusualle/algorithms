class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
# O(N) time O(1) space
def swap_pairs( head):
    next_ = head
    while next_ is not None and next_.next is not None:
        next_.val, next_.next.val = next_.next.val, next_.val
        next_ = next_.next.next
    return head