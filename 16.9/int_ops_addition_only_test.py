import unittest
from int_ops_addition_only import multiply, subtract, divide

class Test_Case_Int_Ops_Addition_Only(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(5,10), 50)
    def test_divide(self):
        self.assertEqual(divide(3,1), 3)
    def test_subtract(self):
        self.assertEqual(subtract(10,7), 3)