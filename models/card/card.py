from models.card.kind import Kind


class Card:
    def __init__(self, suit: str, kind_value: int):
        if type(suit) != str:
            raise TypeError("suit must be a string")
        if type(kind_value) != int:
            raise TypeError("kind_value must be an integer")

        self.suit = suit
        self.kind = Kind(kind_value).type

    def __repr__(self) -> str:
        return f"({self.suit}, {self.kind})"
