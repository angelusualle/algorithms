from build_binary_search_tree import Node, build_binary_search_tree
import unittest

class Test_Case_Binary_Search_Tree(unittest.TestCase):
    def test_build_binary_search_tree(self):
        root = build_binary_search_tree([1,2,3,4,5,6,7])
        holder = []
        get_tree_string(root, 0,holder)
        ans = ''.join(holder)
        print(ans)
        self.assertEqual(ans, '\t\t7\n\t6\n\t\t5\n4\n\t\t3\n\t2\n\t\t1\n')
def get_tree_string(root, level, holder):
    if root.right_child is not None:
        get_tree_string(root.right_child, level+1, holder)
    holder.append(level*'\t' + str(root.data) + '\n')
    if root.left_child is not None:
        get_tree_string(root.left_child, level+1, holder)