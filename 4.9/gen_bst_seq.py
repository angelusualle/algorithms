from copy import deepcopy
class Node():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

# O(n^2) where n is number of nodes time, O(d) depth space complexity
def gen_bst_seq(node):
    if node is None:
        return None
    left_pos = gen_bst_seq(node.left_child)
    right_pos = gen_bst_seq(node.right_child)
    partial_seq = []
    if left_pos is None and right_pos is None:
        partial_seq.append([node.data])
    elif right_pos is None:
        for perm in left_pos:
            perm.insert(0, node.data)
            partial_seq.append(perm)
    elif left_pos is None:
        for perm in right_pos:
            perm.insert(0, node.data)
            partial_seq.append(perm)
    else:
        for pos in left_pos:
            for pos_r in right_pos:
                pos_merge = pos[:]
                pos_merge.extend(pos_r[:])
                pos_merge.insert(0,node.data)
                partial_seq.append(pos_merge)
                pos_merge = pos_r[:]
                pos_merge.insert(0,node.data)
                pos_merge.extend(pos[:])
                partial_seq.append(pos_merge)
    return partial_seq