class Node():
    def __init__(self, val):
        self.val = val
        self.adjacent_nodes = []
        self.visited = False

# O(E^d) where d is depth
def word_transform(w1, w2, dictionary):
    # make dictionary into linked list
    start_node = Node(w1)
    end_node = Node(w2)
    nodes = [start_node, end_node]
    nodes_dict = {start_node.val: start_node, end_node.val: end_node}
    while nodes:
        node = nodes.pop()
        word = node.val
        for w in dictionary:
            if w == word:
                continue
            diff = 0
            for i in range(len(word)):
                if w[i] != word[i]:
                    diff += 1
            if diff == 1:
                if w not in nodes_dict:
                    nodes_dict[w] = Node(w)
                    nodes.append(nodes_dict[w])
                node.adjacent_nodes.append(nodes_dict[w])
    nodes = [start_node]
    path = []
    while nodes:
        node = nodes.pop()
        if node == end_node:
            path.append(node.val)
            return ''.join(path)
        path.append(node.val + ' -> ')
        node.visited = True
        for c in node.adjacent_nodes:
            if not c.visited:
                nodes.append(c)
    return None