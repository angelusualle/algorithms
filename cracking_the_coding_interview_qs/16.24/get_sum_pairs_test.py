import unittest
from get_sum_pairs import get_sum_pairs

class Test_Get_Sum_Pairs(unittest.TestCase):
    def test_get_sum_pairs(self):
        self.assertEqual(str(get_sum_pairs([5,4,3,8,1, 7, 2], 9)), '[(4, 5), (1, 8), (2, 7)]')

if __name__ == '__main__':
    unittest.main()