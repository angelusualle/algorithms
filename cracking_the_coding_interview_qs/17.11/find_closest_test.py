import unittest
from find_closest import find_closest, precomute_word_to_position

class Test_Case_Find_Closest(unittest.TestCase):
    def test_find_closest(self):
        pre = precomute_word_to_position(['the', 'dog', 'that', 'eats', 'fast', 'runs', 'fast', 'and', 'is', 'a', 'fast', 'dog'])
        self.assertEqual(find_closest('fast', 'dog', pre), 1)

if __name__ == '__main__':
    unittest.main()
