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
- **numpy**: Optional for `solve_equation` and `generate_prime_list`. Install via `pip install pchjlib[numpy]` or `pip install numpy`.
- **gmpy2**: Optional for big integer support in future features.

## 🛠️ Installation

Install the core library without optional dependencies:

**Note**: *Run `pchj-icon` to download icon (logo) for the library in `site-pakages`.*
```bash
pip install pchjlib
pchj-icon
```

To enable `solve_equation` and `generate_prime_list`, include `numpy`:

```bash
pip install pchjlib[numpy]
```

---

## 🌟 Key Features

- 🔍 **Special Number Checking and Generation**: Supports prime, emirp, Fibonacci, perfect, narcissistic, amicable, square, strong, twin prime, abundant, and happy numbers.
- 🔗 **Divisor and Multiple Operations**: Generate divisor lists, compute GCD, LCM, and perform prime factorization.
- 🧮 **Equation Solving**: Solves polynomial equations of any degree using `numpy`.
- 🧹 **List and String Processing**: Remove duplicates, extract digits/numbers/characters, and compress/decompress strings.
- 🔐 **Encryption and Decryption**: Implements Caesar cipher (for educational use only).
- ✨ **Special Calculations**: Includes electricity bill calculation, largest number with a given digit sum, sequence generation, and inversion counting.

## 📚 Table of Contents

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

### 🔢 Prime and Related Number Functions

- **is_prime(number)**  
  Checks if a number is prime.  
  - **Parameter**: `number` (int)  
  - **Returns**: `True` if prime, `False` otherwise.  
  - **Raises**: `InvalidInputError` if not an integer.  
  - **Example**: `is_prime(7)` → `True`

- **generate_prime_list(limit)**  
  Generates primes from 0 to `limit` using the Sieve algorithm.  
  - **Parameter**: `limit` (int)  
  - **Returns**: List of primes.  
  - **Raises**: `InvalidInputError` if `limit` < 2 or not an integer; `ImportError` if `numpy` is missing.  
  - **Example**: `generate_prime_list(10)` → `[2, 3, 5, 7]`

- **is_emirp(number)**  
  Checks if a number is an emirp (prime with prime reverse).  
  - **Parameter**: `number` (int)  
  - **Returns**: `True` if emirp, `False` otherwise.  
  - **Raises**: `InvalidInputError` if not a positive integer >= 2.  
  - **Example**: `is_emirp(31)` → `True`

- **generate_emirp_list(limit)**  
  Generates emirp numbers from 2 to `limit`.  
  - **Parameter**: `limit` (int)  
  - **Returns**: List of emirp numbers.  
  - **Raises**: `InvalidInputError` if `limit` < 2 or not an integer.

---

### 🌀 Fibonacci Functions

- **fibonacci_at_index(index)**  
  Calculates the Fibonacci number at a given index with caching.  
  - **Parameter**: `index` (int)  
  - **Returns**: Fibonacci number.  
  - **Raises**: `InvalidInputError` if not a non-negative integer.  
  - **Example**: `fibonacci_at_index(5)` → `5`

- **generate_fibonacci_list(count)**  
  Generates the first `count` Fibonacci numbers.  
  - **Parameter**: `count` (int)  
  - **Returns**: List of Fibonacci numbers.  
  - **Raises**: `InvalidInputError` if not a non-negative integer.

---

### 🧠 Perfect, Narcissistic, Amicable, and Happy Number Functions

- **sum_of_divisors(number)**  
  Computes the sum of positive divisors (excluding itself).  
  - **Parameter**: `number` (int)  
  - **Returns**: Sum of divisors.  
  - **Raises**: `InvalidInputError` if not a positive integer.

- **sum_of_digits(number)**  
  Calculates the sum of a number's digits.  
  - **Parameter**: `number` (int)  
  - **Returns**: Sum of digits.  
  - **Raises**: `InvalidInputError` if not an integer.

- **is_perfect_number(number)**  
  Checks if a number is perfect.  
  - **Parameter**: `number` (int)  
  - **Returns**: `True` if perfect, `False` otherwise.  
  - **Raises**: `InvalidInputError` if not a positive integer.

- **generate_perfect_number_list(limit)**  
  Generates perfect numbers from 1 to `limit`.  
  - **Parameter**: `limit` (int)  
  - **Returns**: List of perfect numbers.  
  - **Raises**: `InvalidInputError` if not a positive integer.

- **is_narcissistic_number(number)**  
  Checks if a number is narcissistic.  
  - **Parameter**: `number` (int)  
  - **Returns**: `True` if narcissistic, `False` otherwise.  
  - **Raises**: `InvalidInputError` if not a non-negative integer.

- **generate_narcissistic_number_list(limit)**  
  Generates narcissistic numbers from 0 to `limit`.  
  - **Parameter**: `limit` (int)  
  - **Returns**: List of narcissistic numbers.  
  - **Raises**: `InvalidInputError` if not a non-negative integer.

- **are_amicable_numbers(number1, number2)**  
  Checks if two numbers are amicable.  
  - **Parameters**: `number1`, `number2` (int)  
  - **Returns**: `True` if amicable, `False` otherwise.  
  - **Raises**: `InvalidInputError` if not positive integers.

- **is_happy_number(number)**  
  Checks if a number is happy.  
  - **Parameter**: `number` (int)  
  - **Returns**: `True` if happy, `False` otherwise.  
  - **Raises**: `InvalidInputError` if not a positive integer.

- **generate_happy_number_list(limit)**  
  Generates happy numbers from 1 to `limit`.  
  - **Parameter**: `limit` (int)  
  - **Returns**: List of happy numbers.  
  - **Raises**: `InvalidInputError` if not a positive integer.

---

### 📐 Square, Strong, and Friendly Number Functions

- **is_square_number(number)**  
  Checks if a number is a perfect square.  
  - **Parameter**: `number` (int)  
  - **Returns**: `True` if square, `False` otherwise.  
  - **Raises**: `InvalidInputError` if not a non-negative integer.

- **generate_square_number_list(limit)**  
  Generates square numbers from 0 to `limit`.  
  - **Parameter**: `limit` (int)  
  - **Returns**: List of square numbers.  
  - **Raises**: `InvalidInputError` if not a non-negative integer.

- **are_friendly_numbers(number1, number2)**  
  Checks if two numbers are friendly.  
  - **Parameters**: `number1`, `number2` (int)  
  - **Returns**: `True` if friendly, `False` otherwise.  
  - **Raises**: `InvalidInputError` if not positive integers.

- **is_strong_number(number, variant=1)**  
  Checks if a number is strong based on the variant.  
  - **Parameters**: `number` (int), `variant` (int)  
  - **Returns**: `True` if strong, `False` otherwise.  
  - **Raises**: `InvalidInputError` if not a non-negative integer or invalid variant.

---

### 📊 Divisor and Multiple Functions

- **generate_divisor_list(number, positive_only=True)**  
  Generates divisors of a number.  
  - **Parameters**: `number` (int), `positive_only` (bool)  
  - **Returns**: List of divisors.  
  - **Raises**: `InvalidInputError` if not an integer or zero.

- **generate_multiple_list(number, limit, positive_only=True)**  
  Generates multiples of a number up to `limit` times.  
  - **Parameters**: `number` (int), `limit` (int), `positive_only` (bool)  
  - **Returns**: List of multiples.  
  - **Raises**: `InvalidInputError` if not integers, number is zero, or limit < 1.

- **common_divisors(numbers)**  
  Generates common divisors for a list of numbers.  
  - **Parameter**: `numbers` (list)  
  - **Returns**: List of common divisors.  
  - **Raises**: `InvalidInputError` if not a list or contains non-integers; `MathError` if fewer than 2 non-zero elements.

- **greatest_common_divisor(numbers)**  
  Computes the GCD of a list of numbers.  
  - **Parameter**: `numbers` (list)  
  - **Returns**: GCD value.  
  - **Raises**: `InvalidInputError` if not a list or contains non-integers; `MathError` if fewer than 2 non-zero elements.

- **least_common_multiple(numbers)**  
  Computes the LCM of a list of numbers.  
  - **Parameter**: `numbers` (list)  
  - **Returns**: LCM value.  
  - **Raises**: `InvalidInputError` if not a list, contains non-integers, or zeros; `MathError` if fewer than 2 elements.

---

### 👯 Twin Prime and Abundant Number Functions

- **is_twin_prime(number)**  
  Checks if a number is a twin prime.  
  - **Parameter**: `number` (int)  
  - **Returns**: `True` if twin prime, `False` otherwise.  
  - **Raises**: `InvalidInputError` if not an integer.

- **generate_twin_prime_list(limit)**  
  Generates twin primes from 2 to `limit`.  
  - **Parameter**: `limit` (int)  
  - **Returns**: List of twin primes.  
  - **Raises**: `InvalidInputError` if not an integer >= 2.

- **is_abundant_number(number)**  
  Checks if a number is abundant.  
  - **Parameter**: `number` (int)  
  - **Returns**: `True` if abundant, `False` otherwise.  
  - **Raises**: `InvalidInputError` if not a positive integer.

- **generate_abundant_number_list(limit)**  
  Generates abundant numbers from 1 to `limit`.  
  - **Parameter**: `limit` (int)  
  - **Returns**: List of abundant numbers.  
  - **Raises**: `InvalidInputError` if not a positive integer.

---

### 🔍 Prime Factorization Functions

- **prime_factors(number)**  
  Factorizes a number into prime factors.  
  - **Parameter**: `number` (int)  
  - **Returns**: List of prime factors.  
  - **Raises**: `InvalidInputError` if not a positive integer > 1.

- **greatest_common_prime_divisor(number1, number2)**  
  Finds the greatest common prime divisor of two numbers.  
  - **Parameters**: `number1`, `number2` (int)  
  - **Returns**: Greatest common prime divisor.  
  - **Raises**: `InvalidInputError` if not positive integers > 1; `MathError` if no common prime divisor.

---

### 🧮 Equation Solving Functions

- **solve_equation(degree, coefficients)**  
  Solves polynomial equations of any degree using `numpy`.  
  - **Parameters**: `degree` (int), `coefficients` (list)  
  - **Returns**: String describing the roots.  
  - **Raises**: `ImportError` if `numpy` is missing; `InvalidInputError` if inputs are invalid.  
  - **Example**:  
    ```python
    solve_equation(2, [1, -3, 2])  # For x² - 3x + 2 = 0
    ```
    Output:
    ```
    Roots of the equation:
    Real roots:
    x1 = 2.0
    x2 = 1.0
    ```

---

### 🧵 List and String Processing Functions

- **remove_duplicates(items)**  
  Removes duplicates from a list and sorts in descending order.  
  - **Parameter**: `items` (list)  
  - **Returns**: Sorted list without duplicates.  
  - **Raises**: `InvalidInputError` if not a list/tuple.

- **extract_digits_from_string(text)**  
  Extracts individual digits from a string.  
  - **Parameter**: `text` (str)  
  - **Returns**: List of digits.  
  - **Example**: `extract_digits_from_string("abc123")` → `[1, 2, 3]`

- **extract_numbers_from_string(text)**  
  Extracts full numbers from a string.  
  - **Parameter**: `text` (str)  
  - **Returns**: List of numbers.  
  - **Example**: `extract_numbers_from_string("abc123def456")` → `[123, 456]`

- **extract_characters(text)**  
  Extracts non-digit characters from a string.  
  - **Parameter**: `text` (str)  
  - **Returns**: List of characters.  
  - **Example**: `extract_characters("a1b2c3")` → `['a', 'b', 'c']`

- **compress_string(text, compress_type)**  
  Compresses a string using two methods.  
  - **Parameters**: `text` (str), `compress_type` (int)  
  - **Returns**: Compressed string.  
  - **Example (type 1)**: `compress_string("google", 1)` → `"2o2gle"`  
  - **Example (type 2)**: `compress_string("google", 2)` → `"g2ogle"`

- **compress_string_without_numbers(input_text)**  
  Compresses a string by removing consecutive duplicates.  
  - **Parameter**: `input_text` (str)  
  - **Returns**: Compressed string.  
  - **Example**: `compress_string_without_numbers("hhhoocssssiiinnnhhhhh")` → `"hocsinh"`

- **decompress_string(text)**  
  Decompresses a string with numeric counts.  
  - **Parameter**: `text` (str)  
  - **Returns**: Decompressed string.  
  - **Example**: `decompress_string("g2ogle")` → `"google"`

- **unique_characters_string(text)**  
  Creates a string with unique characters in order of appearance.  
  - **Parameter**: `text` (str)  
  - **Returns**: String with no duplicates.  
  - **Example**: `unique_characters_string("google")` → `"gole"`

---

### 🏛️ Caesar Cipher Functions

- **caesar_cipher_to_numbers(text, shift)**  
  Converts a string to a list of Caesar cipher numbers.  
  - **Parameters**: `text` (str), `shift` (int)  
  - **Returns**: List of shifted numbers.  
  - **Example**: `caesar_cipher_to_numbers("ABC", 3)` → `[3, 4, 5]`

- **caesar_cipher_from_numbers(numbers, shift)**  
  Decodes a list of Caesar cipher numbers into a string.  
  - **Parameters**: `numbers` (list), `shift` (int)  
  - **Returns**: Decoded string.  
  - **Example**: `caesar_cipher_from_numbers([3, 4, 5], 3)` → `"ABC"`

---

### 💥 Special Calculation Functions

- **calculate_electricity_bill_Vietnamese(old_reading, new_reading)**  
  Calculates an electricity bill based on Vietnamese pricing tiers.  
  - **Parameters**: `old_reading`, `new_reading` (float)  
  - **Returns**: String with consumption and cost.  
  - **Example**: `calculate_electricity_bill_Vietnamese(100, 150)` → `"- Electricity consumed this month: 50.0 Kwh\n- Electricity bill this month: 83900.0 VND"`

- **largest_number_with_digit_sum(digit_count, target_sum)**  
  Finds the largest number with `digit_count` digits summing to `target_sum`.  
  - **Parameters**: `digit_count` (int), `target_sum` (int)  
  - **Returns**: Largest number as a string.  
  - **Example**: `largest_number_with_digit_sum(3, 5)` → `"500"`

---

### 🔁 Sequence Generation Functions

- **generate_sequence_rule_1(number)**  
  Generates a sequence based on a specific rule.  
  - **Parameter**: `number` (int)  
  - **Returns**: List of sequence numbers.  
  - **Example**: `generate_sequence_rule_1(5)` → `[1, 3, 6, 10, 15]`

- **generate_sequence_rule_2(base, count)**  
  Generates `count` multiples of `base`.  
  - **Parameters**: `base` (int), `count` (int)  
  - **Returns**: List of multiples.  
  - **Example**: `generate_sequence_rule_2(3, 4)` → `[0, 3, 6, 9]`

- **generate_sequence_rule_3(count, base)**  
  Generates powers of `base` from 0 to `count-1`.  
  - **Parameters**: `count` (int), `base` (int)  
  - **Returns**: List of powers.  
  - **Example**: `generate_sequence_rule_3(4, 2)` → `[1, 2, 4, 8]`

---

### 🔢 Inversion Counting Functions

- **count_inversions(numbers)**  
  Counts the number of inversions in a list.  
  - **Parameter**: `numbers` (list)  
  - **Returns**: Number of inversions.  
  - **Example**: `count_inversions([3, 1, 2])` → `1`

---

## 🛠️ Update History

> **📅 Latest Update:** 04/08/2025  
> **📦 Total Releases:** 61

### 📌 2025
- **1.1.1** – *(04/08/2025)*  
  🔧 Fixed minor bugs.  

- **1.1.0** – *(04/08/2025)*  
  ✅ Add a logo to the library when running `pip install pchjlib` and running the command `pchj-icon` right after.

- **1.0.2** – *(04/08/2025)*  
  🔧 Fixed minor bugs.  

- **1.0.1** – *(04/08/2025)*  
  ✅ Enhanced `main` allows for expanded function usage.

- **1.0.0** – *(03/08/2025)*  
  🚀 **Major Update**:  
  - **Performance Optimization**:  
    - Added caching to `fibonacci_at_index` to improve speed for large indices.  
    - Optimized `is_emirp` by using arithmetic operations instead of string conversion.  
    - Reduced complexity of `is_strong_number` (variant = 2) by checking only necessary prime factors.
  - **Improved Error Handling**:
    - More specific error messages (e.g., "Input must be a positive integer" instead of generic "Invalid input").
    - Enhanced boundary checks across all functions for robustness.
  - **Documentation Updates**:
    - Added complex examples for `solve_equation` (e.g., solving quadratic equations with real and complex roots) and string processing functions (e.g., compressing/decompressing strings).
    - Provided clear guidance on using the library without `numpy` (e.g., skipping `solve_equation` and `generate_prime_list`).
  - **Unit Testing**:
    - Implemented unit tests to ensure function correctness and detect bugs early during updates.
  - **Feature Expansion**:
    - Prepared support for big integers using `gmpy2` to handle numbers exceeding Python's int limits (to be fully implemented in future releases).
    - Added groundwork for advanced algorithms like Mersenne prime detection and Carmichael number identification (planned for future updates).
  - **README Enhancements**:
    - Updated with detailed examples and improved installation instructions.
    - Removed references to deprecated functions for clarity.

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