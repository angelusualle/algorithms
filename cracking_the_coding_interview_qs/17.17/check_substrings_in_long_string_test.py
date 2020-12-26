import unittest
from check_substrings_in_long_string import check_substrings_in_long_string

class Test_Case_Check_Substrings_In_Long_String(unittest.TestCase):
    def test_check_substrings_in_long_string(self):
        self.assertSetEqual(check_substrings_in_long_string('mississippi', ['is', 'ppi', 'hi', 'sis', 'i', 'ssippi']), {'is', 'ssippi', 'sis', 'i', 'ppi'})

if __name__ == '__main__':
    unittest.main()