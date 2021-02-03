import unittest
from reverse_int import reverse_int

class Test_Case_Reverse_Int(unittest.TestCase):
    def test_reverse_int(self):
        self.assertEqual(reverse_int(321), 123)

if __name__ == '__main__':
    unittest.main()