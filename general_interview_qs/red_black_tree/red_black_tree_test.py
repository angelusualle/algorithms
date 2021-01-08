import unittest
from red_black_tree import Red_Black_Tree

class Test_Case_Red_Black_Tree(unittest.TestCase):
    def test_red_black_tree(self):
        tree = Red_Black_Tree()
        for i in range(10, 0, -1):
            tree.insert(i)
        tots = []
        print('\n'.join(tree.print_tree(ans=tots)))
        self.assertEqual(tots, ['\t\tNone black', '\t10 red', '\t\tNone black', '9 red', '\t\tNone black', '\t8 black', '\t\t\tNone black', '\t\t1 red', '\t\t\tNone black'])
        tree = Red_Black_Tree()
        for i in range(0, 10):
            tree.insert(i)
        tots = []
        print('\n'.join(tree.print_tree(ans=tots)))
        self.assertEqual(tots, ['\t\t\tNone black', '\t\t9 red', '\t\t\tNone black', '\t2 black', '\t\tNone black', '1 red', '\t\tNone black', '\t0 red', '\t\tNone black'])

if __name__ == '__main__':
    unittest.main()