from minimum_stack import Minimum_Stack
import unittest

class Test_Case_Minimum_Stack(unittest.TestCase):
    def test_minimum_stack(self):
        stack = Minimum_Stack()
        stack.push(23)
        stack.push(45)
        stack.push(3)
        stack.push(100)
        self.assertEqual(stack.min(), 3)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.min(), 23)