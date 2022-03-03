class Positions:
    def __init__(self, first_tracked_pos, second_tracked_pos, card_amount=52):
        self.first_tracked_pos = first_tracked_pos
        self.second_tracked_pos = second_tracked_pos
        self.card_amount = card_amount

    def is_now_last(self, tracked_position):
        tracked_position = (
            self.first_tracked_pos
            if tracked_position == "first"
            else self.second_tracked_pos
        )
        return self.is_desired_pos(
            tracked_position,
            self.card_amount - 1,
        )

    def is_touching(self):
        return self.is_desired_pos(
            self.second_tracked_pos, self.first_tracked_pos + 1
        ) or self.is_desired_pos(self.second_tracked_pos + 1, self.first_tracked_pos)

    def is_desired_pos(self, pos, desired_pos):
        return pos == desired_pos
