import unittest
from smallest_difference import smallest_difference

class Test_Case_Smallest_Difference(unittest.TestCase):
    def test_smallest_difference(self):
        self.assertEqual(smallest_difference([1,3,15,11,2], [23,127,235,19,8]), 3)