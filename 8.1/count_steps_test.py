import unittest
from count_steps import count_steps

class Test_Case_Count_Steps(unittest.TestCase):
    def test_count_steps(self):
        self.assertEqual(count_steps(3), 4)
        self.assertEqual(count_steps(4), 7)