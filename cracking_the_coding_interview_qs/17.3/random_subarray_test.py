import unittest
from random_subarray import random_subarray

class Test_Case_Random_Subarray(unittest.TestCase):
    def test_random_subarray(self):
        arrs = []
        for i in range(100000):
            arrs.append(random_subarray([1,2,3], 2))
        self.assertAlmostEqual(len([x for x in arrs if x[0] == 1 and x[1] == 2]) / len(arrs), 0.3333, delta=0.01)

if __name__ == '__main__':
    unittest.main()