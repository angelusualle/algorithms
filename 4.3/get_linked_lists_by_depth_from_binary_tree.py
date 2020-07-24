class Linked_List():
    def __init__(self, head):
        self.head = head

class List_Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Tree_Node():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def get_linked_lists_by_depth_from_binary_tree(root):
    depth_linked_list_store = {}
    get_linked_list_by_depth_for_node(root, 0, depth_linked_list_store)
    return depth_linked_list_store

def get_linked_list_by_depth_for_node(node, level, store):
    if level not in store:
        store[level] = Linked_List(List_Node(node.data))
    else:
        next_one = store[level].head
        while next_one.next is not None:
            next_one = next_one.next
        next_one.next = List_Node(node.data)
    if node.left_child is not None:
        get_linked_list_by_depth_for_node(node.left_child, level + 1, store)
    if node.right_child is not None:
        get_linked_list_by_depth_for_node(node.right_child, level + 1, store)
    