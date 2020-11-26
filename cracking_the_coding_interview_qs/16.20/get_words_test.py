import unittest
from get_words import Number_Pad_To_Words

class Test_Case_Get_Words(unittest.TestCase):
    def test_get_words(self):
        converter = Number_Pad_To_Words(['tree', 'used', 'pots'])
        self.assertListEqual(converter.get_num_to_words(8733), ['tree', 'used'])