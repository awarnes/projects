"""
Function that returns the chronological ordinals (or word versions) of 1, 2, 3, ..., n up to 99.

DocTest:

>>> chron_ord(4)
'fourth'

>>> chron_ord(3)
'third'

>>> chron_ord(22)
'twenty-second'

>>> chron_ord(99)
'ninety-ninth'

"""


def chron_ord(num):
    """
    Function to convert numbers (ints and floats [possibly strings]) into the positional or
    chronological words they are associated with. Will only work with ints.

    Example:
    1 == 'first'
    3 == 'third'
    99 == 'ninety-ninth'
    """

    try:
        num = int(num)

    except ValueError:
        pass

    ones_list = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth', 5: 'fifth', 6: 'sixth',
                 7: 'seventh', 8: 'eighth', 9: 'ninth'}
    teens_list = {11: 'eleventh', 12: 'twelfth', 13: 'thirteenth', 14: 'fourteenth', 15: 'fifteenth',
                  16: 'sixteenth', 17: 'seventeenth', 18: 'eighteenth', 19: 'nineteenth'}
    dec_zero_list = {10: 'tenth', 20: 'twentieth', 30: 'thirtieth', 40: 'fourtieth', 50: 'fiftieth',
                    60: 'sixtieth', 70: 'seventieth', 80: 'eightieth', 90: 'ninetieth'}
    dec_digit_list = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy',
                      8: 'eighty', 9: 'ninety'}

    num = str(num)

    if len(num) == 2 and 11 <= int(num) <= 19:
        return teens_list[int(num)]
    elif len(num) == 2 and num[1] == '0':
        return dec_zero_list[int(num)]
    elif len(num) == 2:
        return dec_digit_list[int(num[0])] + '-' + ones_list[int(num[1])]
    elif len(num) == 1 and num == '0':
        return 'zeroth'
    elif len(num) == 1:
        return ones_list[int(num)]
    else:
        return "ValueError: That's not a number! Do it right and put a number in me next time!"
