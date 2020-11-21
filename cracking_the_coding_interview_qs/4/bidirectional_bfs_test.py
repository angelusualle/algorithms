from bidirectional_bfs import find_shortest_path_bi_dfs
import unittest

class Test_Case_Bidirectional_Bfs(unittest.TestCase):
    def test_find_shortest_path_bi_dfs(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'A'],
            'C': ['E', 'A'],
            'D': ['F', 'B'],
            'E': ['G', 'C'],
            'G': ['Z', 'E'],
            'F': ['H', 'D'],
            'Z': ['P', 'G'],
            'P': ['Z', 'H'],
            'H': ['I', 'F', 'P'],
            'I': []
        }
        start = 'A'
        end = 'I'
        ans = find_shortest_path_bi_dfs(graph, start, end)
        self.assertEqual(ans, ['A', 'B', 'D', 'F', 'H', 'I'])