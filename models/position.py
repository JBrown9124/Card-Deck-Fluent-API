class Position():
    def __init__(self, card, value):
        self.card = card
        self.value = value
    
    def update(
        self,  bottom_half_card, top_half_card, curr_pos
    ):
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

    
        
