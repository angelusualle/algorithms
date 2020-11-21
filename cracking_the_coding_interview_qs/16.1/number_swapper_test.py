import unittest
from number_swapper import number_swapper

class Test_Case_Number_Swapper(unittest.TestCase):
    def test_number_swapper(self):
        self.assertTupleEqual((4,5),number_swapper(5,4))