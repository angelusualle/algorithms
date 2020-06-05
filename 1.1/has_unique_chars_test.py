import unittest
from has_unique_chars import has_unique_chars


class Test_Case_Is_Unique_Chars(unittest.TestCase):
    def test_is_unique_chars(self):
        self.assertTrue(has_unique_chars(''))
        self.assertTrue(has_unique_chars('taco'))
        self.assertFalse(has_unique_chars('ttaco'))
        self.assertFalse(has_unique_chars('taaco'))
        self.assertFalse(has_unique_chars('tacoo'))

if __name__ == '__main__':
    unittest.main()