import unittest
from find_max_dist_optimal_k_post_offices_n_families import find_max_dist_optimal_k_post_offices_n_families

class Test_Case_Find_Max_Dist_Optimal_K_Post_Offices_N_Families(unittest.TestCase):
    def test_find_max_dist_optimal_k_post_offices_n_families(self):
        self.assertTrue(abs(find_max_dist_optimal_k_post_offices_n_families([0, 1, 99, 100], 2) - 0.5) < 0.1)
        self.assertTrue(abs(find_max_dist_optimal_k_post_offices_n_families([0, 2, 98, 100], 2) - 1) < 0.1)
        self.assertTrue(abs(find_max_dist_optimal_k_post_offices_n_families([0, 1, 100], 1) - 25) < 0.1)