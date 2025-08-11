# src/pchjlib/prime_factorization.py

"""
Functions for prime factorization.
"""

from .utils import InvalidInputError, MathError


def prime_factors(input_number: int) -> list:
    """
    Factorize a number into a list of prime factors.

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
    divisor = 2
    while input_number > 1:
        while input_number % divisor == 0:
            factors.append(divisor)
            input_number //= divisor
        divisor += 1
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
