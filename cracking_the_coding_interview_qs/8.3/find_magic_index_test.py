from find_magic_index import find_magic_index
import unittest

class Test_Case_Find_Magic_Index(unittest.TestCase):
    def test_find_magic_index(self):
        self.assertEqual(find_magic_index([-33, -10, 2, 40, 50, 60,70]), 2)
        self.assertIsNone(find_magic_index([1,2,3,4]))