import unittest
from ccdfsdirected import ccdfsdirected

class Test_Case_Ccdfsdirected(unittest.TestCase):
    def test_ccdfsdirected(self):
        self.assertEqual(str(ccdfsdirected({'a': ['c', 'b'],
        'b': ['a','c'],
        'c': ['b', 'a'],
        'd': ['e', 'f'],
        'e': ['d', 'f'],
        'f': ['e', 'd']})), "{'a': (1, 6, True), 'c': (2, 5, True), 'b': (3, 4, True), 'e': (7, 12, True), 'd': (8, 11, True), 'f': (9, 10, True)}")


if __name__ == '__main__':
    unittest.main()