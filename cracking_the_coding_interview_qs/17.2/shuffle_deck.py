import random

def shuffle_deck(deck):
    for i in range(51, -1, -1):
        n = random.randint(0,i)
        deck[i], deck[n] = deck[n], deck[i]
    return deck