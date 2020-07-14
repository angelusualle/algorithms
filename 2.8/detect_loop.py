class Linked_List():
    def __init__(self, head):
        self.head = head
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_loop(linked_list):
    slow = linked_list.head
    fast = linked_list.head
    while slow is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow is None or fast.next is None:
        return None
    slow = linked_list.head
    while True:
        if slow == fast:
            return slow
        slow = slow.next
        fast = fast.next

'''
# O(n) time and space
def detect_loop(linked_list):
    nodes = set()
    next_one = linked_list.head
    while next_one is not None:
        if next_one in nodes:
            return next_one
        nodes.add(next_one)
        next_one = next_one.next
    return None
'''