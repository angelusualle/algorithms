import unittest
from get_longest_palindrome import get_longest_palindrome

class Test_Case_Get_Longest_Palindrome(unittest.TestCase):
    def test_get_longest_palindrome(self):
        self.assertEqual(get_longest_palindrome("babad"), "bab")

if __name__ == "__main__":
    unittest.main()