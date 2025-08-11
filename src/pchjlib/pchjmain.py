# pchjmain.py

"""
PCHJLIB😺
================================================================================================

>>> The module that contains the library's core functions.
>>> For detailed instructions, please see the `README.md` file.

================================================================================================
"""

import math, random, re, argparse
from functools import lru_cache


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


# Optional import for gmpy2 to handle large numbers
try:
    import gmpy2
except ImportError:
    gmpy2 = None


# Functions to check prime numbers and related numbers
def is_prime(input_number: int) -> bool:
    """
    Check if a number is a prime number.

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is prime, False otherwise.

    Raises:
        - InvalidInputError: If the input is not an integer or negative.

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(4)
        False
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 0:
        raise InvalidInputError("Input must be non-negative")
    if gmpy2 and hasattr(gmpy2, "is_prime") and input_number > 2**64:
        return bool(gmpy2.is_prime(input_number))  # type: ignore

    def miller_rabin(n: int, k: int = 5) -> bool:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False

        def check(a: int, s: int, d: int, n: int) -> bool:
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

    return miller_rabin(input_number)


def generate_prime_list(limit: int) -> list:
    """
    Generate a list of prime numbers from 0 to limit using the Sieve algorithm.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of prime numbers.

    Raises:
        - InvalidInputError: If limit is not an integer >= 2.

    Example:
        >>> generate_prime_list(10)
        [2, 3, 5, 7]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 2:
        raise InvalidInputError("Limit must be >= 2")
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(limit + 1) if sieve[i]]


def is_emirp(input_number: int) -> bool:
    """
    Check if a number is an emirp (a prime number whose reverse is also a prime).

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is an emirp, False otherwise.

    Raises:
        - InvalidInputError: If the input is not a positive integer >= 2.

    Example:
        >>> is_emirp(13)
        True
    """

    def reverse_number(input_number: int) -> int:
        """
        Reverse the digits of a number using arithmetic operations.

        Parameters:
            - input_number (int): The number to reverse.

        Returns:
            - int: The reversed number.

        Example:
            >>> reverse_number(123)
            321
        """
        reversed_num = 0
        while input_number > 0:
            digit = input_number % 10
            reversed_num = reversed_num * 10 + digit
            input_number //= 10
        return reversed_num

    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 2:
        raise InvalidInputError("Number must be >= 2")
    if not is_prime(input_number):
        return False
    reversed_number = reverse_number(input_number)
    return is_prime(reversed_number)


def generate_emirp_list(limit: int) -> list:
    """
    Generate a list of emirp numbers from 2 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of emirp numbers.

    Raises:
        - InvalidInputError: If limit is not an integer >= 2.

    Example:
        >>> generate_emirp_list(20)
        [13, 17]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 2:
        raise InvalidInputError("Limit must be >= 2")
    return [i for i in range(2, limit + 1) if is_emirp(i)]


# Fibonacci functions with caching
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


# Functions for perfect, narcissistic, amicable, and other special numbers
def sum_of_divisors(input_number: int) -> int:
    """
    Calculate the sum of positive divisors of a number (excluding itself).

    Parameters:
        - input_number (int): The number to calculate the sum of divisors.

    Returns:
        - int: The sum of divisors.

    Raises:
        - InvalidInputError: If number is not a positive integer.

    Example:
        >>> sum_of_divisors(6)
        6
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Number must be an integer")
    if input_number <= 0:
        raise InvalidInputError("Number must be positive")
    return sum(i for i in range(1, input_number) if input_number % i == 0)


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


# Functions for square numbers, strong numbers, friendly numbers
def is_square_number(input_number: int) -> bool:
    """
    Check if a number is a square number.

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is a square number, False otherwise.

    Raises:
        - InvalidInputError: If number is not a non-negative integer.

    Example:
        >>> is_square_number(16)
        True
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 0:
        raise InvalidInputError("Number must be non-negative")
    sqrt_number = int(math.sqrt(input_number))
    return sqrt_number * sqrt_number == input_number


def generate_square_number_list(limit: int) -> list:
    """
    Generate a list of square numbers from 0 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of square numbers.

    Raises:
        - InvalidInputError: If limit is not a non-negative integer.

    Example:
        >>> generate_square_number_list(10)
        [0, 1, 4, 9]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 0:
        raise InvalidInputError("Limit must be non-negative")
    return [i * i for i in range(int(math.sqrt(limit)) + 1) if i * i <= limit]


def are_friendly_numbers(number1: int, number2: int) -> bool:
    """
    Check if two numbers are friendly numbers.

    Parameters:
        - number1 (int): The first number.
        - number2 (int): The second number.

    Returns:
        - bool: True if the numbers are friendly, False otherwise.

    Raises:
        - InvalidInputError: If the numbers are not positive integers.

    Example:
        >>> are_friendly_numbers(30, 140)
        True
    """
    if not (isinstance(number1, int) and isinstance(number2, int)):
        raise InvalidInputError("Both numbers must be integers")
    if number1 < 1 or number2 < 1:
        raise InvalidInputError("Numbers must be positive")
    return sum_of_divisors(number1) / number1 == sum_of_divisors(number2) / number2


def is_strong_number(input_number: int) -> bool:
    """
    Check if a number is a strong number (sum of factorial of its digits equals the number itself).

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is strong, False otherwise.

    Raises:
        - InvalidInputError: If number is not a non-negative integer.

    Example:
        >>> is_strong_number(145)
        True
        >>> is_strong_number(146)
        False
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 0:
        raise InvalidInputError("Number must be non-negative")
    if input_number == 0:
        return False  # 0! = 1 != 0
    digits = [int(digit) for digit in str(input_number)]
    total = sum(math.factorial(digit) for digit in digits)
    return total == input_number


# Functions for divisors and multiples
def generate_divisor_list(input_number: int, positive_only: bool = True) -> list:
    """
    Generate a list of divisors of a number.

    Parameters:
        - input_number (int): The number to generate the list of divisors.
        - positive_only (bool): If True, only positive divisors are returned.

    Returns:
        - list: A list of divisors of the number.

    Raises:
        - InvalidInputError: If number is not an integer or is zero.

    Example:
        >>> generate_divisor_list(6)
        [1, 2, 3, 6]
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number == 0:
        raise InvalidInputError("Number cannot be zero")
    abs_number = abs(input_number)
    divisors = [i for i in range(1, abs_number + 1) if abs_number % i == 0]
    if not positive_only:
        divisors += [-i for i in divisors]
    return sorted(divisors)


def generate_multiple_list(
    base_number: int, limit: int, positive_only: bool = True
) -> list:
    """
    Generate a list of multiples of a number up to limit times.

    Parameters:
        - base_number (int): The number to generate multiples.
        - limit (int): The limit for the number of multiples.
        - positive_only (bool): If True, only positive multiples are returned.

    Returns:
        - list: A list of multiples of the number.

    Raises:
        - InvalidInputError: If inputs are not integers or number is zero or limit < 1.

    Example:
        >>> generate_multiple_list(3, 5)
        [3, 6, 9, 12, 15]
    """
    if not (isinstance(base_number, int) and isinstance(limit, int)):
        raise InvalidInputError("Inputs must be integers")
    if base_number == 0:
        raise InvalidInputError("Number cannot be zero")
    if limit < 1:
        raise InvalidInputError("Limit must be positive")
    if positive_only:
        return [base_number * i for i in range(1, limit + 1)]
    return sorted(
        [-base_number * i for i in range(1, limit + 1)]
        + [base_number * i for i in range(limit + 1)]
    )


def common_divisors(numbers: list) -> list:
    """
    Generate a list of common divisors of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - list: A list of common divisors.

    Raises:
        - InvalidInputError: If input is not a list or contains non-integers.
        - MathError: If list has fewer than 2 non-zero elements.

    Example:
        >>> common_divisors([12, 18])
        [1, 2, 3, 6]
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


def greatest_common_divisor(numbers: list) -> int:
    """
    Calculate the greatest common divisor of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - int: The greatest common divisor of the list.

    Raises:
        - InvalidInputError: If input is not a list or contains non-integers.
        - MathError: If list has fewer than 2 non-zero elements.

    Example:
        >>> greatest_common_divisor([12, 18])
        6
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


def least_common_multiple(numbers: list) -> int:
    """
    Calculate the least common multiple of a list of numbers.

    Parameters:
        - numbers (list): The list of numbers.

    Returns:
        - int: The least common multiple of the list.

    Raises:
        - InvalidInputError: If input is not a list or contains non-integers or zeros.
        - MathError: If list has fewer than 2 elements.

    Example:
        >>> least_common_multiple([4, 6])
        12
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
def is_twin_prime(input_number: int) -> bool:
    """
    Check if a number is a twin prime.

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is a twin prime, False otherwise.

    Raises:
        - InvalidInputError: If number is not an integer.

    Example:
        >>> is_twin_prime(5)
        True
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    return is_prime(input_number) and (
        is_prime(input_number - 2) or is_prime(input_number + 2)
    )


def generate_twin_prime_list(limit: int) -> list:
    """
    Generate a list of twin primes from 2 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of twin primes.

    Raises:
        - InvalidInputError: If limit is not an integer >= 2.

    Example:
        >>> generate_twin_prime_list(20)
        [3, 5, 7, 11, 13, 17, 19]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 2:
        raise InvalidInputError("Limit must be >= 2")
    return [i for i in range(2, limit + 1) if is_twin_prime(i)]


def is_abundant_number(input_number: int) -> bool:
    """
    Check if a number is an abundant number.

    Parameters:
        - input_number (int): The number to check.

    Returns:
        - bool: True if the number is abundant, False otherwise.

    Raises:
        - InvalidInputError: If number is not a positive integer.

    Example:
        >>> is_abundant_number(12)
        True
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number < 1:
        raise InvalidInputError("Number must be positive")
    return sum_of_divisors(input_number) > input_number


def generate_abundant_number_list(limit: int) -> list:
    """
    Generate a list of abundant numbers from 1 to limit.

    Parameters:
        - limit (int): The upper limit of the list.

    Returns:
        - list: A list of abundant numbers.

    Raises:
        - InvalidInputError: If limit is not a positive integer.

    Example:
        >>> generate_abundant_number_list(20)
        [12, 18, 20]
    """
    if not isinstance(limit, int):
        raise InvalidInputError("Limit must be an integer")
    if limit < 1:
        raise InvalidInputError("Limit must be positive")
    return [i for i in range(1, limit + 1) if is_abundant_number(i)]


def prime_factors(input_number: int) -> list:
    """
    Factorize a number into a list of prime factors.

    Parameters:
        - input_number (int): The number to factorize.

    Returns:
        - list: A list of prime factors.

    Raises:
        - InvalidInputError: If number is not a positive integer > 1.

    Example:
        >>> prime_factors(12)
        [2, 2, 3]
    """
    if not isinstance(input_number, int):
        raise InvalidInputError("Input must be an integer")
    if input_number <= 1:
        raise InvalidInputError("Number must be greater than 1")
    factors = []
    divisor = 2
    while input_number > 1:
        while input_number % divisor == 0:
            factors.append(divisor)
            input_number //= divisor
        divisor += 1
    return factors


def greatest_common_prime_divisor(number1: int, number2: int) -> int:
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

    Example:
        >>> greatest_common_prime_divisor(12, 18)
        3
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


# Functions for list and string processing
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


# Caesar cipher
def caesar_cipher_to_numbers(text: str, shift: int) -> list:
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

    Example:
        >>> caesar_cipher_to_numbers("ABC", 3)
        [3, 4, 5]
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


def caesar_cipher_from_numbers(numbers: list, shift: int) -> str:
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

    Example:
        >>> caesar_cipher_from_numbers([3, 4, 5], 3)
        'ABC'
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
def calculate_electricity_bill_Vietnamese(
    old_reading: float, new_reading: float
) -> str:
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
        >>> calculate_electricity_bill_Vietnamese(100, 150)
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
    return f"- Electricity consumed this month: {kwh} Kwh\n- Electricity bill this month: {total} VND"


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
    if digit_count == 0 or target_sum == 0:
        return "0" * digit_count if digit_count > 0 else "0"
    result = []
    remaining_sum = target_sum
    for _ in range(digit_count):
        digit = min(9, remaining_sum)
        result.append(str(digit))
        remaining_sum -= digit
    return "".join(result[::-1])  # Reverse to get the largest number


# Sequence generation rules
def generate_sequence_rule_1(count: int) -> list:
    """
    Generate a sequence of positive integers according to the rule:
        - 1 number is divisible by 1,
        - 2 numbers are divisible by 2,
        - 3 numbers are divisible by 3,
        - and so on, the numbers increase until the number of numbers is `count`

    Parameters:
        - count (int): The number of elements to generate.

    Returns:
        - list: A list of integers in the sequence.

    Raises:
        - InvalidInputError: If count is not a positive integer.

    Example:
        >>> generate_sequence_rule_1(10)
        [1, 4, 6, 9, 12, 15, 16, 20, 24, 28]
    """
    if not isinstance(count, int):
        raise InvalidInputError("Count must be an integer")
    if count <= 1:
        raise InvalidInputError("Count must be greater than 1")

    def helper(k: int) -> int:
        if k == 1:
            return 1
        number_to_find = 1
        position = 0
        for i in range(1, 10000):  # Increase range for larger counts
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

    return [helper(i) for i in range(1, count + 1)]


def generate_sequence_rule_2(base: int, count: int) -> list:
    """
    Generate a list of multiples of base with count elements.

    Parameters:
        - base (int): The number to generate multiples.
        - count (int): The number of elements.

    Returns:
        - list: A list of multiples of base.

    Raises:
        - InvalidInputError: If inputs are not integers or count is negative.

    Example:
        >>> generate_sequence_rule_2(2, 5)
        [0, 2, 4, 6, 8]
    """
    if not (isinstance(base, int) and isinstance(count, int)):
        raise InvalidInputError("Inputs must be integers")
    if count < 0:
        raise InvalidInputError("Count must be non-negative")
    return [base * i for i in range(count)]


def generate_sequence_rule_3(count: int, base: int) -> list:
    """
    Generate a list of powers of base from 0 to count-1.

    Parameters:
        - count (int): The number of elements.
        - base (int): The base number.

    Returns:
        - list: A list of powers of base.

    Raises:
        - InvalidInputError: If inputs are not integers or count is negative.

    Example:
        >>> generate_sequence_rule_3(5, 2)
        [1, 2, 4, 8, 16]
    """
    if not (isinstance(count, int) and isinstance(base, int)):
        raise InvalidInputError("Inputs must be integers")
    if count < 0:
        raise InvalidInputError("Count must be non-negative")
    return [base**i for i in range(count)]


# Count inversions
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


def main():
    parser = argparse.ArgumentParser(
        description="The pchjlib library is a versatile toolkit for mathematical and string operations😺"
    )
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.5.3")
    subparsers = parser.add_subparsers(dest="category", help="Function categories")

    # 1. Primes and Emirps
    primes_parser = subparsers.add_parser(
        "primes_and_emirps", help="Functions for prime and emirp numbers"
    )
    primes_group = primes_parser.add_mutually_exclusive_group(required=True)
    primes_group.add_argument("--is_prime", type=int, help="Check if a number is prime")
    primes_group.add_argument(
        "--generate_prime_list",
        type=int,
        help="Generate a list of primes up to the limit",
    )
    primes_group.add_argument(
        "--is_emirp", type=int, help="Check if a number is an emirp"
    )
    primes_group.add_argument(
        "--generate_emirp_list",
        type=int,
        help="Generate a list of emirps up to the limit",
    )

    # 2. Twin Primes and Abundant Numbers
    twin_abundant_parser = subparsers.add_parser(
        "twin_primes_and_abundant",
        help="Functions for twin primes and abundant numbers",
    )
    twin_abundant_group = twin_abundant_parser.add_mutually_exclusive_group(
        required=True
    )
    twin_abundant_group.add_argument(
        "--is_twin_prime", type=int, help="Check if a number is a twin prime"
    )
    twin_abundant_group.add_argument(
        "--generate_twin_prime_list",
        type=int,
        help="Generate a list of twin primes up to the limit",
    )
    twin_abundant_group.add_argument(
        "--is_abundant", type=int, help="Check if a number is an abundant number"
    )
    twin_abundant_group.add_argument(
        "--generate_abundant_list",
        type=int,
        help="Generate a list of abundant numbers up to the limit",
    )

    # 3. Fibonacci
    fib_parser = subparsers.add_parser(
        "fibonacci", help="Functions for Fibonacci sequence"
    )
    fib_group = fib_parser.add_mutually_exclusive_group(required=True)
    fib_group.add_argument(
        "--at_index", type=int, help="Calculate the Fibonacci number at the given index"
    )
    fib_group.add_argument(
        "--generate_list",
        type=int,
        help="Generate a list of the first count Fibonacci numbers",
    )

    # 4. Special Numbers 1 (Perfect, Narcissistic, Amicable, Happy)
    special1_parser = subparsers.add_parser(
        "special_numbers_1",
        help="Functions for perfect, narcissistic, amicable, and happy numbers",
    )
    special1_group = special1_parser.add_mutually_exclusive_group(required=True)
    special1_group.add_argument(
        "--is_perfect", type=int, help="Check if a number is a perfect number"
    )
    special1_group.add_argument(
        "--generate_perfect_list",
        type=int,
        help="Generate a list of perfect numbers up to the limit",
    )
    special1_group.add_argument(
        "--is_narcissistic", type=int, help="Check if a number is a narcissistic number"
    )
    special1_group.add_argument(
        "--generate_narcissistic_list",
        type=int,
        help="Generate a list of narcissistic numbers up to the limit",
    )
    special1_group.add_argument(
        "--are_amicable",
        nargs=2,
        type=int,
        help="Check if two numbers are amicable numbers",
    )
    special1_group.add_argument(
        "--is_happy", type=int, help="Check if a number is a happy number"
    )
    special1_group.add_argument(
        "--generate_happy_list",
        type=int,
        help="Generate a list of happy numbers up to the limit",
    )

    # 5. Special Numbers 2 (Square, Strong, Friendly)
    special2_parser = subparsers.add_parser(
        "special_numbers_2", help="Functions for square, strong, and friendly numbers"
    )
    special2_group = special2_parser.add_mutually_exclusive_group(required=True)
    special2_group.add_argument(
        "--is_square", type=int, help="Check if a number is a square number"
    )
    special2_group.add_argument(
        "--generate_square_list",
        type=int,
        help="Generate a list of square numbers up to the limit",
    )
    special2_group.add_argument(
        "--is_strong", type=int, help="Check if a number is a strong number"
    )
    special2_group.add_argument(
        "--are_friendly",
        nargs=2,
        type=int,
        help="Check if two numbers are friendly numbers",
    )

    # 6. Divisors and Multiples
    divisors_parser = subparsers.add_parser(
        "divisors_and_multiples", help="Functions for divisors and multiples"
    )
    divisors_group = divisors_parser.add_mutually_exclusive_group(required=True)
    divisors_group.add_argument(
        "--generate_divisor_list",
        type=int,
        help="Generate a list of divisors of a number",
    )
    divisors_group.add_argument(
        "--generate_multiple_list",
        nargs=2,
        type=int,
        help="Generate a list of multiples of a number up to the limit",
    )
    divisors_group.add_argument(
        "--common_divisors",
        nargs="+",
        type=int,
        help="Find common divisors of a list of numbers",
    )
    divisors_group.add_argument(
        "--gcd",
        nargs="+",
        type=int,
        help="Calculate the greatest common divisor of a list of numbers",
    )
    divisors_group.add_argument(
        "--lcm",
        nargs="+",
        type=int,
        help="Calculate the least common multiple of a list of numbers",
    )

    # 7. Prime Factorization
    factorization_parser = subparsers.add_parser(
        "prime_factorization", help="Functions for prime factorization"
    )
    factorization_group = factorization_parser.add_mutually_exclusive_group(
        required=True
    )
    factorization_group.add_argument(
        "--prime_factors", type=int, help="Factorize a number into prime factors"
    )
    factorization_group.add_argument(
        "--greatest_common_prime_divisor",
        nargs=2,
        type=int,
        help="Find the greatest common prime divisor of two numbers",
    )

    # 8. String Processing (Renumbered from 9)
    string_parser = subparsers.add_parser(
        "string_processing", help="Functions for list and string processing"
    )
    string_group = string_parser.add_mutually_exclusive_group(required=True)
    string_group.add_argument(
        "--remove_duplicates", nargs="+", help="Remove duplicates from a list"
    )
    string_group.add_argument(
        "--extract_digits", type=str, help="Extract digits from a string"
    )
    string_group.add_argument(
        "--extract_numbers", type=str, help="Extract numbers from a string"
    )
    string_group.add_argument(
        "--extract_characters",
        type=str,
        help="Extract non-digit characters from a string",
    )
    string_group.add_argument(
        "--compress",
        nargs=2,
        help="Compress a string: string and compression type (1 or 2)",
    )
    string_group.add_argument(
        "--compress_without_numbers",
        type=str,
        help="Compress a string by removing duplicates",
    )
    string_group.add_argument("--decompress", type=str, help="Decompress a string")
    string_group.add_argument(
        "--unique_characters", type=str, help="Create a string with unique characters"
    )

    # 9. Caesar Cipher (Renumbered from 10)
    caesar_parser = subparsers.add_parser(
        "caesar_cipher", help="Functions for Caesar cipher"
    )
    caesar_group = caesar_parser.add_mutually_exclusive_group(required=True)
    caesar_group.add_argument(
        "--to_numbers",
        nargs=2,
        help="Convert string to Caesar numbers: string and shift",
    )
    caesar_group.add_argument(
        "--from_numbers",
        nargs="+",
        help="Decode Caesar numbers to string: shift followed by numbers",
    )

    # 10. Special Calculations (Renumbered from 11)
    calc_parser = subparsers.add_parser(
        "special_calculations", help="Functions for special calculations"
    )
    calc_group = calc_parser.add_mutually_exclusive_group(required=True)
    calc_group.add_argument(
        "--electricity_bill",
        nargs=2,
        type=float,
        help="Calculate electricity bill: old and new readings",
    )
    calc_group.add_argument(
        "--largest_number",
        nargs=2,
        type=int,
        help="Find the largest number with given digit count and sum",
    )

    # 11. Sequence Generation (Renumbered from 12)
    sequence_parser = subparsers.add_parser(
        "sequence_generation", help="Functions to generate sequences"
    )
    sequence_group = sequence_parser.add_mutually_exclusive_group(required=True)
    sequence_group.add_argument(
        "--rule1", type=int, help="Generate sequence by rule 1 with number of elements"
    )
    sequence_group.add_argument(
        "--rule2",
        nargs=2,
        type=int,
        help="Generate sequence by rule 2: base and number of elements",
    )
    sequence_group.add_argument(
        "--rule3",
        nargs=2,
        type=int,
        help="Generate sequence by rule 3: number of elements and base",
    )

    # 12. Inversion Counting (Renumbered from 13)
    inversion_parser = subparsers.add_parser(
        "inversion_counting", help="Function to count inversions"
    )
    inversion_group = inversion_parser.add_mutually_exclusive_group(required=True)
    inversion_group.add_argument(
        "--count", nargs="+", type=int, help="Count inversions in a list"
    )

    # Parse arguments
    args = parser.parse_args()

    # Handle logic based on category
    if args.category == "primes_and_emirps":
        if args.is_prime is not None:
            try:
                result = is_prime(args.is_prime)
                print(
                    f"{args.is_prime} {'is a prime number' if result else 'is not a prime number'}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.generate_prime_list is not None:
            try:
                result = generate_prime_list(args.generate_prime_list)
                print(
                    f"List of prime numbers up to {args.generate_prime_list}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.is_emirp is not None:
            try:
                result = is_emirp(args.is_emirp)
                print(
                    f"{args.is_emirp} {'is an emirp number' if result else 'is not an emirp number'}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.generate_emirp_list is not None:
            try:
                result = generate_emirp_list(args.generate_emirp_list)
                print(
                    f"List of emirp numbers up to {args.generate_emirp_list}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")

    elif args.category == "twin_primes_and_abundant":
        if args.is_twin_prime is not None:
            try:
                result = is_twin_prime(args.is_twin_prime)
                print(
                    f"{args.is_twin_prime} {'is a twin prime' if result else 'is not a twin prime'}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.generate_twin_prime_list is not None:
            try:
                result = generate_twin_prime_list(args.generate_twin_prime_list)
                print(
                    f"List of twin primes up to {args.generate_twin_prime_list}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.is_abundant is not None:
            try:
                result = is_abundant_number(args.is_abundant)
                print(
                    f"{args.is_abundant} {'is an abundant number' if result else 'is not an abundant number'}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.generate_abundant_list is not None:
            try:
                result = generate_abundant_number_list(args.generate_abundant_list)
                print(
                    f"List of abundant numbers up to {args.generate_abundant_list}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")

    elif args.category == "fibonacci":
        if args.at_index is not None:
            try:
                result = fibonacci_at_index(args.at_index)
                print(f"Fibonacci number at index {args.at_index}: {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif args.generate_list is not None:
            try:
                result = generate_fibonacci_list(args.generate_list)
                print(
                    f"List of the first {args.generate_list} Fibonacci numbers: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")

    elif args.category == "special_numbers_1":
        if args.is_perfect is not None:
            try:
                result = is_perfect_number(args.is_perfect)
                print(
                    f"{args.is_perfect} {'is a perfect number' if result else 'is not a perfect number'}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.generate_perfect_list is not None:
            try:
                result = generate_perfect_number_list(args.generate_perfect_list)
                print(
                    f"List of perfect numbers up to {args.generate_perfect_list}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.is_narcissistic is not None:
            try:
                result = is_narcissistic_number(args.is_narcissistic)
                print(
                    f"{args.is_narcissistic} {'is a narcissistic number' if result else 'is not a narcissistic number'}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.generate_narcissistic_list is not None:
            try:
                result = generate_narcissistic_number_list(
                    args.generate_narcissistic_list
                )
                print(
                    f"List of narcissistic numbers up to {args.generate_narcissistic_list}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.are_amicable is not None:
            try:
                result = are_amicable_numbers(
                    args.are_amicable[0], args.are_amicable[1]
                )
                print(
                    f"{args.are_amicable[0]} and {args.are_amicable[1]} {'are amicable numbers' if result else 'are not amicable numbers'}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.is_happy is not None:
            try:
                result = is_happy_number(args.is_happy)
                print(
                    f"{args.is_happy} {'is a happy number' if result else 'is not a happy number'}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.generate_happy_list is not None:
            try:
                result = generate_happy_number_list(args.generate_happy_list)
                print(
                    f"List of happy numbers up to {args.generate_happy_list}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")

    elif args.category == "special_numbers_2":
        if args.is_square is not None:
            try:
                result = is_square_number(args.is_square)
                print(
                    f"{args.is_square} {'is a square number' if result else 'is not a square number'}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.generate_square_list is not None:
            try:
                result = generate_square_number_list(args.generate_square_list)
                print(
                    f"List of square numbers up to {args.generate_square_list}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.is_strong is not None:
            try:
                result = is_strong_number(args.is_strong)
                print(
                    f"{args.is_strong} {'is a strong number' if result else 'is not a strong number'}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.are_friendly is not None:
            try:
                result = are_friendly_numbers(
                    args.are_friendly[0], args.are_friendly[1]
                )
                print(
                    f"{args.are_friendly[0]} and {args.are_friendly[1]} {'are friendly numbers' if result else 'are not friendly numbers'}"
                )
            except Exception as e:
                print(f"Error: {e}")

    elif args.category == "divisors_and_multiples":
        if args.generate_divisor_list is not None:
            try:
                result = generate_divisor_list(args.generate_divisor_list)
                print(f"List of divisors of {args.generate_divisor_list}: {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif args.generate_multiple_list is not None:
            try:
                result = generate_multiple_list(
                    args.generate_multiple_list[0], args.generate_multiple_list[1]
                )
                print(
                    f"List of multiples of {args.generate_multiple_list[0]} up to {args.generate_multiple_list[1]}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.common_divisors is not None:
            try:
                result = common_divisors(args.common_divisors)
                print(f"Common divisors of {args.common_divisors}: {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif args.gcd is not None:
            try:
                result = greatest_common_divisor(args.gcd)
                print(f"Greatest common divisor of {args.gcd}: {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif args.lcm is not None:
            try:
                result = least_common_multiple(args.lcm)
                print(f"Least common multiple of {args.lcm}: {result}")
            except Exception as e:
                print(f"Error: {e}")

    elif args.category == "prime_factorization":
        if args.prime_factors is not None:
            try:
                result = prime_factors(args.prime_factors)
                print(f"Prime factors of {args.prime_factors}: {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif args.greatest_common_prime_divisor is not None:
            try:
                result = greatest_common_prime_divisor(
                    args.greatest_common_prime_divisor[0],
                    args.greatest_common_prime_divisor[1],
                )
                print(
                    f"Greatest common prime divisor of {args.greatest_common_prime_divisor[0]} and {args.greatest_common_prime_divisor[1]}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")

    elif args.category == "string_processing":
        if args.remove_duplicates is not None:
            try:
                result = remove_duplicates(args.remove_duplicates)
                print(f"List after removing duplicates: {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif args.extract_digits is not None:
            try:
                result = extract_digits_from_string(args.extract_digits)
                print(f"Digits extracted from '{args.extract_digits}': {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif args.extract_numbers is not None:
            try:
                result = extract_numbers_from_string(args.extract_numbers)
                print(f"Numbers extracted from '{args.extract_numbers}': {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif args.extract_characters is not None:
            try:
                result = extract_characters(args.extract_characters)
                print(
                    f"Non-digit characters from '{args.extract_characters}': {result}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.compress is not None:
            try:
                result = compress_string(args.compress[0], int(args.compress[1]))
                print(
                    f"Compressed string from '{args.compress[0]}' (type {args.compress[1]}): {result}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.compress_without_numbers is not None:
            try:
                result = compress_string_without_numbers(args.compress_without_numbers)
                print(
                    f"Compressed string from '{args.compress_without_numbers}': {result}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.decompress is not None:
            try:
                result = decompress_string(args.decompress)
                print(f"Decompressed string from '{args.decompress}': {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif args.unique_characters is not None:
            try:
                result = unique_characters_string(args.unique_characters)
                print(
                    f"String with unique characters from '{args.unique_characters}': {result}"
                )
            except Exception as e:
                print(f"Error: {e}")

    elif args.category == "caesar_cipher":
        if args.to_numbers is not None:
            try:
                result = caesar_cipher_to_numbers(
                    args.to_numbers[0], int(args.to_numbers[1])
                )
                print(
                    f"Caesar numbers from '{args.to_numbers[0]}' with shift {args.to_numbers[1]}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.from_numbers is not None:
            try:
                shift = int(args.from_numbers[0])
                numbers = list(map(int, args.from_numbers[1:]))
                result = caesar_cipher_from_numbers(numbers, shift)
                print(f"String from {numbers} with shift {shift}: {result}")
            except Exception as e:
                print(f"Error: {e}")

    elif args.category == "special_calculations":
        if args.electricity_bill is not None:
            try:
                result = calculate_electricity_bill_Vietnamese(
                    args.electricity_bill[0], args.electricity_bill[1]
                )
                print(result)
            except Exception as e:
                print(f"Error: {e}")
        elif args.largest_number is not None:
            try:
                result = largest_number_with_digit_sum(
                    args.largest_number[0], args.largest_number[1]
                )
                print(
                    f"Largest number with {args.largest_number[0]} digits and sum {args.largest_number[1]}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")

    elif args.category == "sequence_generation":
        if args.rule1 is not None:
            try:
                result = generate_sequence_rule_1(args.rule1)
                print(f"Sequence by rule 1 with {args.rule1} elements: {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif args.rule2 is not None:
            try:
                result = generate_sequence_rule_2(args.rule2[0], args.rule2[1])
                print(
                    f"Sequence by rule 2 with base {args.rule2[0]} and {args.rule2[1]} elements: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")
        elif args.rule3 is not None:
            try:
                result = generate_sequence_rule_3(args.rule3[0], args.rule3[1])
                print(
                    f"Sequence by rule 3 with {args.rule3[0]} elements and base {args.rule3[1]}: {result}"
                )
            except Exception as e:
                print(f"Error: {e}")

    elif args.category == "inversion_counting":
        if args.count is not None:
            try:
                result = count_inversions(args.count)
                print(f"Number of inversions in {args.count}: {result}")
            except Exception as e:
                print(f"Error: {e}")

    else:
        print("Welcome to pchjlib!")
        print("Use -h or --help for more information.")


if __name__ == "__main__":
    main()
