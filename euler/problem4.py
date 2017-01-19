"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_pal(num):
    """
    Returns true if the number is palindromic.
    """

    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

result = [x*y for x in range(800, 1000) for y in range(800, 1000) if is_pal(x*y)]

print(max(result))
