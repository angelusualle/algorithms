import unittest
from minimizing_maximizing_distance import get_minimized_maximum_distance, place_k_elements_in_arr_pos_to_maximize_minimum_distance

class Test_Minimizing_Maximizing_distance(unittest.TestCase):
    def test_place_k_elements_to_maximize_minimum_distance(self):
        self.assertEqual(place_k_elements_in_arr_pos_to_maximize_minimum_distance([0,1,99,100], 2, 10), 50)
        self.assertEqual(place_k_elements_in_arr_pos_to_maximize_minimum_distance([3,5,6,9,1,8], 3, 20), 4)
    def test_place_k_elements_to_maximize_minimum_distance(self):
        self.assertAlmostEqual(get_minimized_maximum_distance([0,1,99,100], 2), 0.5, 4)
