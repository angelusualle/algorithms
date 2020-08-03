import unittest
from multiply import multiply

class Test_Case_Multiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(10,10), 100)
        self.assertEqual(multiply(10,0), 0)
        self.assertEqual(multiply(10,1), 10)