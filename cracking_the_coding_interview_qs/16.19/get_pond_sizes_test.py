import unittest
from get_pond_sizes import get_pond_sizes

class Test_Case_Get_Pond_Sizes(unittest.TestCase):
    def test_get_pond_sizes(self):
        self.assertListEqual(get_pond_sizes([
            [0,2,1,0],
            [0,1,0,1],
            [1,1,0,1],
            [0,1,0,1]
        ]), [2,4,1])