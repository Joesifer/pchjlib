# src/pchjlib/inversion_counting.py

"""
Function to count inversions.
"""

from pchjlib.utils import InvalidInputError


def _merge(arr, temp, left, mid, right):
    """
    Merge two halves and count inversions.
    """
    inv_count = 0
    i = left
    j = mid
    k = left
    while (i <= mid - 1) and (j <= right):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
            inv_count += mid - i
    while i <= mid - 1:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    for idx in range(left, right + 1):
        arr[idx] = temp[idx]
    return inv_count


def _merge_sort(arr, temp, left, right):
    """
    Recursive merge sort with inversion count.
    """
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += _merge_sort(arr, temp, left, mid)
        inv_count += _merge_sort(arr, temp, mid + 1, right)
        inv_count += _merge(arr, temp, left, mid + 1, right)
    return inv_count


def count_inversions(numbers: list) -> int:
    """
    Count the number of inversions in a list using merge sort (O(n log n)).

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
    # Make a copy to avoid modifying original
    arr = numbers[:]
    temp = [0] * len(arr)
    return _merge_sort(arr, temp, 0, len(arr) - 1)
