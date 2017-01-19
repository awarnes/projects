"""
This is a full blackjack or 21 game played with the standard 52 card deck (no jokers).

21: A + 10, J, Q, or K is instant win.

Dealer hits on anything less than 17, including 'soft' 17 (when cards include A)

Problems:
    1: dealing with the Ace: is it high or is it low?
"""


from deck_mechanics import *


deck = deck_builder()
p_hand = list()
d_hand = list()


def card_addition(hand):

    total = 0

    a_count = hand.count('A')

    *********************************************************************************************
    Not Working with string inputs, still need to translate the J, Q, K to integers for total additions.

    if a_count > 0:
        for i in range(a_count):
            hand.pop(hand.index('A'))

        for i in hand:
            total = card_value(i)


        while total + 10 < 21 and a_count > 0:
            total += 11
            a_count -= 1

        while total < 21 and a_count > 0:
            total += 1
            a_count -= 1

    else:
        for i in hand:
            _ = card_value(i)
            total += _

    return total


def p_hit(p_hand, d_hand, deck):
    """
    Function that draws a card from the deck and gives it to the player.

    Will also call game_end() to check if the game has been completed.
    """

    p_tot = card_addition(p_hand)
    d_tot = card_addition(d_hand)

    for card in p_hand:
        print("{}".format(card, sep=' '))

    print('You have a total of {}...'.format(p_tot))
    print('and the dealer is showing {}.'.format(d_tot))
    choice = input("Do you hit or stay? ")

    if 'h' in choice or 'H' in choice:
        p_hand.append(deck.pop())
        return p_hand
    elif 's' in choice or 'S' in choice:
        return p_hand
    else:
        print("I'm sorry, I'm not sure what that meant...")
        hit(p_hand, d_hand, deck)

deck = deck_builder()

p_hit(['h4', 'dQ', 'C3'], d_hand, deck)
