import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(kn*log(k)) where n is max size of list and k is num of lists
def merge_k_lists(lists):
    if len(lists) == 0:
        return None
    q = [(n.val, id(n), n) for n in lists if n is not None]
    if len(q) == 0:
        return None
    heapq.heapify(q)
    _, __, original = heapq.heappop(q)
    head = original
    if head.next is not None:
        heapq.heappush(q, (head.next.val, id(head.next), head.next))
    while q:
        _, __, next_head = heapq.heappop(q)
        head.next = next_head
        head = head.next
        if head.next is not None:
            heapq.heappush(q, (head.next.val, id(head.next), head.next))
    head.next = None
    return original