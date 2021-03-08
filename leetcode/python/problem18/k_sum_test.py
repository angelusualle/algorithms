import unittest
from k_sum import k_sum

class Test_Case_K_Sum(unittest.TestCase):
    def test_k_sum(self):
        self.assertListEqual(k_sum([1,0,-1,0,-2,2], 0, 4), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])

if __name__ == '__main__':
    unittest.main()