import unittest
from detect_loop import detect_loop, Linked_List, Node

class Test_Case_Loop_Detection(unittest.TestCase):
    def test_loop_detection(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = head.next.next
        node = detect_loop(Linked_List(head))
        self.assertEqual(node.data, 3)
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        node = detect_loop(Linked_List(head))
        self.assertIsNone(node)