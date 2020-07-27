from get_build_order import get_build_order
import unittest

class Test_Case_Get_Build_Order(unittest.TestCase):
    def test_get_build_order(self):
        self.assertEqual(get_build_order({
            'A': {'B', 'C'},
            'B': {},
            'C': {'B'}
        }), ['B', 'C', 'A'])