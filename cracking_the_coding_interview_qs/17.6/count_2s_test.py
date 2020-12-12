import unittest
from count_2s import count_2s

class Test_Case_Count_2s(unittest.TestCase):
    def test_count_2s(self):
        self.assertEqual(count_2s(30), 13)


if __name__ == '__main__':
    unittest.main()