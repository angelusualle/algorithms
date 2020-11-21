from get_linked_lists_by_depth_from_binary_tree import List_Node, Tree_Node, Linked_List, get_linked_lists_by_depth_from_binary_tree
import unittest

class Test_Case_Get_Linked_Lists_By_Depth_From_Binary_Tree(unittest.TestCase):
    def test_get_linked_lists_by_depth_from_binary_tree(self):
        root = build_binary_search_tree([1,2,3,4,5,6,7])
        store = get_linked_lists_by_depth_from_binary_tree(root)
        level_0 = []
        next_one = store[0].head
        level_0.append(next_one.data)
        level_1 = []
        next_one = store[1].head
        while next_one is not None:
            level_1.append(next_one.data)
            next_one = next_one.next
        level_2 = []
        next_one = store[2].head
        while next_one is not None:
            level_2.append(next_one.data)
            next_one = next_one.next
        holder = []
        get_tree_string(root, 0,holder)
        ans = ''.join(holder)
        print(ans)
        self.assertEqual(level_0, [4])
        self.assertListEqual(level_1, [2,6])
        self.assertListEqual(level_2, [1,3,5,7])

def build_binary_search_tree(arr):
    if len(arr) == 1:
        return Tree_Node(arr[0])
    mid = len(arr) // 2
    node = Tree_Node(arr[mid])
    node.left_child = build_binary_search_tree(arr[0:mid])
    if len(arr) > 2:
        node.right_child = build_binary_search_tree(arr[mid+1:])
    return node

def get_tree_string(root, level, holder):
    if root.right_child is not None:
        get_tree_string(root.right_child, level+1, holder)
    holder.append(level*'\t' + str(root.data) + '\n')
    if root.left_child is not None:
        get_tree_string(root.left_child, level+1, holder)