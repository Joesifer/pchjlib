# tests/test_pchjlib.py

import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
import unittest

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
    calculate_electricity_bill_Vietnamese,
    largest_number_with_digit_sum,
)
from pchjlib.sequence_generation import (
    generate_sequence_rule_1,
    generate_sequence_rule_2,
    generate_sequence_rule_3,
)
from pchjlib.inversion_counting import count_inversions


class TestPchjlib(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))

    def test_generate_prime_list(self):
        self.assertEqual(generate_prime_list(10), [2, 3, 5, 7])

    def test_is_emirp(self):
        self.assertTrue(is_emirp(13))
        self.assertFalse(is_emirp(4))

    def test_generate_emirp_list(self):
        self.assertEqual(generate_emirp_list(20), [13, 17])

    def test_is_twin_prime(self):
        self.assertTrue(is_twin_prime(5))
        self.assertFalse(is_twin_prime(9))

    def test_generate_twin_prime_list(self):
        self.assertEqual(generate_twin_prime_list(20), [3, 5, 7, 11, 13, 17, 19])

    def test_is_abundant_number(self):
        self.assertTrue(is_abundant_number(12))
        self.assertFalse(is_abundant_number(28))

    def test_generate_abundant_number_list(self):
        self.assertEqual(generate_abundant_number_list(20), [12, 18, 20])

    def test_fibonacci_at_index(self):
        self.assertEqual(fibonacci_at_index(5), 5)

    def test_generate_fibonacci_list(self):
        self.assertEqual(generate_fibonacci_list(5), [0, 1, 1, 2, 3])

    def test_is_perfect_number(self):
        self.assertTrue(is_perfect_number(6))
        self.assertFalse(is_perfect_number(12))

    def test_generate_perfect_number_list(self):
        self.assertEqual(generate_perfect_number_list(10), [6])

    def test_is_narcissistic_number(self):
        self.assertTrue(is_narcissistic_number(153))
        self.assertFalse(is_narcissistic_number(154))

    def test_generate_narcissistic_number_list(self):
        self.assertEqual(
            generate_narcissistic_number_list(10), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        )

    def test_are_amicable_numbers(self):
        self.assertTrue(are_amicable_numbers(220, 284))
        self.assertFalse(are_amicable_numbers(6, 6))

    def test_is_happy_number(self):
        self.assertTrue(is_happy_number(19))
        self.assertFalse(is_happy_number(2))

    def test_generate_happy_number_list(self):
        self.assertEqual(generate_happy_number_list(10), [1, 7, 10])

    def test_is_square_number(self):
        self.assertTrue(is_square_number(16))
        self.assertFalse(is_square_number(15))

    def test_generate_square_number_list(self):
        self.assertEqual(generate_square_number_list(10), [0, 1, 4, 9])

    def test_is_strong_number(self):
        self.assertTrue(is_strong_number(145))
        self.assertFalse(is_strong_number(146))

    def test_are_friendly_numbers(self):
        self.assertTrue(are_friendly_numbers(30, 140))
        self.assertFalse(are_friendly_numbers(220, 284))

    def test_generate_divisor_list(self):
        self.assertEqual(generate_divisor_list(6), [1, 2, 3, 6])

    def test_generate_multiple_list(self):
        self.assertEqual(generate_multiple_list(3, 5), [3, 6, 9, 12, 15])

    def test_common_divisors(self):
        self.assertEqual(common_divisors([12, 18]), [1, 2, 3, 6])

    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor([12, 18]), 6)

    def test_least_common_multiple(self):
        self.assertEqual(least_common_multiple([4, 6]), 12)

    def test_prime_factors(self):
        self.assertEqual(prime_factors(12), [2, 2, 3])

    def test_greatest_common_prime_divisor(self):
        self.assertEqual(greatest_common_prime_divisor(12, 18), 3)

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3]), [3, 2, 1])

    def test_extract_digits_from_string(self):
        self.assertEqual(extract_digits_from_string("abc123"), [1, 2, 3])

    def test_extract_numbers_from_string(self):
        self.assertEqual(extract_numbers_from_string("abc123def456"), [123, 456])

    def test_extract_characters(self):
        self.assertEqual(extract_characters("a1b2c3"), ["a", "b", "c"])

    def test_compress_string(self):
        self.assertEqual(compress_string("google", 1), "e2gl2o")
        self.assertEqual(compress_string("google", 2), "g2ogle")

    def test_compress_string_without_numbers(self):
        self.assertEqual(
            compress_string_without_numbers("hhhoocssssiiinnnhhhhh"), "hocsinh"
        )

    def test_decompress_string(self):
        self.assertEqual(decompress_string("g2ogle"), "google")

    def test_unique_characters_string(self):
        self.assertEqual(unique_characters_string("google"), "gole")

    def test_caesar_cipher_to_numbers(self):
        self.assertEqual(caesar_cipher_to_numbers("ABC", 3), [3, 4, 5])

    def test_caesar_cipher_from_numbers(self):
        self.assertEqual(caesar_cipher_from_numbers([3, 4, 5], 3), "ABC")

    def test_calculate_electricity_bill_Vietnamese(self):
        self.assertEqual(
            calculate_electricity_bill_Vietnamese(100, 150),
            "- Electricity consumed this month: 50.0 Kwh\n- Electricity bill this month: 83900.0 VND",
        )

    def test_largest_number_with_digit_sum(self):
        self.assertEqual(largest_number_with_digit_sum(3, 15), "960")

    def test_generate_sequence_rule_1(self):
        self.assertEqual(
            generate_sequence_rule_1(10), [1, 4, 6, 9, 12, 15, 16, 20, 24, 28]
        )

    def test_generate_sequence_rule_2(self):
        self.assertEqual(generate_sequence_rule_2(2, 5), [2, 4, 6, 8, 10])

    def test_generate_sequence_rule_3(self):
        self.assertEqual(generate_sequence_rule_3(5, 2), [2, 4, 8, 16, 32])

    def test_count_inversions(self):
        self.assertEqual(count_inversions([1, 3, 2]), 1)


if __name__ == "__main__":
    unittest.main()
