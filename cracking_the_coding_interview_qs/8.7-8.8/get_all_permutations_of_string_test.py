import unittest
from get_all_permutations_of_string import get_all_permutations_of_string, get_all_permutations_of_string_with_dups

class Test_Case_Get_All_Permutations_Of_String(unittest.TestCase):
    def test_get_all_permutations_of_string(self):
        self.assertListEqual(get_all_permutations_of_string("tea"), ['tea', 'eta', 'ate', 'tae', 'eat', 'aet'])
    def test_get_all_permutations_of_string_with_dups(self):
        self.assertListEqual(get_all_permutations_of_string_with_dups("aaa"), ['aaa'])
        self.assertListEqual(get_all_permutations_of_string_with_dups("teat"), ['ttea', 'ttae', 'teta', 'teat', 'tate', 'taet', 'etta', 'etat', 'eatt', 'atte', 'atet', 'aett'])