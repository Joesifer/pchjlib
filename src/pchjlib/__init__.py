# __init__.py

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
================================================================================================

Usage
------------------------------------------------------------------------------------------------
``` python

from pchjlib.primes import is_prime
result = is_prime(7)  # Check for prime numbers

```
- For detailed instructions, please refer to https://github.com/Joesifer/pchjlib/blob/main/README.md.

Dependencies
------------------------------------------------------------------------------------------------
- Built-in: `math`, `re`, `random`, `functools`, `argparse`.
- External: `gmpy2` (optional for big integer support).

Feedback and Support
------------------------------------------------------------------------------------------------
>>> Email: phanchanhung12055@gmail.com

THANK YOU!!!
================================================================================================
"""


from importlib.metadata import version
from pchjlib.pchjicon import main as pchj_icon
from pchjlib.pchjmain import main as pchj_main

# Explicit imports to avoid wildcard pollution
from pchjlib.primes import is_prime, generate_prime_list, is_emirp, generate_emirp_list
from pchjlib.twin_abundant import (
    is_twin_prime,
    generate_twin_prime_list,
    is_abundant_number,
    generate_abundant_number_list,
)
from pchjlib.fibonacci import fibonacci_at_index, generate_fibonacci_list
from pchjlib.special_numbers1 import (
    is_perfect_number,
    generate_perfect_number_list,
    is_narcissistic_number,
    generate_narcissistic_number_list,
    are_amicable_numbers,
    is_happy_number,
    generate_happy_number_list,
)
from pchjlib.special_numbers2 import (
    is_square_number,
    generate_square_number_list,
    is_strong_number,
    are_friendly_numbers,
)
from pchjlib.divisors_multiples import (
    sum_of_divisors,
    generate_divisor_list,
    generate_multiple_list,
    common_divisors,
    greatest_common_divisor,
    least_common_multiple,
)
from pchjlib.prime_factorization import prime_factors, greatest_common_prime_divisor
from pchjlib.string_processing import (
    remove_duplicates,
    extract_digits_from_string,
    extract_numbers_from_string,
    extract_characters,
    compress_string,
    compress_string_without_numbers,
    decompress_string,
    unique_characters_string,
)
from pchjlib.caesar_cipher import caesar_cipher_to_numbers, caesar_cipher_from_numbers
from pchjlib.special_calculations import (
    calculate_electricity_bill_vietnam,
    largest_number_with_digit_sum,
)
from pchjlib.sequence_generation import (
    generate_sequence_rule_1,
    generate_sequence_rule_2,
    generate_sequence_rule_3,
)
from pchjlib.inversion_counting import count_inversions

author = "Joesifer (phanchanhung12055@gmail.com)"
copyright = "Copyright (c) 2024 Joesifer"
version = version("pchjlib")
license = "MIT License"
release_date = "August 12, 2025"

__all__ = [
    "is_prime",
    "generate_prime_list",
    "is_emirp",
    "generate_emirp_list",
    "is_twin_prime",
    "generate_twin_prime_list",
    "is_abundant_number",
    "generate_abundant_number_list",
    "fibonacci_at_index",
    "generate_fibonacci_list",
    "is_perfect_number",
    "generate_perfect_number_list",
    "is_narcissistic_number",
    "generate_narcissistic_number_list",
    "are_amicable_numbers",
    "is_happy_number",
    "generate_happy_number_list",
    "is_square_number",
    "generate_square_number_list",
    "is_strong_number",
    "are_friendly_numbers",
    "sum_of_divisors",
    "generate_divisor_list",
    "generate_multiple_list",
    "common_divisors",
    "greatest_common_divisor",
    "least_common_multiple",
    "prime_factors",
    "greatest_common_prime_divisor",
    "remove_duplicates",
    "extract_digits_from_string",
    "extract_numbers_from_string",
    "extract_characters",
    "compress_string",
    "compress_string_without_numbers",
    "decompress_string",
    "unique_characters_string",
    "caesar_cipher_to_numbers",
    "caesar_cipher_from_numbers",
    "calculate_electricity_bill_vietnam",
    "largest_number_with_digit_sum",
    "generate_sequence_rule_1",
    "generate_sequence_rule_2",
    "generate_sequence_rule_3",
    "count_inversions",
    "pchj_main",
    "pchj_icon",
    "version",
    "author",
    "copyright",
    "license",
    "release_date",
]
