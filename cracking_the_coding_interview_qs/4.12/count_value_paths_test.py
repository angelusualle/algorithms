import unittest
from count_value_paths import Node, count_value_paths

class Test_Case_Count_Value_Paths(unittest.TestCase):
    def test_count_value_paths(self):
        root = Node(5)
        root.left = Node(-4)
        root.left.left = Node(-3)
        root.left.left.left = Node(-1)
        root.left.right = Node(2)
        root.right = Node(6)
        root.right.left = Node(7)
        root.right.right = Node(-10)
        print_tree(root)
        self.assertEqual(count_value_paths(root, -1)[0], 1)

def print_tree(node, level = 0):
    if node is None:
        return
    print_tree(node.right, level + 1)
    print("\t"*level + str(node.data))
    print_tree(node.left, level + 1)