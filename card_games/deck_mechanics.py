"""
This is a method to build a deck of cards for a card game.

Using the standard 52 card deck with two optional jokers, calling this method will build a
randomized list with the card name (K, Q, 3), the value (10, 10, 3), and the suit (H, D, S, C).

This method will be used for other card games between human and computer AI opponents. The intention
is that popping off the back (or front) of the list will produce a random card.

This file also contains the method for shuffling or reshuffling a deck with the desired cards.

For determining card values:

    for card in deck:
        test = card.split()
        if card[1].isalpha():
            print("Face!")
        elif card[1] == '1':
            print(10)
        else:
            print(int(card[1]))

"""

# def shuffle(deck):
#     """
#     Shuffles the remaining cards in the deck to a new random but static order.
#     """
#      Prior to understanding that random has a shuffle function....
#      This did not generate sucsessively random inputs as one might have hoped....
#     for i in range(7):
#         new_deck = list()
#
#         #  If the deck is an odd number of cards split it with one more in the right hand.
#         if len(deck) % 2 != 0:
#             lh_deck = deck[len(deck)//2:]
#             rh_deck = deck[:(len(deck)//2) + 1]
#
#         else:
#             lh_deck = deck[len(deck)//2:]
#             rh_deck = deck[:len(deck)//2]
#
#         for i in range(len(rh_deck)):
#             new_deck.append(lh_deck[i])
#             new_deck.append(rh_deck[i])
#
#         deck = new_deck
#
#     print(lh_deck)
#     print(rh_deck)
#     print(deck)
#
#     return deck

def shuffle(deck):
    """
    Shuffles a deck of cards as randomly (or close to?) as Python allows.
    """

    import random

    random.shuffle(deck)

    return deck


def deck_builder(joke_bool=False):
    """
    Build a list that contains all 52 cards in random order and allows the user to decide to
    include jokers.
    """

    import random
    deck = []

    suits = ['H', 'D', 'S', 'C']
    cards = [x for x in range(2, 11)]
    faces = ['J', 'Q', 'K', 'A']

    cards.extend(faces)

    for suit in suits:
        for value in cards:
            deck.append(suit + str(value))

    if joke_bool:
        deck.append('Joker')
        deck.append('Joker')

    random.shuffle(deck)

    return deck

def card_value(card):
    """
    Returns the value of the card.

    Attempting to be as generic as possible:
        If the card is a face card it is possible for it to have two states depending on the other
        cards in the hand, or the rules of the game. This will not be handled here without
        significantly more information from the other card values and specific game rules.
    """

    if card[1].isalpha():
        return card[1]
    elif card[1] == '1':
        return 10
    else:
        return int(card[1])

def card_suit(card):
    """
    Returns the suit of a card.

    This will be important in valuing next moves for possible AI difficulties as well as
    different game rules (solitare for example).
    """

    return card[0]

print(card_value('HQ'))
