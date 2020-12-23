import unittest
from insert_spaces import insert_spaces

class Test_Case_Insert_Spaces(unittest.TestCase):
    def test_insert_spaces(self):
        self.assertEqual(insert_spaces('mydogtimeatslotsofcats', set(['my', 'dog', 'eats', 'lots', 'of', 'cats']))[1], ' my dog tim eats lots of cats ')

if __name__ == '__main__':
    unittest.main()