import unittest
from double_index_max_subsequence import double_index_max_subsequence

class Test_Case_Double_Index_Max_Subsequence(unittest.TestCase):
    def test_double_index_max_subsequence(self):
        self.assertEqual("[(56, 90), (60, 95), (65, 100), (68, 110), (70, 150), (75, 190)]", str(double_index_max_subsequence([(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)])))