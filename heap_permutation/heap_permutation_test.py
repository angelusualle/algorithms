import unittest
from heap_permutation import heap_permutation

class Test_Case_Heap_Permutation(unittest.TestCase):
    def test_heap_permutation(self):
        ans = []
        heap_permutation([1,2,3,4], 4, 4, ans)
        self.assertListEqual(ans,[[1, 2, 3, 4], [2, 1, 3, 4], [3, 2, 1, 4], [2, 3, 1, 4], [1, 2, 3, 4], [2, 1, 3, 4], [4, 2, 3, 1], [2, 4, 3, 1], [3, 2, 4, 1], [2, 3, 4, 1], [4, 2, 3, 1], [2, 4, 3, 1], [4, 1, 3, 2], [1, 4, 3, 2], [3, 1, 4, 2], [1, 3, 4, 2], [4, 1, 3, 2], [1, 4, 3, 2], [4, 1, 2, 3], [1, 4, 2, 3], [2, 1, 4, 3], [1, 2, 4, 3], [4, 1, 2, 3], [1, 4, 2, 3]])