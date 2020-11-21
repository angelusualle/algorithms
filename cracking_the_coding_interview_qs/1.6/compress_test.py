import unittest
from compress import compress

class Test_Case_Compress(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(compress('aabcccccaaa'), 'a2b1c5a3')
        self.assertEqual(compress('abc'), 'abc')
        self.assertEqual(compress('AbC'), 'AbC')
        self.assertEqual(compress('aAbBcC'), 'aAbBcC')
        self.assertEqual(compress('AAaaBBCC'), 'AAaaBBCC')

if __name__ == '__main__':
    unittest.main()