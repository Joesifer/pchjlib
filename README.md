<h1 align="center">
<img src="https://i.imgur.com/AUXxUzd.png" width="500" alt="PCHJLIB - Joesifer">
</h1><br>

[![PyPI Downloads](https://img.shields.io/badge/pchjlib-PyPI_downloads?style=plastic&logo=pchjlib&label=PyPI%20downloads)](https://pypi.org/project/pchjlib/)
[![GitHub](https://img.shields.io/badge/pchjlib-Joesifer_GitHub?style=plastic&logo=GitHub&label=GitHub)](https://github.com/Joesifer/pchjlib)
[![Python](https://img.shields.io/badge/Version_%3E_3.7-1?style=plastic&label=Python)](https://www.python.org/)
[![Owner](https://img.shields.io/badge/Joesifer-1?style=plastic&label=PCHJLIB&labelColor=%2300fff7&color=%23ffe600)](https://github.com/Joesifer)

# 📚 Requirements

- **Python**: >= 3.7
- **numpy**: Optional, required for `solve_equation` and `generate_prime_list`. Install via `pip install pchjlib[numpy]` or `pip install numpy`.

# 🛠️ Installation

Install the core library without optional dependencies:

```bash
pip install pchjlib
```

To enable `solve_equation` and `generate_prime_list`, include `numpy`:

```bash
pip install pchjlib[numpy]
```

---

# 🌟 Key Features

- 🔍 **Special Number Checking and Generation**:  
  Supports prime numbers, emirp numbers, Fibonacci numbers, perfect numbers, narcissistic numbers, amicable numbers, square numbers, strong numbers, twin primes, abundant numbers, and happy numbers.

- 🔗 **Divisor and Multiple Operations**:  
  Generate divisor lists, compute greatest common divisor (GCD), least common multiple (LCM), and perform prime factorization.

- 🧮 **Equation Solving**:  
  Solves polynomial equations from degree 1 to 10.

- 🧹 **List and String Processing**:  
  Removes duplicates, extracts digits/numbers/characters from strings, and compresses/decompresses strings.

- 🔐 **Encryption and Decryption**:  
  Implements Caesar cipher (educational use only, not for secure applications).

- ✨ **Special Calculations**:  
  Calculates electricity bills, finds the largest number with a given digit sum, generates sequences, and counts inversions.

# 📚 Table of Contents

- 🔢 [Prime and Related Number Functions](#prime-and-related-number-functions)  
- 🌀 [Fibonacci Functions](#fibonacci-functions)  
- 🧠 [Perfect, Narcissistic, Amicable, and Happy Number Functions](#perfect-narcissistic-amicable-and-happy-number-functions)  
- 📐 [Square, Strong, and Friendly Number Functions](#square-strong-and-friendly-number-functions)  
- 📊 [Divisor and Multiple Functions](#divisor-and-multiple-functions)  
- 👯 [Twin Prime and Abundant Number Functions](#twin-prime-and-abundant-number-functions)  
- 🔍 [Prime Factorization Functions](#prime-factorization-functions)  
- 🧮 [Equation Solving Functions](#equation-solving-functions)  
- 🧵 [List and String Processing Functions](#list-and-string-processing-functions)  
- 🏛️ [Caesar Cipher Functions](#caesar-cipher-functions)  
- 💥 [Special Calculation Functions](#special-calculation-functions)  
- 🔁 [Sequence Generation Functions](#sequence-generation-functions)  
- 🔢 [Inversion Counting Functions](#inversion-counting-functions)  
- 🛠️ [Update History](#update-history)

---

## 🔢 Prime and Related Number Functions

- **is_prime(number)**  
  Checks if a number is prime.  
  - **Parameter**: `number` (int) - The number to check.  
  - **Returns**: `True` if prime, `False` otherwise.  
  - **Raises**: `InvalidInputError` if the input is not an integer.  
  - **Example**: `is_prime(7)` → `True`.

- **generate_prime_list(limit)**  
  Generates a list of prime numbers from 0 to `limit` using the Sieve algorithm.  
  - **Parameter**: `limit` (int) - Upper limit of the list.  
  - **Returns**: List of prime numbers.  
  - **Raises**: `InvalidInputError` if `limit` is not an integer >= 2; `ImportError` if `numpy` is not installed.  
  - **Example**: `generate_prime_list(10)` → `[2, 3, 5, 7]`.

- **is_emirp(number)**  
  Checks if a number is an emirp (a prime whose reverse is also prime).  
  - **Parameter**: `number` (int) - The number to check.  
  - **Returns**: `True` if emirp, `False` otherwise.  
  - **Raises**: `InvalidInputError` if `number` is not a positive integer.  
  - **Example**: `is_emirp(31)` → `True`.

- **generate_emirp_list(limit)**  
  Generates a list of emirp numbers from 0 to `limit`.  
  - **Parameter**: `limit` (int) - Upper limit of the list.  
  - **Returns**: List of emirp numbers.  
  - **Raises**: `InvalidInputError` if `limit` is not a non-negative integer.  

---

## 🌀 Fibonacci Functions

- **fibonacci_at_index(index)**  
  Calculates the Fibonacci number at a given index using iteration.  
  - **Parameter**: `index` (int) - Position in the Fibonacci sequence (starts at 0).  
  - **Returns**: Fibonacci number at the index.  
  - **Raises**: `InvalidInputError` if `index` is not a non-negative integer.  

- **generate_fibonacci_list(count)**  
  Generates a list of the first `count` Fibonacci numbers.  
  - **Parameter**: `count` (int) - Number of elements to generate.  
  - **Returns**: List of Fibonacci numbers.  
  - **Raises**: `InvalidInputError` if `count` is not a non-negative integer.  

---

## 🧠 Perfect, Narcissistic, Amicable, and Happy Number Functions

- **sum_of_divisors(number)**  
  Computes the sum of positive divisors of a number (excluding itself).  
  - **Parameter**: `number` (int) - Number to calculate divisors for.  
  - **Returns**: Sum of divisors.  
  - **Raises**: `MathError` if `number <= 0`; `InvalidInputError` if not an integer.  

- **sum_of_digits(number)**  
  Calculates the sum of a number's digits.  
  - **Parameter**: `number` (int) - Number to process.  
  - **Returns**: Sum of digits.  
  - **Raises**: `InvalidInputError` if not an integer.  

- **is_perfect_number(number)**  
  Checks if a number is perfect (sum of proper divisors equals the number).  
  - **Parameter**: `number` (int) - Number to check.  
  - **Returns**: `True` if perfect, `False` otherwise.  
  - **Raises**: `MathError` if `number < 1`; `NotIntegerError` if not an integer.  

- **generate_perfect_number_list(limit)**  
  Generates a list of perfect numbers from 1 to `limit`.  
  - **Parameter**: `limit` (int) - Upper limit of the list.  
  - **Returns**: List of perfect numbers.  
  - **Raises**: `NotIntegerError` if `limit` is not an integer; `InvalidInputError` if `limit < 1`.  

- **is_narcissistic_number(number)**  
  Checks if a number is narcissistic (sum of digits raised to the power of digit count equals the number).  
  - **Parameter**: `number` (int) - Number to check.  
  - **Returns**: `True` if narcissistic, `False` otherwise.  
  - **Raises**: `NotIntegerError` if not an integer.  
  - **Note**: In this implementation, checks for 3-digit narcissistic numbers specifically.

- **generate_narcissistic_number_list(limit)**  
  Generates a list of narcissistic numbers from 2 to `limit`.  
  - **Parameter**: `limit` (int) - Upper limit of the list.  
  - **Returns**: List of narcissistic numbers.  
  - **Raises**: `NotIntegerError` if not an integer; `InvalidInputError` if `limit < 2`.  

- **are_amicable_numbers(number1, number2)**  
  Checks if two numbers are amicable (sum of proper divisors of each equals the other).  
  - **Parameters**: `number1`, `number2` (int) - Numbers to check.  
  - **Returns**: `True` if amicable, `False` otherwise.  
  - **Raises**: `MathError` if numbers are negative; `NotIntegerError` if not integers.  

- **is_happy_number(number)**  
  Checks if a number is happy (repeated sum of squared digits reaches 1).  
  - **Parameter**: `number` (int) - Number to check.  
  - **Returns**: `True` if happy, `False` otherwise.  
  - **Raises**: `MathError` if `number < 1`; `NotIntegerError` if not an integer.  

- **generate_happy_number_list(limit)**  
  Generates a list of happy numbers from 1 to `limit`.  
  - **Parameter**: `limit` (int) - Upper limit of the list.  
  - **Returns**: List of happy numbers.  
  - **Raises**: `NotIntegerError` if not an integer; `InvalidInputError` if `limit < 1`.  

---

## 📐 Square, Strong, and Friendly Number Functions

- **is_square_number(number)**  
  Checks if a number is a perfect square.  
  - **Parameter**: `number` (int) - Number to check.  
  - **Returns**: `True` if square, `False` otherwise.  
  - **Raises**: `NotIntegerError` if not an integer.  

- **generate_square_number_list(limit)**  
  Generates a list of square numbers from 0 to `limit`.  
  - **Parameter**: `limit` (int) - Upper limit of the list.  
  - **Returns**: List of square numbers.  
  - **Raises**: `NotIntegerError` if not an integer; `InvalidInputError` if `limit < 0`.  

- **are_friendly_numbers(number1, number2)**  
  Checks if two numbers are friendly (sum of proper divisors of each equals the other).  
  - **Parameters**: `number1`, `number2` (int) - Numbers to check.  
  - **Returns**: `True` if friendly, `False` otherwise.  
  - **Raises**: `MathError` if numbers are not > 1; `NotIntegerError` if not integers.  

- **is_strong_number(number, variant=1)**  
  Checks if a number is strong based on the variant (1: sum of digits is prime; 2: has a square prime factor).  
  - **Parameters**: `number` (int) - Number to check; `variant` (int) - Variant type (1 or 2).  
  - **Returns**: `True` if strong, `False` otherwise.  
  - **Raises**: `NotIntegerError` if `number` is not a non-negative integer.  

---

## 📊 Divisor and Multiple Functions

- **generate_divisor_list(number, positive_only=True)**  
  Generates a list of divisors for a number.  
  - **Parameters**: `number` (int) - Number to process; `positive_only` (bool) - If `True`, only positive divisors.  
  - **Returns**: List of divisors.  
  - **Raises**: `MathError` if `number == 0`; `NotIntegerError` if not an integer.  

- **generate_multiple_list(number, limit, positive_only=True)**  
  Generates a list of multiples of a number up to `limit` times.  
  - **Parameters**: `number` (int) - Base number; `limit` (int) - Number of multiples; `positive_only` (bool) - If `True`, only positive multiples.  
  - **Returns**: List of multiples.  
  - **Raises**: `MathError` if `number == 0`; `NotIntegerError` if inputs are not integers; `InvalidInputError` if `limit <= 1`.  

- **common_divisors(numbers)**  
  Generates a list of common divisors for a list of numbers.  
  - **Parameter**: `numbers` (list) - List of numbers.  
  - **Returns**: List of common divisors.  
  - **Raises**: `MathError` if list has fewer than 2 elements; `ListError` if not a list/tuple; `NotIntegerError` if elements are not integers.  

- **greatest_common_divisor(numbers)**  
  Computes the greatest common divisor of a list of numbers.  
  - **Parameter**: `numbers` (list) - List of numbers.  
  - **Returns**: GCD value.  
  - **Raises**: `MathError` if list is invalid; `ListError` if not a list/tuple; `NotIntegerError` if elements are not integers.  

- **least_common_multiple(numbers)**  
  Computes the least common multiple of a list of numbers.  
  - **Parameter**: `numbers` (list) - List of numbers.  
  - **Returns**: LCM value.  
  - **Raises**: `MathError` if list is invalid or contains 0; `ListError` if not a list/tuple; `NotIntegerError` if elements are not integers.  

---

## 👯 Twin Prime and Abundant Number Functions

- **is_twin_prime(number)**  
  Checks if a number is a twin prime (prime and sum of digits is prime).  
  - **Parameter**: `number` (int) - Number to check.  
  - **Returns**: `True` if twin prime, `False` otherwise.  
  - **Raises**: `NotIntegerError` if not an integer.  

- **generate_twin_prime_list(limit)**  
  Generates a list of twin primes from 0 to `limit`.  
  - **Parameter**: `limit` (int) - Upper limit of the list.  
  - **Returns**: List of twin primes.  
  - **Raises**: `NotIntegerError` if not an integer; `InvalidInputError` if `limit < 0`.  

- **is_abundant_number(number)**  
  Checks if a number is abundant (sum of proper divisors exceeds the number).  
  - **Parameter**: `number` (int) - Number to check.  
  - **Returns**: `True` if abundant, `False` otherwise.  
  - **Raises**: `NotIntegerError` if not an integer.  

- **generate_abundant_number_list(limit)**  
  Generates a list of abundant numbers from 0 to `limit`.  
  - **Parameter**: `limit` (int) - Upper limit of the list.  
  - **Returns**: List of abundant numbers.  
  - **Raises**: `NotIntegerError` if not an integer; `InvalidInputError` if `limit < 0`.  

---

## 🔍 Prime Factorization Functions

- **prime_factors(number)**  
  Factorizes a number into its prime factors.  
  - **Parameter**: `number` (int) - Number to factorize.  
  - **Returns**: List of prime factors.  
  - **Raises**: `MathError` if `number <= 1`; `NotIntegerError` if not an integer.  

- **greatest_common_prime_divisor(number1, number2)**  
  Finds the greatest common prime divisor of two numbers.  
  - **Parameters**: `number1`, `number2` (int) - Numbers to process.  
  - **Returns**: Greatest common prime divisor.  
  - **Raises**: `MathError` if numbers are <= 1 or no common prime divisor exists; `NotIntegerError` if not integers.  

---

## 🧮 Equation Solving Functions

- **solve_equation(degree, coefficients)**  
  Solves polynomial equations from degree 1 to `n` based on coefficients.  
  - **Parameters**: `degree` (int) - Degree of the equation; `coefficients` (list) - List of coefficients.  
  - **Returns**: String describing the roots.  
  - **Raises**: `ImportError` if `numpy` is not installed; `NotIntegerError` if `degree` is not an integer; `InvalidInputError` if inputs are invalid; `ListError` if `coefficients` is not a list/tuple.  

---

## 🧵 List and String Processing Functions

- **remove_duplicates(items)**  
  Removes duplicates from a list and sorts in descending order.  
  - **Parameter**: `items` (list) - List to process.  
  - **Returns**: Sorted list without duplicates.  
  - **Raises**: `ListError` if not a list/tuple.  

- **extract_digits_from_string(text)**  
  Extracts individual digits from a string.  
  - **Parameter**: `text` (str) - Input string.  
  - **Returns**: List of digits (e.g., "abc123" → `[1, 2, 3]`).  
  - **Raises**: `TypeErrorCustom` if not a string; `InvalidInputError` if empty.  

- **extract_numbers_from_string(text)**  
  Extracts full numbers from a string.  
  - **Parameter**: `text` (str) - Input string.  
  - **Returns**: List of numbers (e.g., "abc123" → `[123]`).  
  - **Raises**: `TypeErrorCustom` if not a string; `InvalidInputError` if empty.  

- **extract_characters(text)**  
  Extracts non-digit characters from a string.  
  - **Parameter**: `text` (str) - Input string.  
  - **Returns**: List of characters.  
  - **Raises**: `TypeErrorCustom` if not a string; `InvalidInputError` if empty.  

- **compress_string(text, compress_type)**  
  Compresses a string using two methods (1: sorted with counts; 2: sequential with counts).  
  - **Parameters**: `text` (str) - Input string; `compress_type` (int) - 1 or 2.  
  - **Returns**: Compressed string.  
  - **Raises**: `TypeErrorCustom` if not a string; `InvalidInputError` if empty or `compress_type` is not 1/2.  

- **compress_string_without_numbers(input_text)**  
  Compresses a string by removing consecutive duplicates.  
  - **Parameter**: `input_text` (str) - Input string.  
  - **Returns**: Compressed string (e.g., "hhhoocssssiiinnnhhhhh" → "hocsinh").  
  - **Raises**: `TypeErrorCustom` if not a string; `InvalidInputError` if empty.  

- **decompress_string(text)**  
  Decompresses a string with numeric counts.  
  - **Parameter**: `text` (str) - Input string.  
  - **Returns**: Decompressed string (e.g., "g2ogle" → "google").  
  - **Raises**: `TypeErrorCustom` if not a string; `InvalidInputError` if empty.  

- **unique_characters_string(text)**  
  Creates a string with unique characters in order of appearance.  
  - **Parameter**: `text` (str) - Input string.  
  - **Returns**: String with no duplicates (e.g., "google" → "gole").  
  - **Raises**: `TypeErrorCustom` if not a string; `InvalidInputError` if empty.  

---

## 🏛️ Caesar Cipher Functions

- **caesar_cipher_to_numbers(text, shift)**  
  Converts a string to a list of Caesar cipher numbers.  
  - **Parameters**: `text` (str) - Input string; `shift` (int) - Shift value.  
  - **Returns**: List of shifted numbers.  
  - **Raises**: `TypeErrorCustom` if not a string; `InvalidInputError` if empty or non-alphabetic; `NotIntegerError` if `shift` is not an integer.  

- **caesar_cipher_from_numbers(numbers, shift)**  
  Decodes a list of Caesar cipher numbers into a string.  
  - **Parameters**: `numbers` (list) - List of numbers; `shift` (int) - Shift value.  
  - **Returns**: Decoded string.  
  - **Raises**: `ListError` if not a list/tuple; `InvalidInputError` if empty or numbers not 0-25; `NotIntegerError` if `shift` is not an integer.  

---

## 💥 Special Calculation Functions

- **calculate_electricity_bill_Vietnamese(old_reading, new_reading)**  
  Calculates an electricity bill based on meter readings (Vietnamese pricing tiers).  
  - **Parameters**: `old_reading`, `new_reading` (str) - Old and new meter readings.  
  - **Returns**: String with consumption and cost in VND.  
  - **Raises**: `MathError` if readings are invalid; `TypeErrorCustom` if not convertible to numbers.  

- **largest_number_with_digit_sum(digit_count, target_sum)**  
  Finds the largest number with `digit_count` digits summing to `target_sum`.  
  - **Parameters**: `digit_count` (int) - Number of digits; `target_sum` (int) - Desired digit sum.  
  - **Returns**: Largest number as a string.  
  - **Raises**: `MathError` if conditions cannot be met; `NotIntegerError` if inputs are not integers.  

---

## 🔁 Sequence Generation Functions

- **generate_sequence_rule_1(number)**  
  Generates a sequence where the nth group has n numbers divisible by n, no duplicates.  
  - **Parameter**: `number` (int) - Number of elements to generate.  
  - **Returns**: List of sequence numbers.  
  - **Raises**: `InvalidInputError` if `number <= 1`; `OutOfRangeError` if sequence exceeds limit.  

- **generate_sequence_rule_2(base, count)**  
  Generates a list of `count` multiples of `base`.  
  - **Parameters**: `base` (int) - Base number; `count` (int) - Number of multiples.  
  - **Returns**: List of multiples.  
  - **Raises**: `NotIntegerError` if inputs are not integers; `InvalidInputError` if `count < 0`.  

- **generate_sequence_rule_3(count, base)**  
  Generates a list of powers of `base` from 0 to `count-1`.  
  - **Parameters**: `count` (int) - Number of elements; `base` (int) - Base number.  
  - **Returns**: List of powers.  
  - **Raises**: `NotIntegerError` if inputs are not integers; `InvalidInputError` if `count < 0`.  

---

## 🔢 Inversion Counting Functions

- **count_inversions(numbers)**  
  Counts the number of inversions (pairs where a larger number precedes a smaller one) in a list.  
  - **Parameter**: `numbers` (list) - List to analyze.  
  - **Returns**: Number of inversions.  
  - **Raises**: `ListError` if not a list/tuple; `TypeErrorCustom` if elements are not numbers.  

---

## 🛠️ Update History

> **📅 Latest Update:** 03/08/2025  
> **📦 Total Releases:** 56

### 📌 2025

- **0.1.7** – *(03/08/2025)*  
  ❌ Removed unused functions from README not present in code: `teen_code_yahoo`, `mp_tai_xuong`, `mp_tinh_toan`, `mp_loading`, `mp_christmas_tree`, `chuong_trinh_matrix`, `one_two_three`, `pythagore`, `kiem_tra_so_hoan_hao`, `tao_danh_sach_so_hoan_hao`.
  ✅ Using English for README.
  ✅ Enhanced solve_equation to handle equations of arbitrary degree.

- **0.1.6** – *(03/08/2025)*  
  ✅ Updated `generate_sequence_rule_1`.  

- **0.1.5.2** – *(03/08/2025)*  
  ✅ Enhanced `generate_multiple_list` with multiplication limit and negative multiples support.  

- **0.1.5.1** – *(03/08/2025)*  
  ✅ Extended `greatest_common_divisor` to handle zero.  

- **0.1.5** – *(02/08/2025)*  
  ❌ Removed `chuyen_doi_so_la_ma`.  

- **0.1.4.2** – *(02/08/2025)*  
  🔧 Fixed bug in `chuong_trinh_matrix`.  

- **0.1.4.1** – *(02/08/2025)*  
  ✅ Updated `chuong_trinh_matrix`.  

- **0.1.4** – *(02/08/2025)*  
  ✅ Added negative divisor/multiple options to `generate_multiple_list` and `generate_divisor_list`.  
  🔧 Fixed `common_divisors`.  
  ❌ Removed `greatest_common_divisor`, `trich_xuat_cac_so_tu_so`.  
  ✅ Merged two string compression functions into one.  

- **0.1.3.2** – *(01/08/2025)*  
  🔧 Fixed minor bugs.  

- **0.1.3.1** – *(01/08/2025)*  
  🔧 Fixed minor bugs.  

- **0.1.3** – *(01/08/2025)*  
  ✅ Consolidated two strong number functions into one.  
  ⚡ Optimized Fibonacci with caching.  
  📚 Added type hints and NumPy-style docstrings.  

- **0.1.2.1** – *(01/08/2025)*  
  🔧 Fixed minor bugs.  

- **0.1.2** – *(01/08/2025)*  
  ✅ Improved input validation consistency.  
  ⚡ Optimized Fibonacci and prime number performance.  
  📚 Expanded documentation with expected errors.  

- **0.1.1.3** – *(31/07/2025)*  
  🔧 Updated README.  

- **0.1.1.2** – *(31/07/2025)*  
  🔧 Updated README.  

- **0.1.1.1** – *(31/07/2025)*  
  🔧 Fixed display bug.  

- **0.1.1** – *(31/07/2025)*  
  🔧 Fixed bugs and updated dependencies for `numpy` and `roman`.  

- **0.1.0.7** – *(31/07/2025)*  
  🔧 Fixed bugs.  

- **0.1.0.6** – *(30/07/2025)*  
  🔧 Minor Python version support adjustments.  

- **0.1.0.5** – *(29/07/2025)*  
  🔧 Fixed bugs.  

- **0.1.0.4** – *(28/07/2025)*  
  🔧 Fixed bugs.  

- **0.1.0.3** – *(28/07/2025)*  
  ✏️ Revised README.  

- **0.1.0.2** – *(28/07/2025)*  
  ❌ Removed `thua_so_nguyen_to_day_du`.  

- **0.1.0.1** – *(28/07/2025)*  
  🔧 Fixed minor content bugs.  

- **0.1.0** – *(28/07/2025)*  
  🧹 Complete overhaul.  
  ❌ Removed `giai_pt_bac_1va2_dang_string`, `tinh_toan_vat_ly_8`.  

#### 🔵 0.0.5.x — Minor Tweaks and Updates

- **0.0.5.2.1** – *(27/07/2025)*  
  ✏️ Fixed README.  

- **0.0.5.2** – *(27/07/2025)*  
  ✏️ Fixed README.  

- **0.0.5.1** – *(27/07/2025)*  
  🆕 Updated `teen_code_yahoo`.  

- **0.0.5.0** – *(26/07/2025)*  
  ❌ Removed `an_ky_tu`.  

---

### 📌 2024

- **0.0.4.1** – *(17/10/2024)*  
  🆕 Added `tạo_dãy_chữ`.  
  🔄 Updated `one_two_three`.  

- **0.0.4.0** – *(05/05/2024)*  
  ✏️ Fixed README.  

- **0.0.3.9** – *(05/05/2024)*  
  ✏️ Fixed README.  

- **0.0.3.8** – *(05/05/2024)*  
  🎄 Updated `mp_christmas_tree_cho_VSCode` and `mp_christmas_tree_cho_TEXT`.  

- **0.0.3.7** – *(04/05/2024)*  
  🎄 Updated `mp_christmas_tree`.  

- **0.0.3.6** – *(03/03/2024)*  
  🧪 Testing phase.  

- **0.0.3.5** – *(01/03/2024)*  
  🧪 Testing phase.  

- **0.0.3.4** – *(26/02/2024)*  
  ➕ Added `uoc_chung_cua_danh_sach`.  

- **0.0.3.3** – *(21/02/2024)*  
  🔧 Enhanced README and library metadata.  

- **0.0.3.2** – *(20/02/2024)*  
  ➕ Added abundant number check.  

- **0.0.3.1** – *(20/02/2024)*  
  🔧 Enhanced library information.  

- **0.0.3** – *(20/02/2024)*  
  ➕ Added `xau_ki_tu_khong_trung_lap`.  
  ❌ Removed `ki_tu_trung_lap`.  

- **0.0.2.10** – *(19/02/2024)*  
  🔧 Enhanced README.  

- **0.0.2.9** – *(19/02/2024)*  
  🧪 Testing phase.  

- **0.0.2.8** – *(19/02/2024)*  
  🧪 Testing phase.  

- **0.0.2.7** – *(18/02/2024)*  
  🔧 Enhanced README.  

- **0.0.2.6** – *(18/02/2024)*  
  ⚖️ Switched to **MIT License**.  

- **0.0.2.4** → **0.0.2.5** – *(18/02/2024)*  
  🔧 Enhanced README.  

- **0.0.2.3** – *(18/02/2024)*  
  🧪 Testing phase.  

- **0.0.2.1** → **0.0.2.2** – *(14/02/2024)*  
  🧪 Testing phase.  

- **0.0.2** – *(14/02/2024)*  
  🐞 Fixed missing dependency.  

- **0.0.1.1** → **0.0.1.2** – *(14/02/2024)*  
  🧪 Testing phase.  

- **0.0.1** – *(14/02/2024)*  
  🎉 Initial release!  

- **0.0.0.1** – *(14/02/2024)*  
  🧪 Testing phase.  

---