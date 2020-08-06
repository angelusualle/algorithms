import unittest
from search_through_rotated_array import search_through_rotated_array

class Test_Case_Search_Through_Rotated_Array(unittest.TestCase):
    def test_search_through_rotated_array(self):
        arr = [50, 5, 10, 15, 20]
        val = 15
        self.assertEqual(search_through_rotated_array(arr, val),3)
        arr = [10, 15, 20, 50, 5]
        val = 10
        self.assertEqual(search_through_rotated_array(arr, val),0)
        arr = [20, 50, 5, 10, 15]
        val = 20
        self.assertEqual(search_through_rotated_array(arr, val),0)