# src/pchjlib/utils.py

"""
Common utilities and exceptions for pchjlib.
"""


class MathError(Exception):
    """Base exception for math-related errors."""

    pass


class OutOfRangeError(MathError):
    """Exception raised when a value is out of the allowed range."""

    pass


class InvalidInputError(MathError):
    """Exception raised when the input is invalid."""

    pass
