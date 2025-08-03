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
- 1.0.0.

Release Date
-------------------------------------------------------------------------------
- August 3, 2025.

License
-------------------------------------------------------------------------------
- Copyright © 2024 Joesifer

Supported Python Version
-------------------------------------------------------------------------------
- Python 3.7 or higher.

Dependencies
-------------------------------------------------------------------------------
- Built-in: `math`, `re`, `random`, `functools`, `argparse`.
- External: `numpy` (optional for `solve_equation` and `generate_prime_list`).
- External (plan): `gmpy2` (optional for big integer support).

License Type
-------------------------------------------------------------------------------
- MIT License.

Additional Information
-------------------------------------------------------------------------------

For usage instructions, please refer to:
  >>> Link: https://github.com/Joesifer/pchjlib/blob/main/README.md

Feedback and support are welcome via:
  >>> Email: `phanchanhung12055@gmail.com`

THANK YOU!!!
===============================================================================
"""

import math, random, re, argparse
from functools import lru_cache

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

try:
    __plan__ = "Prepared support for big integers using gmpy2 to handle numbers exceeding Python's int limits (to be fully implemented in future releases)."
    import gmpy2
except ImportError:
    gmpy2 = None


# Functions to check prime numbers and related numbers
def is_prime(number):
    """
    Check if a number is a prime number.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is prime, False otherwise.

    Raises:
        - InvalidInputError: If the input is not an integer.
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

    if not isinstance(number, int):
        raise InvalidInputError("Input must be an integer")
    return miller_rabin(number)


def generate_prime_list(limit):
    """
    Generate a list of prime numbers from 0 to limit using the Sieve algorithm.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of prime numbers.

    Raises:
        - InvalidInputError: If limit is not an integer >= 2.
        - ImportError: If numpy is not installed.
    """
    if numpy is None:
        raise ImportError("This function requires numpy. Please run: pip install numpy")
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 2:
        raise InvalidInputError("Limit must be >= 2")
    sieve = numpy.ones(limit + 1, dtype=bool)
    sieve[0:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i * i : limit + 1 : i] = False
    return numpy.where(sieve)[0].tolist()


def is_emirp(number):
    """
    Check if a number is an emirp (a prime number whose reverse is also a prime).

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is an emirp, False otherwise.

    Raises:
        - InvalidInputError: If the input is not a positive integer >= 2.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Input must be an integer")
    if number < 2:
        raise InvalidInputError("Number must be >= 2")
    if not is_prime(number):
        return False
    reversed_number = reverse_number(number)
    return is_prime(reversed_number)


def reverse_number(number):
    """
    Reverse the digits of a number using arithmetic operations.

    Parameters:
        - number (int): The number to reverse.

    Returns:
        - int: The reversed number.
    """
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10
    return reversed_num


def generate_emirp_list(limit):
    """
    Generate a list of emirp numbers from 2 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of emirp numbers.

    Raises:
        - InvalidInputError: If limit is not an integer >= 2.
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 2:
        raise InvalidInputError("Limit must be >= 2")
    return [i for i in range(2, limit + 1) if is_emirp(i)]


# Fibonacci functions with caching
@lru_cache(maxsize=None)
def fibonacci_at_index(index):
    """
    Calculate the Fibonacci number at the given index using iteration with caching.

    Parameters:
        - index (int): The position of the Fibonacci number (starting from 0).

    Returns:
        - int: The Fibonacci number at the given index.

    Raises:
        - InvalidInputError: If index is not a non-negative integer.
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


def generate_fibonacci_list(count):
    """
    Generate a list of the first count Fibonacci numbers.

    Parameters:
        - count (int): The number of elements in the list.

    Returns:
        - list: A list of Fibonacci numbers.

    Raises:
        - InvalidInputError: If count is not a non-negative integer.
    """
    if not isinstance(count, int):
        raise InvalidInputError("Count must be an integer")
    if count < 0:
        raise InvalidInputError("Count must be non-negative")
    return [fibonacci_at_index(i) for i in range(count)]


# Functions for perfect, narcissistic, amicable, and other special numbers
def sum_of_divisors(number):
    """
    Calculate the sum of positive divisors of a number (excluding itself).

    Parameters:
        - number (int): The number to calculate the sum of divisors.

    Returns:
        - int: The sum of divisors.

    Raises:
        - InvalidInputError: If number is not a positive integer.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Number must be an integer")
    if number <= 0:
        raise InvalidInputError("Number must be positive")
    return sum(i for i in range(1, number) if number % i == 0)


def sum_of_digits(number):
    """
    Calculate the sum of digits of an integer.

    Parameters:
        - number (int): The number to calculate the sum of digits.

    Returns:
        - int: The sum of digits.

    Raises:
        - InvalidInputError: If the input is not an integer.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Number must be an integer")
    return sum(int(digit) for digit in str(abs(number)))


def is_perfect_number(number):
    """
    Check if a number is a perfect number.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is perfect, False otherwise.

    Raises:
        - InvalidInputError: If number is not a positive integer.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Input must be an integer")
    if number < 1:
        raise InvalidInputError("Number must be positive")
    return sum_of_divisors(number) == number


def generate_perfect_number_list(limit):
    """
    Generate a list of perfect numbers from 1 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of perfect numbers.

    Raises:
        - InvalidInputError: If limit is not a positive integer.
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 1:
        raise InvalidInputError("Limit must be positive")
    return [i for i in range(1, limit + 1) if is_perfect_number(i)]


def is_narcissistic_number(number):
    """
    Check if a number is a narcissistic number.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is narcissistic, False otherwise.

    Raises:
        - InvalidInputError: If number is not a non-negative integer.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Input must be an integer")
    if number < 0:
        raise InvalidInputError("Number must be non-negative")
    digits = len(str(number))
    return sum(int(digit) ** digits for digit in str(number)) == number


def generate_narcissistic_number_list(limit):
    """
    Generate a list of narcissistic numbers from 0 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of narcissistic numbers.

    Raises:
        - InvalidInputError: If limit is not a non-negative integer.
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 0:
        raise InvalidInputError("Limit must be non-negative")
    return [i for i in range(limit + 1) if is_narcissistic_number(i)]


def are_amicable_numbers(number1, number2):
    """
    Check if two numbers are amicable numbers.

    Parameters:
        - number1 (int): The first number.
        - number2 (int): The second number.

    Returns:
        - bool: True if the numbers are amicable, False otherwise.

    Raises:
        - InvalidInputError: If the numbers are not positive integers.
    """
    if not (isinstance(number1, int) and isinstance(number2, int)):
        raise InvalidInputError("Both numbers must be integers")
    if number1 < 1 or number2 < 1:
        raise InvalidInputError("Numbers must be positive")
    return sum_of_divisors(number1) == number2 and sum_of_divisors(number2) == number1


def is_happy_number(number):
    """
    Check if a number is a happy number.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is happy, False otherwise.

    Raises:
        - InvalidInputError: If number is not a positive integer.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Input must be an integer")
    if number < 1:
        raise InvalidInputError("Number must be positive")
    seen = set()
    while number != 1 and number not in seen:
        seen.add(number)
        number = sum(int(digit) ** 2 for digit in str(number))
    return number == 1


def generate_happy_number_list(limit):
    """
    Generate a list of happy numbers from 1 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of happy numbers.

    Raises:
        - InvalidInputError: If limit is not a positive integer.
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 1:
        raise InvalidInputError("Limit must be positive")
    return [i for i in range(1, limit + 1) if is_happy_number(i)]


# Functions for square numbers, strong numbers, friendly numbers
def is_square_number(number):
    """
    Check if a number is a square number.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is a square number, False otherwise.

    Raises:
        - InvalidInputError: If number is not a non-negative integer.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Input must be an integer")
    if number < 0:
        raise InvalidInputError("Number must be non-negative")
    sqrt_number = int(math.sqrt(number))
    return sqrt_number * sqrt_number == number


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
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 0:
        raise InvalidInputError("Limit must be non-negative")
    return [i * i for i in range(int(math.sqrt(limit)) + 1) if i * i <= limit]


def are_friendly_numbers(number1, number2):
    """
    Check if two numbers are friendly numbers.

    Parameters:
        - number1 (int): The first number.
        - number2 (int): The second number.

    Returns:
        - bool: True if the numbers are friendly, False otherwise.

    Raises:
        - InvalidInputError: If the numbers are not positive integers.
    """
    if not (isinstance(number1, int) and isinstance(number2, int)):
        raise InvalidInputError("Both numbers must be integers")
    if number1 < 1 or number2 < 1:
        raise InvalidInputError("Numbers must be positive")
    return sum_of_divisors(number1) / number1 == sum_of_divisors(number2) / number2


def is_strong_number(number, variant=1):
    """
    Check if a number is a strong number.

    Parameters:
        - number (int): The number to check.
        - variant (int): 1 - Sum of digits is prime; 2 - Has a square prime factor.

    Returns:
        - bool: True if the number is strong, False otherwise.

    Raises:
        - InvalidInputError: If number is not a non-negative integer or variant is invalid.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Input must be an integer")
    if number < 0:
        raise InvalidInputError("Number must be non-negative")
    if variant not in [1, 2]:
        raise InvalidInputError("Variant must be 1 or 2")
    if variant == 1:
        return is_prime(sum_of_digits(number))
    else:  # variant == 2
        factors = prime_factors(number)
        unique_factors = set(factors)
        for prime in unique_factors:
            if factors.count(prime) >= 2:
                return True
        return False


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
        - InvalidInputError: If number is not an integer or is zero.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Input must be an integer")
    if number == 0:
        raise InvalidInputError("Number cannot be zero")
    number = abs(number)
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    if not positive_only:
        divisors += [-i for i in divisors]
    return sorted(divisors)


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
        - InvalidInputError: If inputs are not integers or number is zero or limit < 1.
    """
    if not (isinstance(number, int) and isinstance(limit, int)):
        raise InvalidInputError("Inputs must be integers")
    if number == 0:
        raise InvalidInputError("Number cannot be zero")
    if limit < 1:
        raise InvalidInputError("Limit must be positive")
    if positive_only:
        return [number * i for i in range(1, limit + 1)]
    return sorted(
        [-number * i for i in range(1, limit + 1)]
        + [number * i for i in range(limit + 1)]
    )


def common_divisors(numbers):
    """
    Generate a list of common divisors of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - list: A list of common divisors.

    Raises:
        - InvalidInputError: If input is not a list or contains non-integers.
        - MathError: If list has fewer than 2 non-zero elements.
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


def greatest_common_divisor(numbers):
    """
    Calculate the greatest common divisor of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - int: The greatest common divisor of the list.

    Raises:
        - InvalidInputError: If input is not a list or contains non-integers.
        - MathError: If list has fewer than 2 non-zero elements.
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


def least_common_multiple(numbers):
    """
    Calculate the least common multiple of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - int: The least common multiple of the list.

    Raises:
        - InvalidInputError: If input is not a list or contains non-integers or zeros.
        - MathError: If list has fewer than 2 elements.
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


# Functions for twin primes and abundant numbers
def is_twin_prime(number):
    """
    Check if a number is a twin prime.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is a twin prime, False otherwise.

    Raises:
        - InvalidInputError: If number is not an integer.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Input must be an integer")
    return is_prime(number) and (is_prime(number - 2) or is_prime(number + 2))


def generate_twin_prime_list(limit):
    """
    Generate a list of twin primes from 2 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of twin primes.

    Raises:
        - InvalidInputError: If limit is not an integer >= 2.
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 2:
        raise InvalidInputError("Limit must be >= 2")
    return [i for i in range(2, limit + 1) if is_twin_prime(i)]


def is_abundant_number(number):
    """
    Check if a number is an abundant number.

    Parameters:
        - number (int): The number to check.

    Returns:
        - bool: True if the number is abundant, False otherwise.

    Raises:
        - InvalidInputError: If number is not a positive integer.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Input must be an integer")
    if number < 1:
        raise InvalidInputError("Number must be positive")
    return sum_of_divisors(number) > number


def generate_abundant_number_list(limit):
    """
    Generate a list of abundant numbers from 1 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of abundant numbers.

    Raises:
        - InvalidInputError: If limit is not a positive integer.
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 1:
        raise InvalidInputError("Limit must be positive")
    return [i for i in range(1, limit + 1) if is_abundant_number(i)]


def prime_factors(number):
    """
    Factorize a number into a list of prime factors.

    Parameters:
        - number (int): The number to factorize.

    Returns:
        - list: A list of prime factors.

    Raises:
        - InvalidInputError: If number is not a positive integer > 1.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Input must be an integer")
    if number <= 1:
        raise InvalidInputError("Number must be greater than 1")
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors


def greatest_common_prime_divisor(number1, number2):
    """
    Find the greatest common prime divisor of two numbers.

    Parameters:
        - number1 (int): The first number.
        - number2 (int): The second number.

    Returns:
        - int: The greatest common prime divisor of number1 and number2.

    Raises:
        - InvalidInputError: If numbers are not positive integers > 1.
        - MathError: If no common prime divisor exists.
    """
    if not (isinstance(number1, int) and isinstance(number2, int)):
        raise InvalidInputError("Both numbers must be integers")
    if number1 <= 1 or number2 <= 1:
        raise InvalidInputError("Numbers must be greater than 1")
    factors1 = set(prime_factors(number1))
    factors2 = set(prime_factors(number2))
    common_factors = factors1.intersection(factors2)
    if not common_factors:
        raise MathError("No common prime divisor")
    return max(common_factors)


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
    if numpy is None:
        raise ImportError("This function requires numpy. Please run: pip install numpy")
    if not isinstance(degree, int):
        raise InvalidInputError("Degree must be an integer")
    if not isinstance(coefficients, (list, tuple)):
        raise InvalidInputError("Coefficients must be a list or tuple")
    if len(coefficients) != degree + 1:
        raise InvalidInputError(
            f"An equation of degree {degree} must have {degree + 1} coefficients"
        )
    for coef in coefficients:
        if not isinstance(coef, (int, float)):
            raise InvalidInputError("Coefficients must be numbers")
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


# Functions for list and string processing
def remove_duplicates(items):
    """
    Remove duplicate elements from a list.

    Parameters:
        - items (list): The list to process.

    Returns:
        - list: A list without duplicate elements.

    Raises:
        - InvalidInputError: If input is not a list or tuple.
    """
    if not isinstance(items, (list, tuple)):
        raise InvalidInputError("Input must be a list or tuple")
    return sorted(list(set(items)), reverse=True)


def extract_digits_from_string(text):
    """
    Extract digits from a string. Example: "abc123" = [1,2,3].

    Parameters:
        - text (str): The input string.

    Returns:
        - list: A list of digits.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    return [int(digit) for digit in re.findall(r"\d", text)]


def extract_numbers_from_string(text):
    """
    Extract numbers from a string. Example: "abc123" = [123].

    Parameters:
        - text (str): The input string.

    Returns:
        - list: A list of numbers.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    return [int(number) for number in re.findall(r"\d+", text)]


def extract_characters(text):
    """
    Extract non-digit characters from a string.

    Parameters:
        - text (str): The input string.

    Returns:
        - list: A list of non-digit characters.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    return re.findall(r"\D", text)


def compress_string(text, compress_type):
    """
    Compress a string into 2 types.

    Parameters:
        - text (str): The input string.
        - compress_type (int): 1 or 2. If 1, "google" → "e2gl2o", if 2, "google" → "g2ogle".

    Returns:
        - str: The compressed string.

    Raises:
        - InvalidInputError: If input is not a string, is empty, or compress_type is invalid.
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    if compress_type not in [1, 2]:
        raise InvalidInputError("Compression type must be 1 or 2")

    if compress_type == 1:
        result = ""
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


def compress_string_without_numbers(input_text):
    """
    Compress a string by removing duplicates (e.g., "hhhoocssssiiinnnhhhhh" → "hocsinh").

    Parameters:
        - input_text (str): The input string.

    Returns:
        - str: The compressed string.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.
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


def decompress_string(text):
    """
    Decompress a string (e.g., "g2ogle" → "google").

    Parameters:
        - text (str): The input string.

    Returns:
        - str: The decompressed string.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.
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


def unique_characters_string(text):
    """
    Create a string with unique characters (e.g., "google" → "gole").

    Parameters:
        - text (str): The input string.

    Returns:
        - str: A string with no duplicate characters.

    Raises:
        - InvalidInputError: If the input is not a string or is empty.
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
        - InvalidInputError: If the input is not a string, is empty, or contains non-alphabetic characters.
        - NotIntegerError: If shift is not an integer.
    """
    if not isinstance(text, str):
        raise InvalidInputError("Input must be a string")
    if not text:
        raise InvalidInputError("String cannot be empty")
    if not isinstance(shift, int):
        raise NotIntegerError("Shift must be an integer")
    text = text.upper()
    if not text.isalpha():
        raise InvalidInputError("String must contain only alphabetic characters")
    return [(ord(char) - 65 + shift) % 26 for char in text]


def caesar_cipher_from_numbers(numbers, shift):
    """
    Decode a list of Caesar cipher numbers to a string.

    Parameters:
        - numbers (list): The list of numbers.
        - shift (int): The shift value.

    Returns:
        - str: The decoded string.

    Raises:
        - InvalidInputError: If the input is not a list, is empty, or contains invalid numbers.
        - NotIntegerError: If shift is not an integer.
    """
    if not isinstance(numbers, (list, tuple)):
        raise InvalidInputError("Input must be a list or tuple")
    if not numbers:
        raise InvalidInputError("List cannot be empty")
    if not isinstance(shift, int):
        raise NotIntegerError("Shift must be an integer")
    for num in numbers:
        if not isinstance(num, int) or num < 0 or num > 25:
            raise InvalidInputError("Numbers must be integers between 0 and 25")
    return "".join(chr((num - shift) % 26 + 65) for num in numbers)


# Special calculation support functions
def calculate_electricity_bill_Vietnamese(old_reading, new_reading):
    """
    Calculate electricity bill based on Vietnamese pricing tiers.

    Parameters:
        - old_reading (float): Old meter reading.
        - new_reading (float): New meter reading.

    Returns:
        - str: Calculation result.

    Raises:
        - InvalidInputError: If readings are not numbers or invalid.
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
    return f"- Electricity consumed this month: {kwh} Kwh\n- Electricity bill this month: {total} VND"


def largest_number_with_digit_sum(digit_count, target_sum):
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
    """
    if not (isinstance(digit_count, int) and isinstance(target_sum, int)):
        raise InvalidInputError("Inputs must be integers")
    if digit_count < 0 or target_sum < 0:
        raise InvalidInputError("Inputs must be non-negative")
    if target_sum > 9 * digit_count:
        raise MathError("Sum cannot exceed 9 times the number of digits")
    if digit_count == 0 or target_sum == 0:
        return "0" * digit_count if digit_count > 0 else "0"
    result = []
    remaining_sum = target_sum
    for i in range(digit_count - 1, -1, -1):
        digit = min(9, remaining_sum)
        result.append(str(digit))
        remaining_sum -= digit
    return "".join(result)


# Sequence generation rules
def generate_sequence_rule_1(number):
    """
    Generate a sequence based on a specific rule.

    Parameters:
        - number (int): The number of elements to generate.

    Returns:
        - list: A list of integers in the sequence.

    Raises:
        - InvalidInputError: If number is not a positive integer.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Number must be an integer")
    if number < 1:
        raise InvalidInputError("Number must be positive")
    result = []
    current = 1
    for i in range(1, number + 1):
        result.append(current)
        current += i
    return result


def generate_sequence_rule_2(base, count):
    """
    Generate a list of multiples of base with count elements.

    Parameters:
        - base (int): The number to generate multiples.
        - count (int): The number of elements.

    Returns:
        - list: A list of multiples of base.

    Raises:
        - InvalidInputError: If inputs are not integers or count is negative.
    """
    if not (isinstance(base, int) and isinstance(count, int)):
        raise InvalidInputError("Inputs must be integers")
    if count < 0:
        raise InvalidInputError("Count must be non-negative")
    return [base * i for i in range(count)]


def generate_sequence_rule_3(count, base):
    """
    Generate a list of powers of base from 0 to count-1.

    Parameters:
        - count (int): The number of elements.
        - base (int): The base number.

    Returns:
        - list: A list of powers of base.

    Raises:
        - InvalidInputError: If inputs are not integers or count is negative.
    """
    if not (isinstance(count, int) and isinstance(base, int)):
        raise InvalidInputError("Inputs must be integers")
    if count < 0:
        raise InvalidInputError("Count must be non-negative")
    return [base**i for i in range(count)]


# Count inversions
def count_inversions(numbers):
    """
    Count the number of inversions in a list.

    Parameters:
        - numbers (list): The list to count inversions.

    Returns:
        - int: The number of inversions.

    Raises:
        - InvalidInputError: If input is not a list or contains non-numbers.
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


def main():
    parser = argparse.ArgumentParser(
        description="The pchjlib library is a versatile toolkit..."
    )

    # Option to display version
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 1.0.0",
        help="Display the version of the library",
    )

    # Option to check for prime number
    parser.add_argument(
        "-p",
        "--prime",
        type=int,
        help="Check whether a number is a prime number",
    )

    # Option to calculate Fibonacci number
    parser.add_argument(
        "-f",
        "--fibonacci",
        type=int,
        help="Calculate the Fibonacci number at the given index",
    )

    args = parser.parse_args()

    if args.prime is not None:
        try:
            result = is_prime(args.prime)
            print(
                f"{args.prime} {'is a prime number' if result else 'is not a prime number'}"
            )
        except Exception as e:
            print(f"Error: {e}")
    elif args.fibonacci is not None:
        try:
            result = fibonacci_at_index(args.fibonacci)
            print(f"Fibonacci number at index {args.fibonacci}: {result}")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Welcome to pchjlib version 1.0.0!")
        print("Use -h or --help for more information.")


if __name__ == "__main__":
    main()
