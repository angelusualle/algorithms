class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self, root):
        self.root = root
    def in_order_traversal(self):
        ans = []
        self.in_order_traversal_node(self.root, ans)
        return ans
    def in_order_traversal_node(self, node, ans):
        if node is None:
            return
        self.in_order_traversal_node(node.left, ans)
        ans.append(node.data)
        self.in_order_traversal_node(node.right, ans)
    def pre_order_traversal(self):
        ans = []
        self.pre_order_traversal_node(self.root, ans)
        return ans
    def pre_order_traversal_node(self, node, ans):
        if node is None:
            return
        ans.append(node.data)
        self.pre_order_traversal_node(node.left, ans)
        self.pre_order_traversal_node(node.right, ans)
    def post_order_traversal(self):
        ans = []
        self.post_order_traversal_node(self.root, ans)
        return ans
    def post_order_traversal_node(self, node, ans):
        if node is None:
            return
        self.post_order_traversal_node(node.left, ans)
        self.post_order_traversal_node(node.right, ans)
        ans.append(node.data)