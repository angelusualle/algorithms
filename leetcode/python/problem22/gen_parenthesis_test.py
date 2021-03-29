import unittest
from gen_parenthesis import gen_parenthesis

class Test_Case_Gen_Parenthesis(unittest.TestCase):
    def test_gen_parenthesis(self):
        ans = []
        gen_parenthesis([], 0, 6, ans)
        self.assertListEqual(ans, ['()()()', '()(())', '(())()', '(()())', '((()))'])

if __name__ == '__main__':
    unittest.main()