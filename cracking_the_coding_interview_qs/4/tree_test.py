from tree import Tree, Node
import unittest

class Test_Case_Tree(unittest.TestCase):
    def test_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        ans = Tree(root).in_order_traversal()
        self.assertListEqual(ans, [2,1,3])
        ans = Tree(root).pre_order_traversal()
        self.assertListEqual(ans, [1,2,3])
        ans = Tree(root).post_order_traversal()
        self.assertListEqual(ans, [2,3,1])