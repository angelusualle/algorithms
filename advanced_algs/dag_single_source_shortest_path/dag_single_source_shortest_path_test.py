import unittest
from dag_single_source_shortest_path import dag_single_source_shortest_path

class Test_Case_Dag_Single_Source_Shortest_Path(unittest.TestCase):
    def test_dag_single_source_shortest_path(self):
        graph = {
            'S': [('A', 1), ('C', 2)],
            'A': [('B', 6)],
            'C': [('A', 4), ('D', 3)],
            'B': [('D', 1), ('E', 2)],
            'D': [('E', 1)],
            'E': []
        }
        sorted_vertexes, dist, parent, _ = dag_single_source_shortest_path('S', graph)
        self.assertListEqual(sorted_vertexes, ['S', 'C', 'A', 'B', 'D', 'E'])
        self.assertListEqual(dist, [0, 2, 1, 7, 5, 6])
        self.assertListEqual(parent, ['-', 'S', 'S', 'A', 'C', 'D'])

if __name__ == '__main__':
    unittest.main()