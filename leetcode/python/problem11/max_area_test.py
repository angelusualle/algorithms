import unittest
from max_area import max_area

class Test_Case_Max_Area(unittest.TestCase):
    def test_max_area(self):
        self.assertEqual(max_area([1,8,6,2,5,4,8,3,7]), 49)

if __name__ == '__main__':
    unittest.main()