import unittest
from get_max_sub_square import get_max_sub_square


class Test_Case_Get_Max_Sub_Square(unittest.TestCase):
    def test_get_max_sub_square(self):
        self.assertListEqual(get_max_sub_square([
            ['w', 'w', 'b', 'b', 'w'],
            ['b', 'w', 'b', 'b', 'w'],
            ['w', 'w', 'w', 'b', 'b'],
            ['b', 'b', 'b', 'w', 'w'],
            ['b', 'w', 'w', 'w', 'w'] ]), [(0, 2), (1, 3)])