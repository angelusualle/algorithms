import unittest
from check_solution import check_solution

class Test_Case_Check_Solution(unittest.TestCase):
    def test_check_solution(self):
        self.assertTupleEqual(check_solution('RGBY', 'GGRR'), (1,1))