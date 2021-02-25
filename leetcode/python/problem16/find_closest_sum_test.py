import unittest
from find_closest_sum import find_closest_sum

class Test_Case_Find_Closest_Sum(unittest.TestCase):
    def test_find_closest_sum(self):
        self.assertEqual(find_closest_sum([-1,2,1,-4], 2), 2)

if __name__ == '__main__':
    unittest.main()