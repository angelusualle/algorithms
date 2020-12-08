import unittest
import pprint
from shuffle_deck import shuffle_deck

class Test_Case_Shuffle_Deck(unittest.TestCase):
    def test_shuffle_deck(self):
        colors = ['heart', 'diamonds', 'spades', 'clubs']
        deck = [(value, color) for value in range(1, 14) for color in colors]
        eights_card = []
        for i in range(100000):
            shuffle_deck(deck)
            eights_card.append(deck[8])
        self.assertAlmostEqual(len([x for x in eights_card if x == (8, 'clubs')]) / len(eights_card), 0.01923, delta=0.0005)