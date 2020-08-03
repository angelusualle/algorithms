import unittest
from get_all_possible_subsets import get_all_possible_subsets

class Test_Case_Get_All_Possible_Subsets(unittest.TestCase):
    def test_get_all_possible_subsets(self):
        ans = get_all_possible_subsets(set([1,2,3,4]))
        print(ans)
