"""
Make a function that advises a player on the best next move in a round of blackjack.
For now, just use 15 as a Hit/Stay Threshold.  Feel free to add testable features.

>>> advise_player(10, 5)
15 Hit.

>>> advise_player('Q', 5)
15 Hit.

>>> advise_player('A', 'K')
21 Blackjack!

>>> advise_player('A', 'A')
12 Hit.

>>> advise_player('J', 'K')
20 Stay.


**************************************************************************************************
Further development has been moved to ~/Documents/abw_codes/Git/projects/card_games as of 1/8/17
**************************************************************************************************
"""

from chrono_ordinals import chron_ord

cards = {str(x): x for x in range(2, 11)}
faces = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}
cards.update(faces)

hand = []

def advise_player_21(hand):
    """
    Check what the smartest move is given a hand of cards and the rules of Blackjack.
    """

    total = 0
    a_count = hand.count('A')

    try:
        thresh = int(input("What should the threshold for hitting be? (15 suggested) "))
    except ValueError:
        print("Please enter a numeral (eg. 15)")
        advise_player_21(hand)


    if a_count > 0:
        for i in range(a_count):
            hand.pop(hand.index('A'))

        for i in hand:
            total += cards[i]

        while total + 10 < 21 and a_count > 0:
            total += 11
            a_count -= 1

        while total < 21 and a_count > 0:
            total += 1
            a_count -= 1

    else:
        for i in hand:
            total += cards[i]

    if total > 21:
        print("{} You lose!".format(total))
    elif total == 21:
        print("{} Blackjack!".format(total))
    elif total <= thresh:
        print("{} Hit.".format(total))
    elif total > thresh:
        print("{} Stay.".format(total))


def hand_builder():
    """
    Allows for user input of cards in hand.
    """
    try:
        hand_num = int(input("How many cards do you have in your hand? "))
    except ValueError:
        print("Please enter a numeral (eg. 3)")
        hand_builder()

    for i in range(1, hand_num+1):
        c1 = input("What is your {} card? ".format(chron_ord(i)))

        if c1 == '10':
            pass
        elif len(c1) > 1:
            print("Please enter one card using it's first initial or it's number (eg. A, 10, 4).")
            hand_builder()

        if c1 not in cards:
            print("Please enter a valid playing card (2-10, J, Q, K, A)!")
            hand_builder()

        hand.append(c1)


    return hand

def run():
    hand = hand_builder()

    advise_player_21(hand)

run()
