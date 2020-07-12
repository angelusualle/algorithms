import unittest
from is_palindrome import is_palindrome, Linked_List, Node

class Test_Case_Is_Palindrome(unittest.TestCase):
    def test_is_palindrome(self):
        head = Node(1)
        head.next = Node(4)
        head.next.next = Node(5)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(1)
        self.assertTrue(is_palindrome(Linked_List(head)))
        head.next.next.next.next.next = Node(2)
        self.assertFalse(is_palindrome(Linked_List(head)))

if __name__ == '__main__':
    unittest.main()