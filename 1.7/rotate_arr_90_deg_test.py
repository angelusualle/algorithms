import unittest
from rotate_arr_90_deg import rotate_arr_90_deg

class Test_Case_Rotate_Arr_90_Deg(unittest.TestCase):
    def test_rotate_arr_90_deg(self):
        self.assertEqual(rotate_arr_90_deg([[1,2,3], [4,5,6], [7,8,9]]), [[7,4,1], [8,5,2], [9,6,3]])