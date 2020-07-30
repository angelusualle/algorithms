import unittest
from generate_prime_numbers import is_prime, generate_prime_numbers

class Test_Case_Generate_Prime_Numbers(unittest.TestCase):
    def test_generate_prime_numbers(self):
        ans = generate_prime_numbers(100)
        print(len(ans))
        for answer in ans:
            self.assertTrue(is_prime(answer))

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(15))
        self.assertTrue(is_prime(47))