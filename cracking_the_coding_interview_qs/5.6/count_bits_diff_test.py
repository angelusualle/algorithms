from count_bits_diff import count_bits_diff
import unittest

class Test_Case_Count_Bits_Diff(unittest.TestCase):
    def test_count_bits_diff(self):
        self.assertEqual(count_bits_diff(29, 15), 2)