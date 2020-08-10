import unittest
from find_duplicates_memory_limit import find_duplicates_memory_limit


class Test_Case_Find_Dups_Mem_Limit(unittest.TestCase):
    def test_find_duplicates_within_memory_limit(self):
        self.assertListEqual(find_duplicates_memory_limit([1,2,3,4,5,6,7,8, 8]), [8])