import unittest
from get_intersection import get_intersection

class Test_Case_Get_Intersection(unittest.TestCase):
    def test_get_intersection(self):
        self.assertTupleEqual(get_intersection([(0,0), (10,10)], [(10,0), (0,10)]), (5,5))