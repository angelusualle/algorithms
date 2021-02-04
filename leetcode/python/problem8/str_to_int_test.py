import unittest
from str_to_int import str_to_int

class Test_Case_Str_To_Int(unittest.TestCase):
    def test_str_to_int(self):
        self.assertEqual(str_to_int("413"), 413)

if __name__ == "__main__":
    unittest.main()