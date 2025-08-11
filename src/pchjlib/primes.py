# src/pchjlib/primes.py

"""
Functions for prime and emirp numbers.
"""

import math, random
from pchjlib.utils import InvalidInputError

# Optional import for gmpy2 to handle large numbers
try:
    import gmpy2
except ImportError:
    gmpy2 = None


def is_prime(input_number: int) -> bool:
    """
    Check if a number is a prime number.

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is prime, False otherwise.

    Raises:
        - InvalidInputError: If the input is not an integer or negative.

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(4)
        False
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 0:
        raise InvalidInputError("Input must be non-negative")
    if gmpy2 and hasattr(gmpy2, "is_prime") and input_number > 2**64:
        return bool(gmpy2.is_prime(input_number))  # type: ignore

    def miller_rabin(n: int, k: int = 5) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        def check(a: int, s: int, d: int, n: int) -> bool:
            x = pow(a, d, n)
            if x == 1:
                return True
            for _ in range(s - 1):
                if x == n - 1:
                    return True
                x = (x * x) % n
            return x == n - 1

        s = 0
        d = n - 1
        while d % 2 == 0:
            s += 1
            d //= 2

        for _ in range(k):
            a = random.randrange(2, n - 1)
            if not check(a, s, d, n):
                return False
        return True

    return miller_rabin(input_number)


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
