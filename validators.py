from models.card.card import Card


def is_int(name: str, *args) -> None:
    for arg in args:
        if type(arg) != int:
            raise TypeError(f"{name} must be an integer")


def is_str(name: str, *args) -> None:
    for arg in args:
        if type(arg) != str:
            raise TypeError(f"{name} must be a string")


def is_card(name: str, *args) -> None:
    for arg in args:
        if type(arg) != Card:
            raise TypeError(f"{name} must be a card")
