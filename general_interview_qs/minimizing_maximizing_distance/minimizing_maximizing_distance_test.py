import unittest
from minimizing_maximizing_distance import get_minimized_maximum_distance, place_k_elements_in_arr_pos_to_maximize_minimum_distance, place_k_elements_in_arr_pos_to_minimize_maximum_distance

class Test_Minimizing_Maximizing_distance(unittest.TestCase):
    def test_place_k_elements_to_maximize_minimum_distance(self):
        self.assertEqual(place_k_elements_in_arr_pos_to_maximize_minimum_distance([0,1,99,100], 2, 20), 50)
        self.assertEqual(place_k_elements_in_arr_pos_to_maximize_minimum_distance([3,5,6,9,1,8], 3, 20), 4)
    def test_place_k_elements_in_arr_pos_to_minimize_maximum_distance(self):
        self.assertAlmostEqual(place_k_elements_in_arr_pos_to_minimize_maximum_distance([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9, 20), 0.5, 4)
    def test_place_k_elements_to_maximize_minimum_distance(self):
        self.assertAlmostEqual(get_minimized_maximum_distance([0,1,99,100], 2), 0.5, 4)
