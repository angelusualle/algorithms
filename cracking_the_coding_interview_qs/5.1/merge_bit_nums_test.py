import bitarray
import unittest
from merge_bit_nums import merge_bit_nums

class Test_Case_Merge_Bit_Nums(unittest.TestCase):
    def test_merge_bit_nums(self):
        num1 = bitarray.bitarray(32)
        num1.setall(0)
        num2 = bitarray.bitarray(5)
        num2.setall(1)
        ans = merge_bit_nums(num1, num2, 20, 24)
        self.assertEqual(str(bitarray.bitarray('0000000000000000000011111000000000000')), str(ans))