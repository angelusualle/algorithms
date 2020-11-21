import unittest
from print_8_queens import print_8_queens

class Test_Case_print_8_queens(unittest.TestCase):
    def test_print_8_queens(self):
        num_ans = [0]
        print_8_queens(num_ans=num_ans)
        self.assertEqual(num_ans[0], 92)