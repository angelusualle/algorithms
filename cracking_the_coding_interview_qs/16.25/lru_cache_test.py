import unittest
from lru_cache import LRU_Cache

class Test_Case_LRU_Cache(unittest.TestCase):
    def test_lru_cache(self):
        cache = LRU_Cache(51)
        for i in range(60):
            cache.add_item('test%i' % i, i)
            cache.get_item('test2')
        self.assertIsNone(cache.get_item('test0'))
        self.assertEqual(cache.get_item('test20'), 20)
        self.assertEqual(cache.get_item('test2'), 2)

if __name__ == '__main__':
    unittest.main()
