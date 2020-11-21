import unittest
from sorting_algs import bucket_sort_age, Person, bubble_sort, selection_sort, merge_sort, quick_sort

class Test_Case_Sorting_Algs(unittest.TestCase):
    def test_bucket_sort(self):
        people = [Person(99, 'Nancy'), Person(104, 'Peter'), Person(0, 'AJ'), Person(10, 'Bibby')]
        ans = bucket_sort_age(people)
        self.assertTrue(ans[0].age == 0)

    def test_bubble_sort(self):
        arr = [99, 104, 0, 10, 99]
        bubble_sort(arr)
        self.assertListEqual(arr, [0, 10, 99, 99, 104])

    def test_selection_sort(self):
        arr = [99, 104, 0, 10, 99]
        selection_sort(arr)
        self.assertListEqual(arr, [0, 10, 99, 99, 104])

    def test_merge_sort(self):
        arr = [99, 104, 0, 10, 99]
        arr = merge_sort(arr)
        self.assertListEqual(arr, [0, 10, 99, 99, 104])

    def test_quick_sort(self):
        arr = [99, 104, 0, 10, 99]
        quick_sort(arr)
        self.assertListEqual(arr, [0, 10, 99, 99, 104])
