# src/pchjlib/prime_factorization.py

"""
Functions for prime factorization.
"""

import math
import random

from pchjlib.utils import InvalidInputError, MathError
from pchjlib.primes import is_prime  # For checking if factor is prime


def _gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def _pollard_rho(n: int) -> int:
    """
    Pollard's Rho to find a non-trivial factor.
    """
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    x = random.randint(1, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = _gcd(abs(x - y), n)
        if d == n:
            return _pollard_rho(n)  # Retry if failed
    return d


def prime_factors(input_number: int) -> list:
    """
    Factorize a number into a list of prime factors using trial + Pollard's Rho.

    Parameters:
        - input_number (int): The number to factorize.

    Returns:
        - list: A list of prime factors.

    Raises:
        - InvalidInputError: If number is not a positive integer > 1.

    Example:
        >>> prime_factors(12)
        [2, 2, 3]
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number <= 1:
        raise InvalidInputError("Number must be greater than 1")
    factors = []
    n = input_number
    # Trial division for small factors
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, min(10**6, int(math.sqrt(n)) + 1), 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # If remaining is prime
    if n > 1:
        if is_prime(n):
            factors.append(n)
        else:
            # Use Pollard's Rho for large composite
            while n > 1:
                factor = _pollard_rho(n)
                while n % factor == 0:
                    factors.append(factor)
                    n //= factor
    return factors


def greatest_common_prime_divisor(number1: int, number2: int) -> int:
    """
    Find the greatest common prime divisor of two numbers.

    Parameters:
        - number1 (int): The first number.
        - number2 (int): The second number.

    Returns:
        - int: The greatest common prime divisor of number1 and number2.

    Raises:
        - InvalidInputError: If numbers are not positive integers > 1.
        - MathError: If no common prime divisor exists.

    Example:
        >>> greatest_common_prime_divisor(12, 18)
        3
    """
    if not (isinstance(number1, int) and isinstance(number2, int)):
        raise InvalidInputError("Both numbers must be integers")
    if number1 <= 1 or number2 <= 1:
        raise InvalidInputError("Numbers must be greater than 1")
    factors1 = set(prime_factors(number1))
    factors2 = set(prime_factors(number2))
    common_factors = factors1.intersection(factors2)
    if not common_factors:
        raise MathError("No common prime divisor")
    return max(common_factors)
