import unittest
from convert_to_doubly_linked_list import convert_to_doubly_linked_list, Node

class Test_Case_Convert_To_Doubly_Linked_List(unittest.TestCase):
    def test_convert_to_doubly_linked_list(self):
        root = Node(4)

        root.n1 = Node(2)
        root.n1.n1 = Node(1)
        root.n1.n2 = Node(3)
        
        root.n2 = Node(6)
        root.n2.n1 = Node(5)
        root.n2.n2 = Node(7)

        r = convert_to_doubly_linked_list(root)
        ans = []
        while r is not None:
            ans.append(r.val)
            r = r.n2
        self.assertListEqual(list(range(1,8)), ans)

if __name__ == '__main__':
    unittest.main()