import unittest
from get_sorted_arrays_med import get_sorted_arrays_med

class Test_Case_Get_Sorted_Arrays_Med(unittest.TestCase):
    def test_get_sorted_arrays_med(self):
        self.assertEqual(get_sorted_arrays_med([1,3], [2]), 2)

if __name__ == "__main__":
    unittest.main()