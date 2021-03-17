import unittest
from is_valid_parenthesis import is_valid_parenthesis

class Test_Case_Is_Valid_Parenthesis(unittest.TestCase):
    def test_is_valid_parenthesis(self):
        self.assertTrue(is_valid_parenthesis('(())'))
        self.assertFalse(is_valid_parenthesis('(]()'))

if __name__ == '__main__':
    unittest.main()