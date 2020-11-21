import unittest
from group_anagrams import group_anagrams

class Test_Case_Group_Anagrams(unittest.TestCase):
    def test_group_anagrams(self):
        words = ['dream', 'of', 'you', 'are', 'like', 'maerd', 'rea', 'ekil', 'fo']
        ans = group_anagrams(words)
        self.assertListEqual(ans, ['dream', 'maerd', 'of', 'fo', 'you', 'are', 'rea', 'like', 'ekil'])