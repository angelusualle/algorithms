import unittest
from is_num_palindrome import is_num_palindrome

class Test_Case_Is_Num_Palindrome(unittest.TestCase):
    def test_is_num_palindrome(self):
        self.assertTrue(is_num_palindrome(121))
        self.assertFalse(is_num_palindrome(35))

if __name__ == '__main__':
    unittest.main()