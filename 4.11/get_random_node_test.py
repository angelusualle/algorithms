import unittest
from get_random_node import Tree, Node

class Test_Case_Get_Random_Node(unittest.TestCase):
    def test_get_random_node(self):
        root = Node(4)
        tree = Tree(root)
        tree.insert_in_order(2)
        tree.insert_in_order(1)
        tree.insert_in_order(3)
        tree.insert_in_order(6)
        tree.insert_in_order(5)
        tree.insert_in_order(7)
        ans = []
        for i in range(100000):
            ans.append(tree.get_random_node()[1].data)
        self.assertAlmostEqual(len([x for x in ans if x == 4])/100000, 0.14, 2)