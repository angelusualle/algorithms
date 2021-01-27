import unittest
from get_longest_unique_substring import get_longest_unique_substring

class Test_Case_Get_Longest_Unique_Substring(unittest.TestCase):
    def test_get_longest_unique_substring(self):
        self.assertEqual(get_longest_unique_substring("abcabcbb"), 3)

if __name__ == "__main__":
    unittest.main()