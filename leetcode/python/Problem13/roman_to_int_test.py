import unittest
from roman_to_int import roman_to_int

class Test_Case_Roman_To_Int(unittest.TestCase):
    def test_roman_to_int(self):
        self.assertEqual(roman_to_int('MMM'), 3000)

if __name__ == '__main__':
    unittest.main()