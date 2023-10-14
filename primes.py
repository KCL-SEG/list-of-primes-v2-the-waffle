"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

def is_prime(x : int) -> bool:
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def primes(number_of_primes : int) -> list[int]:
    if number_of_primes <= 0:
        raise ValueError()

    if number_of_primes == 1:
        return [2]
    if number_of_primes == 2:
        return [2,3]
    
    ret : list[int] = [2, 3]
    n = 1
    while len(ret) < number_of_primes:
        if is_prime(6 * n - 1):
            ret.append(6 * n - 1)
        if is_prime(6 * n + 1):
            ret.append(6 * n + 1)
        n += 1

    if len(ret) == number_of_primes + 1:
        ret.pop()

    return ret
