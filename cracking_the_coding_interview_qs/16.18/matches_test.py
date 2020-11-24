import unittest
from matches import matches

class Test_Case_Matches(unittest.TestCase):
    def test_matches(self):
        self.assertTrue(matches('aabab', 'catcatgocatgo'))