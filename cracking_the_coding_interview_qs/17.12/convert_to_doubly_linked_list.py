class Node():
    def __init__(self, val):
        self.n1 = None
        self.n2 = None
        self.val = val

def convert_to_doubly_linked_list_(root, left=True):
    if root is None or (root.n1 is None and root.n2 is None):
        return root
    l = convert_to_doubly_linked_list_(root.n1)
    if l is not None:
        l.n2 = root
        root.n1 = l
    r = convert_to_doubly_linked_list_(root.n2, False)
    if r is not None:
        root.n2 = r
        r.n1 = root
    if left:
        if r is None:
            return root
        else:
            return r
    else:
        if l is None:
            return root
        else:
            return l
# O(N) time, O(logN) space
def convert_to_doubly_linked_list(root):
    root = convert_to_doubly_linked_list_(root)
    n = root
    while n.n1 is not None:
        n = n.n1
    return n