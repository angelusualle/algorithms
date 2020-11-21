import unittest
from find_first_ancestor import Node, find_first_ancestor

class Test_Case_Find_First_Ancestor(unittest.TestCase):
    def test_find_first_ancestor(self):
        root = Node(1)
        # build left
        root.left_child = Node(2)
        root.left_child.parent = root
        root.left_child.left_child = Node(4)
        root.left_child.left_child.parent = root.left_child
        root.left_child.right_child = Node(5)
        root.left_child.right_child.parent = root.left_child
        # build right
        root.right_child = Node(3)
        root.right_child.parent = root
        root.right_child.left_child = Node(6)
        root.right_child.left_child.parent = root.right_child
        root.right_child.left_child.right_child = Node(10)
        root.right_child.left_child.right_child.parent = root.right_child.left_child
        root.right_child.left_child.left_child = Node(7)
        root.right_child.left_child.left_child.parent = root.right_child.left_child
        root.right_child.left_child.left_child.left_child = Node(8)
        root.right_child.left_child.left_child.left_child.parent = root.right_child.left_child.left_child
        print_tree(root, 0)
        self.assertEqual(find_first_ancestor(root.right_child.left_child.right_child, root.right_child.left_child.left_child.left_child), root.right_child.left_child)

def print_tree(node, level):
    if node is None:
        return
    print_tree(node.right_child, level +1)
    print("\t"* level + str(node.d))
    print_tree(node.left_child, level +1)