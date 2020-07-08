import unittest
from remove_dups import remove_dups, Linked_List, Node


class Test_Case_Remove_Dups(unittest.TestCase):
    def test_remove_dups(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(1)
        head.next.next.next.next.next = Node(1)
        head.next.next.next.next.next.next = Node(2)
        linked_list = Linked_List(head)
        linked_list = remove_dups(linked_list)
        vals = []
        next_one = linked_list.head
        while next_one is not None:
            vals.append(next_one.data)
            next_one = next_one.next
        self.assertEqual(vals, [3,4])