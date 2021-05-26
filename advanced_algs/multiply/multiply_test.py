import unittest
from multiply import multiply

class Test_Case_Multiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(5,10), 50)
        self.assertEqual(multiply(6,10), 60)

if __name__ == '__main__':
    unittest.main()