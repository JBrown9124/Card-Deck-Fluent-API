from validators import is_int, is_str


class Positions:
    def __init__(
        self, first_tracked_pos: int, second_tracked_pos: int, card_amount: int = 52
    ) -> None:
        is_int("track_pos", first_tracked_pos, second_tracked_pos)
        is_int("card_amount", card_amount)

        self.first_tracked_pos = first_tracked_pos
        self.second_tracked_pos = second_tracked_pos

        self.card_amount = card_amount

    def is_now_last(self, tracked_position: str) -> bool:
        is_str("track_position", tracked_position)

        currently_tracked_pos = (
            self.first_tracked_pos
            if tracked_position == "first"
            else self.second_tracked_pos
        )

        return self.is_desired_pos(
            currently_tracked_pos,
            self.card_amount - 1,
        )

    def is_touching(self) -> bool:
        return self.is_desired_pos(
            self.second_tracked_pos, self.first_tracked_pos + 1
        ) or self.is_desired_pos(self.second_tracked_pos + 1, self.first_tracked_pos)

    def is_desired_pos(self, pos, desired_pos) -> bool:
        is_int("desired_pos", desired_pos)
        return pos == desired_pos
