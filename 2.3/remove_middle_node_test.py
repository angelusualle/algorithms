import unittest
from remove_middle_node import remove_middle_node, Linked_List, Node

class Test_Case_Remove_Middle_Node(unittest.TestCase):
    def test_remove_middle_node(self):
        head = Node('a')
        head.next = Node('b')
        head.next.next = Node('c')
        head.next.next.next = Node('d')
        head.next.next.next.next = Node('e')
        linked_list = Linked_List(head)
        remove_middle_node(head.next.next)
        new_list = []
        next_one = linked_list.head
        while next_one is not None:
            new_list.append(next_one.data)
            next_one = next_one.next
        self.assertEqual(['a', 'b', 'd', 'e'], new_list)

if __name__ == '__main__':
    unittest.main()