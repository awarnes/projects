"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
1/15/17
"""


def is_prime(num):
    """
    Returns true for a prime number, otherwise false.
    """
    import math


    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True

primes = list()

for i in range(3, 2000001, 2):
    if is_prime(i):
        primes.append(i)

result = sum(primes) + 2

# print(primes)
print(result)
