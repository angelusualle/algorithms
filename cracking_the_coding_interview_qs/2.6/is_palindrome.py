class Linked_List():
    def __init__(self, head):
        self.head = head

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# O(N) time and space
def is_palindrome(linked_list):
    reversed_list = []
    next_one = linked_list.head
    while next_one is not None:
        reversed_list.insert(0, next_one.data)
        next_one = next_one.next
    i = 0
    next_one = linked_list.head
    while i < len(reversed_list) // 2:
        if next_one.data != reversed_list[i]:
            return False
        i += 1
        next_one = next_one.next
    return True