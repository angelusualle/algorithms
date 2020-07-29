from is_subtree import is_subtree, Node
import unittest

class Test_Case_Is_Subtree(unittest.TestCase):
    def test_is_subtree(self):
        root = Node(1)
        
        root.left_child = Node(2)
        root.left_child.left_child = Node(3)
        root.left_child.right_child = Node(4)

        root.right_child = Node(5)
        root.right_child.left_child = Node(6)
        root.right_child.right_child = Node(7)
        root.right_child.right_child.left_child = Node(8)
        root.right_child.right_child.right_child = Node(9)
        root.right_child.right_child.left_child.left_child = Node(10)

        subtree_root = Node(7)
        subtree_root.left_child = Node(8)
        subtree_root.right_child = Node(9)
        subtree_root.left_child.left_child = Node(10)
        
        print_tree(root)
        print("-------")
        print_tree(subtree_root)
        self.assertTrue(is_subtree(root, subtree_root))
        subtree_root.left_child.left_child = Node(11)
        self.assertFalse(is_subtree(root, subtree_root))

def print_tree(node, level=0):
    if node is None:
        return
    print_tree(node.right_child, level + 1)
    print('\t'*level + str(node.data))
    print_tree(node.left_child, level + 1)