class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

# O(n)
def find_successor_of_node_in_bst(node):
    if node.right_child is not None:
        next_one = node.right_child
        while next_one.left_child is not None:
            next_one = next_one.left_child
        return next_one
    next_one = node.parent
    while next_one == next_one.parent.right_child:
        next_one = next_one.parent
    return next_one.parent