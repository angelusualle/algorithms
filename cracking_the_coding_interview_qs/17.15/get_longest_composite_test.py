import unittest
from get_longest_composite import get_longest_composite

class Test_Case_Get_Longest_Composite(unittest.TestCase):
    def test_get_longest_composite(self):
        self.assertEqual(get_longest_composite(['bobby', 'brosef', 'john', 'apple', 'seed', 'pear', 'punch', 'bottom', 'appleseeds', 'applejohn']), 'applejohn')

if __name__ == '__main__':
    unittest.main()