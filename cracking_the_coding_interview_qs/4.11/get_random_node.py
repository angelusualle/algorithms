import random

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self, root):
        self.root = root
        self.size = 1
    def insert_in_order(self, data):
        self.insert_in_order_recurse(data, self.root)
    def insert_in_order_recurse(self, data, node):
        if data <= node.data:
            if node.left is None:
                node.left = Node(data)
                self.size += 1
            else:
                self.insert_in_order_recurse(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
                self.size += 1
            else:
                self.insert_in_order_recurse(data, node.right)
    def delete(self, node_to_delete, current_node):
        if current_node is None:
            return
        if node_to_delete == self.root:
            self.root = None
            size -= 1
            return
        if current_node.left == node_to_delete:
            current_node.left = None
            size -= 1
            return
        if current_node.right == node_to_delete:
            current_node.right = None
            size -= 1
            return
        self.delete(node_to_delete, current_node.left)
        self.delete(node_to_delete, current_node.right)
    def get_random_node(self):
        ans = None
        steps = random.randint(0, self.size-1)
        return self.get_random_node_recurse(self.root, 0, steps)
    def get_random_node_recurse(self, node, num, steps):
        if node is None:
            return num-1, None
        if num == steps:
            return num, node
        num, left= self.get_random_node_recurse (node.left, num +1, steps)
        if left is not None:
            return num, left
        num, right = self.get_random_node_recurse (node.right, num +1, steps)
        if right is not None:
            return num, right
        return num, None