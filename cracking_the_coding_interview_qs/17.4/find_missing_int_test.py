import unittest
from find_missing_int import find_missing_int

class Test_Case_Find_Missing_Int(unittest.TestCase):
    def test_find_missing_int(self):
        self.assertEqual(find_missing_int([0,1,3,4,5,6,7,8], 8), 2)
        self.assertEqual(find_missing_int([0,1,2,3,5,6,7,8,9], 9), 4)
        self.assertEqual(find_missing_int(range(0,20), 20), 20)

if __name__ == '__main__':
    unittest.main()