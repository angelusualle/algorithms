import unittest
from make_change import make_change

class Test_Case_Make_Change(unittest.TestCase):
    def test_make_change(self):
        self.assertEqual(make_change(10), 4)
        self.assertEqual(make_change(100), 242)