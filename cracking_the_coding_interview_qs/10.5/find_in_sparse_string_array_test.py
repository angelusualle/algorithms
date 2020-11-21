import unittest
from find_in_sparse_string_array import find_in_sparse_string_array

class Test_Case_Find_In_Sparse_String_Array(unittest.TestCase):
    def test_find_in_sparse_string_array(self):
        arr = ['cats','', '', 'are', 'not', '', '', '', 'as', '', '', '', 'great', 'as', '', '', 'dogs']
        self.assertEqual(find_in_sparse_string_array(arr, 'are'), 3)
        self.assertEqual(find_in_sparse_string_array(arr, 'great'), 12)