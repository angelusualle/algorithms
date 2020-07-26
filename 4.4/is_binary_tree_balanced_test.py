from is_binary_tree_balanced import Node, is_binary_tree_balanced
import unittest

class Test_Case_Is_Binary_Tree_Balanced(unittest.TestCase):
    def test_is_binary_tree_balanced(self):
        root = Node(1)
        root.left_child = Node(2)
        root.right_child = Node(3)
        root.left_child.left_child = Node(4)
        root.left_child.right_child= Node(5)
        root.right_child.left_child = Node(6)
        root.right_child.right_child = Node(7)
        print("------Balanced Tree--------")
        print_tree(root)
        self.assertTrue(is_binary_tree_balanced(root)[0])
        root.right_child.right_child.right_child = Node(8)
        print("------Balanced Tree--------")
        print_tree(root)
        self.assertTrue(is_binary_tree_balanced(root)[0])
        root.right_child.right_child.right_child.right_child = Node(9)
        print("------UnBalanced Tree--------")
        print_tree(root)
        self.assertFalse(is_binary_tree_balanced(root)[0])

def print_tree(root, depth=0):
    if root is None:
        return
    print_tree(root.right_child, depth + 1)
    print("\t"*depth + str(root.d))
    print_tree(root.left_child, depth + 1)
