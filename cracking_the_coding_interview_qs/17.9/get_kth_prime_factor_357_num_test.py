import unittest
from get_kth_prime_factor_357_num import get_kth_prime_factor_357_num

class Test_Case_Get_Kth_Prime_Factor_357_Num(unittest.TestCase):
    def test_get_kth_prime_factor_357_num(self):
        self.assertEqual(get_kth_prime_factor_357_num(5), 9)
        self.assertEqual(get_kth_prime_factor_357_num(6), 15)

if __name__ == '__main__':
    unittest.main()