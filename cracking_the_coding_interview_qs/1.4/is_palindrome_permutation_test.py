import unittest
from is_palindrome_permutation import is_palindrome_permutation

class Test_Case_Is_Palindrome_Permutation(unittest.TestCase):
    def test_is_palindrom_permutation(self):
        self.assertTrue(is_palindrome_permutation("Taco cat"))
        self.assertFalse(is_palindrome_permutation("Taco zcat"))
        self.assertTrue(is_palindrome_permutation("oo tt"))
        self.assertFalse(is_palindrome_permutation("bedroom"))
        self.assertTrue(is_palindrome_permutation("racecar"))