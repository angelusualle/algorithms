import unittest
from sparse_similarity import sparse_similarity

class Test_Case_Sparse_Similarity(unittest.TestCase):
    def test_sparse_similarity(self):
        self.assertListEqual(sparse_similarity(
            {
                'ID1': {1,3,4,5,6,7},
                'ID2': {23, 4, 6, 7, 8, 9, 10},
                'ID3': {8, 9, 10 , 11, 23},
                'ID4': {67, 34, 52, 699, 800},
            }), ['ID1 to ID2 : 0.300000', 'ID2 to ID3 : 0.500000', 'ID2 to ID1 : 0.300000', 'ID3 to ID2 : 0.500000'])

if __name__ == '__main__':
    unittest.main()