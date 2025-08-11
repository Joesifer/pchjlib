# src/pchjlib/twin_abundant.py

"""
Functions for twin primes and abundant numbers.
"""

from .primes import is_prime
from .divisors_multiples import sum_of_divisors
from .utils import InvalidInputError


def is_twin_prime(input_number: int) -> bool:
    """
    Check if a number is a twin prime.

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is a twin prime, False otherwise.

    Raises:
        - InvalidInputError: If number is not an integer.

    Example:
        >>> is_twin_prime(5)
        True
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    return is_prime(input_number) and (
        is_prime(input_number - 2) or is_prime(input_number + 2)
    )


def generate_twin_prime_list(limit: int) -> list:
    """
    Generate a list of twin primes from 2 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of twin primes.

    Raises:
        - InvalidInputError: If limit is not an integer >= 2.

    Example:
        >>> generate_twin_prime_list(20)
        [3, 5, 7, 11, 13, 17, 19]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 2:
        raise InvalidInputError("Limit must be >= 2")
    return [i for i in range(2, limit + 1) if is_twin_prime(i)]


def is_abundant_number(input_number: int) -> bool:
    """
    Check if a number is an abundant number.

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is abundant, False otherwise.

    Raises:
        - InvalidInputError: If number is not a positive integer.

    Example:
        >>> is_abundant_number(12)
        True
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 1:
        raise InvalidInputError("Number must be positive")
    return sum_of_divisors(input_number) > input_number


def generate_abundant_number_list(limit: int) -> list:
    """
    Generate a list of abundant numbers from 1 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of abundant numbers.

    Raises:
        - InvalidInputError: If limit is not a positive integer.

    Example:
        >>> generate_abundant_number_list(20)
        [12, 18, 20]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 1:
        raise InvalidInputError("Limit must be positive")
    return [i for i in range(1, limit + 1) if is_abundant_number(i)]
