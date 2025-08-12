# PCHJLIB - Joesifer

<h1 align="center">
<img src="https://i.imgur.com/AUXxUzd.png" width="500" alt="PCHJLIB - Joesifer">
</h1><br>

[![PyPI Downloads](https://img.shields.io/badge/pchjlib-PyPI_downloads?style=plastic&logo=pchjlib&label=PyPI%20downloads)](https://pypi.org/project/pchjlib/)
[![GitHub](https://img.shields.io/badge/pchjlib-Joesifer_GitHub?style=plastic&logo=GitHub&label=GitHub)](https://github.com/Joesifer/pchjlib)
[![Python](https://img.shields.io/badge/Version_%3E_3.7-1?style=plastic&label=Python)](https://www.python.org/)
[![Owner](https://img.shields.io/badge/Joesifer-1?style=plastic&label=PCHJLIB&labelColor=%2300fff7&color=%23ffe600)](https://github.com/Joesifer)

## 📚 Requirements

- **Python**: >= 3.7
- **gmpy2**: Optional for big integer support in features like checking large primes. Install via `pip install gmpy2`.

## 🛠️ Installation

🚀 Install the core library without optional dependencies.

💡 **Note:** To download the icon (logo) to your `site-packages` folder, run `pchj-icon`. Warning: This modifies folder attributes (sets system/hidden) on Windows only.

### 🔧 Option 1: Install from GitHub (development version)

```bash
python -m pip install git+https://github.com/Joesifer/pchjlib.git
```

### 📦 Option 2: Install from PyPI (stable release)

```bash
python -m pip install pchjlib
```

### 🔄 Then run:

```bash
pchj-icon
```

### 🌟 Optional: Enable additional features

To activate big integer support (e.g., for large primes in `is_prime`), install `gmpy2`:

```bash
python -m pip install gmpy2
```

---

## ❓ Basic Usage

💡 **Note:** `{function}` can be `is_prime`, `generate_prime_list`, etc. `{___}` can be `primes`, `fibonacci`, `sequence_generation`, etc.

### ✅ Option 1: Import a single function

```bash
from pchjlib.{___} import {function}
result = {function}(value_1, value_2, ...)
```

### ✅ Option 2: Call via the module

```bash
import pchjlib.{___}
result = pchjlib.{___}.{function}(value_1, value_2, ...)
```

---

## 🌟 Key Features

- 🔍 **Special Number Checking and Generation**: Supports prime, emirp, Fibonacci, perfect, narcissistic, amicable, square, strong, twin prime, abundant, and happy numbers.
- 🔗 **Divisor and Multiple Operations**: Generate divisor lists, compute GCD, LCM, and perform prime factorization.
- 🧹 **List and String Processing**: Remove duplicates, extract digits/numbers/characters, and compress/decompress strings.
- 🔐 **Encryption and Decryption**: Implements Caesar cipher (for educational use only).
- ✨ **Special Calculations**: Includes electricity bill calculation, largest number with a given digit sum, sequence generation, and inversion counting.

## 📚 Table of Contents

- 🔢 [Prime and Related Number Functions](#-prime-and-related-number-functions-primespy)
- 🌀 [Fibonacci Functions](#-fibonacci-functions-fibonaccipy)
- 🧠 [Perfect, Narcissistic, Amicable, and Happy Number Functions](#-perfect-narcissistic-amicable-and-happy-number-functions-special_numbers1py)
- 📐 [Square, Strong, and Friendly Number Functions](#-square-strong-and-friendly-number-functions-special_numbers2py)
- 📊 [Divisor and Multiple Functions](#-divisor-and-multiple-functions-divisors_multiplespy)
- 👯 [Twin Prime and Abundant Number Functions](#-twin-prime-and-abundant-number-functions-twin_abundantpy)
- 🔍 [Prime Factorization Functions](#-prime-factorization-functions-prime_factorizationpy)
- 🧵 [List and String Processing Functions](#-list-and-string-processing-functions-string_processingpy)
- 🏛️ [Caesar Cipher Functions](#%EF%B8%8F-caesar-cipher-functions-caesar_cipherpy)
- 💥 [Special Calculation Functions](#-special-calculation-functions-special_calculationspy)
- 🔁 [Sequence Generation Functions](#-sequence-generation-functions-sequence_generationpy)
- 🔢 [Inversion Counting Functions](#-inversion-counting-functions-inversion_countingpy)
- 📋 [Sample Command List for the `pchjlib` Library](#-sample-command-list-for-the-pchjlib-library)
- 🧪 [Running Tests](#-running-tests)
- 🛠️ [Update History](#%EF%B8%8F-update-history)

---

### 🔢 Prime and Related Number Functions (primes.py)

Note: Miller-Rabin primality test is now deterministic using fixed witnesses for accuracy.

**is_prime(input_number)**
Checks if a number is prime. 
 - Parameter: `input_number` (int) 
 - Returns: `True` if prime, `False` otherwise. 
 - Raises: `InvalidInputError` if not an integer or negative. 
 - Example: `is_prime(7)` → `True`

**generate_prime_list(limit)**
Generates primes from 0 to `limit` using the Sieve algorithm. 
 - Parameter: `limit` (int) 
 - Returns: List of primes. 
 - Raises: `InvalidInputError` if `limit` < 2 or not an integer. 
 - Example: `generate_prime_list(10)` → `[2, 3, 5, 7]`

**is_emirp(input_number)**
Checks if a number is an emirp (prime with prime reverse). 
 - Parameter: `input_number` (int) 
 - Returns: `True` if emirp, `False` otherwise. 
 - Raises: `InvalidInputError` if not a positive integer >= 2. 
 - Example: `is_emirp(13)` → `True`

**generate_emirp_list(limit)**
Generates emirp numbers from 2 to `limit`. 
 - Parameter: `limit` (int) 
 - Returns: List of emirp numbers. 
 - Raises: `InvalidInputError` if `limit` < 2 or not an integer. 
 - Example: `generate_emirp_list(20)` → `[13, 17]`

---

### 🌀 Fibonacci Functions (fibonacci.py)

**fibonacci_at_index(index)**
Calculates the Fibonacci number at a given index with caching. 
 - Parameter: `index` (int) 
 - Returns: Fibonacci number. 
 - Raises: `InvalidInputError` if not a non-negative integer. 
 - Example: `fibonacci_at_index(5)` → `5`

**generate_fibonacci_list(count)**
Generates the first `count` Fibonacci numbers. 
 - Parameter: `count` (int) 
 - Returns: List of Fibonacci numbers. 
 - Raises: `InvalidInputError` if not a non-negative integer. 
 - Example: `generate_fibonacci_list(5)` → `[0, 1, 1, 2, 3]`

---

### 🧠 Perfect, Narcissistic, Amicable, and Happy Number Functions (special_numbers1.py)

**sum_of_divisors(input_number)**
Computes the sum of positive divisors (excluding itself). 
 - Parameter: `input_number` (int) 
 - Returns: Sum of divisors. 
 - Raises: `InvalidInputError` if not a positive integer. 
 - Example: `sum_of_divisors(6)` → `6`

**sum_of_digits(input_number)**
Calculates the sum of a number's digits. 
 - Parameter: `input_number` (int) 
 - Returns: Sum of digits. 
 - Raises: `InvalidInputError` if not an integer. 
 - Example: `sum_of_digits(123)` → `6`

**is_perfect_number(input_number)**
Checks if a number is perfect. 
 - Parameter: `input_number` (int) 
 - Returns: `True` if perfect, `False` otherwise. 
 - Raises: `InvalidInputError` if not a positive integer. 
 - Example: `is_perfect_number(6)` → `True`

**generate_perfect_number_list(limit)**
Generates perfect numbers from 1 to `limit`. 
 - Parameter: `limit` (int) 
 - Returns: List of perfect numbers. 
 - Raises: `InvalidInputError` if not a positive integer. 
 - Example: `generate_perfect_number_list(10)` → `[6]`

**is_narcissistic_number(input_number)**
Checks if a number is narcissistic. 
 - Parameter: `input_number` (int) 
 - Returns: `True` if narcissistic, `False` otherwise. 
 - Raises: `InvalidInputError` if not a non-negative integer. 
 - Example: `is_narcissistic_number(153)` → `True`

**generate_narcissistic_number_list(limit)**
Generates narcissistic numbers from 0 to `limit`. 
 - Parameter: `limit` (int) 
 - Returns: List of narcissistic numbers. 
 - Raises: `InvalidInputError` if not a non-negative integer. 
 - Example: `generate_narcissistic_number_list(10000)` → `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474]`

**are_amicable_numbers(number1, number2)**
Checks if two numbers are amicable. 
 - Parameters: `number1`, `number2` (int) 
 - Returns: `True` if amicable, `False` otherwise. 
 - Raises: `InvalidInputError` if not positive integers. 
 - Example: `are_amicable_numbers(220, 284)` → `True`

**is_happy_number(input_number)**
Checks if a number is happy. 
 - Parameter: `input_number` (int) 
 - Returns: `True` if happy, `False` otherwise. 
 - Raises: `InvalidInputError` if not a positive integer. 
 - Example: `is_happy_number(19)` → `True`

**generate_happy_number_list(limit)**
Generates happy numbers from 1 to `limit`. 
 - Parameter: `limit` (int) 
 - Returns: List of happy numbers. 
 - Raises: `InvalidInputError` if not a positive integer. 
 - Example: `generate_happy_number_list(10)` → `[1, 7, 10]`

---

### 📐 Square, Strong, and Friendly Number Functions (special_numbers2.py)

**is_square_number(input_number)**
Checks if a number is a perfect square. 
 - Parameter: `input_number` (int) 
 - Returns: `True` if square, `False` otherwise. 
 - Raises: `InvalidInputError` if not a non-negative integer. 
 - Example: `is_square_number(16)` → `True`

**generate_square_number_list(limit)**
Generates square numbers from 0 to `limit`. 
 - Parameter: `limit` (int) 
 - Returns: List of square numbers. 
 - Raises: `InvalidInputError` if not a non-negative integer. 
 - Example: `generate_square_number_list(10)` → `[0, 1, 4, 9]`

**are_friendly_numbers(number1, number2)**
Checks if two numbers are friendly. 
 - Parameters: `number1`, `number2` (int) 
 - Returns: `True` if friendly, `False` otherwise. 
 - Raises: `InvalidInputError` if not positive integers. 
 - Example: `are_friendly_numbers(30, 140)` → `True`

**is_strong_number(input_number)**
Checks if a number is strong (sum of factorial of digits equals number). 
 - Parameter: `input_number` (int) 
 - Returns: `True` if strong, `False` otherwise. 
 - Raises: `InvalidInputError` if not a non-negative integer. 
 - Example: `is_strong_number(145)` → `True`

---

### 📊 Divisor and Multiple Functions (divisors_multiples.py)

**sum_of_divisors(input_number)**
Computes the sum of positive divisors (excluding itself). 
 - Parameter: `input_number` (int) 
 - Returns: Sum of divisors. 
 - Raises: `InvalidInputError` if not a positive integer. 
 - Example: `sum_of_divisors(6)` → `6`

**generate_divisor_list(input_number, positive_only=True)**
Generates divisors of a number. 
 - Parameters: `input_number` (int), `positive_only` (bool) 
 - Returns: List of divisors. 
 - Raises: `InvalidInputError` if not an integer or zero. 
 - Example: `generate_divisor_list(6)` → `[1, 2, 3, 6]`

**generate_multiple_list(base_number, limit, positive_only=True)**
Generates multiples of a number up to `limit` times. 
 - Parameters: `base_number` (int), `limit` (int), `positive_only` (bool) 
 - Returns: List of multiples. 
 - Raises: `InvalidInputError` if not integers, number is zero, or limit < 1. 
 - Example: `generate_multiple_list(3, 5)` → `[3, 6, 9, 12, 15]`

**common_divisors(numbers)**
Generates common divisors for a list of numbers. 
 - Parameter: `numbers` (list) 
 - Returns: List of common divisors. 
 - Raises: `InvalidInputError` if not a list or contains non-integers; `MathError` if fewer than 2 non-zero elements. 
 - Example: `common_divisors([12, 18])` → `[1, 2, 3, 6]`

**greatest_common_divisor(numbers)**
Computes the GCD of a list of numbers. 
 - Parameter: `numbers` (list) 
 - Returns: GCD value. 
 - Raises: `InvalidInputError` if not a list or contains non-integers; `MathError` if fewer than 2 non-zero elements. 
 - Example: `greatest_common_divisor([12, 18])` → `6`

**least_common_multiple(numbers)**
Computes the LCM of a list of numbers. 
 - Parameter: `numbers` (list) 
 - Returns: LCM value. 
 - Raises: `InvalidInputError` if not a list, contains non-integers, or zeros; `MathError` if fewer than 2 elements. 
 - Example: `least_common_multiple([4, 6])` → `12`

---

### 👯 Twin Prime and Abundant Number Functions (twin_abundant.py)

**is_twin_prime(input_number)**
Checks if a number is a twin prime. 
 - Parameter: `input_number` (int) 
 - Returns: `True` if twin prime, `False` otherwise. 
 - Raises: `InvalidInputError` if not an integer. 
 - Example: `is_twin_prime(5)` → `True`

**generate_twin_prime_list(limit)**
Generates twin primes from 2 to `limit`. 
 - Parameter: `limit` (int) 
 - Returns: List of twin primes. 
 - Raises: `InvalidInputError` if not an integer >= 2. 
 - Example: `generate_twin_prime_list(20)` → `[3, 5, 7, 11, 13, 17, 19]`

**is_abundant_number(input_number)**
Checks if a number is abundant. 
 - Parameter: `input_number` (int) 
 - Returns: `True` if abundant, `False` otherwise. 
 - Raises: `InvalidInputError` if not a positive integer. 
 - Example: `is_abundant_number(12)` → `True`

**generate_abundant_number_list(limit)**
Generates abundant numbers from 1 to `limit`. 
 - Parameter: `limit` (int) 
 - Returns: List of abundant numbers. 
 - Raises: `InvalidInputError` if not a positive integer. 
 - Example: `generate_abundant_number_list(20)` → `[12, 18, 20]`

---

### 🔍 Prime Factorization Functions (prime_factorization.py)

**prime_factors(input_number)**
Factorizes a number into prime factors. 
 - Parameter: `input_number` (int) 
 - Returns: List of prime factors. 
 - Raises: `InvalidInputError` if not a positive integer > 1. 
 - Example: `prime_factors(12)` → `[2, 2, 3]`

**greatest_common_prime_divisor(number1, number2)**
Finds the greatest common prime divisor of two numbers. 
 - Parameters: `number1`, `number2` (int) 
 - Returns: Greatest common prime divisor. 
 - Raises: `InvalidInputError` if not positive integers > 1; `MathError` if no common prime divisor. 
 - Example: `greatest_common_prime_divisor(12, 18)` → `3`

---

### 🧵 List and String Processing Functions (string_processing.py)

**remove_duplicates(items)**
Removes duplicates from a list and sorts in descending order. 
 - Parameter: `items` (list) 
 - Returns: Sorted list without duplicates. 
 - Raises: `InvalidInputError` if not a list/tuple. 
 - Example: `remove_duplicates([1, 2, 2, 3])` → `[3, 2, 1]`

**extract_digits_from_string(text)**
Extracts individual digits from a string. 
 - Parameter: `text` (str) 
 - Returns: List of digits. 
 - Example: `extract_digits_from_string("abc123")` → `[1, 2, 3]`

**extract_numbers_from_string(text)**
Extracts full numbers from a string. 
 - Parameter: `text` (str) 
 - Returns: List of numbers. 
 - Example: `extract_numbers_from_string("abc123def456")` → `[123, 456]`

**extract_characters(text)**
Extracts non-digit characters from a string. 
 - Parameter: `text` (str) 
 - Returns: List of characters. 
 - Example: `extract_characters("a1b2c3")` → `['a', 'b', 'c']`

**compress_string(text, compress_type)**
Compresses a string using two methods. 
 - Parameters: `text` (str), `compress_type` (int) 
 - Returns: Compressed string. 
 - Example (type 1): `compress_string("google", 1)` → `'e2gl2o'` 
 - Example (type 2): `compress_string("google", 2)` → `'g2ogle'`

**compress_string_without_numbers(input_text)**
Compresses a string by removing consecutive duplicates. 
 - Parameter: `input_text` (str) 
 - Returns: Compressed string. 
 - Example: `compress_string_without_numbers("hhhoocssssiiinnnhhhhh")` → `'hocsinh'`

**decompress_string(text)**
Decompresses a string with numeric counts. 
 - Parameter: `text` (str) 
 - Returns: Decompressed string. 
 - Example: `decompress_string("g2ogle")` → `"google"`

**unique_characters_string(text)**
Creates a string with unique characters in order of appearance. 
 - Parameter: `text` (str) 
 - Returns: String with no duplicates. 
 - Example: `unique_characters_string("google")` → `"gole"`

---

### 🏛️ Caesar Cipher Functions (caesar_cipher.py)

**caesar_cipher_to_numbers(text, shift)**
Converts a string to a list of Caesar cipher numbers. 
 - Parameters: `text` (str), `shift` (int) 
 - Returns: List of shifted numbers. 
 - Example: `caesar_cipher_to_numbers("ABC", 3)` → `[3, 4, 5]`

**caesar_cipher_from_numbers(numbers, shift)**
Decodes a list of Caesar cipher numbers into a string. 
 - Parameters: `numbers` (list), `shift` (int) 
 - Returns: Decoded string. 
 - Example: `caesar_cipher_from_numbers([3, 4, 5], 3)` → `"ABC"`

---

### 💥 Special Calculation Functions (special_calculations.py)

**calculate_electricity_bill_vietnam(old_reading, new_reading)**
Calculates an electricity bill based on Vietnamese pricing tiers. 
 - Parameters: `old_reading`, `new_reading` (float) 
 - Returns: String with consumption and cost. 
 - Example: `calculate_electricity_bill_vietnam(100, 150)` → `"- Electricity consumed this month: 50.0 Kwh\n- Electricity bill this month: 83900.0 VND"`

**largest_number_with_digit_sum(digit_count, target_sum)**
Finds the largest number with `digit_count` digits summing to `target_sum`. 
 - Parameters: `digit_count` (int), `target_sum` (int) 
 - Returns: Largest number as a string. 
 - Example: `largest_number_with_digit_sum(3, 15)` → `'960'`

---

### 🔁 Sequence Generation Functions (sequence_generation.py)

**generate_sequence_rule_1(count)**
Generate a sequence according to the rule: 1 divisible by 1, 2 by 2, etc. 
 - Parameter: `count` (int) 
 - Returns: List of sequence numbers. 
 - Example: `generate_sequence_rule_1(10)` → `[1, 4, 6, 9, 12, 15, 16, 20, 24, 28]`

**generate_sequence_rule_2(base, count)**
Generates `count` multiples of `base`. 
 - Parameters: `base` (int), `count` (int) 
 - Returns: List of multiples. 
 - Example: `generate_sequence_rule_2(2, 5)` → `[2, 4, 6, 8, 10]`

**generate_sequence_rule_3(count, base)**
Generates powers of `base` from 1 to `count`. 
 - Parameters: `count` (int), `base` (int) 
 - Returns: List of powers. 
 - Example: `generate_sequence_rule_3(5, 2)` → `[2, 4, 8, 16, 32]`

---

### 🔢 Inversion Counting Functions (inversion_counting.py)

**count_inversions(numbers)**
Counts the number of inversions in a list. 
 - Parameter: `numbers` (list) 
 - Returns: Number of inversions. 
 - Example: `count_inversions([1, 3, 2])` → `1`

---

## 📋 Sample Command List for the `pchjlib` Library

## 1. Primes and Emirps

- **Check if a number is prime:**
`python pchjmain.py primes_and_emirps --is_prime <number>` 
 _Example:_ `python pchjmain.py primes_and_emirps --is_prime 17`

- **Generate a list of primes:**
`python pchjmain.py primes_and_emirps --generate_prime_list <limit>` 
 _Example:_ `python pchjmain.py primes_and_emirps --generate_prime_list 50`

- **Check if a number is an emirp:**
`python pchjmain.py primes_and_emirps --is_emirp <number>` 
 _Example:_ `python pchjmain.py primes_and_emirps --is_emirp 13`

- **Generate a list of emirps:**
`python pchjmain.py primes_and_emirps --generate_emirp_list <limit>` 
 _Example:_ `python pchjmain.py primes_and_emirps --generate_emirp_list 100`

## 2. Twin Primes and Abundant Numbers

- **Check if a number is a twin prime:**
`python pchjmain.py twin_primes_and_abundant --is_twin_prime <number>` 
 _Example:_ `python pchjmain.py twin_primes_and_abundant --is_twin_prime 5`

- **Generate a list of twin primes:**
`python pchjmain.py twin_primes_and_abundant --generate_twin_prime_list <limit>` 
 _Example:_ `python pchjmain.py twin_primes_and_abundant --generate_twin_prime_list 50`

- **Check if a number is abundant:**
`python pchjmain.py twin_primes_and_abundant --is_abundant <number>` 
 _Example:_ `python pchjmain.py twin_primes_and_abundant --is_abundant 12`

- **Generate a list of abundant numbers:**
`python pchjmain.py twin_primes_and_abundant --generate_abundant_list <limit>` 
 _Example:_ `python pchjmain.py twin_primes_and_abundant --generate_abundant_list 100`

## 3. Fibonacci Sequence

- **Compute the Fibonacci number at a given index:**
`python pchjmain.py fibonacci --at_index <index>` 
 _Example:_ `python pchjmain.py fibonacci --at_index 10`

- **Generate a list of Fibonacci numbers:**
`python pchjmain.py fibonacci --generate_list <count>` 
 _Example:_ `python pchjmain.py fibonacci --generate_list 5`

## 4. Special Numbers 1 (Perfect, Narcissistic, Amicable, Happy)

- **Check if a number is perfect:**
`python pchjmain.py special_numbers_1 --is_perfect <number>` 
 _Example:_ `python pchjmain.py special_numbers_1 --is_perfect 28`

- **Generate a list of perfect numbers:**
`python pchjmain.py special_numbers_1 --generate_perfect_list <limit>` 
 _Example:_ `python pchjmain.py special_numbers_1 --generate_perfect_list 1000`

- **Check if a number is narcissistic:**
`python pchjmain.py special_numbers_1 --is_narcissistic <number>` 
 _Example:_ `python pchjmain.py special_numbers_1 --is_narcissistic 153`

- **Generate a list of narcissistic numbers:**
`python pchjmain.py special_numbers_1 --generate_narcissistic_list <limit>` 
 _Example:_ `python pchjmain.py special_numbers_1 --generate_narcissistic_list 1000`

- **Check if two numbers are amicable:**
`python pchjmain.py special_numbers_1 --are_amicable <number1> <number2>` 
 _Example:_ `python pchjmain.py special_numbers_1 --are_amicable 220 284`

- **Check if a number is happy:**
`python pchjmain.py special_numbers_1 --is_happy <number>` 
 _Example:_ `python pchjmain.py special_numbers_1 --is_happy 19`

- **Generate a list of happy numbers:**
`python pchjmain.py special_numbers_1 --generate_happy_list <limit>` 
 _Example:_ `python pchjmain.py special_numbers_1 --generate_happy_list 100`

## 5. Special Numbers 2 (Square, Strong, Friendly)

- **Check if a number is a perfect square:**
`python pchjmain.py special_numbers_2 --is_square <number>` 
 _Example:_ `python pchjmain.py special_numbers_2 --is_square 16`

- **Generate a list of perfect squares:**
`python pchjmain.py special_numbers_2 --generate_square_list <limit>` 
 _Example:_ `python pchjmain.py special_numbers_2 --generate_square_list 100`

- **Check if a number is strong:**
`python pchjmain.py special_numbers_2 --is_strong <number>` 
 _Example:_ `python pchjmain.py special_numbers_2 --is_strong 145`

- **Check if two numbers are friendly:**
`python pchjmain.py special_numbers_2 --are_friendly <number1> <number2>` 
 _Example:_ `python pchjmain.py special_numbers_2 --are_friendly 30 140`

## 6. Divisors and Multiples

- **Generate a list of divisors:**
`python pchjmain.py divisors_and_multiples --generate_divisor_list <number>` 
 _Example:_ `python pchjmain.py divisors_and_multiples --generate_divisor_list 28`

- **Generate a list of multiples:**
`python pchjmain.py divisors_and_multiples --generate_multiple_list <number> <limit>` 
 _Example:_ `python pchjmain.py divisors_and_multiples --generate_multiple_list 3 20`

- **Find common divisors:**
`python pchjmain.py divisors_and_multiples --common_divisors <number1> <number2> [<number3> ...]` 
 _Example:_ `python pchjmain.py divisors_and_multiples --common_divisors 12 18 24`

- **Compute GCD (Greatest Common Divisor):**
`python pchjmain.py divisors_and_multiples --gcd <number1> <number2> [<number3> ...]` 
 _Example:_ `python pchjmain.py divisors_and_multiples --gcd 12 18 24`

- **Compute LCM (Least Common Multiple):**
`python pchjmain.py divisors_and_multiples --lcm <number1> <number2> [<number3> ...]` 
 _Example:_ `python pchjmain.py divisors_and_multiples --lcm 4 5 6`

## 7. Prime Factorization

- **Prime factorization:**
`python pchjmain.py prime_factorization --prime_factors <number>` 
 _Example:_ `python pchjmain.py prime_factorization --prime_factors 100`

- **Greatest common prime divisor:**
`python pchjmain.py prime_factorization --greatest_common_prime_divisor <number1> <number2>` 
 _Example:_ `python pchjmain.py prime_factorization --greatest_common_prime_divisor 12 18`

## 8. String Processing

- **Remove duplicate elements:**
`python pchjmain.py string_processing --remove_duplicates <elem1> <elem2> ...` 
 _Example:_ `python pchjmain.py string_processing --remove_duplicates 1 2 2 3 4 4`

- **Extract digits:**
`python pchjmain.py string_processing --extract_digits "<string>"` 
 _Example:_ `python pchjmain.py string_processing --extract_digits "a1b2c3"`

- **Extract numbers:**
`python pchjmain.py string_processing --extract_numbers "<string>"` 
 _Example:_ `python pchjmain.py string_processing --extract_numbers "a12b34c56"`

- **Extract non-digit characters:**
`python pchjmain.py string_processing --extract_characters "<string>"` 
 _Example:_ `python pchjmain.py string_processing --extract_characters "a1b2c3"`

- **Compress a string (type 1 or 2):**
`python pchjmain.py string_processing --compress "<string>" <compress_type>` 
 _Example:_ `python pchjmain.py string_processing --compress "aaabbbcc" 1`

- **Compress a string without counts:**
`python pchjmain.py string_processing --compress_without_numbers "<string>"` 
 _Example:_ `python pchjmain.py string_processing --compress_without_numbers "aaabbbcc"`

- **Decompress a string:**
`python pchjmain.py string_processing --decompress "<compressed_string>"` 
 _Example:_ `python pchjmain.py string_processing --decompress "a3b2c1"`

- **Get unique characters in a string:**
`python pchjmain.py string_processing --unique_characters "<string>"` 
 _Example:_ `python pchjmain.py string_processing --unique_characters "aaabbbcc"`

## 9. Caesar Cipher

- **Convert text to Caesar numbers:**
`python pchjmain.py caesar_cipher --to_numbers "<text>" <shift>` 
 _Example:_ `python pchjmain.py caesar_cipher --to_numbers "abc" 3`

- **Convert Caesar numbers back to text:**
`python pchjmain.py caesar_cipher --from_numbers <shift> <num1> <num2> ...` 
 _Example:_ `python pchjmain.py caesar_cipher --from_numbers 3 4 5 6`

## 10. Special Calculations

- **Calculate an electricity bill:**
`python pchjmain.py special_calculations --electricity_bill <old_reading> <new_reading>` 
 _Example:_ `python pchjmain.py special_calculations --electricity_bill 100 200`

- **Find the largest number with given digits sum:**
`python pchjmain.py special_calculations --largest_number <digit_count> <digit_sum>` 
 _Example:_ `python pchjmain.py special_calculations --largest_number 3 15`

## 11. Sequence Generation

- **Generate sequence by rule 1:**
`python pchjmain.py sequence_generation --rule1 <count>` 
 _Example:_ `python pchjmain.py sequence_generation --rule1 5`

- **Generate sequence by rule 2:**
`python pchjmain.py sequence_generation --rule2 <base> <count>` 
 _Example:_ `python pchjmain.py sequence_generation --rule2 2 5`

- **Generate sequence by rule 3:**
`python pchjmain.py sequence_generation --rule3 <count> <base>` 
 _Example:_ `python pchjmain.py sequence_generation --rule3 5 2`

## 12. Inversion Counting

- **Count inversions in a list:**
`python pchjmain.py inversion_counting --count <elem1> <elem2> ...` 
 _Example:_ `python pchjmain.py inversion_counting --count 2 3 1 4`

---

### Note

- Replace `<...>` with actual values when running the command. 
- Ensure commands are executed in the directory containing `pchjmain.py`. 
- For detailed help on any category, run `python pchjmain.py <category> -h` (e.g., `python pchjmain.py primes_and_emirps -h`).

---

## 🧪 Running Tests

To run the unit tests for the library, navigate to the project root and execute:

```bash
python -m unittest discover tests
```

This will discover and run all tests in the `tests/` directory. Ensure the library is installed in editable mode (`pip install -e .`) for proper import resolution.

---

## 🛠️ Update History

> **📅 Latest Update:** August 12, 2025
> **📦 Total Releases:** 98

### 📌 2025

#### 1.7.0 (August 12, 2025)
- **Performance Improvements**: Implemented merge sort for O(n log n) inversion counting; added Pollard's Rho for faster prime factorization on large numbers; made sequence generation dynamic to handle larger counts; integrated optional gmpy2 for accelerated GCD/LCM.
- **Code Quality Enhancements**: Standardized function names (e.g., `calculate_electricity_bill_Vietnamese` to `calculate_electricity_bill_vietnam`); replaced wildcard imports with explicit ones in `__init__.py`; fixed bug in `largest_number_with_digit_sum` for correct largest output (e.g., '960' for 3 digits sum 15); improved CLI error handling with detailed tracebacks; added user warning for side-effects in `pchjicon.py`; made Miller-Rabin primality test deterministic using fixed witnesses.
- **Documentation Updates**: Fixed incorrect examples in README (e.g., largest number); summarized update history for brevity; removed redundant sections and added warnings for probabilistic methods (now deterministic) and side-effects.

#### 1.6.5 → 1.5.0 (August 11-12, 2025)
- Fixed minor bugs and optimized `generate_sequence_rule_3`/`generate_sequence_rule_2`.
- Updated `is_strong_number` to standard factorion definition.
- Removed `solve_equation` and its CLI category.
- Eliminated `numpy` dependency; added optional gmpy2 integration.
- Added type hints, examples, and performance optimizations (e.g., iterative Fibonacci).

#### 1.4.5 → 1.3.0 (August 7-8, 2025)
- Fixed minor bugs.

#### 1.2.3 → 1.0.1 (August 4–5, 2025)
- Removed unused functions; added logo support via `pchj-icon`.
- Added Sample Command List; enhanced CLI.

#### 1.0.0 → 0.1.5.1 (August 3-4, 2025)
- Major overhaul: Optimizations, error handling, documentation, and tests.
- Removed legacy dependencies and functions; switched README to English.

#### 0.1.5 → 0.1.4 (August 2, 2025)
- Removed Roman numeral conversion; fixed matrix program.
- Added negative divisors/multiples; merged string compression.

#### 0.1.3.2 → 0.1.2 (August 1, 2025)
- Minor fixes; consolidated strong-number logic; optimized Fibonacci/primes.

#### 0.1.1.3 → 0.1.0.7 (July 31, 2025)
- README updates; dependency fixes.

#### 0.1.0.6 → 0.1.0.3 (July 28–30, 2025)
- Bug fixes.

#### 0.1.0.2 → 0.1.0 (July 28, 2025)
- Minor fixes; removed legacy functions; code overhaul.

#### 0.0.5.2.1 → 0.0.5.0 (July 26-27, 2025)
- README tweaks; updated teen code.

### 📌 2024
- **0.0.4.1 (October 17, 2024)**: Added sequence creation; updated one-two-three.
- **0.0.4.0 → 0.0.3.5 (May 3–5, 2024)**: README fixes; updated Christmas tree variants; testing.
- **0.0.3.4 (February 26, 2024)**: Added common divisors list.
- **0.0.3.3 → 0.0.3 (February 20–21, 2024)**: README enhancements; added abundant check and unique string; removed duplicates check.
- **0.0.2.10 → 0.0.2.6 (February 18–19, 2024)**: README updates; testing; switched to MIT License.
- **0.0.2.5 → 0.0.2.1 (February 14–18, 2024)**: README and tests.
- **0.0.2 → 0.0.0.1 (February 14, 2024)**: Dependency fixes; testing; initial release.