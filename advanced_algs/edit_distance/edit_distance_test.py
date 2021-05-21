import unittest
from edit_distance import edit_distance

class Test_Case_Edit_Distance(unittest.TestCase):
    def test_edit_distance(self):
        self.assertEqual(edit_distance("exponential","polynomial"), 6)

if __name__ == '__main__':
    unittest.main()