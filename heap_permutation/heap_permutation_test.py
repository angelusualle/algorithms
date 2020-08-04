import unittest
from heap_permutation import heap_permutation

class Test_Case_Heap_Permutation(unittest.TestCase):
    def test_heap_permutation(self):
        ans = []
        heap_permutation([1,2,3], 3, 3, ans)
        self.assertListEqual(ans, [[1, 2, 3], [2, 1, 3], [3, 1, 2], [1, 3, 2], [2, 3, 1], [3, 2, 1]])
