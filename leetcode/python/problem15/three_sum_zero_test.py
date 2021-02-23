import unittest
from three_sum_zero import three_sum_zero

class Test_Case_Three_Sum_Zero(unittest.TestCase):
    def test_three_sum_zero(self):
        self.assertListEqual(three_sum_zero([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])

if __name__ == '__main__':
    unittest.main()