# src/pchjlib/special_calculations.py
"""
Functions for special calculations.
"""

from pchjlib.utils import InvalidInputError, MathError


def calculate_electricity_bill_vietnam(old_reading: float, new_reading: float) -> str:
    """
    Calculate electricity bill based on Vietnamese pricing tiers.

    Parameters:
        - old_reading (float): Old meter reading.
        - new_reading (float): New meter reading.

    Returns:
        - str: Calculation result.

    Raises:
        - InvalidInputError: If readings are not numbers or invalid.

    Example:
        >>> calculate_electricity_bill_vietnam(100, 150)
        '- Electricity consumed this month: 50.0 Kwh\n- Electricity bill this month: 83900.0 VND'
    """
    if not (
        isinstance(old_reading, (int, float)) and isinstance(new_reading, (int, float))
    ):
        raise InvalidInputError("Readings must be numbers")
    if new_reading < old_reading or old_reading < 0:
        raise InvalidInputError(
            "New reading must be greater than old reading and both must be non-negative"
        )
    kwh = new_reading - old_reading
    if kwh <= 50:
        total = kwh * 1678
    elif kwh <= 100:
        total = 50 * 1678 + (kwh - 50) * 1734
    elif kwh <= 200:
        total = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
    elif kwh <= 300:
        total = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536
    elif kwh <= 400:
        total = 50 * 1678 + 50 * 1734 + 100 * 2014 + 100 * 2536 + (kwh - 300) * 2834
    else:
        total = (
            50 * 1678
            + 50 * 1734
            + 100 * 2014
            + 100 * 2536
            + 100 * 2834
            + (kwh - 400) * 2927
        )
    return f"- Electricity consumed this month: {kwh:.1f} Kwh\n- Electricity bill this month: {total:.1f} VND"


def largest_number_with_digit_sum(digit_count: int, target_sum: int) -> str:
    """
    Find the largest number with digit_count digits and sum of digits equal to target_sum.

    Parameters:
        - digit_count (int): Number of digits.
        - target_sum (int): Sum of digits.

    Returns:
        - str: The largest number satisfying the condition.

    Raises:
        - InvalidInputError: If inputs are not non-negative integers.
        - MathError: If no such number exists.

    Example:
        >>> largest_number_with_digit_sum(3, 15)
        '960'
    """
    if not (isinstance(digit_count, int) and isinstance(target_sum, int)):
        raise InvalidInputError("Inputs must be integers")
    if digit_count < 0 or target_sum < 0:
        raise InvalidInputError("Inputs must be non-negative")
    if target_sum > 9 * digit_count:
        raise MathError("Sum cannot exceed 9 times the number of digits")
    if target_sum == 0 or digit_count == 0:
        return "0" * digit_count if digit_count > 0 else "0"
    if (
        target_sum < digit_count - 1
    ):  # Cannot have leading zero in largest, but allow zeros
        raise MathError("No valid number without leading zeros")
    result = []
    remaining_sum = target_sum
    for _ in range(digit_count):
        digit = min(9, remaining_sum)
        result.append(digit)
        remaining_sum -= digit
    # Adjust for exact sum: if remaining >0, impossible (but min ensures not)
    # To make largest, start with as many 9s as possible
    # Actually, the code above builds [9,9,..., (target - 9*(d-1)), 0...]
    # But to fix: we need to place smallest at end
    # Correct way: initialize with 0s, then add from left
    result = ["0"] * digit_count
    remaining = target_sum
    for i in range(digit_count):
        add = min(9, remaining)
        result[i] = str(add)
        remaining -= add
        if remaining == 0:
            break
    return "".join(result)
