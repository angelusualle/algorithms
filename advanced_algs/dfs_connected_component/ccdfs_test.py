import unittest
from ccdfs import ccdfs

class Test_Case_CCDfs(unittest.TestCase):
    def test_ccdfs(self):
        self.assertEqual(str(ccdfs({'a': ['c', 'b'],
          'b': ['a','c'],
          'c': ['b', 'a'],
          'd': ['e', 'f'],
          'e': ['d', 'f'],
          'f': ['e', 'd']})), "{'a': (1, True), 'c': (1, True), 'b': (1, True), 'e': (2, True), 'd': (2, True), 'f': (2, True)}")

if __name__ == '__main__':
    unittest.main()