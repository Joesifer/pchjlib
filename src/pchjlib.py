# pchjlib.py
################################################################################################
#
# Copyright (c) 2024 Joesifer
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
################################################################################################
"""
PCHJLIB😺
===============================================================================
-------------------------------------------------------------------------------
Author
-------------------------------------------------------------------------------
- Joesifer.

Version
-------------------------------------------------------------------------------
- 0.1.7.

Release Date
-------------------------------------------------------------------------------
- February 14, 2024.

License
-------------------------------------------------------------------------------
- Copyright © 2024 Joesifer

Supported Python Version
-------------------------------------------------------------------------------
- Python 3.7 or higher.

Dependencies
-------------------------------------------------------------------------------
- Built-in: `math`, `re`, `random`.
- External: `numpy`.

License Type
-------------------------------------------------------------------------------
- MIT License.

Additional Information
-------------------------------------------------------------------------------

For usage instructions, please refer to:
  >>> [https://github.com/Joesifer/pchjlib/blob/main/README.md](https://github.com/Joesifer/pchjlib/blob/main/README.md)

Feedback and support are welcome via:
  >>> Email: `phanchanhung12055@gmail.com`

THANK YOU!!!
===============================================================================
"""

import math, random, re

__author__ = "Joesifer (phanchanhung12055@gmail.com)"
__copyright__ = "Copyright (c) 2024 Joesifer"


# Custom exception classes
class MathError(Exception):
    """Base exception for math-related errors."""

    pass


class OutOfRangeError(MathError):
    """Exception raised when a value is out of the allowed range."""

    pass


class NotIntegerError(MathError):
    """Exception raised when a value is not an integer."""

    pass


class InvalidInputError(MathError):
    """Exception raised when the input is invalid."""

    pass


class DivisionByZeroError(MathError):
    """Exception raised when division by zero occurs."""

    pass


class TypeErrorCustom(MathError):
    """Exception raised when the data type is incorrect."""

    pass


class ListError(MathError):
    """Exception raised when the list input is invalid."""

    pass


# Check and import dependent libraries
try:
    import numpy
except ImportError:
    numpy = None


# Functions to check prime numbers and related numbers
def is_prime(number):
    """
    Check if a number is a prime number.

    Parameters:
        - number (int or float): The number to check.

    Returns:
        - bool: True if the number is prime, False otherwise.

    Raises:
        - InvalidInputError: If the input is not an integer.
        - Example: is_prime(7) → True, is_prime(3.5) → "Invalid input" error.
    """

    def miller_rabin(n, k=5):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        def check(a, s, d, n):
            x = pow(a, d, n)
            if x == 1:
                return True
            for _ in range(s - 1):
                if x == n - 1:
                    return True
                x = (x * x) % n
            return x == n - 1

        s = 0
        d = n - 1
        while d % 2 == 0:
            s += 1
            d //= 2

        for _ in range(k):
            a = random.randrange(2, n - 1)
            if not check(a, s, d, n):
                return False
        return True

    try:
        if not isinstance(number, int):
            raise InvalidInputError("Input must be an integer")
        return miller_rabin(number)
    except (ValueError, TypeError):
        raise InvalidInputError("Invalid input")


def generate_prime_list(limit):
    """
    Generate a list of prime numbers from 0 to limit using the Sieve algorithm.

    Parameters:
        - limit (int or float): The upper limit of the list.

    Returns:
        - list: A list of prime numbers.

    Raises:
        - InvalidInputError: If limit is not an integer >= 2.
        - Example: generate_prime_list(10) → [2, 3, 5, 7].
    """
    try:
        if numpy is None:
            raise ImportError(
                "This function requires numpy. Please run: pip install numpy"
            )
        if isinstance(limit, float) and not limit.is_integer():
            raise InvalidInputError("Invalid input: Limit must be an integer")
        limit = int(limit)
        if limit < 2:
            raise InvalidInputError("Invalid input: Limit must be >= 2")
        sieve = numpy.ones(limit + 1, dtype=bool)  # Pre-allocate memory with numpy
        sieve[0:2] = False
        for i in range(2, int(limit**0.5) + 1):
            if sieve[i]:
                sieve[i * i : limit + 1 : i] = False
        return numpy.where(sieve)[0].tolist()
    except (ValueError, TypeError):
        raise InvalidInputError("Invalid input: Limit must be an integer")


def is_emirp(number):
    """
    Check if a number is an emirp (a prime number whose reverse is also a prime).

    Parameters:
        - number (int or float): The number to check.

    Returns:
        - bool: True if the number is an emirp, False otherwise.

    Raises:
        - InvalidInputError: If the input is not a positive integer.
        - Example: is_emirp(31) → True since 31 is also a prime,
                   is_emirp(3.5) → "Invalid input" error.
    """
    try:
        if isinstance(number, float) and not number.is_integer():
            raise InvalidInputError("Invalid input: Float values are not accepted")
        number = int(number)
        if number < 2:
            raise InvalidInputError("Invalid input: Number must be >= 2")
        if not is_prime(number):
            return False
        reversed_number = int(str(number)[::-1])
        return is_prime(reversed_number)
    except (ValueError, TypeError):
        raise InvalidInputError("Invalid input: Value must be an integer")


def generate_emirp_list(limit):
    """
    Generate a list of emirp numbers from 0 to limit.

    Parameters:
        - limit (int or float): The upper limit of the list.

    Returns:
        - list: A list of emirp numbers.

    Raises:
        - InvalidInputError: If limit is not a non-negative integer.
    """
    try:
        if isinstance(limit, float) and not limit.is_integer():
            raise InvalidInputError("Invalid input: Limit must be an integer")
        limit = int(limit)
        if limit < 0:
            raise InvalidInputError("Invalid input: Limit must be non-negative")
        return [i for i in range(2, limit) if is_emirp(i)]
    except (ValueError, TypeError):
        raise InvalidInputError("Invalid input: Limit must be an integer")


# Fibonacci functions
def fibonacci_at_index(index):
    """
    Calculate the Fibonacci number at the given index using iteration, accepting only non-negative integers.

    Parameters:
        - index (int): The position of the Fibonacci number (starting from 0).

    Returns:
        - int: The Fibonacci number at the given index.

    Raises:
        - InvalidInputError: If index is not a non-negative integer.
    """
    if not isinstance(index, int) or index < 0:
        raise InvalidInputError("Invalid input: Must be a non-negative integer")
    a, b = 0, 1
    for _ in range(index):
        a, b = b, a + b
    return a


def generate_fibonacci_list(count):
    """
    Generate a list of the first count Fibonacci numbers.

    Parameters:
        - count (int or float): The number of elements in the list.

    Returns:
        - list: A list of Fibonacci numbers.

    Raises:
        - InvalidInputError: If count is not a non-negative integer.
    """
    try:
        if isinstance(count, float) and not count.is_integer():
            raise InvalidInputError("Invalid input: Count must be an integer")
        count = int(count)
        if count < 0:
            raise InvalidInputError("Invalid input: Count must be non-negative")
        return [fibonacci_at_index(i) for i in range(count)]
    except (ValueError, TypeError):
        raise InvalidInputError("Invalid input: Count must be an integer")


# Functions for perfect, narcissistic, amicable, and other special numbers
def sum_of_divisors(number):
    """
    Calculate the sum of positive divisors of a number (excluding itself).

    Parameters:
        - number (int or float): The number to calculate the sum of divisors.

    Returns:
        - int: The sum of divisors.

    Raises:
        - MathError: If number <= 0, InvalidInputError if not an integer.
    """
    try:
        if isinstance(number, float) and not number.is_integer():
            raise InvalidInputError("Invalid input: Float values are not accepted")
        number = int(number)
        if number <= 0:
            raise MathError("Number must be greater than 0")
        return sum(i for i in range(1, number) if number % i == 0)
    except (ValueError, TypeError):
        raise InvalidInputError("Invalid input: Value must be an integer")


def sum_of_digits(number):
    """
    Calculate the sum of digits of an integer.

    Parameters:
        - number (int or float): The number to calculate the sum of digits.

    Returns:
        - int: The sum of digits.

    Raises:
        - InvalidInputError: If the input is not a valid integer.
    """
    try:
        if isinstance(number, float) and not number.is_integer():
            raise InvalidInputError(
                "Invalid input: Float values with decimal parts are not accepted"
            )
        number = int(number)
        return sum(int(digit) for digit in str(abs(number)))
    except (ValueError, TypeError):
        raise InvalidInputError("Invalid input: Value must be an integer")


def is_perfect_number(number):
    """
    Check if a number is a perfect number.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is perfect, False otherwise.

    Raises:
        - MathError: If number < 1.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Input must be an integer")
        number = int(number)
        if number < 1:
            raise MathError("Number must be greater than 0")
        return sum_of_divisors(number) == number
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def generate_perfect_number_list(limit):
    """
    Generate a list of perfect numbers from 0 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of perfect numbers.

    Raises:
        - NotIntegerError: If not an integer, InvalidInputError if not greater than 1.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Limit must be an integer")
        limit = int(limit)
        if limit < 1:
            raise InvalidInputError("Limit must be greater than 0")
        return [i for i in range(1, limit + 1) if is_perfect_number(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def is_narcissistic_number(number):
    """
    Check if a number is a narcissistic number.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is narcissistic, False otherwise.

    Raises:
        - InvalidInputError: If number is not an integer >= 2.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Input must be an integer")
        number = int(number)
        if number < 0:
            return False
        return sum(int(digit) ** 3 for digit in str(number)) == number
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def generate_narcissistic_number_list(limit):
    """
    Generate a list of narcissistic numbers from 0 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of narcissistic numbers.

    Raises:
        - InvalidInputError: If limit is not an integer >= 2.
        - NotIntegerError: If limit is not an integer.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Limit must be an integer")
        limit = int(limit)
        if limit < 2:
            raise InvalidInputError("Limit must be greater than or equal to 2")
        return [i for i in range(2, limit) if is_narcissistic_number(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def are_amicable_numbers(number1, number2):
    """
    Check if two numbers are amicable numbers.

    Parameters:
        - number1 (int): The first number.
        - number2 (int): The second number.

    Returns:
        - bool: True if the numbers are amicable, False otherwise.

    Raises:
        - MathError: If the numbers are negative.
        - InvalidInputError: If the numbers are not integers.
    """
    try:
        if not (
            isinstance(number1, (int, float)) and isinstance(number2, (int, float))
        ) or not (float(number1).is_integer() and float(number2).is_integer()):
            raise NotIntegerError("Both numbers must be integers")
        number1, number2 = int(number1), int(number2)
        if number1 < 0 or number2 < 0:
            raise MathError("Numbers must be non-negative")
        return (
            sum_of_divisors(number1) == number2 + 1
            and sum_of_divisors(number2) == number1 + 1
        )
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def is_happy_number(number):
    """
    Check if a number is a happy number.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is happy, False otherwise.

    Raises:
        - MathError: If number < 1, InvalidInputError if not an integer.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Input must be an integer")
        number = int(number)
        if number < 1:
            raise MathError("Number must be greater than 0")
        seen = set()
        while number != 1 and number not in seen:
            seen.add(number)
            number = sum(int(digit) ** 2 for digit in str(number))
        return number == 1
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def generate_happy_number_list(limit):
    """
    Generate a list of happy numbers from 0 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of happy numbers.

    Raises:
        - InvalidInputError: If limit is not an integer > 0.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Limit must be an integer")
        limit = int(limit)
        if limit < 1:
            raise InvalidInputError("Limit must be greater than 0")
        return [i for i in range(1, limit) if is_happy_number(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


# Functions for square numbers, strong numbers, friendly numbers
def is_square_number(number):
    """
    Check if a number is a square number.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is a square number, False otherwise.

    Raises:
        - InvalidInputError: If not an integer.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Input must be an integer")
        number = int(number)
        if number < 0:
            return False
        sqrt_number = int(math.sqrt(number))
        return sqrt_number * sqrt_number == number
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def generate_square_number_list(limit):
    """
    Generate a list of square numbers from 0 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of square numbers.

    Raises:
        - InvalidInputError: If limit is not a non-negative integer.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Limit must be an integer")
        limit = int(limit)
        if limit < 0:
            raise InvalidInputError("Limit must be non-negative")
        return [i for i in range(limit) if is_square_number(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def are_friendly_numbers(number1, number2):
    """
    Check if two numbers are friendly numbers.

    Parameters:
        - number1 (int): The first number.
        - number2 (int): The second number.

    Returns:
        - bool: True if the numbers are friendly, False otherwise.

    Raises:
        - MathError: If the numbers are not greater than 1.
        - InvalidInputError: If not integers.
    """
    try:
        if not (
            isinstance(number1, (int, float)) and isinstance(number2, (int, float))
        ) or not (float(number1).is_integer() and float(number2).is_integer()):
            raise NotIntegerError("Both numbers must be integers")
        number1, number2 = int(number1), int(number2)
        if number1 <= 1 or number2 <= 1:
            raise MathError("Numbers must be greater than 1")
        return (
            sum_of_divisors(number1) == number2 and sum_of_divisors(number2) == number1
        )
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def is_strong_number(number, variant=1):
    """
    Check if a number is a strong number (sum of digits is prime).

    Parameters:
        - number (int): The number to check.
        - variant (int): 1 - Sum of digits is prime; 2 - Has a square prime factor.

    Returns:
        - bool: True if the number is strong, False otherwise.

    Raises:
        - InvalidInputError: If not an integer.
    """
    try:
        if not isinstance(number, int) or number < 0:
            raise NotIntegerError("Input must be a non-negative integer")
        number = int(number)
        if variant == 1:
            return is_prime(sum_of_digits(number))
        elif variant == 2:
            prime_list = [i for i in range(2, number) if is_prime(i)]
            for prime in prime_list:
                if number % prime == 0 and number % (prime**2) == 0:
                    return True
            return False
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


# Functions for divisors and multiples
def generate_divisor_list(number, positive_only=True):
    """
    Generate a list of divisors of a number.

    Parameters:
        - number (int): The number to generate the list of divisors.
        - positive_only (bool): If True, only positive divisors are returned.

    Returns:
        - list: A list of divisors of the number.

    Raises:
        - MathError: If number is 0.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Input must be an integer")
        number = int(number)
        if number == 0:
            raise MathError("Cannot generate divisor list for 0")
        number = abs(number)
        divisors = [i for i in range(1, number + 1) if number % i == 0]
        if not positive_only:
            divisors += [-i for i in divisors]
        return sorted(divisors)
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def generate_multiple_list(number, limit, positive_only=True):
    """
    Generate a list of multiples of a number up to limit times.

    Parameters:
        - number (int): The number to generate multiples.
        - limit (int): The limit for the number of multiples.
        - positive_only (bool): If True, only positive multiples are returned.

    Returns:
        - list: A list of multiples of the number.

    Raises:
        - MathError: If number is 0.
        - NotIntegerError: Input must be integers.
        - InvalidInputError: Limit must be greater than 1.
    """
    try:
        if (
            not isinstance(number, (int, float))
            or not float(number).is_integer()
            or not isinstance(limit, (int))
            or not int(limit).is_integer()
        ):
            raise NotIntegerError("Inputs must be integers")
        if limit <= 1:
            raise InvalidInputError("Limit must be greater than 1")
        number = int(number)
        if number == 0:
            raise MathError("Cannot generate multiple list for 0")
        if not positive_only:
            return sorted(
                [-number * i for i in range(1, limit)]
                + [number * i for i in range(limit)]
            )
        return [number * i for i in range(limit)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def common_divisors(numbers):
    """
    Generate a list of common divisors of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - list: A list of common divisors.

    Raises:
        - MathError: If the list does not have enough elements.
        - ListError: Input must be a list or tuple.
    """

    def get_divisors(n):
        try:
            n = abs(int(n))
            return set(
                [i for i in range(1, n + 1) if n % i == 0]
                + [-i for i in range(1, n + 1) if n % i == 0]
            )
        except (ValueError, TypeError):
            raise TypeErrorCustom("List element is invalid")

    try:
        numbers = list(set(numbers))
        for i in numbers:
            if i == 0:
                numbers.remove(i)
        if not isinstance(numbers, (list, tuple)):
            raise ListError("Input must be a list or tuple")
        if len(numbers) < 2:
            raise MathError("List must have at least 2 elements")
        for num in numbers:
            if not isinstance(num, (int, float)) or not float(num).is_integer():
                raise NotIntegerError("All elements must be integers")
        result = get_divisors(numbers[0])
        for num in numbers[1:]:
            result = result.intersection(get_divisors(num))
        return sorted(list(result))
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


def greatest_common_divisor(numbers):
    """
    Calculate the greatest common divisor of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - int: The greatest common divisor of the list.

    Raises:
        - MathError: If the list is invalid.
        - ListError: If the input is not a list or tuple.
    """

    def get_gcd(number1, number2):
        try:
            if not (
                isinstance(number1, (int, float)) and isinstance(number2, (int, float))
            ) or not (float(number1).is_integer() and float(number2).is_integer()):
                raise NotIntegerError("Both numbers must be integers")
            number1, number2 = int(number1), int(number2)
            return math.gcd(number1, number2)
        except (ValueError, TypeError):
            raise TypeErrorCustom("Invalid input or not a number")

    try:
        numbers = list(set(numbers))
        for i in numbers:
            if i == 0:
                numbers.remove(i)
        if not isinstance(numbers, (list, tuple)):
            raise ListError("Input must be a list or tuple")
        if len(numbers) < 2:
            raise MathError("List is invalid")
        for num in numbers:
            if not isinstance(num, (int, float)) or not float(num).is_integer():
                raise NotIntegerError("All elements must be integers")
        result = int(numbers[0])
        for num in numbers[1:]:
            result = get_gcd(result, int(num))
            if result == 1:
                break
        return result
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


def least_common_multiple(numbers):
    """
    Calculate the least common multiple of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - int: The least common multiple of the list.

    Raises:
        - MathError: If the list is invalid.
        - ListError: Input must be a list or tuple.
    """

    def get_lcm(number1, number2):
        try:
            if not (
                isinstance(number1, (int, float)) and isinstance(number2, (int, float))
            ) or not (float(number1).is_integer() and float(number2).is_integer()):
                raise NotIntegerError("Both numbers must be integers")
            number1, number2 = int(number1), int(number2)
            if number1 == 0 or number2 == 0:
                raise DivisionByZeroError("Cannot calculate LCM with 0")
            return math.lcm(number1, number2)
        except (ValueError, TypeError):
            raise TypeErrorCustom("Invalid input or not a number")

    try:
        if not isinstance(numbers, (list, tuple)):
            raise ListError("Input must be a list or tuple")
        if len(numbers) < 2 or 0 in numbers:
            raise MathError("List is invalid")
        for num in numbers:
            if not isinstance(num, (int, float)) or not float(num).is_integer():
                raise NotIntegerError("All elements must be integers")
        result = int(numbers[0])
        for num in numbers[1:]:
            result = get_lcm(result, int(num))
        return result
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


# Functions for twin primes and abundant numbers
def is_twin_prime(number):
    """
    Check if a number is a twin prime.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is a twin prime, False otherwise.

    Raises:
        - NotIntegerError: Input must be an integer.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Input must be an integer")
        number = int(number)
        return is_prime(number) and is_prime(sum_of_digits(number))
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def generate_twin_prime_list(limit):
    """
    Generate a list of twin primes from 0 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of twin primes.

    Raises:
        - NotIntegerError: Input must be an integer.
        - InvalidInputError: Limit must be non-negative.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Limit must be an integer")
        limit = int(limit)
        if limit < 0:
            raise InvalidInputError("Limit must be non-negative")
        return [i for i in range(limit) if is_twin_prime(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def is_abundant_number(number):
    """
    Check if a number is an abundant number.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is abundant, False otherwise.

    Raises:
        - NotIntegerError: Input must be an integer.
        - InvalidInputError: Limit must be non-negative.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Input must be an integer")
        number = int(number)
        if number <= 0:
            return False
        return sum(i for i in range(1, number) if number % i == 0) > number
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def generate_abundant_number_list(limit):
    """
    Generate a list of abundant numbers from 0 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of abundant numbers.

    Raises:
        - NotIntegerError: Input must be an integer.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Limit must be an integer")
        limit = int(limit)
        if limit < 0:
            raise InvalidInputError("Limit must be non-negative")
        return [i for i in range(limit) if is_abundant_number(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def prime_factors(number):
    """
    Factorize a number into a list of prime factors.

    Parameters:
        - number (int): The number to factorize.

    Returns:
        - list: A list of prime factors.

    Raises:
        - MathError: If number <= 1.
        - NotIntegerError: Input must be an integer.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Input must be an integer")
        number = int(number)
        if number <= 1:
            raise MathError("Number must be greater than 1")
        factors = []
        divisor = 2
        while number > 1:
            while number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            divisor += 1
        return factors
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def greatest_common_prime_divisor(number1, number2):
    """
    Find the greatest common prime divisor of two numbers.

    Parameters:
        - number1 (int): The first number.
        - number2 (int): The second number.

    Returns:
        - int: The greatest common prime divisor of number1 and number2.

    Raises:
        - MathError: If the numbers are not greater than 1 or have no common prime divisor.
        - NotIntegerError: Both numbers must be integers.
    """
    try:
        if not (
            isinstance(number1, (int, float)) and isinstance(number2, (int, float))
        ) or not (float(number1).is_integer() and float(number2).is_integer()):
            raise NotIntegerError("Both numbers must be integers")
        number1, number2 = int(number1), int(number2)
        if number1 <= 1 or number2 <= 1:
            raise MathError("Numbers must be greater than 1")
        factors1 = set(prime_factors(number1))
        factors2 = set(prime_factors(number2))
        common_factors = factors1.intersection(factors2)
        if not common_factors:
            raise MathError("No common prime divisor")
        return max(common_factors)
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


# Function to solve equations
def solve_equation(degree, coefficients):
    """
    Solve equations from degree 1 to degree `n` based on coefficients.

    Parameters:
        - degree (int): The degree of the equation.
        - coefficients (list): The list of coefficients of the equation.

    Returns:
        - str: The result of the equation's roots.

    Raises:
        - ImportError: If numpy is not installed.
        - InvalidInputError: If the degree or coefficients are invalid.
    """
    try:
        if numpy is None:
            raise ImportError(
                "This function requires numpy. Please run: pip install numpy"
            )
        if not isinstance(degree, (int, float)) or not float(degree).is_integer():
            raise NotIntegerError("Degree must be an integer")
        degree = int(degree)
        if not isinstance(coefficients, (list, tuple)):
            raise ListError("Coefficients must be a list or tuple")
        if len(coefficients) != degree + 1:
            raise InvalidInputError(
                f"An equation of degree {degree} must have {degree + 1} coefficients"
            )
        for coef in coefficients:
            if not isinstance(coef, (int, float)):
                raise TypeErrorCustom("Coefficients must be numbers")
        roots = numpy.roots(coefficients)
        real_roots = [r for r in roots if numpy.isreal(r)]
        complex_roots = [r for r in roots if not numpy.isreal(r)]
        result = "Roots of the equation:\n"
        if real_roots:
            result += "\nReal roots:\n" + "\n".join(
                f"x{i+1} = {r.real}" for i, r in enumerate(real_roots)
            )
        if complex_roots:
            result += "\nComplex roots:\n" + "\n".join(
                f"x{i+1} = {r}" for i, r in enumerate(complex_roots)
            )
        return (
            result.strip()
            if real_roots or complex_roots
            else "The equation has no real or complex roots"
        )
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


# Functions for list and string processing
def remove_duplicates(items):
    """
    Remove duplicate elements from a list.

    Parameters:
        - items (list): The list to process.

    Returns:
        - list: A list without duplicate elements.

    Raises:
        - ListError: Input must be a list or tuple.
    """
    try:
        if not isinstance(items, (list, tuple)):
            raise ListError("Input must be a list or tuple")
        return sorted(list(set(items)), reverse=True)
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


def extract_digits_from_string(text):
    """
    Extract digits from a string. Example: "abc123" = [1,2,3].

    Parameters:
        - text (str): The input string.

    Returns:
        - list: A list of digits.

    Raises:
        - InvalidInputError: If the string is empty.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Input must be a string")
        if not text:
            raise InvalidInputError("String cannot be empty")
        return [int(digit) for digit in re.findall(r"\d", text)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


def extract_numbers_from_string(text):
    """
    Extract numbers from a string. Example: "abc123" = [123].

    Parameters:
        - text (str): The input string.

    Returns:
        - list: A list of numbers.

    Raises:
        - InvalidInputError: If the string is empty.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Input must be a string")
        if not text:
            raise InvalidInputError("String cannot be empty")
        return [int(number) for number in re.findall(r"\d+", text)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


def extract_characters(text):
    """
    Extract non-digit characters from a string.

    Parameters:
        - text (str): The input string.

    Returns:
        - list: A list of non-digit characters.

    Raises:
        - TypeErrorCustom: Input must be a string.
        - InvalidInputError: String cannot be empty.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Input must be a string")
        if not text:
            raise InvalidInputError("String cannot be empty")
        return re.findall(r"\D", text)
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


def compress_string(text, compress_type):
    """
    Compress a string into 2 types.

    Parameters:
        - text (str): The input string.
        - compress_type (int): 1 or 2. If 1, "google" → "2ol2ge", if 2, "google" → "g2ogle".

    Returns:
        - str: The compressed string.

    Raises:
        - InvalidInputError: Compression type must be 1 or 2.
    """

    def type_1(text):
        try:
            if not isinstance(text, str):
                raise TypeErrorCustom("Input must be a string")
            if not text:
                raise InvalidInputError("String cannot be empty")
            sorted_chars = sorted([char for char in text], reverse=True)
            result = ""
            count = 1
            for i in range(1, len(sorted_chars)):
                if sorted_chars[i] == sorted_chars[i - 1]:
                    count += 1
                else:
                    result += (
                        str(count) + sorted_chars[i - 1]
                        if count > 1
                        else sorted_chars[i - 1]
                    )
                    count = 1
            result += str(count) + sorted_chars[-1] if count > 1 else sorted_chars[-1]
            return result
        except (ValueError, TypeError):
            raise TypeErrorCustom("Invalid input")

    def type_2(text):
        try:
            if not isinstance(text, str):
                raise TypeErrorCustom("Input must be a string")
            if not text:
                raise InvalidInputError("String cannot be empty")
            result = ""
            count = 1
            for i in range(1, len(text)):
                if text[i] == text[i - 1]:
                    count += 1
                else:
                    result += str(count) + text[i - 1] if count > 1 else text[i - 1]
                    count = 1
            result += str(count) + text[-1] if count > 1 else text[-1]
            return result
        except (ValueError, TypeError):
            raise TypeErrorCustom("Invalid input")

    if compress_type == 1:
        return type_1(text)
    elif compress_type == 2:
        return type_2(text)
    else:
        raise InvalidInputError("Compression type must be 1 or 2")


def compress_string_without_numbers(input_text):
    """
    Compress a string by removing numbers (e.g., "hhhoocssssiiinnnhhhhh" → "hocsinh").

    Parameters:
        - input_text (str): The input string.

    Returns:
        - str: The compressed string.

    Raises:
        - InvalidInputError: String cannot be empty.
    """
    try:
        if not isinstance(input_text, str):
            raise TypeErrorCustom("Input must be a string")
        if not input_text:
            raise InvalidInputError("String cannot be empty")
        result = input_text[0]
        for char in input_text[1:]:
            if char != result[-1]:
                result += char
        return result
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


def decompress_string(text):
    """
    Decompress a string (e.g., "g2ogle" → "google").

    Parameters:
        - text (str): The input string.

    Returns:
        - str: The decompressed string.

    Raises:
        - InvalidInputError: If the string is empty.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Input must be a string")
        if not text:
            raise InvalidInputError("String cannot be empty")
        result = ""
        count = ""
        for char in text:
            if char.isdigit():
                count += char
            else:
                result += char if count == "" else int(count) * char
                count = ""
        return result
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or invalid number in string")


def unique_characters_string(text):
    """
    Create a string with unique characters (e.g., "google" → "gole").

    Parameters:
        - text (str): The input string.

    Returns:
        - str: A string with no duplicate characters.

    Raises:
        - InvalidInputError: If the string is empty.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Input must be a string")
        if not text:
            raise InvalidInputError("String cannot be empty")
        text = text.lower()
        unique_chars = ""
        for char in text:
            if char not in unique_chars:
                unique_chars += char
        return unique_chars
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


# Caesar cipher
def caesar_cipher_to_numbers(text, shift):
    """
    Convert a string to a list of Caesar cipher numbers.

    Parameters:
        - text (str): The input string.
        - shift (int): The shift value.

    Returns:
        - list: A list of Caesar cipher numbers.

    Raises:
        - InvalidInputError: If the string is empty or contains non-alphabetic characters.
        - NotIntegerError: Shift must be an integer.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Input must be a string")
        if not isinstance(shift, (int, float)) or not float(shift).is_integer():
            raise NotIntegerError("Shift must be an integer")
        shift = int(shift)
        if not text:
            raise InvalidInputError("String cannot be empty")
        text = "".join([char for char in text.upper() if char != " "]).strip()
        if not text.isalpha():
            raise InvalidInputError("String must contain only alphabetic characters")
        char_map = {chr(65 + i): i for i in range(26)}
        shifted_map = [(i + shift) % 26 for i in range(26)]
        return [shifted_map[char_map[char]] for char in text]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


def caesar_cipher_from_numbers(numbers, shift):
    """
    Decode a list of Caesar cipher numbers to a string.

    Parameters:
        - numbers (list): The list of numbers.
        - shift (int): The shift value.

    Returns:
        - str: The decoded string.

    Raises:
        - InvalidInputError: If the list is empty or numbers are not integers from 0 to 25.
        - ListError: Input must be a list or tuple.
        - NotIntegerError: Shift must be an integer.
    """
    try:
        if not isinstance(numbers, (list, tuple)):
            raise ListError("Input must be a list or tuple")
        if not isinstance(shift, (int, float)) or not float(shift).is_integer():
            raise NotIntegerError("Shift must be an integer")
        shift = int(shift)
        if not numbers:
            raise InvalidInputError("List cannot be empty")
        for num in numbers:
            if (
                not isinstance(num, (int, float))
                or not float(num).is_integer()
                or int(num) < 0
                or int(num) > 25
            ):
                raise InvalidInputError("Numbers must be integers from 0 to 25")
        char_map = {i: chr(65 + i) for i in range(26)}
        shifted_map = [(i + shift) % 26 for i in range(26)]
        reverse_map = {shifted_map[i]: i for i in range(26)}
        decoded = [reverse_map[int(num)] for num in numbers]
        return "".join([char_map[i] for i in decoded])
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")


# Special calculation support functions
def calculate_electricity_bill_Vietnamese(old_reading, new_reading):
    """
    Calculate electricity bill.

    Parameters:
        - old_reading (str): Old meter reading.
        - new_reading (str): New meter reading.

    Returns:
        - str: Calculation result.

    Raises:
        - MathError: If readings are invalid.
    """
    try:
        old_val = float(old_reading)
        new_val = float(new_reading)
        if new_val > old_val and old_val > 0 and new_val > 0:
            kwh = new_val - old_val
            if 0 <= kwh < 51:
                total = kwh * 1678
            elif 50 < kwh < 101:
                total = ((kwh - 50) * 1734) + 50 * 1678
            elif 100 < kwh < 201:
                total = ((kwh - 100) * 2014) + 50 * 1734 + 50 * 1678
            elif 200 < kwh < 301:
                total = ((kwh - 200) * 2536) + 100 * 2014 + 50 * 1734 + 50 * 1678
            elif 300 < kwh < 401:
                total = (
                    ((kwh - 300) * 2834)
                    + 100 * 2536
                    + 100 * 2014
                    + 50 * 1734
                    + 50 * 1678
                )
            else:
                total = (
                    ((kwh - 400) * 2927)
                    + 100 * 2834
                    + 100 * 2536
                    + 100 * 2014
                    + 50 * 1734
                    + 50 * 1678
                )
            return f"- Electricity consumed this month: {kwh} Kwh\n- Electricity bill this month: {total} VND"
        raise MathError("Invalid readings")
    except (ValueError, TypeError):
        raise TypeErrorCustom("Readings must be valid numbers")


def largest_number_with_digit_sum(digit_count, target_sum):
    """
    Find the largest number with digit_count digits and sum of digits equal to target_sum.

    Parameters:
        - digit_count (int): Number of digits.
        - target_sum (int): Sum of digits.

    Returns:
        - str: The largest number satisfying the condition.

    Raises:
        - MathError: If unable to create a number that satisfies the condition.
    """
    try:
        if not (
            isinstance(digit_count, (int, float))
            and isinstance(target_sum, (int, float))
        ) or not (float(digit_count).is_integer() and float(target_sum).is_integer()):
            raise NotIntegerError("Inputs must be integers")
        digits = abs(int(digit_count))
        total = abs(int(target_sum))
        if digits == 0 or total == 0:
            return "0"
        if total > 9 * digits:
            raise MathError(
                "Cannot create a number with digit sum greater than 9 * number of digits"
            )
        result = ["9"] * (total // 9)
        if total % 9 != 0:
            result.append(str(total % 9))
        while len(result) < digits:
            result.append("0")
        return "".join(result[:digits])
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


# Sequence generation rules
def generate_sequence_rule_1(number):
    """
    Generate a sequence of positive integers based on the rule:
    - 1 number divisible by 1,
    - 2 numbers divisible by 2,
    - 3 numbers divisible by 3,
    - and so on, with increasing numbers and no duplicates.

    Parameters:
        - number (int): The number of elements to generate in the sequence.

    Returns:
        - list: A list of the first number integers in the sequence.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Number must be an integer")
    if number <= 1:
        raise InvalidInputError("Number must be greater than 1")

    def helper(k):
        if k == 1:
            return 1
        number_to_find = 1
        position = 0
        for i in range(1, 1000):
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

    return [helper(i) for i in range(1, number + 1)]


def generate_sequence_rule_2(base, count):
    """
    Generate a list of multiples of base with count elements.

    Parameters:
        - base (int): The number to generate multiples.
        - count (int): The number of elements.

    Returns:
        - list: A list of multiples of base.
    """
    try:
        if not (
            isinstance(base, (int, float)) and isinstance(count, (int, float))
        ) or not (float(base).is_integer() and float(count).is_integer()):
            raise NotIntegerError("Both parameters must be integers")
        base, count = int(base), int(count)
        if count < 0:
            raise InvalidInputError("Count must be non-negative")
        return [base * i for i in range(count)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


def generate_sequence_rule_3(count, base):
    """
    Generate a list of powers of base from 0 to count.

    Parameters:
        - count (int): The number of elements.
        - base (int): The base number.

    Returns:
        - list: A list of powers of base.
    """
    try:
        if not (
            isinstance(count, (int, float)) and isinstance(base, (int, float))
        ) or not (float(count).is_integer() and float(base).is_integer()):
            raise NotIntegerError("Both parameters must be integers")
        count, base = int(count), int(base)
        if count < 0:
            raise InvalidInputError("Count must be non-negative")
        return [base**i for i in range(count)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input or not a number")


# Count inversions
def count_inversions(numbers):
    """
    Count the number of inversions in a list.

    Parameters:
        - numbers (list): The list to count inversions.

    Returns:
        - int: The number of inversions.
    """
    try:
        if not isinstance(numbers, (list, tuple)):
            raise ListError("Input must be a list or tuple")
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise TypeErrorCustom("Elements must be numbers")
        count = 0
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] > numbers[j]:
                    count += 1
        return count
    except (ValueError, TypeError):
        raise TypeErrorCustom("Invalid input")
