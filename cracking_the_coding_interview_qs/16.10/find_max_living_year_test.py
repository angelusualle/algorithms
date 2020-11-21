from find_max_living_year import find_max_living_year
import unittest

class Test_Case_Find_Max_Living_Year(unittest.TestCase):
    def test_find_max_living_year(self):
        yrs = [(1900, 1925), (1980, None), (1950, 1960), (1990, None), (1901, 1922), (1925, 1999), (1901, 2000)]
        self.assertEqual(find_max_living_year(yrs), 1990)
        