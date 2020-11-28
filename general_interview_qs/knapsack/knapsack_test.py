import unittest
from knapsack import Knapsack

class Test_Case_Knapsack(unittest.TestCase):
    def test_knapsack(self):
        ksack = Knapsack(20, [4,2,6,3,1,9], [1,1,2,14,5,6])
        ksack.solve()

if __name__ == '__main__':
    unittest.TestCase()