class Kind:
    def __init__(self, value: int):
        self.values = {
            1: "ace",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "jack",
            12: "queen",
            13: "king",
        }
        if type(value) != int:
            raise TypeError("kind_value must be an integer")

        if value not in self.values:
            raise ValueError("kind_value must be a card kind")

        self.value = 0
        self.type = self.values[value]
