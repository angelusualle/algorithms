import unittest
from count_boolean_parenthesis import count_boolean_parenthesis

class Test_Case_Count_Boolean_Parenthesis(unittest.TestCase):
    def test_count_boolean_parenthesis(self):
        self.assertEqual(count_boolean_parenthesis("1^0|0|1", False), 2)