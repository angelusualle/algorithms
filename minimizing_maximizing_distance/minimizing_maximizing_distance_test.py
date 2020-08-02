import unittest
from minimizing_maximizing_distance import get_minimized_maximum_distance

class Test_Minimizing_Maximizing_distance(unittest.TestCase):
    def test_place_k_elements_to_maximize_minimum_distance(self):
        self.assertAlmostEqual(get_minimized_maximum_distance([0,1,99,100], 2), 0.5, 4)
