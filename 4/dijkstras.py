import heapq

class Node:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.children = []

class Graph:
    def __init__(self):
        self.nodes = []
    def shortest_path(self, node1, node2):
        q = []
        heapq.heapify(q)
        dist_table = {}
        for node in self.nodes:
            dist_table[node] = {
                                'distance' : float('inf'),
                                'parent': None
                                }
        dist_table[node1]['distance'] = 0
        heapq.heappush(q, (0, 0, node1))
        while len(q) > 0:
            (dist, _, node) = heapq.heappop(q)
            for i, child in enumerate(node.children):
                if not child.visited:
                    heapq.heappush(q, (dist + 1, i, child))
                if dist_table[child]['distance'] > dist + 1:
                    dist_table[child]['distance'] = dist + 1
                    dist_table[child]['parent'] = node
            node.visited = True
        ans = []
        ans.append(node2)
        next_node = dist_table[node2]['parent']
        while next_node is not node1:
            ans.append(next_node)
            next_node = dist_table[next_node]['parent']
        ans.append(node1)
        return ans