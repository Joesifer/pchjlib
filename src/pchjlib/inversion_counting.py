# src/pchjlib/inversion_counting.py

"""
Function to count inversions.
"""

from .utils import InvalidInputError


def count_inversions(numbers: list) -> int:
    """
    Count the number of inversions in a list.

    Parameters:
        - numbers (list): The list to count inversions.

    Returns:
        - int: The number of inversions.

    Raises:
        - InvalidInputError: If input is not a list or contains non-numbers.

    Example:
        >>> count_inversions([1, 3, 2])
        1
    """
    if not isinstance(numbers, (list, tuple)):
        raise InvalidInputError("Input must be a list or tuple")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise InvalidInputError("Elements must be numbers")
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                count += 1
    return count
