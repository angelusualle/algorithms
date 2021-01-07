import unittest
from avl_tree import AVL_Tree

class Test_AVL_Tree(unittest.TestCase):
    def test_avl_tree(self):
        tree = AVL_Tree()
        for i in range(10, 0, -1):
            tree.insert(i)
        tots = []
        print('\n'.join(tree.print_tree(ans=tots)))