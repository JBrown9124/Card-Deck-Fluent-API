from models.card.kind import Kind


class Card:
    def __init__(self, suit: str, kind_value: int):
        self.suit = suit
        self.kind = Kind(kind_value).type

    def __repr__(self):
        return f"({self.suit}, {self.kind })"
