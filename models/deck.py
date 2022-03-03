from validators import is_str
from .card.card import Card
from .shuffle import Shuffle


class Deck:
    def __init__(self):
        self.suits = ["clubs", "spades", "hearts", "diamonds"]
        self.cards = [
            Card(suit, value) for suit in self.suits for value in range(1, 14)
        ]

    def shuffle(self, type: str) -> Shuffle:
        is_str("type", type)

        return Shuffle(self, type)

    def show_cards(self) -> None:
        for card in self.cards:
            print(card)

    def __len__(self) -> int:
        return len(self.cards)

    def __iter__(self) -> Card:
        for card in self.cards:
            yield card

    def __repr__(self) -> str:
        return self.cards.__repr__()

    def __getitem__(self, idx: int) -> Card:
        return self.cards[idx]

    def __contains__(self, card: Card) -> Card:
        if type(card) != Card:
            raise TypeError("card must be of type Card")

        return card in self.cards

    def __setitem__(self, idx: int, card: Card):
        self.cards[idx] = card
