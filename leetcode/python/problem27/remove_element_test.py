import unittest
from remove_element import remove_element

class Test_Case_Remove_Element(unittest.TestCase):
    def test_remove_element(self):
        self.assertEqual(remove_element([1,2,3,4,4], 4), 3)

if __name__ == '__main__':
    unittest.main()