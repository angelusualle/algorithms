import unittest
from get_str_zig_zagged import get_str_zig_zagged

class Test_Case_Get_Str_Zig_Zagged(unittest.TestCase):
    def test_get_str_zig_zagged(self):
        self.assertEqual(get_str_zig_zagged("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

if __name__ == "__main__":
    unittest.main()