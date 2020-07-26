class Node():
    def __init__(self, d):
        self.d = d
        self.right_child = None
        self.left_child = None

def is_binary_tree_balanced(root):
    if root is None:
        return True, 0
    l_is_balanced,l_depth = is_binary_tree_balanced(root.left_child)
    r_is_balanced,r_depth = is_binary_tree_balanced(root.right_child)
    if (not l_is_balanced) or (not r_is_balanced):
        return False, None
    if abs(l_depth-r_depth) > 1:
        return False, None
    else:
        return True, 1 + max(l_depth, r_depth)