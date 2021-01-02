from histo_volume import histo_volume
import unittest

class Test_Case_Histo_Volume_Test(unittest.TestCase):
    def test_histo_volume(self):
        self.assertEqual(histo_volume([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]), 26)

if __name__ == '__main__':
    unittest.main()