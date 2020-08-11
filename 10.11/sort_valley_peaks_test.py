import unittest
from sort_valley_peaks import sort_valley_peaks

class Test_Case_Sort_Valley_Peaks(unittest.TestCase):
    def test_sort_valley_peaks(self):
        arr = [5,3,1,2,3]
        sort_valley_peaks(arr)
        self.assertListEqual(arr, [3, 5, 1, 3, 2])