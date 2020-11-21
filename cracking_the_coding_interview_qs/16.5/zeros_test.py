import unittest
from zeros import zeros

class Test_Case_Zeros(unittest.TestCase):
    def test_zeros(self):
        self.assertEqual(zeros(19), 3)