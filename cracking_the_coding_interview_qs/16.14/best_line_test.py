import unittest
from best_line import best_line

class Test_Case_Best_Line(unittest.TestCase):
    def test_best_line(self):
        self.assertEqual(best_line([(0, 1), (1, 2), (2, 3), (-5, 5)]), '1.0:1.0')