"""
Base classes for card games, including card, deck, and hand.
"""

from random import shuffle
from itertools import product
from collections import deque


class Card:

    def __init__(self, rank, suit):
        """initialize card with a certain rank and suit."""
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """Shows the user what the card is"""
        return "{0.rank} {0.suit}".format(self)

    def __repr__(self):
        """Shows the user what the card is"""
        return "{0.rank} {0.suit}".format(self)


class Deck:

    def __init__(self, number=1):
        """
        Intitialize the deck with card objects. Optional ability to combine multiple 52 card decks
        (default = 1).
        """

        self.card_list = deque(maxlen=number*52)

        ranks = [rank for rank in range(2, 11)]
        faces = ['J', 'Q', 'K', 'A']
        ranks.extend(faces)

        suits = ['Heart', 'Spade', 'Diamond', 'Club']

        all_possible_cards = product(ranks, suits)

        for _ in range(number):
            for card in all_possible_cards:
                c = Card(card[0], card[1])
                self.card_list.append(c)

    def __len__(self):
        return len(self.card_list)

    def shuffle(self):
        """Shuffle the deck"""

        for shuffle_times in range(7):
            shuffle(self.card_list)

    def cut(self):
        """Cut the deck in half."""

        self.card_list.rotate(len(self.card_list)//2)

    def draw(self):
        """Draws one card off the top of the deck"""

        return self.card_list.popleft()


class Hand:

    def __init__(self):
        """Starts an empty hand and able to add into it."""

        self.hand = list()

    def draw_card(self, deck):
        """Adds a card to the hand from the deck."""

        self.hand.append(deck.draw())

    def hand_from_list(self):
        """Alternate constructor for a pre-designated hand."""
        pass


if __name__ == '__main__':
    first_deck = Deck()
    player_hand = Hand()

    # for card in deck.card_list:
    #     print(card)

    first_deck.shuffle()
    first_deck.cut()
    print('-'*20)
    print(len(first_deck))
    player_hand.draw_card(first_deck)
    player_hand.draw_card(first_deck)
    player_hand.draw_card(first_deck)

    print(player_hand.hand)
    print(len(first_deck))
    print(player_hand.hand[0] in first_deck.card_list)
