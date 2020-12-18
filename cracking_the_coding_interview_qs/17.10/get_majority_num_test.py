import unittest
from get_majority_num import get_majority_num

class Test_Case_Get_Majority_Num(unittest.TestCase):
    def test_get_majority_num(self):
        self.assertEqual(get_majority_num([1,4,5,8,5,5,5]), 5)

if __name__ == '__main__':
    unittest.main()