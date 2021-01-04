import unittest
from word_transform import word_transform

class Test_Case_Word_Transform(unittest.TestCase):
    def test_word_transform(self):
        self.assertEqual(word_transform('DAMP', 'LIKE', {}, set(['DAMP', 'LIKE', 'LAMP', 'LIMP', 'LIME'])), 'DAMP-> LAMP-> LIMP-> LIME-> LIKE')