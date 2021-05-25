import unittest
from can_make_change import can_make_change

class Test_Case_Can_Make_Change(unittest.TestCase):
    def test_can_make_change(self):
        self.assertTrue(can_make_change([5,7], 35))
        self.assertFalse(can_make_change([5,10], 12))

if __name__ == '__main__':
    unittest.main()