# src/pchjlib/sequence_generation.py

"""
Functions to generate sequences.
"""

from .utils import InvalidInputError, OutOfRangeError


def generate_sequence_rule_1(count: int) -> list:
    """
    Generate a sequence of positive integers according to the rule:
        - 1 number is divisible by 1,
        - 2 numbers are divisible by 2,
        - 3 numbers are divisible by 3,
        - and so on, the numbers increase until the number of numbers is `count`

    Parameters:
        - count (int): The number of elements to generate.

    Returns:
        - list: A list of integers in the sequence.

    Raises:
        - InvalidInputError: If count is not a positive integer.

    Example:
        >>> generate_sequence_rule_1(10)
        [1, 4, 6, 9, 12, 15, 16, 20, 24, 28]
    """
    if not isinstance(count, int):
        raise InvalidInputError("Count must be an integer")
    if count <= 1:
        raise InvalidInputError("Count must be greater than 1")

    def helper(k: int) -> int:
        if k == 1:
            return 1
        number_to_find = 1
        position = 0
        for i in range(1, 100000):  # Increased range for larger counts
            number_to_find = (number_to_find // i + 1) * i
            position += 1
            if position == k:
                return number_to_find
            for _ in range(i - 1):
                number_to_find += i
                position += 1
                if position == k:
                    return number_to_find
        raise OutOfRangeError(f"Cannot find the {k}-th number.")

    return [helper(i) for i in range(1, count + 1)]


def generate_sequence_rule_2(base: int, count: int) -> list:
    """
    Generate a list of multiples of base with count elements.

    Parameters:
        - base (int): The number to generate multiples.
        - count (int): The number of elements.

    Returns:
        - list: A list of multiples of base.

    Raises:
        - InvalidInputError: If inputs are not integers or count is negative.

    Example:
        >>> generate_sequence_rule_2(2, 5)
        [0, 2, 4, 6, 8]
    """
    if not (isinstance(base, int) and isinstance(count, int)):
        raise InvalidInputError("Inputs must be integers")
    if count < 0:
        raise InvalidInputError("Count must be non-negative")
    return [base * i for i in range(count)]


def generate_sequence_rule_3(count: int, base: int) -> list:
    """
    Generate a list of powers of base from 0 to count-1.

    Parameters:
        - count (int): The number of elements.
        - base (int): The base number.

    Returns:
        - list: A list of powers of base.

    Raises:
        - InvalidInputError: If inputs are not integers or count is negative.

    Example:
        >>> generate_sequence_rule_3(5, 2)
        [1, 2, 4, 8, 16]
    """
    if not (isinstance(count, int) and isinstance(base, int)):
        raise InvalidInputError("Inputs must be integers")
    if count < 0:
        raise InvalidInputError("Count must be non-negative")
    return [base**i for i in range(count)]
