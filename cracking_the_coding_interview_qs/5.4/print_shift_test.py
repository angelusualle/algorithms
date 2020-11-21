from print_shift import print_shift
import unittest

class Test_Case_Unit_Test_Print_Shift(unittest.TestCase):
    def test_print_shift(self):
        self.assertTupleEqual(print_shift(5), (6,3))