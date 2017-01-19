"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

Solution: 837799

After setting up the for loop at the bottom, I hypothsized that the solution would be somewhere
between 900,000 and 1,000,000 (higher number is higher length of chain, right?). After that didn't
work I manually went in and changed the range so search 200k at a time from 600k-800k (returning
the solution), then 400k-600k (to make sure there wasn't an even bigger answer)
and finally 100k-400k (because I got impatient).

I could have just done a range search from 100k to 1m, but decided against that at first due to the
fear that it would take too long (my first actual attempt was from 900-1m for some reason thinking
I had entered 900k and that was taking longer than the split second I was patient for).

I also could have setup the range to populate programatically and spit out the longest of the chains
at the end of searching rather than running the program several times. Though this would have
probably been equivalent in resources to just running 100k to 1m in the first place (not sure how
Python would work there though.) 1/16/17
"""


def collatz(num):
    """
    Create a Collatz chain from a given number:
    n/2 if n is even
    3n+1 if n is odd
    """

    chain = [num]

    while chain[-1] != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = (3*num) + 1
        chain.append(num)

    return chain


start, length = 0, 0

for i in range(100000, 400000):
    if len(collatz(i)) > length:
        start, length = i, len(collatz(i))

print(start)
print(length)
