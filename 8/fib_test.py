from fib import fib
import unittest

class Test_Case_Fib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(10), 55)