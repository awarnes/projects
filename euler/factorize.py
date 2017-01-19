"""
Importable function that returns a set of factors for a given number.
Amalgamation of best code from:
http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
"""


def factors(num):
    """
    Returns the factors of given number as a set (**UNSORTED**).
    """
    from math import sqrt

    step = 2 if num % 2 else 1
    return set(x for tup in ([i, num//i] for i in range(1, int(sqrt(num))+1, step) if num % i == 0) for x in tup)


# choice = input(">>> ")
#
# print(factors(int(choice)))
# print(len(factors(int(choice))))
