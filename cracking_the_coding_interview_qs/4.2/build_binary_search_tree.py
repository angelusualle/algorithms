class Node():
    def __init__(self, d):
        self.data = d
        self.left_child = None
        self.right_child = None

def build_binary_search_tree(arr):
    if len(arr) == 1:
        return Node(arr[0])
    mid = len(arr) // 2
    node = Node(arr[mid])
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