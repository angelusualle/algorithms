import unittest
from get_all_permutations_of_string import get_all_permutations_of_string, get_all_permutations_of_string_with_dups

class Test_Case_Get_All_Permutations_Of_String(unittest.TestCase):
    def test_get_all_permutations_of_string(self):
        self.assertListEqual(get_all_permutations_of_string_with_dups("tea"), ['tea', 'eta', 'aet', 'eat', 'tea', 'eta'])