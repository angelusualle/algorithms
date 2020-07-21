import unittest
from min_heap import Min_Heap

class Test_Case_Min_Heap(unittest.TestCase):
    def test_min_heap(self):
        heap = Min_Heap()
        heap.insert(1)
        heap.insert(2)
        heap.insert(3)
        heap.insert(4)
        heap.insert(5)
        self.assertListEqual(heap.arr, [1,2,3,4,5])
        heap.insert(-1)
        self.assertListEqual(heap.arr, [-1,2,1,4,5,3])
        self.assertEqual(heap.extract_min(), -1)
        heap.print_heap()
        self.assertEqual(heap.extract_min(), 1)
        heap.print_heap()
if __name__ == '__main__':
    unittest.main()