import unittest
from get_max_height import get_max_height

class Test_Case_Get_Max_Height(unittest.TestCase):
    def test_get_max_height(self):
        ans = [0]
        get_max_height([(1,5,3), (3,4,5), (6,7,8)], max_height=ans)
        self.assertEqual(ans[0], 13)