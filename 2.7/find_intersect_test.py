from find_intersect import find_intersect, Linked_List, Node
import unittest

class Test_Case_Find_Intersect(unittest.TestCase):
    def test_find_intersect(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(-1)
        head.next.next.next = Node(4)
        head2 = Node(3)
        head2.next = head.next.next
        node = find_intersect(Linked_List(head), Linked_List(head2))
        self.assertEqual(node.data, -1)
        head2 = Node(1)
        node = find_intersect(Linked_List(head), Linked_List(head2))
        self.assertIsNone(node)