import unittest
from get_continous_median import Get_Continous_Median

class Test_Case_Get_Continous_Median(unittest.TestCase):
    def test_get_continous_median(self):
        tracker = Get_Continous_Median()
        for i in range(1, 8):
            tracker.add_num(i)
        self.assertEqual(tracker.get_median(), 4)

if __name__ == '__main__':
    unittest.main()