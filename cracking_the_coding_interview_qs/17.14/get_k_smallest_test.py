import unittest
from get_k_smallest import get_k_smallest

class Test_Case_Get_K_Smallest(unittest.TestCase):
    def test_get_k_smallest(self):
        self.assertListEqual(get_k_smallest(3, list(range(30))), [0,1,2])

if __name__ == '__main__':
    unittest.main()