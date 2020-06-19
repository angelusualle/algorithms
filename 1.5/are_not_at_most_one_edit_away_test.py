import unittest
from are_not_at_most_one_edit_away import are_not_at_most_one_edit_away

class Test_Case_Are_Not_At_Most_One_Edit_Away(unittest.TestCase):
    def test_are_not_at_most_one_edit_away(self):
        self.assertTrue(are_not_at_most_one_edit_away('cat', 'ca'))
        self.assertTrue(are_not_at_most_one_edit_away('catz', 'cate'))
        self.assertTrue(are_not_at_most_one_edit_away('', ''))
        self.assertTrue(are_not_at_most_one_edit_away('m', ''))
        self.assertTrue(are_not_at_most_one_edit_away('ct', 'cat'))

        self.assertFalse(are_not_at_most_one_edit_away('cater', 'catos'))
        self.assertFalse(are_not_at_most_one_edit_away('mete', 'metzr'))
        self.assertFalse(are_not_at_most_one_edit_away('ct', 'caet'))

if __name__ == '__main__':
    unittest.main()