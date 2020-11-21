class Linked_List():
    def __init__(self, head):
        self.head = head

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


# O(N) space and O(1) time
def find_k_to_last(linked_list, k):
    if linked_list.head is None:
        return None
    i = 1
    next_one = linked_list.head
    kth_one = linked_list.head
    while i < k:
        next_one = next_one.next
        i += 1
    while next_one.next is not None:
        next_one = next_one.next
        kth_one = kth_one.next
    return kth_one

'''
# O(N) space and time
def find_k_to_last(linked_list, k):
    node_pos = {}
    next_one = linked_list.head
    i = 0
    while next_one is not None:
        node_pos[i] = next_one
        next_one = next_one.next
        i -= 1
    return node_pos[i + k]
'''