from flip_bit_to_win import flip_bit_to_win
import unittest

class Test_Case_Flip_Bit_To_Win(unittest.TestCase):
    def test_flip_bit_to_win(self):
        self.assertEqual(flip_bit_to_win(1775), 8)