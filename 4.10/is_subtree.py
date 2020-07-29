class Node():
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None
# O(nm) time and O(m) space n is size of big tree and m is size of bigger tree, n is smaller tree
def is_subtree(big_root, small_root):
    candidates = []
    get_candidates(big_root, small_root.data, candidates)
    for candidate in candidates:
        if are_equal(candidate, small_root):
            return True
    return False

def get_candidates(node, val, candidates):
    if node is None:
        return
    if node.data == val:
        candidates.append(node)
    get_candidates(node.left_child, val, candidates)
    get_candidates(node.right_child, val, candidates)

def are_equal(node1, node2):
    if node1 is None and node2 is None:
        return True
    elif node1 is None:
        return False
    elif node2 is None:
        return False
    equal = node1.data == node2.data
    left_equal = are_equal(node1.left_child, node2.left_child)
    right_equal = are_equal(node1.right_child, node2.right_child)
    return equal and left_equal and right_equal