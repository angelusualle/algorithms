from collections import deque

class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.visited = False
class Graph():
    def __init__(self):
        self.nodes = []
    def DFS(self, arr):
        if len(self.nodes) == 0:
            return
        for node in self.nodes:
            self.dfs_search(node, arr)
    def dfs_search(self, node, arr):
        arr.append(node.data)
        node.visited = True
        for child in node.children:
            if not node.visited:
                self.dfs_search(child, arr)
    def BFS(self):
        arr = []
        if len(self.nodes) == 0:
            return
        for node in self.nodes:
            if not node.visited:
                self.bfs_search(node, arr)
        return arr
    def bfs_search(self, node, arr):
        q = deque()
        q.append(node)
        while len(q) > 0:
            next_node = q.popleft()
            if next_node.visited:
                continue
            next_node.visited = True
            arr.append(next_node.data)
            for child in next_node.children:
                if not child.visited:
                    q.append(child)