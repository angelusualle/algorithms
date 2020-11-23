import unittest
from get_max_cont import get_max_cont

class Test_Case_Get_Max_Cont(unittest.TestCase):
    def test_get_max_cont(self):
        self.assertEqual(get_max_cont([2,3,-8,-1,2,4,-2,3]), 7)
        self.assertEqual(get_max_cont([-1,-2,-3,-4]), -1)