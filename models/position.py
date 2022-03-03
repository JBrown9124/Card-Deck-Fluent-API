from validators import is_card, is_int
from .card.card import Card



class Position:
    def __init__(self, card, value: int):
        is_card("card", card)
        is_int("position value", value)

        self.card = card
        self.value = value

    def update(
        self, bottom_half_card: Card, top_half_card: Card, curr_pos: int
    ) -> None:
        is_card("bottom_half_card", bottom_half_card)
        is_card("top_half_card", top_half_card)
        is_int("curr_pos", curr_pos)

        is_bottom_half_card = (
            bottom_half_card.suit == self.card.suit
            and bottom_half_card.kind == self.card.kind
        )
        is_top_half_card = (
            top_half_card.suit == self.card.suit
            and top_half_card.kind == self.card.kind
        )

        if is_bottom_half_card:
            self.value = curr_pos - 1

        elif is_top_half_card:
            self.value = curr_pos
