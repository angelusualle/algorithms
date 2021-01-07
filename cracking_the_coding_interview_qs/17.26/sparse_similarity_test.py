import unittest
from sparse_similarity import sparse_similarity

class Test_Case_Sparse_Similarity(unittest.TestCase):
    def test_sparse_similarity(self):
        print(sparse_similarity(
            {
                'ID1': {1,3,4,5,6,7},
                'ID2': {23, 4, 6, 7, 8, 9, 10},
                'ID3': {8, 9, 10 , 11, 23},
                'ID4': {67, 34, 52, 699, 800},
            }))