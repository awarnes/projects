"""
Make a program that guesses the number you are thinking of when you tell it higher or lower.

comp_guess(45)
>>> 45

"""

"""
def comp_guess(num=45):

    **********HAVE NOT FIGURED OUT HOW TO MAKE THIS OPTION WORK, MAY COME BACK TO IT*************
    45 is the target number, the computer is not aware that this is the number.



    guess = 50
    last_guess, hot_cold = list(), list()
    count = 1
    # high, low = int(), int()

    while guess != num:
        print("I will guess {}. Is your number higher or lower ('h' or 'l')?".format(guess))
        choice = input(">>> ")
        print("Okay, I'm thinking...")

        hot_cold.append(choice)
        last_guess.append(guess)

        try:
            if hot_cold[-1] < hot_cold[-2]:
                high = last_guess[-1]
            elif hot_cold[-1] > hot_cold[-2]:
                low = last_guess[-1]
        except IndexError:
            pass

        if 'h' in choice:
            if count == 1:
                guess = (100 + last_guess[-1]) // 2
                count += 1
            else:
                guess = (max(last_guess) + last_guess[-1]) // 2
                if guess > high:
                    guess = high - 1

        elif 'l' in choice:
            if count == 1:
                guess = (1 + last_guess[-1]) // 2
                count += 1
            else:
                guess = (min(last_guess) + last_guess[-1]) // 2
                if guess < low:
                    guess = low + 1

        else:
            print("I don't understand...")

    answer = guess
    return answer
"""

def comp_guess(num=45):
    """
    Using a list and removing ranges off the list will come up with the final answer.
    """


    guess = 50
    numbers = [i for i in range(1, 101)]

    while len(numbers) > 1:
        print("I will guess {}. Is your number higher or lower ('h' or 'l')?".format(guess))
        choice = input(">>> ")
        print("Okay, I'm thinking...")


        if 'h' in choice:
            numbers = [i for i in numbers if i > guess]
            guess = numbers[len(numbers) // 2]
            answer = numbers[0]

        elif 'l' in choice:
            numbers = [i for i in numbers if i < guess]
            guess = numbers[len(numbers) // 2]
            answer = numbers[0]

        elif 's' in choice:
            answer = guess
            break
            
        else:
            print("I don't understand...")



    return answer

def run():
    """
    Runs the program.
    """


    choice = input("Please choose a number from 1 to 100. ")

    try:
        answer = comp_guess(num=int(choice))

    except ValueError:
        print("That's not a number...")
        print("Let's just go with 45 then.")
        answer = comp_guess()

    print("Wow, then your number is {}".format(answer))

run()
