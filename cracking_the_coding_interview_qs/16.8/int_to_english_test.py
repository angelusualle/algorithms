import unittest
from int_to_english import int_to_english

class Test_Case_Int_To_English(unittest.TestCase):
    def test_int_to_english(self):
        self.assertEqual('one thousand one hundred fourty four ', int_to_english(1144))
        self.assertEqual('negative one thousand one hundred fourty four ', int_to_english(-1144))
        self.assertEqual('one billion one hundred fourty four ', int_to_english(1000144))