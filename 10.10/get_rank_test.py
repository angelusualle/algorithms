import unittest
from get_rank import get_rank, insert, Node

class Test_Case_Get_Rank(unittest.TestCase):
    def test_get_rank(self):
        root = Node(5)
        insert(7, root)
        insert(10, root)
        insert(8, root)
        insert(6, root)
        insert(5, root)
        insert(4, root)
        print_tree(root)
        self.assertEqual(get_rank(5, root), 3)
        self.assertEqual(get_rank(8, root), 6)

def print_tree(node, level=0):
    if node is None:
        return
    print_tree(node.right_child, level + 1)
    print('\t'*level + str(node.val))
    print_tree(node.left_child, level + 1)