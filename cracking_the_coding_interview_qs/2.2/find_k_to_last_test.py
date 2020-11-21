import unittest
from find_k_to_last import find_k_to_last, Linked_List, Node

class Test_Case_Find_K_To_Last(unittest.TestCase):
    def test_find_k_to_last(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.next.next.next.next.next = Node(6)
        linked_list = Linked_List(head)
        node = find_k_to_last(linked_list, 2)
        self.assertEqual(node.data, 5)
        node = find_k_to_last(linked_list, 1)
        self.assertEqual(node.data, 6)