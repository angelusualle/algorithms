from find_successor_in_bst import find_successor_of_node_in_bst, Node
import unittest

class Test_Case_Find_Successor_In_Bst(unittest.TestCase):
    def test_find_successor_in_bst(self):
        root = build_binary_search_tree([1,2,3,4,5,6,7])
        three_node = root.left_child.right_child
        ans = find_successor_of_node_in_bst(three_node)
        self.assertEqual(ans, root)

def build_binary_search_tree(arr):
    if len(arr) == 1:
        return Node(arr[0])
    mid = len(arr) // 2
    node = Node(arr[mid])
    node.left_child = build_binary_search_tree(arr[0:mid])
    node.left_child.parent = node
    if len(arr) > 2:
        node.right_child = build_binary_search_tree(arr[mid+1:])
        node.right_child.parent = node
    return node