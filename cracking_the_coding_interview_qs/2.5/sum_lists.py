class Linked_List():
    def __init__(self, head):
        self.head = head

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

# O(n) time and O(n) space
def sum_lists_fwd(linked_list1, linked_list2):
    node1 = linked_list1.head
    node2 = linked_list2.head
    result = []
    sum_nodes(node1, node2, result)
    result_list = Linked_List(Node(None))
    result_node = result_list.head
    while len(result) > 0:
        result_node.data = result.pop()
        if len(result) > 0:
            result_node.next = Node(None)
            result_node = result_node.next
    return result_list

def sum_nodes(node1, node2, result):
    if node1 is None and node2 is None:
        return 0
    elif node1 is None and node2 is not None:
        result.append(node2.data)
        sum_nodes(node1, node2.next, result)
        return 0
    elif node2 is None and node1 is not None:
        result.append(node1.data)
        sum_nodes(node1, node1.next, result)
        return 0
    else:
        carry_over = sum_nodes(node1.next, node2.next, result)
        result_num = node1.data + node2.data + carry_over
        if result_num > 9:
            result.append(result_num % 10)
            return 1
        else:
            result.append(result_num)
            return 0
    

# O(n) time and O(1) space
def sum_lists_bwd(linked_list1, linked_list2):
    carry_over = 0
    linked_result = Linked_List(None)
    linked_result.head = Node(None)
    result = linked_result.head
    node_1 = linked_list1.head
    node_2 = linked_list2.head
    while node_1 is not None or node_2 is not None:
        sum_carry = False
        new_val = -1
        if node_1 is None:
            new_val = node_2.data
        elif node_2 is None:
            new_val = node_1.data
        else:
            the_sum = node_1.data + node_2.data
            if the_sum > 9:
                sum_carry = True
                new_val = the_sum % 10
            else:
                new_val = the_sum
        if carry_over == 1:
            new_val += 1
            if not sum_carry:
                carry_over = 0
        if sum_carry:
            carry_over = 1
        result.data = new_val
        if node_1.next is not None or node_2.next is not None:
            result.next = Node(None)
            result = result.next
        if node_1 is not None:
            node_1 = node_1.next
        if node_2 is not None:
            node_2 = node_2.next
    return linked_result