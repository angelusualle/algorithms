import unittest
from trie import Trie

class Test_Case_Trie(unittest.TestCase):
    def test_trie(self):
        trie = Trie()
        trie.add_word("apple")
        trie.add_word("fats")
        self.assertTrue(trie.valid_prefix("ap"))
        self.assertFalse(trie.valid_prefix("az"))