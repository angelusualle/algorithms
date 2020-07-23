import unittest
from graph import Graph, Node

class Test_Case_Graph(unittest.TestCase):
    def test_graph_dfs(self):
        graph = Graph()
        graph.nodes.append(Node(1))
        graph.nodes[0].children.append(Node(2))
        graph.nodes.append(Node(2))
        graph.nodes[0].children[0].children.append(Node(4))
        graph.nodes.append(Node(4))
        graph.nodes[0].children.append(Node(3))
        graph.nodes.append(Node(3))
        arr = []
        graph.DFS(arr)
        self.assertListEqual(arr, [1,2,4,3])
    def test_graph_bfs(self):
        graph = Graph()
        graph.nodes.append(Node(1))
        node = Node(2)
        graph.nodes[0].children.append(node)
        graph.nodes.append(node)
        node = Node(4)
        graph.nodes[0].children[0].children.append(node)
        graph.nodes.append(node)
        node = Node(3)
        graph.nodes[0].children.append(node)
        graph.nodes.append(node)
        arr = graph.BFS()
        self.assertListEqual(arr, [1,2,3,4])