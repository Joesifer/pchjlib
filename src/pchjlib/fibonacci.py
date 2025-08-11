# src/pchjlib/fibonacci.py

"""
Functions for Fibonacci sequence.
"""

from functools import lru_cache

from .utils import InvalidInputError


@lru_cache(maxsize=None)
def fibonacci_at_index(index: int) -> int:
    """
    Calculate the Fibonacci number at the given index using iteration with caching.

    Parameters:
        - index (int): The position of the Fibonacci number (starting from 0).

    Returns:
        - int: The Fibonacci number at the given index.

    Raises:
        - InvalidInputError: If index is not a non-negative integer.

    Example:
        >>> fibonacci_at_index(5)
        5
    """
    if not isinstance(index, int):
        raise InvalidInputError("Index must be an integer")
    if index < 0:
        raise InvalidInputError("Index must be non-negative")
    if index == 0:
        return 0
    if index == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, index + 1):
        a, b = b, a + b
    return b


def generate_fibonacci_list(count: int) -> list:
    """
    Generate a list of the first count Fibonacci numbers.

    Parameters:
        - count (int): The number of elements in the list.

    Returns:
        - list: A list of Fibonacci numbers.

    Raises:
        - InvalidInputError: If count is not a non-negative integer.

    Example:
        >>> generate_fibonacci_list(5)
        [0, 1, 1, 2, 3]
    """
    if not isinstance(count, int):
        raise InvalidInputError("Count must be an integer")
    if count < 0:
        raise InvalidInputError("Count must be non-negative")
    return [fibonacci_at_index(i) for i in range(count)]
