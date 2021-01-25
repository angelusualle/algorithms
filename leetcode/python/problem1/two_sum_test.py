import unittest
from two_sum import two_sum

class Test_Case_Two_Sum(unittest.TestCase):
    def test_two_sum(self):
        self.assertTupleEqual(two_sum([10,5,7,20,3,8,4], 12), (2,1))

if __name__ == "__main__":
    unittest.main()