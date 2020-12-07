import unittest
from add import add

class Test_Case_Add(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(30,25), 55)
        self.assertEqual(add(10,11), 21)

if __name__ == '__main__':
    unittest.main()