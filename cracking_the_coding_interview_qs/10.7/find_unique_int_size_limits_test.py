from find_unique_int_size_limits import find_unique_int_size_limits
import unittest

class Test_Case_Find_Unique_Int_Size_Limits(unittest.TestCase):
    def test_find_unique_int_size_limits(self):
        print(find_unique_int_size_limits([[1,2,3,4], [3,4,5,6,7]]))
        self.assertEqual(find_unique_int_size_limits([[1,2,3,4], [3,4,5,6,7]]), 0)