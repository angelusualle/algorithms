import unittest
from get_buy_sell_dates import get_buy_sell_dates

class Test_Case_Get_Buy_Sell_Dates(unittest.TestCase):
    def test_get_buy_sell_dates(self):
        self.assertTupleEqual(get_buy_sell_dates([56, 12, 15, 5, 10, 20, 15, 60, 45]), (55, 3, 7))