import unittest
from letter_combinations_dial_pad import letter_combinations_dial_pad

class Test_Case_Letter_Combinations(unittest.TestCase):
    def test_letter_combinations_dial_pad(self):
        self.assertListEqual(letter_combinations_dial_pad("23"), ["ad","bd","cd","ae","be","ce","af","bf","cf"])

if __name__ == "__main__":
    unittest.main()