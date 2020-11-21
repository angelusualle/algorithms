from find_funcs import find_val, find_last_in_series
import unittest

class Test_Case_Find_Funcs(unittest.TestCase):
    def test_find_val(self):
        self.assertEqual(find_val([1,2,3,4,5,6,7], 5), 4)
    def test_find_first_in_series(self):
        self.assertEqual(find_last_in_series([1,2,3,4,5,6,7], lambda x: x <= 5), 4) 