"""
The U.S government has commissioned you to catch the terrorists!
There is a mathematical pyramid with the following pattern:
1
11
21
1211
111221
312211
you must write a program to calculate up to the 40th line of this pyramid.
If you don't, the terrorists win!

Pattern:
1 -> one 1 -> 11
11 -> two 1s -> 21
21 -> one 2 and one 1 -> 1211
1211 -> one 1 and one 2 and two 1s -> 111221
111221 -> three 1s and two 2s and one 1 -> 312211
"""


from time import *


def pattern_calc(line=40):
    """
    Calculate the pattern above and return it, up to the line specified.
    """


    from itertools import groupby

    line = line - 1
    temp1 = '1'

    while line > 0:
        line -= 1
        groups = groupby(temp1, key=lambda char: char)
        result = [(str(len(list(group))) + digit) for digit, group in groups]
        temp2 = ''.join(result)
        temp1 = temp2


    return temp1

choice = int(input("What line of the pattern to calculate? "))

start = time()
result = pattern_calc(choice)
print(result)
print(len(result))
print("{} seconds".format(time()-start))
