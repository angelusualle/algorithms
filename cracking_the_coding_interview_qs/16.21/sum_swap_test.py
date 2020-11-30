import unittest
from sum_swap import sum_swap

class Test_Case_Sum_Swap(unittest.TestCase):
    def test_sum_swap(self):
        self.assertTupleEqual(sum_swap([4,1,2,1,1,2], [3,6,3,3]), (0,1))