from is_bst import Node, is_bst
import unittest

class Test_Case_Is_BST(unittest.TestCase):
    def test_is_bst(self):
        root = build_binary_search_tree([1,2,3,4,5,6,7])
        ans, _, __, = is_bst(root)
        self.assertTrue(ans)
        root.right_child.right_child.right_child = Node(1)
        ans, _, __, = is_bst(root)
        self.assertFalse(ans)


def build_binary_search_tree(arr):
    if len(arr) == 1:
        return Node(arr[0])
    mid = len(arr) // 2
    node = Node(arr[mid])
    node.left_child = build_binary_search_tree(arr[0:mid])
    if len(arr) > 2:
        node.right_child = build_binary_search_tree(arr[mid+1:])
    return node