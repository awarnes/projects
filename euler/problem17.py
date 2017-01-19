"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is
in compliance with British usage.

List of unique numbers/strings (mostly): + and
one
two
three
four
five
six
seven
eight
nine
ten
eleven
twelve
thirteen
fourteen
fifteen
sixteen
seventeen
eighteen
nineteen
twenty
thirty
fourty
fifty
sixty
seventy
eighty
ninety
hundred
thousand

"""


num_list = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3]

for num in range(1, 1001):
    word = str(num)
    for char in word:
        if len(word) == 4:
            #  Simply add 11 for 1000 since only one 4-digit number.
            ans += 11
        elif len(word) == 3 and word.index(1) == 1 and int(char) == 0:
            #  Check for 10 ("ten") which is not "zero" (4 characters)
            ans += 3
        elif len(word) == 2 and word.index(0) == 1 and int(char) == 0:
            #  Check for 10 ("ten") which is not "zero" (4 characters)
            ans += 3
        else:
            #  Match each digit to the number of letters for it.
            if len(word) == 3:
                




        ans += num_list[int[char]]
