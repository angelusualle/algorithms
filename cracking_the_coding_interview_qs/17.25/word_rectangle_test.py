import unittest
from word_rectangle import word_rectangle

class Test_Case_Word_Rectangle(unittest.TestCase):
    def test_word_rectangle(self):
        self.assertTupleEqual(word_rectangle(['anonymous', 'mouses', 'peanut', 'pea', 'ee', 'pp', 'aa']), (6, ['peanut'], (0, 3)))


if __name__ == '__main__':
    unittest.main()