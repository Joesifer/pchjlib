# src/pchjlib/string_processing.py

"""
Functions for list and string processing.
"""

import re

from pchjlib.utils import InvalidInputError


def remove_duplicates(items: list) -> list:
    """
    Remove duplicate elements from a list.

    Parameters:
        - items (list): The list to process.

    Returns:
        - list: A list without duplicate elements.

    Raises:
        - InvalidInputError: If input is not a list or tuple.

    Example:
        >>> remove_duplicates([1, 2, 2, 3])
        [3, 2, 1]
    """
    if not isinstance(items, (list, tuple)):
        raise InvalidInputError("Input must be a list or tuple")
    return sorted(list(set(items)), reverse=True)


def extract_digits_from_string(text: str) -> list:
    """
    Extract digits from a string. Example: "abc123" = [1,2,3].

    Parameters:
        - text (str): The input string.

    Returns:
        - list: A list of digits.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.

    Example:
        >>> extract_digits_from_string("abc123")
        [1, 2, 3]
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    return [int(digit) for digit in re.findall(r"\d", text)]


def extract_numbers_from_string(text: str) -> list:
    """
    Extract numbers from a string. Example: "abc123" = [123].

    Parameters:
        - text (str): The input string.

    Returns:
        - list: A list of numbers.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.

    Example:
        >>> extract_numbers_from_string("abc123def456")
        [123, 456]
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    return [int(number) for number in re.findall(r"\d+", text)]


def extract_characters(text: str) -> list:
    """
    Extract non-digit characters from a string.

    Parameters:
        - text (str): The input string.

    Returns:
        - list: A list of non-digit characters.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.

    Example:
        >>> extract_characters("a1b2c3")
        ['a', 'b', 'c']
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    return re.findall(r"\D", text)


def compress_string(text: str, compress_type: int) -> str:
    """
    Compress a string into 2 types.

    Parameters:
        - text (str): The input string.
        - compress_type (int): 1 or 2. If 1, "google" → "e2gl2o", if 2, "google" → "g2ogle".

    Returns:
        - str: The compressed string.

    Raises:
        - InvalidInputError: If input is not a string, is empty, or compress_type is invalid.

    Example:
        >>> compress_string("google", 1)
        'e2gl2o'
        >>> compress_string("google", 2)
        'g2ogle'
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    if compress_type not in [1, 2]:
        raise InvalidInputError("Compression type must be 1 or 2")

    if compress_type == 1:
        sorted_chars = sorted(text)
        compressed = ""
        count = 1
        for i in range(1, len(sorted_chars)):
            if sorted_chars[i] == sorted_chars[i - 1]:
                count += 1
            else:
                compressed += (str(count) if count > 1 else "") + sorted_chars[i - 1]
                count = 1
        compressed += (str(count) if count > 1 else "") + sorted_chars[-1]
        return compressed
    else:
        result = ""
        count = 1
        for i in range(1, len(text)):
            if text[i] == text[i - 1]:
                count += 1
            else:
                result += (str(count) if count > 1 else "") + text[i - 1]
                count = 1
        result += (str(count) if count > 1 else "") + text[-1]
        return result


def compress_string_without_numbers(input_text: str) -> str:
    """
    Compress a string by removing duplicates (e.g., "hhhoocssssiiinnnhhhhh" → "hocsinh").

    Parameters:
        - input_text (str): The input string.

    Returns:
        - str: The compressed string.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.

    Example:
        >>> compress_string_without_numbers("hhhoocssssiiinnnhhhhh")
        'hocsinh'
    """
    if not isinstance(input_text, str):
        raise InvalidInputError("Input must be a string")
    if not input_text:
        raise InvalidInputError("String cannot be empty")
    result = input_text[0]
    for char in input_text[1:]:
        if char != result[-1]:
            result += char
    return result


def decompress_string(text: str) -> str:
    """
    Decompress a string (e.g., "g2ogle" → "google").

    Parameters:
        - text (str): The input string.

    Returns:
        - str: The decompressed string.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.

    Example:
        >>> decompress_string("g2ogle")
        'google'
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    result = ""
    count = ""
    for char in text:
        if char.isdigit():
            count += char
        else:
            result += char if not count else char * int(count)
            count = ""
    return result


def unique_characters_string(text: str) -> str:
    """
    Create a string with unique characters (e.g., "google" → "gole").

    Parameters:
        - text (str): The input string.

    Returns:
        - str: A string with no duplicate characters.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.

    Example:
        >>> unique_characters_string("google")
        'gole'
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    seen = set()
    result = ""
    for char in text:
        if char not in seen:
            seen.add(char)
            result += char
    return result
