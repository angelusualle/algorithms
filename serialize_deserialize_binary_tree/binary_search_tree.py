class Node():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def serialize_bst(root):
    return root and (root.value, serialize_bst(root.left_child), serialize_bst(root.right_child))

def deserialize_bst(data):
    if data:
        root = Node(data[0])
        root.left_child = deserialize_bst(data[1])
        root.right_child = deserialize_bst(data[2])
        return root