import unittest
from random_subarray import random_subarray

class Test_Case_Random_Subarray(unittest.TestCase):
    def test_random_subarray(self):
        arrs = []
        for i in range(100000):
            arrs.append(random_subarray([1,2,3], 2))
        print(len([x for x in arrs if x[0] == 1 and x[1] == 2]) / len(arrs))

if __name__ == '__main__':
    unittest.main()