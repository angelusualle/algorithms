import unittest
from is_permutation import is_permutation

class Test_Case_Is_Permutation(unittest.TestCase):
    def test_is_permutation(self):
        self.assertTrue(is_permutation('cat', 'act'))
        self.assertTrue(is_permutation('catt', 'actt'))
        self.assertFalse(is_permutation('cazz', 'actt'))
        self.assertFalse(is_permutation('', ''))
        self.assertFalse(is_permutation('ab', ''))

if __name__ == '__main__':
    unittest.main()