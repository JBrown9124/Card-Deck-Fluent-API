from models.deck import Deck


if __name__ == "__main__":
    deck = Deck()
    
    first_question_answer = (
        deck.shuffle("in").times(7).tracking_card(1).execute().first_tracked_pos
    )
    second_question_answer = (
        deck.shuffle("in")
        .until("CARD_IS_LAST")
        .tracking_card(1)
        .execute()
        .times_shuffled
    )
    third_question_answer = (
        deck.shuffle("in")
        .until("TOUCHING")
        .tracking_cards(1, 52)
        .execute()
        .times_shuffled
        + 1
    )

    print(first_question_answer)
    print(second_question_answer)
    print(third_question_answer)
