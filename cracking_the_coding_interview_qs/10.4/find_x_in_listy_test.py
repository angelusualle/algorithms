import unittest
from find_x_in_listy import find_x_in_listy, Listy

class Test_Case_Find_X_In_Listy(unittest.TestCase):
    def test_case_find_x_in_listy(self):
        listy = Listy(list(range(0, 1*10**8)))
        self.assertEqual(find_x_in_listy(listy, 5678), 5678)