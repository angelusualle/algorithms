class Linked_List():
    def __init__(self, head):
        self.head = head

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# O(n + m) time and O(1) space.
def find_intersect(linked_list1, linked_list2):
    length_1 = 0
    length_2 = 0
    next_one_1 = linked_list1.head
    next_one_2 = linked_list2.head
    while next_one_1.next is not None:
        next_one_1 = next_one_1.next
        length_1 += 1
    length_1 += 1
    while next_one_2.next is not None:
        next_one_2 = next_one_2.next
        length_2 += 1
    length_2 += 1
    if next_one_1 != next_one_2:
        return None
    dist = abs(length_1 - length_2)
    catch_up_list = linked_list1
    other_list = linked_list2
    if length_2 > length_1:
        catch_up_list = linked_list2
        other_list = linked_list1
    i = 0
    next_one = catch_up_list.head
    while i < dist:
        next_one = next_one.next
        i += 1
    next_one_other = other_list.head
    while next_one is not None:
        if next_one == next_one_other:
            return next_one
        next_one = next_one.next
        next_one_other = next_one_other.next
    return None

'''
# O(n + m) time and O(n) space where n and m are two linked list sizes.
def find_intersect(linked_list1, linked_list2):
    nodes = set()
    next_one = linked_list1.head
    while next_one is not None:
        nodes.add(next_one)
        next_one = next_one.next
    next_one = linked_list2.head
    while next_one is not None:
        if next_one in nodes:
            return next_one
        next_one = next_one.next
    return None
'''