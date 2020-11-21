class Node():
    def __init__(self, val):
        self.val = val
        self.right_child = None
        self.left_child = None
        self.left_size = 0

# O log(n) where n is nodes
def insert(val, root):
    next_one = root
    while next_one is not None:
        if val <= next_one.val:
            if next_one.left_child is None:
                next_one.left_child = Node(val)
                next_one.left_size += 1
                next_one = None
            else:
                next_one = next_one.left_child
        else:
            if next_one.right_child is None:
                next_one.right_child = Node(val)
                next_one = None
            else:
                next_one = next_one.right_child
# O log(n) where n is nodes
def get_rank(val, node):
    if node is None:
        return 0
    if node.val == val:
        return get_rank(val, node.left_child) + 1
    elif node.val > val:
        return get_rank(val, node.left_child)
    else:
        return get_rank(val, node.left_child) + 1 + get_rank(val,node.right_child)
