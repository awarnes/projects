"""
The game module that lets someone play Blackjack!
"""


import base_classes
from os import system


def main_menu():
    """
    The main menu of the game where one starts a new game or quits.
    """

    mm_options = {1: new_game, 2: exit}

    print("What do you want to do? ")
    print("1: Play new game.")
    print("2: Quit")

    try:
        mm_choice = int(input(">>> "))
    except ValueError:
        print("Please choose a numbered option.")

    mm_options[mm_choice]()

def score(hand):
    """
    Takes a hand and scores it.
    Number rank = Number
    Face rank = 10
    Ace = 1 or 11
    """

    score = 0
    rank_dict = {k: k for k in range(2, 11)}
    rank_dict.update({'A': (1, 11), 'J': 10, 'Q': 10, 'K': 10})

    for card in hand.hand:
        if card.rank != 'A':
            score += rank_dict[card.rank]

    for card in hand.hand:
        if card.rank == 'A':
            if score <= 10:
                score += 11
            else:
                score += 1

    return score


def dealer_turn(dealer_hand, play_deck, thresh=16):
    """
    Plays the dealer turn for Blackjack.
    """

    dealer_done = False
    dealer_lose = False

    while not dealer_done:
        if score(dealer_hand) > 21:
            dealer_lose = True
            dealer_done = True

        elif score(dealer_hand) == 21:
            dealer_done = True

        elif score(dealer_hand) <= thresh:
            dealer_hand.draw_card(play_deck)

        elif score(dealer_hand) > thresh:
            dealer_done = True

    return dealer_lose


def new_game():
    """
    Plays a new game against the computer.
    """

    play_deck = base_classes.Deck(number=6)
    play_deck.shuffle()
    play_deck.cut()

    player_hand = base_classes.Hand()
    dealer_hand = base_classes.Hand()

    player_hand.draw_card(play_deck)
    player_hand.draw_card(play_deck)

    dealer_hand.draw_card(play_deck)
    dealer_hand.draw_card(play_deck)

    done = False
    lose = False

    while done == False:
        system('clear')
        print("Your hand is:")
        print(player_hand.hand)
        if score(player_hand) == 21:
            print("You win!")
            lose = False
            input("...")
            break
        elif score(player_hand) > 21:
            print("Bust! You lose!")
            lose = True
            input("...")
            break
        print("Your current score is: {}".format(score(player_hand)))
        print("The dealer is showing: {}".format(dealer_hand.hand[0]))

        print("What do you want to do? ")
        print("1: Hit")
        print("2: Stay")
        play_choice = input(">>> ")

        if '1' in play_choice or 'hit' in play_choice.lower():
            player_hand.draw_card(play_deck)

        elif '2' in play_choice or 'stay' in play_choice.lower():
            done = True
            system('clear')
        else:
            print("I'm not sure what you mean...")
            input("...")
            system('clear')

    if not lose:
        dealer_lose = dealer_turn(dealer_hand, play_deck)
        if dealer_lose == False:
            if score(dealer_hand) < score(player_hand):
                print("You won against the dealer!! {} to {}!!".format(score(player_hand), score(dealer_hand)))
            else:
                print("Sorry, you lost to the dealer {} to {}.".format(score(player_hand), score(dealer_hand)))
        else:
            print("The dealer busted! You won with {}".format(score(player_hand)))
    else:
        print("Sorry, you lost to a bust with {}".format(score(player_hand)))

    input("...")
    main_menu()


if __name__ == '__main__':

    print("Welcome to the table!")
    print("Blackjack is the game here!")

    main_menu()
