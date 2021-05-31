import unittest
from get_median import get_median

class Test_Case_Get_Median(unittest.TestCase):
        def test_get_median(self):
            self.assertEqual(get_median([5,6,7,9,1,2,3]), 5)
            self.assertEqual(get_median([90, 100, 78, 89, 67]), 89)

if __name__ == '__main__':
    unittest.main()