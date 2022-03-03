from .card.card import Card
from .shuffle import Shuffle


class Deck:
    def __init__(self):
        self.suits = ["clubs", "spades", "hearts", "diamonds"]
        self.cards = [
            Card(suit, value) for suit in self.suits for value in range(1, 14)
        ]

    def shuffle(self, type):
        return Shuffle(self, type)

    def show_cards(self):
        for card in self.cards:
            print(card)

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        for card in self.cards:
            yield card

    def __repr__(self):
        return self.cards.__repr__()
   
    def __getitem__(self, index):
        return self.cards[index]
    
    def __contains__(self, element):
        return element in self.cards
    
    def __setitem__(self, index, value):
        self.cards[index] = value
    
