import unittest
from partition_linked_list import partition_linked_list, Node, Linked_List

class Test_Case_Partition_Linked_list(unittest.TestCase):
    def test_partiion_linked_list(self):
        head = Node(3)
        head.next = Node(5)
        head.next.next = Node(8)
        head.next.next.next = Node(5)
        head.next.next.next.next = Node(10)
        head.next.next.next.next.next = Node(2)
        head.next.next.next.next.next.next = Node(1)
        linked_list = Linked_List(head)
        linked_list = partition_linked_list(linked_list, 5)
        ans = []
        next_one = linked_list.head
        while next_one is not None:
            ans.append(next_one.data)
            next_one = next_one.next
        self.assertEqual(ans, [1,2,3,10,5,8,5])

if __name__ == '__main__':
    unittest.main()