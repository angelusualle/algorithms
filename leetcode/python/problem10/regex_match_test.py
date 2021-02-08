import unittest
from regex_match import regex_match

class Test_Case_Regex_Match(unittest.TestCase):
    def test_regex_match(self):
        self.assertTrue(regex_match("aabbcc", "a*b*c*"))

if __name__ == '__main__':
    unittest.main()