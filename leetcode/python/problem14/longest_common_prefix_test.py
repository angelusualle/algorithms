import unittest
from longest_common_prefix import longest_common_prefix

class Test_Case_Longest_Common_Prefix(unittest.TestCase):
    def test_longest_common_prefix(self):
        self.assertEqual(longest_common_prefix(["flower","flow","flight"]), "fl")

if __name__ == "__main__":
    unittest.main()