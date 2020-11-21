import unittest
from find_in_sorted_matrix import find_in_sorted_matrix

class Test_Case_Find_In_Sorted_Matrix(unittest.TestCase):
    def test_find_in_sorted_matrix(self):
        self.assertTupleEqual(find_in_sorted_matrix([
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20]
        ], 5), (0,4))
        self.assertTupleEqual(find_in_sorted_matrix([
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20]
        ], 10), (1,4))
