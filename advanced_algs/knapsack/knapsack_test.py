import unittest
from knapsack_with_repetition import knapsack_with_repetition
from knapsack_no_repetition import knapsack_no_repetition

class Test_Case_Knapsack(unittest.TestCase):
    def test_knapsack_with_repetition(self):
        self.assertEqual(knapsack_with_repetition([6, 3, 4, 2], [30,14,16,9], 10), 48)
    def test_knapsack_no_repetition(self):
        self.assertEqual(knapsack_no_repetition([6, 3, 4, 2], [30,14,16,9], 10), 46)

if __name__ == '__main__':
    unittest.main()