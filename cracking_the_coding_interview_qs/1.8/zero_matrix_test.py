import unittest
from zero_matrix import zero_matrix

class Test_Case_Zero_Matrix(unittest.TestCase):
    def test_zero_matrix(self):
        self.assertEqual(zero_matrix([[1,2,3,4], [5,6,7,8], [9,0,11,12]]),[[1,0,3,4], [5,0,7,8], [0,0,0,0]])

if __name__ == "__main__":
    unittest.main()