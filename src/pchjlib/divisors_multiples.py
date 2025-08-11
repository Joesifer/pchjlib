# src/pchjlib/divisors_multiples.py

"""
Functions for divisors and multiples.
"""

import math

from pchjlib.utils import InvalidInputError, MathError


def sum_of_divisors(input_number: int) -> int:
    """
    Calculate the sum of positive divisors of a number (excluding itself).

    Parameters:
        - input_number (int): The number to calculate the sum of divisors.

    Returns:
        - int: The sum of divisors.

    Raises:
        - InvalidInputError: If number is not a positive integer.

    Example:
        >>> sum_of_divisors(6)
        6
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Number must be an integer")
    if input_number <= 0:
        raise InvalidInputError("Number must be positive")
    return sum(i for i in range(1, input_number) if input_number % i == 0)


def generate_divisor_list(input_number: int, positive_only: bool = True) -> list:
    """
    Generate a list of divisors of a number.

    Parameters:
        - input_number (int): The number to generate the list of divisors.
        - positive_only (bool): If True, only positive divisors are returned.

    Returns:
        - list: A list of divisors of the number.

    Raises:
        - InvalidInputError: If number is not an integer or is zero.

    Example:
        >>> generate_divisor_list(6)
        [1, 2, 3, 6]
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number == 0:
        raise InvalidInputError("Number cannot be zero")
    abs_number = abs(input_number)
    divisors = [i for i in range(1, abs_number + 1) if abs_number % i == 0]
    if not positive_only:
        divisors += [-i for i in divisors]
    return sorted(divisors)


def generate_multiple_list(
    base_number: int, limit: int, positive_only: bool = True
) -> list:
    """
    Generate a list of multiples of a number up to limit times.

    Parameters:
        - base_number (int): The number to generate multiples.
        - limit (int): The limit for the number of multiples.
        - positive_only (bool): If True, only positive multiples are returned.

    Returns:
        - list: A list of multiples of the number.

    Raises:
        - InvalidInputError: If inputs are not integers or number is zero or limit < 1.

    Example:
        >>> generate_multiple_list(3, 5)
        [3, 6, 9, 12, 15]
    """
    if not (isinstance(base_number, int) and isinstance(limit, int)):
        raise InvalidInputError("Inputs must be integers")
    if base_number == 0:
        raise InvalidInputError("Number cannot be zero")
    if limit < 1:
        raise InvalidInputError("Limit must be positive")
    if positive_only:
        return [base_number * i for i in range(1, limit + 1)]
    return sorted(
        [-base_number * i for i in range(1, limit + 1)]
        + [base_number * i for i in range(limit + 1)]
    )


def common_divisors(numbers: list) -> list:
    """
    Generate a list of common divisors of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - list: A list of common divisors.

    Raises:
        - InvalidInputError: If input is not a list or contains non-integers.
        - MathError: If list has fewer than 2 non-zero elements.

    Example:
        >>> common_divisors([12, 18])
        [1, 2, 3, 6]
    """
    if not isinstance(numbers, (list, tuple)):
        raise InvalidInputError("Input must be a list or tuple")
    if len([n for n in numbers if n != 0]) < 2:
        raise MathError("List must have at least 2 non-zero elements")
    for num in numbers:
        if not isinstance(num, int):
            raise InvalidInputError("All elements must be integers")
    divisors = set(generate_divisor_list(abs(numbers[0])))
    for num in numbers[1:]:
        if num != 0:
            divisors.intersection_update(generate_divisor_list(abs(num)))
    return sorted(list(divisors))


def greatest_common_divisor(numbers: list) -> int:
    """
    Calculate the greatest common divisor of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - int: The greatest common divisor of the list.

    Raises:
        - InvalidInputError: If input is not a list or contains non-integers.
        - MathError: If list has fewer than 2 non-zero elements.

    Example:
        >>> greatest_common_divisor([12, 18])
        6
    """
    if not isinstance(numbers, (list, tuple)):
        raise InvalidInputError("Input must be a list or tuple")
    if len([n for n in numbers if n != 0]) < 2:
        raise MathError("List must have at least 2 non-zero elements")
    for num in numbers:
        if not isinstance(num, int):
            raise InvalidInputError("All elements must be integers")
    result = abs(numbers[0])
    for num in numbers[1:]:
        if num != 0:
            result = math.gcd(result, abs(num))
    return result


def least_common_multiple(numbers: list) -> int:
    """
    Calculate the least common multiple of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - int: The least common multiple of the list.

    Raises:
        - InvalidInputError: If input is not a list or contains non-integers or zeros.
        - MathError: If list has fewer than 2 elements.

    Example:
        >>> least_common_multiple([4, 6])
        12
    """
    if not isinstance(numbers, (list, tuple)):
        raise InvalidInputError("Input must be a list or tuple")
    if len(numbers) < 2:
        raise MathError("List must have at least 2 elements")
    if 0 in numbers:
        raise InvalidInputError("List cannot contain zero")
    for num in numbers:
        if not isinstance(num, int):
            raise InvalidInputError("All elements must be integers")
    result = abs(numbers[0])
    for num in numbers[1:]:
        result = abs(result * num) // math.gcd(result, abs(num))
    return result
