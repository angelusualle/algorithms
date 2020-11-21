from half_square import half_square
import unittest

class Test_Case_Half_Square(unittest.TestCase):
    def test_half_square(self):
        self.assertEqual(half_square(((0,0), (1, 1)),((0,2), (1,3))), ((0.5, 0.5), (0.5, 2.5)))