import unittest
from longest_symmetric_subsequence import longest_palindromic_subsequence

class Test_Case_Longest_Symmetric_Subsequence(unittest.TestCase):
    def test_longest_symmetric_subsequence(self):
        self.assertEqual(longest_palindromic_subsequence('abcdaf'), 3)

if __name__ == '__main__':
    unittest.main()