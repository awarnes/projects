"""
Make a stopwatch with START, STOP, and LAP functionality.

Extra: ***** NOT YET ENABLED ******
It shoud write out to a program to be able to read from later.
"""
from time import *
from chrono_ordinals import *

def stopwatch():
    """
    This function is the meat of the module, doing start, stop and lap. It will return a time,
    which can be used to write out to a file if needed.
    """

    times = list()
    lap = list()

    choice = input("[s]tart, s[t]op, [l]ap. ")
    times.append(round(time(), 4))

    while 't' not in choice:

        choice = input("s[t]op, [l]ap. ")
        if 'l' in choice:
            lap.append(round(time(), 4))
        else:
            times.append(round(time(), 4))

    if len(lap) > 1:
        final = lap[-1]
        for index, t in enumerate(lap):
            if index == 0:
                print("The {} lap took {} seconds.".format\
                    (chron_ord(index + 1), round(t - times[0], 4)))
            else:
                print("The {} lap took {} seconds.".format\
                    (chron_ord(index + 1), round(t - lap[index - 1], 4)))

        print("And the {} lap took {} seconds.".format\
            (chron_ord(len(lap) + 1), round(times[-1] - final, 4)))

    else:
        print("Wow that was only {} seconds!".format(round(times[-1] - times[0], 4)))

    return lap, times
stopwatch()
