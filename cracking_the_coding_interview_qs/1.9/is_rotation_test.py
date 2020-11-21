import unittest
from is_rotation import is_rotation

class Test_Case_Is_Rotation(unittest.TestCase):
    def test_is_rotation(self):
        self.assertTrue(is_rotation('meerkat', 'atmeerk'))
        self.assertFalse(is_rotation('meerkat', 'atmeer'))

if __name__ == '__main__':
    unittest.main()