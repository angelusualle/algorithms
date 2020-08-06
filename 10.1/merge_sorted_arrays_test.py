from merge_sorted_arrays import merge_sorted_arrays
import unittest

class Test_Case_Merge_Sorted_Arrays(unittest.TestCase):
    def test_merge_sorted_arrays(self):
        test = [0,1,3,17,20,50]
        test2 = [1, 20, 21, 22, 27, 80]
        ans = merge_sorted_arrays(test, test2)
        self.assertListEqual(ans, [0, 1, 1, 3, 17, 20, 20, 21, 22, 27, 50, 80])