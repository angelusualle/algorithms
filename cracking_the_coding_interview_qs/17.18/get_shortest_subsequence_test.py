from get_shortest_subsequence import get_shortest_subsequence
import unittest

class Test_Case_Get_Shortest_Subsequence(unittest.TestCase):
    def test_get_shortest_subsequence(self):
        self.assertTupleEqual(get_shortest_subsequence([1,5,9], [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]), (7,10))

if __name__ == '__main__':
    unittest.main()

