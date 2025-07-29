################################################################################################
#                                                                                              #
# Copyright (c) 2024 Joesifer                                                                  #
#                                                                                              #
# MIT License                                                                                  #
#                                                                                              #
# Permission is hereby granted, free of charge, to any person obtaining a copy                 #
# of this software and associated documentation files (the "Software"), to deal                #
# in the Software without restriction, including without limitation the rights                 #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell                    #
# copies of the Software, and to permit persons to whom the Software is                        #
# furnished to do so, subject to the following conditions:                                     #
#                                                                                              #
# The above copyright notice and this permission notice shall be included in all               #
# copies or substantial portions of the Software.                                              #
#                                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR                   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,                     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE                  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,                #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE                #
# SOFTWARE.                                                                                    #
#                                                                                              #
################################################################################################

"""
PCHJLIB
===========
---------------------------------------------------------
Tác giả
---------------------------------------------------------
- Joesifer.

Phiên bản
---------------------------------------------------------
- 0.1.0.5.

Ngày đăng
---------------------------------------------------------
- Ngày 14 tháng Hai, năm 2024.

Bản quyền
---------------------------------------------------------
- Copyright (c) 2024 Joesifer.

Phiên bản python được hỗ trợ.
---------------------------------------------------------
- Lớn hơn hoặc bằng 3.7.

Thư viện phụ thuộc.
---------------------------------------------------------
- math, re, sys, time, numpy, roman.

Giấy phép.
---------------------------------------------------------
- MIT License.

Thông tin.
---------------------------------------------------------

Nếu bạn không biết cách dùng thì hãy::

  >>> Truy cập: `https://github.com/Joesifer/pchjlib/blob/main/README.md` .

Và bạn có thể góp ý hoặc ủng hộ bằng::

  >>> Gửi email : `phanchanhung12055@gmail.com` .


CẢM ƠN!
================================

"""

import math, random, re, sys, time, numpy, roman


# Các class lỗi tùy chỉnh
class MathError(Exception):
    """Lỗi cơ bản liên quan đến toán học."""

    pass


class OutOfRangeError(MathError):
    """Lỗi khi giá trị nằm ngoài phạm vi cho phép."""

    pass


class NotIntegerError(MathError):
    """Lỗi khi giá trị không phải số nguyên."""

    pass


class InvalidInputError(MathError):
    """Lỗi khi đầu vào không hợp lệ."""

    pass


# Các hàm kiểm tra số nguyên tố và số liên quan
def kiem_tra_so_nguyen_to(number):
    """
    Kiểm tra xem một số có phải là số nguyên tố hay không.

    Thông số:
        number (int): Số cần kiểm tra.

    Trả lại:
        bool: True nếu number là số nguyên tố, False nếu không.

    Raises:
        InvalidInputError: Nếu number không phải số nguyên.
    """
    if not isinstance(number, int):
        raise InvalidInputError("Đầu vào phải là số nguyên")
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def tao_danh_sach_so_nguyen_to(limit):
    """
    Tạo danh sách các số nguyên tố từ 0 đến limit.

    Thông số:
        limit (int): Giới hạn trên của danh sách.

    Trả lại:
        list: Danh sách các số nguyên tố.
    """
    if limit < 5:
        limit = 10
    return [i for i in range(limit) if kiem_tra_so_nguyen_to(i)]


def kiem_tra_so_emirp(number):
    """
    Kiểm tra xem một số có phải là số emirp hay không.

    Thông số:
        number (int): Số cần kiểm tra.

    Trả lại:
        bool: True nếu number là số emirp, False nếu không.
    """
    if kiem_tra_so_nguyen_to(number):
        reversed_number = int(str(number)[::-1])
        return number != reversed_number and kiem_tra_so_nguyen_to(reversed_number)
    return False


def tao_danh_sach_so_emirp(limit):
    """
    Tạo danh sách các số emirp từ 0 đến limit.

    Thông số:
        limit (int): Giới hạn trên của danh sách.

    Trả lại:
        list: Danh sách các số emirp.
    """
    return [i for i in range(limit) if kiem_tra_so_emirp(i)]


# Các hàm Fibonacci
def vi_tri_so_Fibonacci(index, memo={0: 0, 1: 1}):
    """
    Tính số Fibonacci thứ index bằng cách sử dụng memoization.

    Thông số:
        index (int): Vị trí của số Fibonacci.
        memo (dict, optional): Từ điển lưu các giá trị đã tính.

    Trả lại:
        int: Số Fibonacci thứ index.
    """
    if index not in memo:
        memo[index] = vi_tri_so_Fibonacci(index - 1, memo) + vi_tri_so_Fibonacci(
            index - 2, memo
        )
    return memo[index]


def tao_danh_sach_so_Fibonacci(count):
    """
    Tạo danh sách các số Fibonacci với count phần tử.

    Thông số:
        count (int): Số lượng phần tử trong danh sách.

    Trả lại:
        list: Danh sách các số Fibonacci.
    """
    return [vi_tri_so_Fibonacci(i) for i in range(count)]


# Các hàm tính số hoàn thiện, tự mãn, hữu hảo, hoàn hào, thân thiết
def tong_uoc_so(number):
    """
    Tính tổng các ước số dương của number (không tính number).

    Thông số:
        number (int): Số cần tính tổng ước số.

    Trả lại:
        int: Tổng các ước số của number.

    Raises:
        MathError: Nếu number không lớn hơn 0.
    """
    if number <= 0:
        raise MathError("Số phải lớn hơn 0")
    return sum(i for i in range(1, number) if number % i == 0)


def tong_chu_so(number):
    """
    Tính tổng các chữ số của một số.

    Thông số:
        number (int): Số cần tính tổng chữ số.

    Trả lại:
        int: Tổng các chữ số của number.
    """
    return sum(int(digit) for digit in str(abs(number)))


def kiem_tra_so_hoan_thien(number):
    """
    Kiểm tra xem một số có phải là số hoàn thiện hay không.

    Thông số:
        number (int): Số cần kiểm tra.

    Trả lại:
        bool: True nếu number là số hoàn thiện, False nếu không.

    Raises:
        MathError: Nếu number không lớn hơn 0.
    """
    if number < 1:
        raise MathError("Số phải lớn hơn 0")
    return tong_uoc_so(number) == number


def tao_danh_sach_so_hoan_thien(limit):
    """
    Tạo danh sách các số hoàn thiện từ 0 đến limit.

    Thông số:
        limit (int): Giới hạn trên của danh sách.

    Trả lại:
        list: Danh sách các số hoàn thiện.
    """
    return [i for i in range(1, limit + 1) if kiem_tra_so_hoan_thien(i)]


def kiem_tra_so_tu_man(number):
    """
    Kiểm tra xem một số có phải là số tự mãn hay không.

    Thông số:
        number (int): Số cần kiểm tra.

    Trả lại:
        bool: True nếu number là số tự mãn, False nếu không.
    """
    if number < 0:
        return False
    return sum(int(digit) ** 3 for digit in str(number)) == number


def tao_danh_sach_so_tu_man(limit):
    """
    Tạo danh sách các số tự mãn từ 0 đến limit.

    Thông số:
        limit (int): Giới hạn trên của danh sách.

    Trả lại:
        list: Danh sách các số tự mãn.
    """
    return [i for i in range(2, limit) if kiem_tra_so_tu_man(i)]


def cap_so_hua_hon(number1, number2):
    """
    Kiểm tra xem hai số có phải là cặp số hữu hảo hay không.

    Thông số:
        number1 (int): Số thứ nhất.
        number2 (int): Số thứ hai.

    Trả lại:
        bool: True nếu number1 và number2 là cặp số hữu hảo, False nếu không.

    Raises:
        MathError: Nếu các số âm.
    """
    if number1 < 0 or number2 < 0:
        raise MathError("Các số phải không âm")
    return tong_uoc_so(number1) == number2 + 1 and tong_uoc_so(number2) == number1 + 1


def kiem_tra_so_hoan_hao(number):
    """
    Kiểm tra xem một số có phải là số hoàn hảo hay không.

    Thông số:
        number (int): Số cần kiểm tra.

    Trả lại:
        bool: True nếu number là số hoàn hảo, False nếu không.

    Raises:
        MathError: Nếu number không lớn hơn 0.
    """
    if number < 1:
        raise MathError("Số phải lớn hơn 0")
    return sum(i for i in range(1, number) if number % i == 0) == number


def tao_danh_sach_so_hoan_hao(limit):
    """
    Tạo danh sách các số hoàn hảo từ 0 đến limit.

    Thông số:
        limit (int): Giới hạn trên của danh sách.

    Trả lại:
        list: Danh sách các số hoàn hảo.
    """
    return [i for i in range(1, limit) if kiem_tra_so_hoan_hao(i)]


# Các hàm số chính phương, mạnh mẽ, thân thiết
def kiem_tra_so_chinh_phuong(number):
    """
    Kiểm tra xem một số có phải là số chính phương hay không.

    Thông số:
        number (int): Số cần kiểm tra.

    Trả lại:
        bool: True nếu number là số chính phương, False nếu không.
    """
    if number < 0:
        return False
    sqrt_number = int(math.sqrt(number))
    return sqrt_number * sqrt_number == number


def tao_danh_sach_so_chinh_phuong(limit):
    """
    Tạo danh sách các số chính phương từ 0 đến limit.

    Thông số:
        limit (int): Giới hạn trên của danh sách.

    Trả lại:
        list: Danh sách các số chính phương.
    """
    return [i for i in range(limit) if kiem_tra_so_chinh_phuong(i)]


def cap_so_than_thiet(number1, number2):
    """
    Kiểm tra xem hai số có phải là cặp số thân thiết hay không.

    Thông số:
        number1 (int): Số thứ nhất.
        number2 (int): Số thứ hai.

    Trả lại:
        bool: True nếu number1 và number2 là cặp số thân thiết, False nếu không.

    Raises:
        MathError: Nếu các số không lớn hơn 1.
    """
    if number1 <= 1 or number2 <= 1:
        raise MathError("Các số phải lớn hơn 1")
    return tong_uoc_so(number1) == number2 and tong_uoc_so(number2) == number1


def kiem_tra_so_manh_me_1(number):
    """
    Kiểm tra xem một số có phải là số mạnh mẽ (tổng chữ số là nguyên tố) hay không.

    Thông số:
        number (int): Số cần kiểm tra.

    Trả lại:
        bool: True nếu number là số mạnh mẽ, False nếu không.
    """
    if number < 0:
        return False
    return kiem_tra_so_nguyen_to(tong_chu_so(number))


def kiem_tra_so_manh_me_2(number):
    """
    Kiểm tra xem một số có phải là số mạnh mẽ loại 2 hay không.

    Thông số:
        number (int): Số cần kiểm tra.

    Trả lại:
        bool: True nếu number là số mạnh mẽ loại 2, False nếu không.
    """
    if number < 0:
        return False
    prime_list = [i for i in range(2, number) if kiem_tra_so_nguyen_to(i)]
    for prime in prime_list:
        if number % prime == 0 and number % (prime**2) == 0:
            return True
    return False


# Các hàm về ước số và bội số
def tao_danh_sach_uoc_so(number):
    """
    Tạo danh sách các ước số của number.

    Thông số:
        number (int): Số cần tạo danh sách ước số.

    Trả lại:
        list: Danh sách các ước số của number.

    Raises:
        MathError: Nếu number là 0.
    """
    if number == 0:
        raise MathError("Không thể tạo danh sách ước số cho 0")
    number = abs(number)
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return sorted(divisors + [-i for i in divisors])


def uoc_chung_lon_nhat(number1, number2):
    """
    Tìm ước chung lớn nhất của hai số.

    Thông số:
        number1 (int): Số thứ nhất.
        number2 (int): Số thứ hai.

    Trả lại:
        int: Ước chung lớn nhất của number1 và number2.
    """
    return math.gcd(number1, number2)


def uoc_chung_lon_nhat_cua_danh_sach(numbers):
    """
    Tính ước chung lớn nhất của một danh sách các số.

    Thông số:
        numbers (list): Danh sách các số.

    Trả lại:
        int: Ước chung lớn nhất của danh sách.

    Raises:
        MathError: Nếu danh sách không hợp lệ.
    """
    if len(numbers) < 2 or 0 in numbers:
        raise MathError("Danh sách không hợp lệ")
    result = numbers[0]
    for num in numbers[1:]:
        result = uoc_chung_lon_nhat(result, num)
        if result == 1:
            break
    return result


def boi_chung_nho_nhat(number1, number2):
    """
    Tính bội chung nhỏ nhất của hai số.

    Thông số:
        number1 (int): Số thứ nhất.
        number2 (int): Số thứ hai.

    Trả lại:
        int: Bội chung nhỏ nhất của number1 và number2.
    """
    return math.lcm(number1, number2)


def boi_chung_nho_nhat_cua_danh_sach(numbers):
    """
    Tính bội chung nhỏ nhất của một danh sách các số.

    Thông số:
        numbers (list): Danh sách các số.

    Trả lại:
        int: Bội chung nhỏ nhất của danh sách.

    Raises:
        MathError: Nếu danh sách không hợp lệ.
    """
    if len(numbers) < 2 or 0 in numbers:
        raise MathError("Danh sách không hợp lệ")
    result = numbers[0]
    for num in numbers[1:]:
        result = boi_chung_nho_nhat(result, num)
    return result


def tao_danh_sach_boi_so(number):
    """
    Tạo danh sách bội số của number từ 0 đến 10 lần.

    Thông số:
        number (int): Số cần tạo danh sách bội số.

    Trả lại:
        list: Danh sách bội số của number.

    Raises:
        MathError: Nếu number là 0.
    """
    if number == 0:
        raise MathError("Không thể tạo danh sách bội số cho 0")
    return [number * i for i in range(11)]


def uoc_chung_cua_danh_sach(numbers):
    """
    Tạo danh sách các ước chung của một danh sách các số.

    Thông số:
        numbers (list): Danh sách các số.

    Trả lại:
        list: Danh sách các ước chung.

    Raises:
        MathError: Nếu danh sách không đủ phần tử.
    """

    def get_divisors(n):
        if n == 0:
            return {1}
        n = abs(n)
        return set(
            [i for i in range(1, n + 1) if n % i == 0]
            + [-i for i in range(1, n + 1) if n % i == 0]
        )

    if len(numbers) < 2:
        raise MathError("Danh sách phải có ít nhất 2 phần tử")
    result = get_divisors(numbers[0])
    for num in numbers[1:]:
        result = result.intersection(get_divisors(num))
    return sorted(list(result))


# Các hàm số song tố và số phong phú
def kiem_tra_so_song_to(number):
    """
    Kiểm tra xem một số có phải là số song tố hay không.

    Thông số:
        number (int): Số cần kiểm tra.

    Trả lại:
        bool: True nếu number là số song tố, False nếu không.
    """
    return kiem_tra_so_nguyen_to(number) and kiem_tra_so_nguyen_to(tong_chu_so(number))


def tao_danh_sach_so_song_to(limit):
    """
    Tạo danh sách các số song tố từ 0 đến limit.

    Thông số:
        limit (int): Giới hạn trên của danh sách.

    Trả lại:
        list: Danh sách các số song tố.
    """
    return [i for i in range(limit) if kiem_tra_so_song_to(i)]


def kiem_tra_so_phong_phu(number):
    """
    Kiểm tra xem một số có phải là số phong phú hay không.

    Thông số:
        number (int): Số cần kiểm tra.

    Trả lại:
        bool: True nếu number là số phong phú, False nếu không.
    """
    if number <= 0:
        return False
    return sum(i for i in range(1, number) if number % i == 0) > number


def tao_danh_sach_so_phong_phu(limit):
    """
    Tạo danh sách các số phong phú từ 0 đến limit.

    Thông số:
        limit (int): Giới hạn trên của danh sách.

    Trả lại:
        list: Danh sách các số phong phú.
    """
    return [i for i in range(limit) if kiem_tra_so_phong_phu(i)]


def thua_so_nguyen_to(number):
    """
    Phân tích một số thành danh sách các thừa số nguyên tố.

    Thông số:
        number (int): Số cần phân tích.

    Trả lại:
        list: Danh sách các thừa số nguyên tố.

    Raises:
        MathError: Nếu number không lớn hơn 1.
    """
    if number <= 1:
        raise MathError("Số phải lớn hơn 1")
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors


def uoc_chung_nguyen_to_2_so(number1, number2):
    """
    Tìm ước chung nguyên tố lớn nhất của hai số.

    Thông số:
        number1 (int): Số thứ nhất.
        number2 (int): Số thứ hai.

    Trả lại:
        int: Ước chung nguyên tố lớn nhất của number1 và number2.

    Raises:
        MathError: Nếu các số không lớn hơn 1 hoặc không có ước chung nguyên tố.
    """
    if number1 <= 1 or number2 <= 1:
        raise MathError("Các số phải lớn hơn 1")
    factors1 = set(thua_so_nguyen_to(number1))
    factors2 = set(thua_so_nguyen_to(number2))
    common_factors = factors1.intersection(factors2)
    if not common_factors:
        raise MathError("Không có ước chung nguyên tố")
    return max(common_factors)


# Hàm giải phương trình
def giai_phuong_trinh(degree, coefficients):
    """
    Giải phương trình từ bậc 1 đến bậc 10 theo hệ số.

    Thông số:
        degree (int): Bậc của phương trình.
        coefficients (list): Danh sách các hệ số của phương trình.

    Trả lại:
        str: Kết quả nghiệm của phương trình.

    Raises:
        InvalidInputError: Nếu bậc hoặc hệ số không hợp lệ.
    """
    if degree < 1 or degree > 10:
        raise InvalidInputError("Bậc của phương trình phải từ 1 đến 10")
    if len(coefficients) != degree + 1:
        raise InvalidInputError(f"Phương trình bậc {degree} phải có {degree + 1} hệ số")

    roots = numpy.roots(coefficients)
    result = "Nghiệm của phương trình là:\n"
    for i, root in enumerate(roots, 1):
        result += f"x{i} = {root}\n"
    return result.strip()


# Các hàm xử lý danh sách và chuỗi
def danh_sach_khong_trung_lap(items):
    """
    Loại bỏ phần tử trùng lặp trong danh sách.

    Thông số:
        items (list): Danh sách cần xử lý.

    Trả lại:
        list: Danh sách không có phần tử trùng lặp.
    """
    return sorted(list(set(items)), reverse=True)


def trich_xuat_chu_so_tu_chuoi(text):
    """
    Trích xuất chuỗi chữ số từ chuỗi.

    Thông số:
        text (str): Chuỗi đầu vào.

    Trả lại:
        list: Danh sách các chữ số.
    """
    if not text:
        raise InvalidInputError("Chuỗi không thể rỗng")
    return [int(digit) for digit in re.findall(r"\d", text)]


def trich_xuat_so_tu_chuoi(text):
    """
    Trích xuất chuỗi số từ chuỗi.

    Thông số:
        text (str): Chuỗi đầu vào.

    Trả lại:
        list: Danh sách các số.
    """
    if not text:
        raise InvalidInputError("Chuỗi không thể rỗng")
    return [int(number) for number in re.findall(r"\d+", text)]


def trich_xuat_ki_tu(text):
    """
    Trích xuất các ký tự không phải số từ chuỗi.

    Thông số:
        text (str): Chuỗi đầu vào.

    Trả lại:
        list: Danh sách các ký tự không phải số.
    """
    if not text:
        raise InvalidInputError("Chuỗi không thể rỗng")
    return re.findall(r"\D", text)


def trich_xuat_cac_so_tu_so(text):
    """
    Trích xuất các số từ chuỗi số (ví dụ “32/232343244” → 32.232343244).

    Thông số:
        text (str): Chuỗi đầu vào.

    Trả lại:
        float: Số được trích xuất.

    Raises:
        InvalidInputError: Nếu chuỗi không hợp lệ.
    """
    if not text:
        raise InvalidInputError("Chuỗi không thể rỗng")
    numbers = re.findall(r"\d+", text)
    if not numbers:
        return 0.0
    if "." in text:
        return float(".".join(numbers))
    return float("".join(numbers))


def xau_duoc_nen_1(text):
    """
    Nén xâu loại 1 (ví dụ “google” → “2ol2ge”).

    Thông số:
        text (str): Chuỗi đầu vào.

    Trả lại:
        str: Chuỗi đã nén.
    """
    if not text:
        raise InvalidInputError("Chuỗi không thể rỗng")
    sorted_chars = sorted([char for char in text], reverse=True)
    result = ""
    count = 1
    for i in range(1, len(sorted_chars)):
        if sorted_chars[i] == sorted_chars[i - 1]:
            count += 1
        else:
            result += (
                str(count) + sorted_chars[i - 1] if count > 1 else sorted_chars[i - 1]
            )
            count = 1
    result += str(count) + sorted_chars[-1] if count > 1 else sorted_chars[-1]
    return result


def xau_duoc_nen_2(text):
    """
    Nén xâu loại 2 (ví dụ “google” → “g2ogle”).

    Thông số:
        text (str): Chuỗi đầu vào.

    Trả lại:
        str: Chuỗi đã nén.
    """
    if not text:
        raise InvalidInputError("Chuỗi không thể rỗng")
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


def xau_duoc_nen_khong_so(input_text):
    """
    Nén xâu bỏ số (ví dụ “hhhooccsiinh” → “hocsinh”).

    Thông số:
        input_text (str): Chuỗi đầu vào.

    Trả lại:
        str: Chuỗi đã nén.
    """
    if not input_text:
        raise InvalidInputError("Chuỗi không thể rỗng")
    result = input_text[0]
    for char in input_text[1:]:
        if char != result[-1]:
            result += char
    return result


def xau_duoc_giai_nen(text):
    """
    Giải nén xâu (ví dụ “3ab3c” → “aaabccc”).

    Thông số:
        text (str): Chuỗi đầu vào.

    Trả lại:
        str: Chuỗi đã giải nén.
    """
    if not text:
        raise InvalidInputError("Chuỗi không thể rỗng")
    result = ""
    count = ""
    for char in text:
        if char.isdigit():
            count += char
        else:
            result += char if count == "" else int(count) * char
            count = ""
    return result


def xau_ki_tu_khong_trung_lap(text):
    """
    Tạo xâu ký tự không trùng lặp (ví dụ “Google” → “gole”).

    Thông số:
        text (str): Chuỗi đầu vào.

    Trả lại:
        str: Chuỗi không có ký tự trùng lặp.
    """
    if not text:
        raise InvalidInputError("Chuỗi không thể rỗng")
    text = text.lower()
    unique_chars = ""
    for char in text:
        if char not in unique_chars:
            unique_chars += char
    return unique_chars


# Mật mã Caesar
def chuyen_hoa_caesar(text, shift):
    """
    Chuyển chuỗi thành dãy số mật mã Caesar.

    Thông số:
        text (str): Chuỗi đầu vào.
        shift (int): Số bước dịch chuyển.

    Trả lại:
        list: Dãy số mật mã Caesar.
    """
    if not text:
        raise InvalidInputError("Chuỗi không thể rỗng")
    text = "".join([char for char in text.upper() if char != " "]).strip()
    char_map = {chr(65 + i): i for i in range(26)}
    shifted_map = [(i + shift) % 26 for i in range(26)]
    return [shifted_map[char_map[char]] for char in text]


def ma_hoa_caesar(numbers, shift):
    """
    Mã hóa dãy số Caesar thành xâu.

    Thông số:
        numbers (list): Dãy số đầu vào.
        shift (int): Số bước dịch chuyển.

    Trả lại:
        str: Chuỗi đã mã hóa.
    """
    if not numbers:
        raise InvalidInputError("Danh sách không thể rỗng")
    char_map = {i: chr(65 + i) for i in range(26)}
    shifted_map = [(i + shift) % 26 for i in range(26)]
    reverse_map = {shifted_map[i]: i for i in range(26)}
    decoded = [reverse_map[num] for num in numbers]
    return "".join([char_map[i] for i in decoded])


# Teen Code Yahoo
def teen_code_yahoo(input_text):
    """
    Chuyển xâu thành Teen Code Yahoo.

    Thông số:
        input_text (str): Chuỗi đầu vào.

    Trả lại:
        str: Chuỗi Teen Code Yahoo.
    """

    teen_code_ya = {
        " ": " ",
        "a": "4",
        "á": "4'",
        "à": "4`",
        "ả": "4?",
        "ã": "4~",
        "ạ": "4.",
        "ă": "4",
        "ắ": "4'",
        "ằ": "4`",
        "ẳ": "4?",
        "ẵ": "4~",
        "ặ": "4.",
        "â": "4",
        "ấ": "4'",
        "ầ": "4`",
        "ẩ": "4?",
        "ẫ": "4~",
        "ậ": "4.",
        "e": "3",
        "é": "3'",
        "è": "3`",
        "ẻ": "3?",
        "ẽ": "3~",
        "ẹ": "3.",
        "ê": "3^",
        "ế": "3^'",
        "ề": "3^`",
        "ể": "3^?",
        "ễ": "3^~",
        "ệ": "3^.",
        "i": "!",
        "í": "!'",
        "ì": "!`",
        "ỉ": "!?",
        "ĩ": "!~",
        "ị": "!.",
        "o": "0",
        "ó": "0'",
        "ò": "0`",
        "ỏ": "0?",
        "õ": "0~",
        "ọ": "0.",
        "ô": "0^",
        "ố": "0^'",
        "ồ": "0^`",
        "ổ": "0^?",
        "ỗ": "0^~",
        "ộ": "0^.",
        "ơ": "0",
        "ớ": "0'",
        "ờ": "0`",
        "ở": "0?",
        "ỡ": "0~",
        "ợ": "0.'",
        "u": "⊔",
        "ú": "⊔'",
        "ù": "⊔`",
        "ủ": "⊔?",
        "ũ": "⊔~",
        "ụ": "⊔.",
        "ư": "⊔",
        "ứ": "⊔'",
        "ừ": "⊔`",
        "ử": "⊔?",
        "ữ": "⊔~",
        "ự": "⊔.",
        "y": "¥",
        "ý": "¥'",
        "ỳ": "¥`",
        "ỷ": "¥?",
        "ỹ": "¥~",
        "ỵ": "¥.",
        "b": "|3",
        "c": "©",
        "d": "|)",
        "đ": "+)",
        "g": "9",
        "h": "|-|",
        "k": "|<",
        "l": "1",
        "m": "|V|",
        "n": "π",
        "p": "|⁾",
        "q": "⁽|",
        "r": "Γ",
        "s": "∫",
        "t": "τ",
        "v": "√",
        "x": "⨉",
    }

    input_text = (str(input_text)).lower()
    change = []
    result = ""

    for i in range(len(list(input_text))):
        if input_text[i] in teen_code_ya:
            change.append(str(teen_code_ya[input_text[i]]))
        else:
            change.append(input_text[i])

    for i in change:
        result += i

    return result


# Các hàm mô phỏng chỉ với string
def mp_tai_xuong(steps):
    """
    Mô phỏng quá trình tải xuống.

    Thông số:
        steps (int): Số bước tải xuống.

    Raises:
        OutOfRangeError: Nếu steps không nằm trong phạm vi hợp lệ.
    """
    if steps < 0 or steps > 88 or steps <= 1:
        raise OutOfRangeError("Số bước phải từ 2 đến 88")
    steps = int(steps)
    for i in range(steps):
        sys.stdout.write(
            "Dang tai xuong [{}{}] {}%\r".format(
                "■" * i, " " * (steps - 1 - i), (i + 1) * 100 // steps
            )
        )
        sys.stdout.flush()
        time.sleep(0.1)
    print("\nTai xuong hoan tat!")


def mp_tinh_toan(steps):
    """
    Mô phỏng quá trình tính toán.

    Thông số:
        steps (int): Số bước tính toán.

    Raises:
        OutOfRangeError: Nếu steps không nằm trong phạm vi hợp lệ.
    """
    if steps < 0 or steps >= 88:
        raise OutOfRangeError("Số bước phải từ 0 đến 87")
    steps = int(steps)
    for i in range(steps):
        sys.stdout.write(
            "    AD: Dang tinh toan [{}{}] {}%\r".format(
                "■" * i, " " * (steps - 1 - i), (i + 1) * 100 // steps
            )
        )
        sys.stdout.flush()
        time.sleep(0.2)


def mp_loading(count):
    """
    Mô phỏng quá trình loading.

    Thông số:
        count (int): Số lần lặp.
    """
    sys.stdout.write("LOADING")
    sys.stdout.flush()
    time.sleep(0.5)
    for _ in range(count):
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.4)
        sys.stdout.write("\b\b\b   \b\b\b")
        sys.stdout.flush()


def mp_christmas_tree_cho_VSCode():
    """
    Mô phỏng cây thông Giáng sinh cho VSCode.

    Thông số:
        None

    Trả lại:
        None: In cây thông ra màn hình.

    Hướng dẫn:
        - Nhập chiều cao cây thông khi được yêu cầu.
    """
    height = int(input("- Nhập chiều cao cây thông: "))
    tree = []
    for i in range(height):
        tree.append(" " * (height - i - 1) + "* " * (i + 1))
    for i in range(height // 3):
        tree.append(" " * (height - 1) + "H")
    for line in tree:
        print(line)


def mp_christmas_tree_cho_TEXT():
    """
    Mô phỏng cây thông Giáng sinh cho TEXT.

    Thông số:
        None

    Trả lại:
        None: In cây thông ra màn hình.

    Hướng dẫn:
        - Nhập chiều cao cây thông khi được yêu cầu.
    """
    height = int(input("- Nhập chiều cao cây thông: "))
    tree = []
    for i in range(height):
        tree.append("  " * (height - i - 1) + " * " * (i + 1))
    for i in range(height // 3):
        tree.append("  " * (height - 1) + "H")
    for line in tree:
        print(line)


# Hàm hỗ trợ tính toán đặc biệt


def tinh_toan_tien_dien(old_reading, new_reading):
    """
    Tính toán tiền điện.

    Thông số:
        old_reading (str): Chỉ số cũ.
        new_reading (str): Chỉ số mới.

    Trả lại:
        str: Kết quả tính toán.

    Raises:
        MathError: Nếu chỉ số không hợp lệ.
    """
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
                ((kwh - 300) * 2834) + 100 * 2536 + 100 * 2014 + 50 * 1734 + 50 * 1678
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
        return f"- So Kwh dien tieu thu trong thang: {kwh} Kwh\n- So tien dien can tra trong thang: {total} VND"
    raise MathError("Chi so khong hop le")


def tong_chu_so_lon_nhat_bang_n(digit_count, target_sum):
    """
    Tìm số lớn nhất có digit_count chữ số và tổng các chữ số bằng target_sum.

    Thông số:
        digit_count (int): Số chữ số.
        target_sum (int): Tổng các chữ số.

    Trả lại:
        str: Số lớn nhất thỏa mãn điều kiện.

    Raises:
        MathError: Nếu không thể tạo số thỏa mãn.
    """
    digits = abs(digit_count)
    total = abs(target_sum)
    if digits == 0 or total == 0:
        return "0"
    if total > 9 * digits:
        raise MathError("Khong the tao so voi tong chu so lon hon 9 * so chu so")
    result = ["9"] * (total // 9)
    if total % 9 != 0:
        result.append(str(total % 9))
    while len(result) < digits:
        result.append("0")
    return "".join(result[:digits])


def pythagore(side_a, side_b, side_c):
    """
    Tính cạnh còn lại trong tam giác vuông.

    Thông số:
        side_a (float or bool): Cạnh a.
        side_b (float or bool): Cạnh b.
        side_c (float or bool): Cạnh c.

    Trả lại:
        str: Kết quả tính toán.

    Raises:
        MathError: Nếu đầu vào không hợp lệ.
    """
    sides = [side_a, side_b, side_c]
    if sides.count(False) > 1 or any(side < 0 for side in sides if side is not False):
        raise MathError("Dau vao khong hop le")
    if side_a is False:
        if side_c < side_b:
            raise MathError("Canh huyen phai lon hon canh goc vuong")
        result = math.sqrt(side_c**2 - side_b**2)
        return f"Canh goc vuong 1 = {result}"
    elif side_b is False:
        if side_c < side_a:
            raise MathError("Canh huyen phai lon hon canh goc vuong")
        result = math.sqrt(side_c**2 - side_a**2)
        return f"Canh goc vuong 2 = {result}"
    elif side_c is False:
        result = math.sqrt(side_a**2 + side_b**2)
        return f"Canh huyen = {result}"


# Quy luật sinh dãy
def tao_danh_sach_quy_luat_1(total):
    """
    Tạo danh sách theo quy luật: 1 số ⋮ 1, 2 số ⋮ 2, 3 số ⋮ 3, ...

    Thông số:
        total (int): Tổng số lượng phần tử.

    Trả lại:
        list: Danh sách theo quy luật.
    """
    result = []
    step = 1
    while len(result) < total:
        for _ in range(step):
            if len(result) < total:
                result.append(step)
        step += 1
    return result


def tao_danh_sach_quy_luat_2(base, count):
    """
    Tạo danh sách các bội của base với count phần tử.

    Thông số:
        base (int): Số để tạo bội.
        count (int): Số phần tử.

    Trả lại:
        list: Danh sách các bội của base.
    """
    return [base * i for i in range(count)]


def tao_danh_sach_quy_luat_3(count, base):
    """
    Tạo danh sách lũy thừa của base từ 0 đến count.

    Thông số:
        count (int): Số lượng phần tử.
        base (int): Cơ số.

    Trả lại:
        list: Danh sách lũy thừa của base.
    """
    return [base**i for i in range(count)]


# Chuyển đổi và đếm
def chuyen_doi_so_la_ma(number):
    """
    Chuyển đổi số thành số La Mã.

    Thông số:
        number (int): Số cần chuyển đổi.

    Trả lại:
        str: Số La Mã.

    Raises:
        OutOfRangeError: Nếu number không nằm trong phạm vi 1 đến 3999.
    """
    if number <= 0 or number > 3999:
        raise OutOfRangeError("So phai tu 1 den 3999")
    return roman.toRoman(number)


def dem_so_nghich_the(numbers):
    """
    Đếm số cặp nghịch thế trong danh sách.

    Thông số:
        numbers (list): Danh sách cần đếm.

    Trả lại:
        int: Số cặp nghịch thế.
    """
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                count += 1
    return count


def one_two_three():
    """
    Chơi kéo búa bao với A.I.

    Thông số:
        None

    Trả lại:
        None: In kết quả ra màn hình.

    Hướng dẫn:
        - Nhập số trận đấu.
        - Nhập lựa chọn của bạn (Keo, Bua, Bao).
    """
    choices = {1: "Keo", 2: "Bua", 3: "Bao"}
    human_score, ai_score = 0, 0
    matches = int(input("- Number of matches: "))

    for _ in range(matches):
        ai_choice = choices[random.randint(1, 3)]
        user_input = input("- User's choice: ").title()

        print(f"- User's chosen = {user_input}, A.I's chosen = {ai_choice}")

        if user_input not in ["Keo", "Bua", "Bao"]:
            print(">>> ! ERROR !")
            continue

        if user_input == ai_choice:
            print(">>> DRAW")
        elif (
            (user_input == "Keo" and ai_choice == "Bao")
            or (user_input == "Bua" and ai_choice == "Keo")
            or (user_input == "Bao" and ai_choice == "Bua")
        ):
            print(">>> USER WON")
            human_score += 1
        else:
            print(">>> A.I WON")
            ai_score += 1

    print("- RESULT:")
    if human_score > ai_score:
        print(
            f">>> User's won with {human_score} point(s), A.I's lost with {ai_score} point(s)"
        )
    elif ai_score > human_score:
        print(
            f">>> A.I's won with {ai_score} point(s), User's lost with {human_score} point(s)"
        )
    else:
        print(">>> DRAW")


def tao_day_chu(rows, columns, repeats):
    """
    Tạo dãy chữ với rows dòng, columns cột, 2 đường chéo, lặp lại repeats lần.

    Thông số:
        rows (int): Số dòng.
        columns (int): Số cột.
        repeats (int): Số lần lặp lại.

    Trả lại:
        None: In dãy chữ ra màn hình.

    Hướng dẫn:
        - Nhập chuỗi đầu tiên khi được yêu cầu.
    """
    text = input("Nhap day dau tien: ")
    for _ in range(repeats):
        # In cột
        for _ in range(columns):
            for _ in range(rows):
                print(text)
        # In đường chéo 1
        for i in range(rows):
            print("  " * i + text)
        # In đường chéo 2
        for i in range(rows - 1, -1, -1):
            print("  " * i + text)
