"""
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

sum of natural numbers from 1 to n is = (n**2)+n//2

1/16/17
"""

from factorize import factors

num = 1000

# trinum = ((num**2)+num)//2

while True:
    trinum = ((num**2)+num)//2
    if len(factors(trinum)) > 500:
        print(trinum)
        break
    else:
        num += 1

# print(find_divisors(trinum))