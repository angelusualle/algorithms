from binary_search_tree import serialize_bst, deserialize_bst, Node
import unittest

class Test_Case_Binary_Search_Tree(unittest.TestCase):
    def test_binary_search_tree_serailization(self):
        root = Node(20)
        root.left_child = Node(8)
        root.left_child.left_child = Node(4)

        root.right_child = Node(22)
        root.right_child.left_child = Node(21)
        root.right_child.right_child = Node(23)
        print_tree(root)
        arr = serialize_bst(root)
        print_tree(deserialize_bst(arr))

def print_tree(node, level=0):
    if node is None:
        return
    print_tree(node.right_child, level + 1)
    print("\t"*level + str(node.value))
    print_tree(node.left_child, level + 1)