from models.deck import Deck

# An ‘in shuffle’ is a perfect riffle shuffle on a standard deck of 52 playing cards -
# that just means a shuffle by splitting the deck in half, then interleaving cards,
# starting with the top half. Can you write a quick program to solve the following?

# What is the position of the first card after the 7th shuffle?

# How many times must you perform the shuffle so that the top card becomes the bottom card?

# When do the first and last cards in the deck touch?

if __name__ == "__main__":
    deck = Deck()

    # What is the position of the first card after the 7th shuffle?
    first_question_answer = (
        deck.shuffle("in").times(7).tracking_card(1).execute().first_tracked_pos
    )

    # How many times must you perform the shuffle so that the top card becomes the bottom card?
    second_question_answer = (
        deck.shuffle("in")
        .until("CARD_IS_LAST")
        .tracking_card(1)
        .execute()
        .times_shuffled
    )

    # When do the first and last cards in the deck touch?
    third_question_answer = (
        deck.shuffle("in")
        .until("TOUCHING")
        .tracking_cards(1, 52)
        .execute()
        .times_shuffled
        + 1
    )

    print(
        f"What is the position of the first card after the 7th shuffle?\nA: {first_question_answer}"
    )

    print(
        f"\nHow many times must you perform the shuffle so that the top card becomes the bottom card?\nA: {second_question_answer}"
    )

    print(
        f"\nWhen do the first and last cards in the deck touch?\nA: {third_question_answer}"
    )
