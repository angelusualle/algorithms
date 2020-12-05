import unittest
from calculator import calculator


class Test_Case_Calculator(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(calculator('2*3+4-6/2'), '7.0')


if __name__ == '__main__':
    unittest.main()