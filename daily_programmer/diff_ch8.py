"""
Write a program that will take coordinates, and tell you the corresponding number in pascals triangle.

For example: (test)

>>> pascals(1, 1)
1
>>> pascals(4, 2)
3
>>> pascals(1, 19)
'non-existant'

the format should be "line number, integer number"

for extra credit, add a function to simply print the triangle, for the extra credit to count,
it must print at least 15 lines.
"""

from math import factorial as fac
from pprint import pprint as pp

def gen_pascal(lines=15):
    """
    Generate pascal's triangle up to the number of lines requested.
    """


    pascal = list()
    temp = list()
    temp2 = list()

    pascal = [pascals(i, x) for i in range(lines) for x in range(i) if pascals(i, x) != 'non-existant']

    for index, num in enumerate(pascal):
        if num == 1:
            temp.extend([1, 1])
        else:
            temp.append(num)
    temp.append(1)
    pascal = temp

    for i in range(1, lines+1):
        temp = pascal[:i]
        temp2.append(temp)
        pascal = pascal[i:]
    pascal = temp2
    pascal.pop()

    return pascal

def pascals(r, c):
    """
    Find the integer in pascal's triangle given the coordinates (r, c) or (row #, column #)
    with the formula (r, c) = r! / c! (r - c)!
    """
    try:
        result = fac(r - 1) // (fac(c - 1) * (fac((r - 1) - (c - 1))))
    except ValueError:
        result = 'non-existant'

    return result


print(pascals(41,21))
#  Would like to center the pyramid on the final line printed...
# for index, nums in enumerate(gen_pascal(22)):
#     print("{}: ".format(index+1, end=' '))
#     print("{}".format(nums).center(len(gen_pascal(22)[-1])))
