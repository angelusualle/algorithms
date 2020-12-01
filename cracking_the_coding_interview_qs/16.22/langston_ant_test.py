import unittest
from langston_ant import langston_ant

class Test_Case_Langston_Ant(unittest.TestCase):
    def test_langston_ant(self):
        self.assertListEqual(langston_ant(5), [['b', 'w', 'b', 'b', 'w'], ['w', 'b', 'b', 'w', 'w'], ['b', 'w', 'w', 'w', 'b'], ['w', 'b', 'w', 'b', 'w'], ['b', 'w', 'b', 'w', 'b']])