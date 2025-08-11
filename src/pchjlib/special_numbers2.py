# src/pchjlib/special_numbers2.py

"""
Functions for square, strong, and friendly numbers.
"""

import math

from .divisors_multiples import sum_of_divisors
from .utils import InvalidInputError


def is_square_number(input_number: int) -> bool:
    """
    Check if a number is a square number.

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is a square number, False otherwise.

    Raises:
        - InvalidInputError: If number is not a non-negative integer.

    Example:
        >>> is_square_number(16)
        True
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 0:
        raise InvalidInputError("Number must be non-negative")
    sqrt_number = int(math.sqrt(input_number))
    return sqrt_number * sqrt_number == input_number


def generate_square_number_list(limit: int) -> list:
    """
    Generate a list of square numbers from 0 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of square numbers.

    Raises:
        - InvalidInputError: If limit is not a non-negative integer.

    Example:
        >>> generate_square_number_list(10)
        [0, 1, 4, 9]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 0:
        raise InvalidInputError("Limit must be non-negative")
    return [i * i for i in range(int(math.sqrt(limit)) + 1) if i * i <= limit]


def are_friendly_numbers(number1: int, number2: int) -> bool:
    """
    Check if two numbers are friendly numbers.

    Parameters:
        - number1 (int): The first number.
        - number2 (int): The second number.

    Returns:
        - bool: True if the numbers are friendly, False otherwise.

    Raises:
        - InvalidInputError: If the numbers are not positive integers.

    Example:
        >>> are_friendly_numbers(30, 140)
        True
    """
    if not (isinstance(number1, int) and isinstance(number2, int)):
        raise InvalidInputError("Both numbers must be integers")
    if number1 < 1 or number2 < 1:
        raise InvalidInputError("Numbers must be positive")
    return sum_of_divisors(number1) / number1 == sum_of_divisors(number2) / number2


def is_strong_number(input_number: int) -> bool:
    """
    Check if a number is a strong number (sum of factorial of its digits equals the number itself).

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is strong, False otherwise.

    Raises:
        - InvalidInputError: If number is not a non-negative integer.

    Example:
        >>> is_strong_number(145)
        True
        >>> is_strong_number(146)
        False
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 0:
        raise InvalidInputError("Number must be non-negative")
    if input_number == 0:
        return False  # 0! = 1 != 0
    digits = [int(digit) for digit in str(input_number)]
    total = sum(math.factorial(digit) for digit in digits)
    return total == input_number
