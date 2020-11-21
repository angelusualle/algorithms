class Linked_List():
    def __init__(self, head):
        self.head = head

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# O(N) space and O(N) time
def partition_linked_list(linked_list, partition):
    less_than = []
    greater_than_or_equal = []
    next_one = linked_list.head
    while next_one is not None:
        if next_one.data < partition:
            less_than.append(next_one.data)
        else:
            greater_than_or_equal.append(next_one.data)
        next_one = next_one.next
    next_one = linked_list.head
    while next_one is not None:
        if len(less_than) > 0:
            next_one.data = less_than.pop()
        else:
            next_one.data = greater_than_or_equal.pop()
        next_one = next_one.next
    return linked_list