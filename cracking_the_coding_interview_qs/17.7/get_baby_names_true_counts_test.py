import unittest
from get_baby_names_true_counts import get_baby_names_true_counts

class Test_Case_Get_Baby_Names_True_Counts(unittest.TestCase):
    def test_get_baby_names_true_counts(self):
        self.assertDictEqual(get_baby_names_true_counts({'John': 3, 'Johnny': 4, 'Jon': 7, 'Elsa': 4, 'Elton':2, 'Elsaser': 4}, 
        {'John': 'Johnny', 'Johnny':'Jon', 'Elsa':'Elsaser'}),
        {'Elsa': 8, 'Elton': 2, 'John': 14})

if __name__ == '__main__':
    unittest.main()