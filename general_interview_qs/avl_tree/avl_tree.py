class AVL_Tree():
    
    class Node():
        def __init__(self, val):
            self.height = 0
            self.val = val
            self.left_child = None
            self.right_child = None
            self.parent = None

    def __init__(self):
        self.head = None
    
    def insert(self, val):
        if self.head is None:
            self.head = AVL_Tree.Node(val)
            return
        insertion_node = AVL_Tree.Node(val)
        iterator = self.head
        while True:
            if val > iterator.val and iterator.right_child is not None:
                iterator = iterator.right_child
                continue
            if val <= iterator.val and iterator.left_child is not None:
                iterator = iterator.left_child
                continue
            if val > iterator.val:
                iterator.right_child = insertion_node
                insertion_node.parent = iterator
                break
            else:
                iterator.left_child = insertion_node
                insertion_node.parent = iterator
                break
        if iterator.left_child is None and iterator.right_child is None:
            iterator.height = 0
        elif iterator.left_child is None:
            iterator.height = iterator.right_child.height + 1
        elif iterator.right_child is None:
            iterator.height = iterator.left_child.height + 1
        else:
            iterator.height = max(iterator.left_child.height, iterator.right_child.height) + 1 
        # propogate heights
        iterator = insertion_node
        self.propogate_heights(iterator)
        # do rotations as needed

        while iterator is not None:
            left = 0
            if iterator.left_child is not None:
                left = iterator.left_child.height
            right = 0
            if iterator.right_child is not None:
                right = iterator.right_child.height
            bal = left - right
            if abs(bal) <= 1:
                iterator = iterator.parent
                continue

            if bal > 0:
                old_left_child = iterator.left_child
                if iterator.left_child.right_child is not None:
                    iterator.left_child = iterator.left_child.right_child
                    iterator.left_child.parent = iterator

                    old_left_child.parent = iterator.left_child
                    old_left_child.right_child = iterator.left_child.left_child
                    if old_left_child.right_child is not None:
                        old_left_child.right_child.parent = old_left_child
                    iterator.left_child.left_child  = old_left_child
                # right rotation
                if iterator.parent is not None and iterator.parent.left_child == iterator:
                    iterator.parent.left_child = iterator.left_child
                    iterator.left_child.parent = iterator.parent
                elif iterator.parent is not None and iterator.parent.right_child == iterator:
                    iterator.parent.right_child = iterator.right_child
                    iterator.left_child.parent = iterator.parent
                else:
                    iterator.left_child.parent = None
                    self.head = iterator.left_child
                ol =  iterator.left_child
                iterator.left_child = iterator.left_child.right_child
                if iterator.left_child is not None:
                    iterator.left_child.parent = iterator              

                iterator.parent = ol
                ol.right_child = iterator
            else:
                # left rotation
                old_right_child = iterator.right_child

                iterator.right_child = iterator.right_child.left_child
                iterator.right_child.parent = iterator

                old_right_child.parent = iterator.right_child
                iterator.right_child.right_child  = old_right_child

                old_left_child.left_child = iterator.left_child.left_child
                old_left_child.left_child.parent = old_right_child
                    
                # right rotation
                if iterator.parent is not None and iterator.parent.right_child == iterator:
                    iterator.parent.right_child = iterator.right_child
                    iterator.right_child.parent = iterator.parent
                elif iterator.parent is not None and iterator.parent.left_child == iterator:
                    iterator.parent.left_child = iterator.left_child
                    iterator.right_child.parent = iterator.parent
                else:
                    iterator.right_child.parent = None
                iterator.right_child = iterator.right_child.left_child
                iterator.right_child.parent = iterator              
                
                iterator.parent = iterator.right_child
                itereator.parent.left_child = iterator
            self.propogate_heights(iterator)



    def propogate_heights(self, node):
        iterator = node
        while True:
            left = -1
            if iterator.left_child is not None:
                left = iterator.left_child.height
            right = -1
            if iterator.right_child is not None:
                right = iterator.right_child.height
            iterator.height = max(left, right) + 1
            if iterator == self.head:
                break
            else:
                iterator = iterator.parent
    
    def print_tree(self, node=None, level=0, ans=[]):
        if node is None:
            node = self.head
        if node.right_child is not None:
            self.print_tree(node.right_child, level + 1, ans)
        ans.append('\t'*level+str(node.val))
        if node.left_child is not None:
            self.print_tree(node.left_child, level + 1, ans)   
        return ans
