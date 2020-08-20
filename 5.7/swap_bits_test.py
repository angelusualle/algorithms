import unittest
from swap_bits import swap_bits

class Test_Case_Swap_Bits(unittest.TestCase):
    def test_swap_bits(self):
        self.assertEqual(swap_bits(5), 10)