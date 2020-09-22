import unittest
from get_all_lens import get_all_lens

class Test_Case_Get_All_Lens(unittest.TestCase):
    def test_get_all_lens(self):
        self.assertListEqual(get_all_lens(3, 5, 3), [9, 11, 13, 15])
        self.assertListEqual(get_all_lens(3, 3, 3), [9])