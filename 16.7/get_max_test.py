import unittest
from get_max import get_max

class Test_Get_Max(unittest.TestCase):
    def test_get_max(self):
        self.assertEqual(get_max(5, 10), 10)
        self.assertEqual(get_max(5, 1), 5)
        self.assertEqual(get_max(-5, 1), 1)
        self.assertEqual(get_max(1, -1), 1)
        self.assertEqual(get_max(-5, 10), 10)
        self.assertEqual(get_max(-5, -10), -5)