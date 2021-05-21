import unittest
from get_longest_increasing_subsequence import get_longest_increasing_subsequence

class Test_Case_Longest_Increasing_Subsequence(unittest.TestCase):
    def test_get_ongest_increasing_subsequence(self):
        nums = [5,2,8,6,3,6,9,7]
        self.assertListEqual(get_longest_increasing_subsequence(nums)[0], [6, 5, 4, 1, '-'])