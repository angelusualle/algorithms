import json
class Node():
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

def serialize_bst(root):
    return json.dumps(serialize_bst_recursive(root))
def serialize_bst_recursive(root):
    return root and (root.value, serialize_bst_recursive(root.left_child), serialize_bst_recursive(root.right_child))


def deserialize_bst(data):
    return deserialize_bst_recursive(json.loads(data))
def deserialize_bst_recursive(data):
    if data:
        root = Node(data[0])
        root.left_child = deserialize_bst_recursive(data[1])
        root.right_child = deserialize_bst_recursive(data[2])
        return root