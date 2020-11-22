import unittest
from get_sort_indexes import get_sort_indexes

class Test_Case_Get_Sort_Indexes(unittest.TestCase):
    def test_get_sort_indexes(self):
        self.assertTupleEqual(get_sort_indexes([1,3,4,2,5,6,7]), (1,3))

if __name__ == '__main__':
    unittest.main()