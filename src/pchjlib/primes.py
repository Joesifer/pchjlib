# src/pchjlib/primes.py

"""
Functions for prime and emirp numbers.
"""

import math
from pchjlib.utils import InvalidInputError

# Optional import for gmpy2 to handle large numbers

try:
    import gmpy2
    from gmpy2 import isqrt as g_isqrt, powmod as g_powmod  # type: ignore[attr-defined]

    GMPY2_AVAILABLE = True
except ImportError:
    from math import isqrt as g_isqrt

    GMPY2_AVAILABLE = False


def _quick_checks(n: int) -> int:
    """
    Perform quick checks before running Miller - Rabin.

    Returns:
        0  -> definitely composite
        1  -> definitely prime
       -1  -> inconclusive, continue with Miller - Rabin
    """
    if n < 2:
        return 0
    if n % 2 == 0:
        return 1 if n == 2 else 0
    if n % 3 == 0:
        return 1 if n == 3 else 0
    r = g_isqrt(n)
    if r * r == n:
        return 0
    return -1


def _miller_rabin(n: int, bases: tuple[int, ...]) -> bool:
    """
    Miller - Rabin primality test.

    Args:
        n (int): Number to test.
        bases (tuple[int, ...]): Test bases to use.

    Returns:
        bool: True if n passes all bases (probably prime), False if composite.
    """
    d = n - 1
    s = (d & -d).bit_length() - 1
    d >>= s
    for a in bases:
        if a % n == 0:
            continue
        x = g_powmod(a, d, n) if GMPY2_AVAILABLE else pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def is_prime(n: int) -> bool:
    """
    Determine whether a number is prime.

    Parameters:
        n (int): The integer to test.

    Returns:
        bool: True if n is prime, False otherwise.

    Raises:
        - InvalidInputError: If number is not an integer.

    Notes:
        - Negative numbers, 0, and 1 always return False.
        - Uses quick trial division by small primes and perfect square elimination.
        - Falls back on a deterministic Miller - Rabin test with bases chosen
          according to n's bit length.
        - If gmpy2 is installed, powmod and isqrt are accelerated.

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(4)
        False
        >>> is_prime(-5)
        False
    """

    if not isinstance(n, int):
        raise InvalidInputError("Number must be an integer")

    t = _quick_checks(n)
    if t != -1:
        return t == 1

    bl = n.bit_length()
    if bl <= 32:
        bases = (2, 7, 61)
    elif bl <= 64:
        bases = (2, 3, 5, 7, 11, 13, 17)
    elif bl <= 128:
        bases = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    else:
        bases = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    return _miller_rabin(n, bases)


def generate_prime_list(limit: int) -> list:
    """
    Generate a list of prime numbers from 0 to limit using the Sieve algorithm.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of prime numbers.

    Raises:
        - InvalidInputError: If limit is not an integer >= 2.

    Example:
        >>> generate_prime_list(10)
        [2, 3, 5, 7]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 2:
        raise InvalidInputError("Limit must be >= 2")
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(limit + 1) if sieve[i]]


def is_emirp(input_number: int) -> bool:
    """
    Check if a number is an emirp (a prime number whose reverse is also a prime).

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is an emirp, False otherwise.

    Raises:
        - InvalidInputError: If the input is not a positive integer >= 2.

    Example:
        >>> is_emirp(13)
        True
    """

    def reverse_number(input_number: int) -> int:
        """
        Reverse the digits of a number using arithmetic operations.

        Parameters:
            - input_number (int): The number to reverse.

        Returns:
            - int: The reversed number.

        Example:
            >>> reverse_number(123)
            321
        """
        reversed_num = 0
        while input_number > 0:
            digit = input_number % 10
            reversed_num = reversed_num * 10 + digit
            input_number //= 10
        return reversed_num

    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 2:
        raise InvalidInputError("Number must be >= 2")
    if not is_prime(input_number):
        return False
    reversed_number = reverse_number(input_number)
    if input_number == reversed_number:
        return False  # Exclude palindromic primes for standard emirp definition
    return is_prime(reversed_number)


def generate_emirp_list(limit: int) -> list:
    """
    Generate a list of emirp numbers from 2 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of emirp numbers.

    Raises:
        - InvalidInputError: If limit is not an integer >= 2.

    Example:
        >>> generate_emirp_list(20)
        [13, 17]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 2:
        raise InvalidInputError("Limit must be >= 2")
    return [i for i in range(2, limit + 1) if is_emirp(i)]
