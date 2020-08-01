import unittest
from place_k_elements_to_maximize_minimum_distance import place_k_elements_to_maximize_minimum_distance

class Test_Case_Find_Max_Dist_Optimal_K_Post_Offices_N_Families(unittest.TestCase):
    def test_place_k_elements_to_maximize_minimum_distance(self):
        print(place_k_elements_to_maximize_minimum_distance([3,5,6,9,1,8], 3, 20))