class Node():
    def __init__(self, d):
        self.d = d
        self.right_child = None
        self.left_child = None
        self.parent = None

# O(d) where d is depth time and O(1) space
def find_first_ancestor(node1, node2):
    depth1 = -1
    next1 = node1
    depth2 = -1
    next2 = node2
    while next1 is not None:
        depth1 += 1
        next1 = next1.parent
    while next2 is not None:
        depth2 += 1
        next2 = next2.parent
    diff = abs(depth1 - depth2)
    next1 = node1
    next2 = node2
    if depth1 > depth2:
        i = 0
        while i < diff:
            next1 = next1.parent
            i += 1
    else:
        i = 0
        while i < diff:
            next2 = next2.parent
            i += 1
    while next1 is not None and next2 is not None:
        if next1 == next2:
            return next1
        else:
            next1 = next1.parent
            next2 = next2.parent
    return None

"""
# O(d^2) time where d is depth and O(1) space
def find_first_ancestor(node1, node2):
    fast = node1
    slow = node2
    while slow is not None:
        while fast is not None:
            if slow == fast:
                return slow
            fast = fast.parent
        slow = slow.parent
        fast = node1
    return None
"""