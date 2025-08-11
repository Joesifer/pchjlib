# src/pchjlib/caesar_cipher.py

"""
Functions for Caesar cipher.
"""

from pchjlib.utils import InvalidInputError


def caesar_cipher_to_numbers(text: str, shift: int) -> list:
    """
    Convert a string to a list of Caesar cipher numbers.

    Parameters:
        - text (str): The input string.
        - shift (int): The shift value.

    Returns:
        - list: A list of Caesar cipher numbers.

    Raises:
        - InvalidInputError: If the input is not a string, is empty, or contains non-alphabetic characters. If shift is not an integer.

    Example:
        >>> caesar_cipher_to_numbers("ABC", 3)
        [3, 4, 5]
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    if not isinstance(shift, int):
        raise InvalidInputError("Shift must be an integer")
    text = text.upper()
    if not text.isalpha():
        raise InvalidInputError("String must contain only alphabetic characters")
    return [(ord(char) - 65 + shift) % 26 for char in text]


def caesar_cipher_from_numbers(numbers: list, shift: int) -> str:
    """
    Decode a list of Caesar cipher numbers to a string.

    Parameters:
        - numbers (list): The list of numbers.
        - shift (int): The shift value.

    Returns:
        - str: The decoded string.

    Raises:
        - InvalidInputError: If the input is not a list, is empty, or contains invalid numbers. If shift is not an integer.

    Example:
        >>> caesar_cipher_from_numbers([3, 4, 5], 3)
        'ABC'
    """
    if not isinstance(numbers, (list, tuple)):
        raise InvalidInputError("Input must be a list or tuple")
    if not numbers:
        raise InvalidInputError("List cannot be empty")
    if not isinstance(shift, int):
        raise InvalidInputError("Shift must be an integer")
    for num in numbers:
        if not isinstance(num, int) or num < 0 or num > 25:
            raise InvalidInputError("Numbers must be integers between 0 and 25")
    return "".join(chr((num - shift) % 26 + 65) for num in numbers)
