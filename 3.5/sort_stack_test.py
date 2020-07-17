from sort_stack import sort_stack
import unittest

class Test_Case_Sort_Stack(unittest.TestCase):
    def test_sort_stack(self):
        stack = [5,4,3,1,2]
        self.assertListEqual(sort_stack(stack), sorted(stack, reverse=True))