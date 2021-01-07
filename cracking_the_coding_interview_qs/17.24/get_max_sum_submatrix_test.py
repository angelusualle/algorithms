import unittest
from get_max_sum_submatrix import get_max_sum_submatrix

class Test_Case_Get_Max_Sum_Submatrix(unittest.TestCase):
    def test_get_max_sum_submatrix(self):
        self.assertTupleEqual(get_max_sum_submatrix([
            [9, -8, 1, 3, 2],
            [-3, 7, 6, -2, 4], 
            [6, -4, -4, 8, -7] 
        ]), (19, 0, 4))