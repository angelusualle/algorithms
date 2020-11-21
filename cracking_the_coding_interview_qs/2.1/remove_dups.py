# singly linked list class an node class
class Linked_List():
    def __init__(self, head):
        self.head = head

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# no buffer allowed O(N^2) time and O(1) space
def remove_dups(linked_list):
    dup = True
    # removing duplicates pass by pass until no more
    while dup is True:
        # detection logic
        dup = False
        next_one = linked_list.head
        while next_one is not None and next_one.next is not None:
            if dup:
                break
            dupval = next_one.data
            next_one_child = next_one.next
            while next_one_child is not None:
                if next_one.data == next_one_child.data:
                    dup = True
                    break
                else:
                    next_one_child = next_one_child.next
            next_one = next_one.next
        if not dup:
            continue
        # removal logic
        while linked_list.head.data == dupval:
            linked_list.head = linked_list.head.next
        next_one = linked_list.head
        while next_one is not None and next_one.next is not None:
            while next_one is not None and next_one.next is not None and next_one.next.data == dupval:
                next_one.next = next_one.next.next
            next_one = next_one.next
    return linked_list
'''
# with buffered allowed, O(N) where N is length of linked list time,
# O(N) space
def remove_dups(linked_list):
    data_nodes = {}
    next_one = linked_list.head
    while next_one is not None:
        if next_one.data not in data_nodes:
            data_nodes[next_one.data] = 1
        else:
            data_nodes[next_one.data] += 1
        next_one = next_one.next
    next_one = linked_list.head
    while next_one is not None and data_nodes[next_one.data] > 1:
        linked_list.head = next_one.next
        next_one = linked_list.head
    while next_one is not None:
        while next_one.next is not None and data_nodes[next_one.next.data] > 1:
            next_one.next = next_one.next.next
        next_one = next_one.next
    return linked_list
'''