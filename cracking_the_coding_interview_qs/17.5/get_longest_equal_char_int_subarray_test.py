import unittest
from get_longest_equal_char_int_subarray import get_longest_equal_char_int_subarray

class Test_Case_Get_Longest_Equal_Char_Int_Subarray(unittest.TestCase):
    def test_get_longest_equal_char_char_int_subarray(self):
        self.assertListEqual(get_longest_equal_char_int_subarray(['a', 'b', 'c', 'd', 1, 2, 3]), ['b', 'c', 'd', 1, 2, 3])
        self.assertListEqual(get_longest_equal_char_int_subarray(['a', 'b', 'c', 'd', 1, 2, 'z']), ['d', 1, 2,'z'])