import unittest
from min_span_tree_kruskal import min_span_tree_kruskal


class Test_Case_Min_Span_Tree_Kruskal(unittest.TestCase):
    def test_min_span_tree_kruskal(self):
        self.assertEqual(str(min_span_tree_kruskal({
            'a': [('c', 1), ('b', 4), ('d', 3)],
            'b': [('a', 4), ('c', 4), ('d', 4)],
            'c': [('a', 1), ('b', 4), ('d', 2), ('f', 4)],
            'd': [('a', 3), ('c', 2), ('b', 4), ('f', 6)],
            'f': [('c', 4), ('d', 6), ('e', 5)],
            'e': [('f', 5)]
        })), "[(1, 'a', 'c'), (2, 'c', 'd'), (4, 'a', 'b'), (4, 'c', 'f'), (5, 'e', 'f')]")


if __name__ == '__main__':
    unittest.main()
