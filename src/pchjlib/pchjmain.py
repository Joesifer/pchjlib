#  src/pchjlib/pchjmain.py


"""
PCHJLIB😺
================================================================================================

>>> The module that contains the library's CLI entry point.
>>> For detailed instructions, please see the `README.md` file.

================================================================================================
"""

import argparse
import traceback  # Added for detailed error handling

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


def main():
    parser = argparse.ArgumentParser(
        description="The pchjlib library is a toolkit for mathematical and string operations😺"
    )
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.7.1")
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

    # 8. String Processing
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

    # 9. Caesar Cipher
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

    # 10. Special Calculations
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

    # 11. Sequence Generation
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

    # 12. Inversion Counting
    inversion_parser = subparsers.add_parser(
        "inversion_counting", help="Function to count inversions"
    )
    inversion_group = inversion_parser.add_mutually_exclusive_group(required=True)
    inversion_group.add_argument(
        "--count", nargs="+", type=int, help="Count inversions in a list"
    )

    args = parser.parse_args()

    if args.category == "primes_and_emirps":
        if args.is_prime is not None:
            try:
                result = is_prime(args.is_prime)
                print(
                    f"{args.is_prime} {'is a prime number' if result else 'is not a prime number'}"
                )
            except Exception as e:
                print(
                    f"Error in primes_and_emirps --is_prime: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.generate_prime_list is not None:
            try:
                result = generate_prime_list(args.generate_prime_list)
                print(
                    f"List of prime numbers up to {args.generate_prime_list}: {result}"
                )
            except Exception as e:
                print(
                    f"Error in primes_and_emirps --generate_prime_list: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.is_emirp is not None:
            try:
                result = is_emirp(args.is_emirp)
                print(
                    f"{args.is_emirp} {'is an emirp number' if result else 'is not an emirp number'}"
                )
            except Exception as e:
                print(
                    f"Error in primes_and_emirps --is_emirp: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.generate_emirp_list is not None:
            try:
                result = generate_emirp_list(args.generate_emirp_list)
                print(
                    f"List of emirp numbers up to {args.generate_emirp_list}: {result}"
                )
            except Exception as e:
                print(
                    f"Error in primes_and_emirps --generate_emirp_list: {str(e)}\nDetails: {traceback.format_exc()}"
                )

    elif args.category == "twin_primes_and_abundant":
        if args.is_twin_prime is not None:
            try:
                result = is_twin_prime(args.is_twin_prime)
                print(
                    f"{args.is_twin_prime} {'is a twin prime' if result else 'is not a twin prime'}"
                )
            except Exception as e:
                print(
                    f"Error in twin_primes_and_abundant --is_twin_prime: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.generate_twin_prime_list is not None:
            try:
                result = generate_twin_prime_list(args.generate_twin_prime_list)
                print(
                    f"List of twin primes up to {args.generate_twin_prime_list}: {result}"
                )
            except Exception as e:
                print(
                    f"Error in twin_primes_and_abundant --generate_twin_prime_list: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.is_abundant is not None:
            try:
                result = is_abundant_number(args.is_abundant)
                print(
                    f"{args.is_abundant} {'is an abundant number' if result else 'is not an abundant number'}"
                )
            except Exception as e:
                print(
                    f"Error in twin_primes_and_abundant --is_abundant: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.generate_abundant_list is not None:
            try:
                result = generate_abundant_number_list(args.generate_abundant_list)
                print(
                    f"List of abundant numbers up to {args.generate_abundant_list}: {result}"
                )
            except Exception as e:
                print(
                    f"Error in twin_primes_and_abundant --generate_abundant_list: {str(e)}\nDetails: {traceback.format_exc()}"
                )

    elif args.category == "fibonacci":
        if args.at_index is not None:
            try:
                result = fibonacci_at_index(args.at_index)
                print(f"Fibonacci number at index {args.at_index}: {result}")
            except Exception as e:
                print(
                    f"Error in fibonacci --at_index: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.generate_list is not None:
            try:
                result = generate_fibonacci_list(args.generate_list)
                print(
                    f"List of the first {args.generate_list} Fibonacci numbers: {result}"
                )
            except Exception as e:
                print(
                    f"Error in fibonacci --generate_list: {str(e)}\nDetails: {traceback.format_exc()}"
                )

    elif args.category == "special_numbers_1":
        if args.is_perfect is not None:
            try:
                result = is_perfect_number(args.is_perfect)
                print(
                    f"{args.is_perfect} {'is a perfect number' if result else 'is not a perfect number'}"
                )
            except Exception as e:
                print(
                    f"Error in special_numbers_1 --is_perfect: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.generate_perfect_list is not None:
            try:
                result = generate_perfect_number_list(args.generate_perfect_list)
                print(
                    f"List of perfect numbers up to {args.generate_perfect_list}: {result}"
                )
            except Exception as e:
                print(
                    f"Error in special_numbers_1 --generate_perfect_list: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.is_narcissistic is not None:
            try:
                result = is_narcissistic_number(args.is_narcissistic)
                print(
                    f"{args.is_narcissistic} {'is a narcissistic number' if result else 'is not a narcissistic number'}"
                )
            except Exception as e:
                print(
                    f"Error in special_numbers_1 --is_narcissistic: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.generate_narcissistic_list is not None:
            try:
                result = generate_narcissistic_number_list(
                    args.generate_narcissistic_list
                )
                print(
                    f"List of narcissistic numbers up to {args.generate_narcissistic_list}: {result}"
                )
            except Exception as e:
                print(
                    f"Error in special_numbers_1 --generate_narcissistic_list: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.are_amicable is not None:
            try:
                result = are_amicable_numbers(
                    args.are_amicable[0], args.are_amicable[1]
                )
                print(
                    f"{args.are_amicable[0]} and {args.are_amicable[1]} {'are amicable numbers' if result else 'are not amicable numbers'}"
                )
            except Exception as e:
                print(
                    f"Error in special_numbers_1 --are_amicable: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.is_happy is not None:
            try:
                result = is_happy_number(args.is_happy)
                print(
                    f"{args.is_happy} {'is a happy number' if result else 'is not a happy number'}"
                )
            except Exception as e:
                print(
                    f"Error in special_numbers_1 --is_happy: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.generate_happy_list is not None:
            try:
                result = generate_happy_number_list(args.generate_happy_list)
                print(
                    f"List of happy numbers up to {args.generate_happy_list}: {result}"
                )
            except Exception as e:
                print(
                    f"Error in special_numbers_1 --generate_happy_list: {str(e)}\nDetails: {traceback.format_exc()}"
                )

    elif args.category == "special_numbers_2":
        if args.is_square is not None:
            try:
                result = is_square_number(args.is_square)
                print(
                    f"{args.is_square} {'is a square number' if result else 'is not a square number'}"
                )
            except Exception as e:
                print(
                    f"Error in special_numbers_2 --is_square: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.generate_square_list is not None:
            try:
                result = generate_square_number_list(args.generate_square_list)
                print(
                    f"List of square numbers up to {args.generate_square_list}: {result}"
                )
            except Exception as e:
                print(
                    f"Error in special_numbers_2 --generate_square_list: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.is_strong is not None:
            try:
                result = is_strong_number(args.is_strong)
                print(
                    f"{args.is_strong} {'is a strong number' if result else 'is not a strong number'}"
                )
            except Exception as e:
                print(
                    f"Error in special_numbers_2 --is_strong: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.are_friendly is not None:
            try:
                result = are_friendly_numbers(
                    args.are_friendly[0], args.are_friendly[1]
                )
                print(
                    f"{args.are_friendly[0]} and {args.are_friendly[1]} {'are friendly numbers' if result else 'are not friendly numbers'}"
                )
            except Exception as e:
                print(
                    f"Error in special_numbers_2 --are_friendly: {str(e)}\nDetails: {traceback.format_exc()}"
                )

    elif args.category == "divisors_and_multiples":
        if args.generate_divisor_list is not None:
            try:
                result = generate_divisor_list(args.generate_divisor_list)
                print(f"List of divisors of {args.generate_divisor_list}: {result}")
            except Exception as e:
                print(
                    f"Error in divisors_and_multiples --generate_divisor_list: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.generate_multiple_list is not None:
            try:
                result = generate_multiple_list(
                    args.generate_multiple_list[0], args.generate_multiple_list[1]
                )
                print(
                    f"List of multiples of {args.generate_multiple_list[0]} up to {args.generate_multiple_list[1]} times: {result}"
                )
            except Exception as e:
                print(
                    f"Error in divisors_and_multiples --generate_multiple_list: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.common_divisors is not None:
            try:
                result = common_divisors(args.common_divisors)
                print(f"Common divisors of {args.common_divisors}: {result}")
            except Exception as e:
                print(
                    f"Error in divisors_and_multiples --common_divisors: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.gcd is not None:
            try:
                result = greatest_common_divisor(args.gcd)
                print(f"Greatest common divisor of {args.gcd}: {result}")
            except Exception as e:
                print(
                    f"Error in divisors_and_multiples --gcd: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.lcm is not None:
            try:
                result = least_common_multiple(args.lcm)
                print(f"Least common multiple of {args.lcm}: {result}")
            except Exception as e:
                print(
                    f"Error in divisors_and_multiples --lcm: {str(e)}\nDetails: {traceback.format_exc()}"
                )

    elif args.category == "prime_factorization":
        if args.prime_factors is not None:
            try:
                result = prime_factors(args.prime_factors)
                print(f"Prime factors of {args.prime_factors}: {result}")
            except Exception as e:
                print(
                    f"Error in prime_factorization --prime_factors: {str(e)}\nDetails: {traceback.format_exc()}"
                )
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
                print(
                    f"Error in prime_factorization --greatest_common_prime_divisor: {str(e)}\nDetails: {traceback.format_exc()}"
                )

    elif args.category == "string_processing":
        if args.remove_duplicates is not None:
            try:
                result = remove_duplicates(args.remove_duplicates)
                print(f"List after removing duplicates: {result}")
            except Exception as e:
                print(
                    f"Error in string_processing --remove_duplicates: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.extract_digits is not None:
            try:
                result = extract_digits_from_string(args.extract_digits)
                print(f"Digits extracted from '{args.extract_digits}': {result}")
            except Exception as e:
                print(
                    f"Error in string_processing --extract_digits: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.extract_numbers is not None:
            try:
                result = extract_numbers_from_string(args.extract_numbers)
                print(f"Numbers extracted from '{args.extract_numbers}': {result}")
            except Exception as e:
                print(
                    f"Error in string_processing --extract_numbers: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.extract_characters is not None:
            try:
                result = extract_characters(args.extract_characters)
                print(
                    f"Non-digit characters from '{args.extract_characters}': {result}"
                )
            except Exception as e:
                print(
                    f"Error in string_processing --extract_characters: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.compress is not None:
            try:
                result = compress_string(args.compress[0], int(args.compress[1]))
                print(
                    f"Compressed string from '{args.compress[0]}' (type {args.compress[1]}): {result}"
                )
            except Exception as e:
                print(
                    f"Error in string_processing --compress: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.compress_without_numbers is not None:
            try:
                result = compress_string_without_numbers(args.compress_without_numbers)
                print(
                    f"Compressed string from '{args.compress_without_numbers}': {result}"
                )
            except Exception as e:
                print(
                    f"Error in string_processing --compress_without_numbers: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.decompress is not None:
            try:
                result = decompress_string(args.decompress)
                print(f"Decompressed string from '{args.decompress}': {result}")
            except Exception as e:
                print(
                    f"Error in string_processing --decompress: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.unique_characters is not None:
            try:
                result = unique_characters_string(args.unique_characters)
                print(
                    f"String with unique characters from '{args.unique_characters}': {result}"
                )
            except Exception as e:
                print(
                    f"Error in string_processing --unique_characters: {str(e)}\nDetails: {traceback.format_exc()}"
                )

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
                print(
                    f"Error in caesar_cipher --to_numbers: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.from_numbers is not None:
            try:
                shift = int(args.from_numbers[0])
                numbers = list(map(int, args.from_numbers[1:]))
                result = caesar_cipher_from_numbers(numbers, shift)
                print(f"String from {numbers} with shift {shift}: {result}")
            except Exception as e:
                print(
                    f"Error in caesar_cipher --from_numbers: {str(e)}\nDetails: {traceback.format_exc()}"
                )

    elif args.category == "special_calculations":
        if args.electricity_bill is not None:
            try:
                result = calculate_electricity_bill_vietnam(
                    args.electricity_bill[0], args.electricity_bill[1]
                )
                print(result)
            except Exception as e:
                print(
                    f"Error in special_calculations --electricity_bill: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.largest_number is not None:
            try:
                result = largest_number_with_digit_sum(
                    args.largest_number[0], args.largest_number[1]
                )
                print(
                    f"Largest number with {args.largest_number[0]} digits and sum {args.largest_number[1]}: {result}"
                )
            except Exception as e:
                print(
                    f"Error in special_calculations --largest_number: {str(e)}\nDetails: {traceback.format_exc()}"
                )

    elif args.category == "sequence_generation":
        if args.rule1 is not None:
            try:
                result = generate_sequence_rule_1(args.rule1)
                print(f"Sequence by rule 1 with {args.rule1} elements: {result}")
            except Exception as e:
                print(
                    f"Error in sequence_generation --rule1: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.rule2 is not None:
            try:
                result = generate_sequence_rule_2(args.rule2[0], args.rule2[1])
                print(
                    f"Sequence by rule 2 with base {args.rule2[0]} and {args.rule2[1]} elements: {result}"
                )
            except Exception as e:
                print(
                    f"Error in sequence_generation --rule2: {str(e)}\nDetails: {traceback.format_exc()}"
                )
        elif args.rule3 is not None:
            try:
                result = generate_sequence_rule_3(args.rule3[0], args.rule3[1])
                print(
                    f"Sequence by rule 3 with {args.rule3[0]} elements and base {args.rule3[1]}: {result}"
                )
            except Exception as e:
                print(
                    f"Error in sequence_generation --rule3: {str(e)}\nDetails: {traceback.format_exc()}"
                )

    elif args.category == "inversion_counting":
        if args.count is not None:
            try:
                result = count_inversions(args.count)
                print(f"Number of inversions in {args.count}: {result}")
            except Exception as e:
                print(
                    f"Error in inversion_counting --count: {str(e)}\nDetails: {traceback.format_exc()}"
                )

    else:
        print("Welcome to pchjlib!")
        print("Use -h or --help for more information.")


if __name__ == "__main__":
    main()
