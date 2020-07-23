from dijkstras import Node, Graph
import unittest

class Test_Case_Dijkstras(unittest.TestCase):
    def test_dijkstras(self):
        root = Node(1)
        root.children.append(Node(2))
        end = Node(6)
        root.children.append(end)
        root.children[0].children.append(Node(3))
        root.children[0].children[0].children.append(Node(4))
        root.children[0].children[0].children[0].children.append(end)
        graph = Graph()
        graph.nodes.append(root)
        graph.nodes.append(root.children[0])
        graph.nodes.append(root.children[0].children[0])
        graph.nodes.append(root.children[0].children[0].children[0])
        graph.nodes.append(end)
        ans = graph.shortest_path(root, root.children[0].children[0].children[0])
        ans_list = []
        while len(ans) > 0:
            ans_list.append(ans.pop().data)
        self.assertListEqual(ans_list, [1,2,3,4])
        ans = graph.shortest_path(root, end)
        ans_list = []
        while len(ans) > 0:
            ans_list.append(ans.pop().data)
        self.assertListEqual(ans_list, [1,6])