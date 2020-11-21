class Linked_List():
    def __init__(self, head):
        self.head = head

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# O(N) time, O(1) space
def remove_middle_node(node):
    if node.next is None:
        return
    while node.next.next is not None:
        node.data = node.next.data
        node = node.next
    node.data = node.next.data
    node.next = None