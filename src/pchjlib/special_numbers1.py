# src/pchjlib/special_numbers1.py
"""
Functions for perfect, narcissistic, amicable, and happy numbers.
"""


from .utils import InvalidInputError

from .divisors_multiples import (
    sum_of_divisors,
)  # Assuming sum_of_divisors is in divisors_multiples.py; adjust if needed


def sum_of_digits(input_number: int) -> int:
    """
    Calculate the sum of digits of an integer.

    Parameters:
        - input_number (int): The number to calculate the sum of digits.

    Returns:
        - int: The sum of digits.

    Raises:
        - InvalidInputError: If the input is not an integer.

    Example:
        >>> sum_of_digits(123)
        6
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Number must be an integer")
    return sum(int(digit) for digit in str(abs(input_number)))


def is_perfect_number(input_number: int) -> bool:
    """
    Check if a number is a perfect number.

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is perfect, False otherwise.

    Raises:
        - InvalidInputError: If number is not a positive integer.

    Example:
        >>> is_perfect_number(6)
        True
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 1:
        raise InvalidInputError("Number must be positive")
    return sum_of_divisors(input_number) == input_number


def generate_perfect_number_list(limit: int) -> list:
    """
    Generate a list of perfect numbers from 1 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of perfect numbers.

    Raises:
        - InvalidInputError: If limit is not a positive integer.

    Example:
        >>> generate_perfect_number_list(10)
        [6]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 1:
        raise InvalidInputError("Limit must be positive")
    return [i for i in range(1, limit + 1) if is_perfect_number(i)]


def is_narcissistic_number(input_number: int) -> bool:
    """
    Check if a number is a narcissistic number.

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is narcissistic, False otherwise.

    Raises:
        - InvalidInputError: If number is not a non-negative integer.

    Example:
        >>> is_narcissistic_number(153)
        True
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 0:
        raise InvalidInputError("Number must be non-negative")
    digits = len(str(input_number))
    return sum(int(digit) ** digits for digit in str(input_number)) == input_number


def generate_narcissistic_number_list(limit: int) -> list:
    """
    Generate a list of narcissistic numbers from 0 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of narcissistic numbers.

    Raises:
        - InvalidInputError: If limit is not a non-negative integer.

    Example:
        >>> generate_narcissistic_number_list(10)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 0:
        raise InvalidInputError("Limit must be non-negative")
    return [i for i in range(limit + 1) if is_narcissistic_number(i)]


def are_amicable_numbers(number1: int, number2: int) -> bool:
    """
    Check if two numbers are amicable numbers.

    Parameters:
        - number1 (int): The first number.
        - number2 (int): The second number.

    Returns:
        - bool: True if the numbers are amicable, False otherwise.

    Raises:
        - InvalidInputError: If the numbers are not positive integers.

    Example:
        >>> are_amicable_numbers(220, 284)
        True
    """
    if not (isinstance(number1, int) and isinstance(number2, int)):
        raise InvalidInputError("Both numbers must be integers")
    if number1 < 1 or number2 < 1:
        raise InvalidInputError("Numbers must be positive")
    if number1 == number2:
        return False  # Amicable pairs must be distinct numbers
    return sum_of_divisors(number1) == number2 and sum_of_divisors(number2) == number1


def is_happy_number(input_number: int) -> bool:
    """
    Check if a number is a happy number.

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is happy, False otherwise.

    Raises:
        - InvalidInputError: If number is not a positive integer.

    Example:
        >>> is_happy_number(19)
        True
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 1:
        raise InvalidInputError("Number must be positive")
    seen = set()
    while input_number != 1 and input_number not in seen:
        seen.add(input_number)
        input_number = sum(int(digit) ** 2 for digit in str(input_number))
    return input_number == 1


def generate_happy_number_list(limit: int) -> list:
    """
    Generate a list of happy numbers from 1 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of happy numbers.

    Raises:
        - InvalidInputError: If limit is not a positive integer.

    Example:
        >>> generate_happy_number_list(10)
        [1, 7, 10]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 1:
        raise InvalidInputError("Limit must be positive")
    return [i for i in range(1, limit + 1) if is_happy_number(i)]
