class Red_Black_Tree():
    class Node():
        def __init__(self, val, color='red'):
            self.val = val
            self.parent = None
            self.left_child = None
            self.right_child = None
            self.color = color
    
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        if self.head is None:
            self.head = Red_Black_Tree.Node(val)
            self.head.left_child = Red_Black_Tree.Node(None, color='black')
            self.head.left_child.parent = self.head
            self.head.right_child = Red_Black_Tree.Node(None, color='black')
            self.head.right_child.parent = self.head
            return
        iterator = self.head
        while True:
            if iterator.val <= val and iterator.right_child.val is None:
                insertion_node = iterator.right_child
                insertion_node.val = val
                insertion_node.color = 'red'
                insertion_node.left_child = Red_Black_Tree.Node(None, color='black')
                insertion_node.left_child.parent = insertion_node
                insertion_node.right_child = Red_Black_Tree.Node(None, color='black')
                insertion_node.right_child.parent = insertion_node
                break
            elif iterator.val > val and iterator.left_child.val is None:
                insertion_node = iterator.left_child
                insertion_node.val = val
                insertion_node.color = 'red'
                insertion_node.left_child = Red_Black_Tree.Node(None, color='black')
                insertion_node.left_child.parent = insertion_node
                insertion_node.right_child = Red_Black_Tree.Node(None, color='black')
                insertion_node.right_child.parent = insertion_node
                break
            elif iterator.val <= val:
                iterator = iterator.right_child
                continue
            else:
                iterator = iterator.left_child
                continue
        # fix violations from placement
        if (insertion_node == self.head.left_child or insertion_node == self.head.right_child) and self.head.color == 'red' and insertion_node.color == 'red':
            self.head.color = 'black'
            return
        if insertion_node.color == 'red' and insertion_node.parent.color == 'red':
            uncle = None
            if insertion_node.parent.parent.left_child == insertion_node.parent:
                uncle = insertion_node.parent.parent.right_child
            else:
                uncle = insertion_node.parent.parent.left_child
            if uncle.color == 'red':
                if insertion_node.parent.color == 'red':
                    insertion_node.parent.color = 'black'
                else:
                    insertion_node.parent.color = 'red'
                uncle.color == 'black'
                if insertion_node.parent.parent.color == 'red':
                    insertion_node.parent.parent.color = 'black'
                else:
                    insertion_node.parent.parent.color = 'red'
            else:
                # uncle is black
                # parent is left child of grand parent and new node is left_child of its parent
                if insertion_node.parent.left_child == insertion_node and insertion_node.parent == insertion_node.parent.parent.left_child:
                    if insertion_node.parent.parent.color == 'red':
                        insertion_node.parent.parent.color = 'black'
                    else:
                        insertion_node.parent.parent.color = 'red'
                    if insertion_node.parent.color == 'red':
                        insertion_node.parent.color = 'black'
                    else:
                        insertion_node.parent.color = 'red' 
                    if insertion_node.parent.parent == self.head:
                        self.head = insertion_node.parent
                    insertion_node.parent.parent.left_child = insertion_node.parent.right_child
                    insertion_node.parent.parent.left_child.parent = insertion_node.parent.parent

                    insertion_node.parent.right_child = insertion_node.parent.parent
                    gparent_parent = insertion_node.parent.parent.parent 
                    insertion_node.parent.parent.parent = insertion_node.parent

                    insertion_node.parent.parent = gparent_parent
                    return
                if insertion_node.parent.right_child == insertion_node and insertion_node.parent == insertion_node.parent.parent.left_child:
                    if insertion_node.parent.parent.color == 'red':
                        insertion_node.parent.parent.color = 'black'
                    else:
                        insertion_node.parent.parent.color = 'red'
                    if insertion_node.color == 'red':
                        insertion_node.color = 'black'
                    else:
                        insertion_node.color = 'red' 
                    if insertion_node.parent.parent == self.head:
                        self.head = insertion_node
                    insertion_node.parent.right_child = insertion_node.left_child
                    insertion_node.parent.right_child.parent = insertion_node.parent
                    
                    insertion_node.parent.parent.left_child = insertion_node.right_child
                    insertion_node.parent.parent.left_child.parent = insertion_node.parent.parent

                    insertion_node.left_child = insertion_node.parent
                    insertion_node.right_child = insertion_node.parent.parent

                    gparent_parent = insertion_node.parent.parent.parent
                    if gparent_parent.left_child == insertion_node.parent.parent:
                        gparent_parent.left_child = insertion_node
                    else:
                        gparent_parent.right_child = insertion_node
                    insertion_node.parent = gparent_parent
                    return
                if insertion_node.parent.right_child == insertion_node and insertion_node.parent == insertion_node.parent.parent.right_child:
                    if insertion_node.parent.parent.color == 'red':
                        insertion_node.parent.parent.color = 'black'
                    else:
                        insertion_node.parent.parent.color = 'red'
                    if insertion_node.parent.color == 'red':
                        insertion_node.parent.color = 'black'
                    else:
                        insertion_node.parent.color = 'red' 
                    if insertion_node.parent.parent == self.head:
                        self.head = insertion_node.parent
                    insertion_node.parent.parent.right_child = insertion_node.parent.left_child
                    insertion_node.parent.parent.right_child.parent = insertion_node.parent.parent

                    insertion_node.parent.left_child = insertion_node.parent.parent
                    gparent_parent = insertion_node.parent.parent.parent 
                    insertion_node.parent.parent.parent = insertion_node.parent

                    insertion_node.parent.parent = gparent_parent
                    return
                if insertion_node.parent.left_child == insertion_node and insertion_node.parent == insertion_node.parent.parent.right_child:
                    if insertion_node.parent.parent.color == 'red':
                        insertion_node.parent.parent.color = 'black'
                    else:
                        insertion_node.parent.parent.color = 'red'
                    if insertion_node.color == 'red':
                        insertion_node.color = 'black'
                    else:
                        insertion_node.color = 'red' 
                    if insertion_node.parent.parent == self.head:
                        self.head = insertion_node
                    insertion_node.parent.left_child = insertion_node.right_child
                    insertion_node.parent.left_child.parent = insertion_node.parent
                    
                    insertion_node.parent.parent.right_child = insertion_node.left_child
                    insertion_node.parent.parent.right_child.parent = insertion_node.parent.parent

                    insertion_node.right_child = insertion_node.parent
                    insertion_node.left_child = insertion_node.parent.parent

                    gparent_parent = insertion_node.parent.parent.parent
                    if gparent_parent.right_child == insertion_node.parent.parent:
                        gparent_parent.right_child = insertion_node
                    else:
                        gparent_parent.left_child = insertion_node
                    insertion_node.parent = gparent_parent
                    return
    def print_tree(self, node=None, level=0, ans=[]):
        if node is None:
            node = self.head
        if node.right_child is not None:
            self.print_tree(node.right_child, level + 1, ans)
        ans.append('\t'*level+str(node.val) + ' ' + node.color)
        if node.left_child is not None:
            self.print_tree(node.left_child, level + 1, ans)   
        return ans
