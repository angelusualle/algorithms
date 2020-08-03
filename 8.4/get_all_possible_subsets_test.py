import unittest
from get_all_possible_subsets import get_all_possible_subsets

class Test_Case_Get_All_Possible_Subsets(unittest.TestCase):
    def test_get_all_possible_subsets(self):
        ans = get_all_possible_subsets(set([1,2,3,4]))
        self.assertListEqual(ans, [set(), {4}, {3}, {3, 4}, {2}, {2, 4}, {2, 3}, {2, 3, 4}, {1}, {1, 4}, {1, 3}, {1, 3, 4}, {1, 2}, {1, 2, 4}, {1, 2, 3}, {1, 2, 3, 4}])
