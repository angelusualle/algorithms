import unittest
from get_max_minutes import get_max_minutes

class Test_Case_Get_Max_Minutes(unittest.TestCase):
    def test_get_max_minutes(self):
        self.assertEqual(get_max_minutes([30, 15, 60, 75, 45, 15, 15, 45]), 180)

if __name__ == '__main__':
    unittest.main()