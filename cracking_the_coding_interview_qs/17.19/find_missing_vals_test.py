import unittest
from find_missing_vals import find_missing_vals

class Test_Case_Find_Missing_Vals(unittest.TestCase):
    def test_find_missing_vals(self):
        self.assertEqual(find_missing_vals(10, [1,2,3,4,5,6,8,9,10]), 7)
        self.assertTupleEqual(find_missing_vals(10, [1,3,5,6,7,8,9,10]), (2,4))

if __name__ == '__main__':
    unittest.main()