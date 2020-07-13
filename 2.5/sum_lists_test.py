import unittest
from sum_lists import Linked_List, Node, sum_lists_bwd, sum_lists_fwd

class Test_Case_Sum_Lists_Bwd_fwd(unittest.TestCase):
    def test_sum_lists_bwd(self):
        list_1 = Linked_List(None)
        list_1.head = Node(7)
        list_1.head.next = Node(1)
        list_1.head.next.next = Node(6)
        list_2 = Linked_List(None)
        list_2.head = Node(5)
        list_2.head.next = Node(9)
        list_2.head.next.next = Node(2)
        result_list = sum_lists_bwd(list_1, list_2)
        result = []
        next_one = result_list.head
        while next_one is not None:
            result.append(next_one.data)
            next_one = next_one.next
        self.assertEqual([2, 1, 9], result)

    def test_sum_lists_fwd(self):
        list_1 = Linked_List(None)
        list_1.head = Node(6)
        list_1.head.next = Node(1)
        list_1.head.next.next = Node(7)
        list_2 = Linked_List(None)
        list_2.head = Node(2)
        list_2.head.next = Node(9)
        list_2.head.next.next = Node(5)
        result_list = sum_lists_fwd(list_1, list_2)
        result = []
        next_one = result_list.head
        while next_one is not None:
            result.append(next_one.data)
            next_one = next_one.next
        self.assertEqual([9, 1, 2], result)

if __name__ == '__main__':
    unittest.main()