import unittest
from avl_tree import AVL_Tree

class Test_AVL_Tree(unittest.TestCase):
    def test_avl_tree(self):
        tree = AVL_Tree()
        for i in range(10, 0, -1):
            tree.insert(i)
        tots = []
        print('\n'.join(tree.print_tree(ans=tots)))
        self.assertEqual(tots, ['\t\t\t10', '\t\t9', '\t8', '\t\t7', '6', '\t\t\t5', '\t\t4', '\t3', '\t\t2', '\t\t\t1'])
        tree = AVL_Tree()
        for i in range(0, 10):
            tree.insert(i)
        tots = []
        print('\n'.join(tree.print_tree(ans=tots)))
        self.assertEqual(tots, ['\t\t\t9', '\t\t8', '\t7', '\t\t6', '\t\t\t5', '4', '\t\t3', '\t2', '\t\t1', '\t\t\t0'])