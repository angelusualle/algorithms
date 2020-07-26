class Node():
    def __init__(self, d):
        self.d = d
        self.left_child = None
        self.right_child = None
# O(n), best possible
def is_bst(node):
    if node is None:
        return True, None, None
    l_valid, l_min, l_max = is_bst(node.left_child)
    r_valid, r_min, r_max = is_bst(node.right_child)
    if (not l_valid) or (not r_valid):
        return False, None, None
    if l_min is None and r_min is None:
        return True, node.d, node.d
    if l_max is not None and l_max > node.d:
        return False, None, None
    if r_min is not None and r_min < node.d:
        return False, None, None
    if l_max is None:
        return True, node.d, r_max
    if r_min is None:
        return True, l_min, node.d
    return True, l_min, r_max