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
Tác giả
-------------------------------------------------------------------------------
- Joesifer.

Phiên bản
-------------------------------------------------------------------------------
- 0.1.5.1

Ngày đăng
-------------------------------------------------------------------------------
- Ngày 14 tháng 2, năm 2024.

Bản quyền
-------------------------------------------------------------------------------
- Copyright (c) 2024 Joesifer.

Phiên bản python được hỗ trợ.
-------------------------------------------------------------------------------
- Lớn hơn hoặc bằng 3.7.

Thư viện phụ thuộc.
-------------------------------------------------------------------------------
- math, re, sys, time (numpy, roman).

Giấy phép.
-------------------------------------------------------------------------------
- MIT License.

Thông tin.
-------------------------------------------------------------------------------

Nếu bạn cần hướng dẫn cách dùng thì hãy::

  >>> Truy cập: `https://github.com/Joesifer/pchjlib/blob/main/README.md`.

Và bạn có thể góp ý hoặc ủng hộ bằng::

  >>> Gửi email : `phanchanhung12055@gmail.com` .


CẢM ƠN!!!
===============================================================================

"""

import math, random, re, sys, time

__author__ = "Joesifer (phanchanhung12055@gmail.com)"
__copyright__ = "Copyright (c) 2024 Joesifer"


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


class DivisionByZeroError(MathError):
    """Lỗi khi chia cho 0."""

    pass


class TypeErrorCustom(MathError):
    """Lỗi khi kiểu dữ liệu không phù hợp."""

    pass


class ListError(MathError):
    """Lỗi liên quan đến danh sách đầu vào."""

    pass


# Kiểm tra và import các thư viện phụ thuộc
try:
    import numpy
except ImportError:
    numpy = None

try:
    import roman
except ImportError:
    roman = None


# Các hàm kiểm tra số nguyên tố và số liên quan
def kiem_tra_so_nguyen_to(number):
    """
    Kiểm tra xem một số có phải là số nguyên tố hay không.

    Tham số:
        - number (int hoặc float) - Số cần kiểm tra.

    Trả về:
        - True nếu là số nguyên tố, False nếu không (bool).

    Ném lỗi:
        - InvalidInputError nếu đầu vào không phải số nguyên.
        - Ví dụ: kiem_tra_so_nguyen_to(7) → True, kiem_tra_so_nguyen_to(3.5) → lỗi "Đầu vào không hợp lệ".
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
            raise InvalidInputError("Đầu vào phải là số nguyên")
        return miller_rabin(number)
    except (ValueError, TypeError):
        raise InvalidInputError("Đầu vào không hợp lệ")


def tao_danh_sach_so_nguyen_to(limit):
    """
    Tạo danh sách các số nguyên tố từ 0 đến limit bằng thuật toán Sieve.

    Tham số:
        - limit (int hoặc float) - Giới hạn trên của danh sách.

    Trả về:
        - Danh sách các số nguyên tố (list).

    Ném lỗi:
        - InvalidInputError nếu limit không phải số nguyên >= 2.
        - Ví dụ: tao_danh_sach_so_nguyen_to(10) → [2, 3, 5, 7].
    """
    try:
        if numpy is None:
            raise ImportError(
                "Hàm này yêu cầu cài đặt numpy. Hãy chạy: pip install numpy"
            )
        else:
            if isinstance(limit, float) and not limit.is_integer():
                raise InvalidInputError(
                    "Đầu vào không hợp lệ: Giới hạn phải là số nguyên"
                )
            limit = int(limit)
            if limit < 2:
                raise InvalidInputError("Đầu vào không hợp lệ: Giới hạn phải >= 2")
            if numpy is not None:
                sieve = numpy.ones(
                    limit + 1, dtype=bool
                )  # Phân bổ trước bộ nhớ với numpy
                sieve[0:2] = False
                for i in range(2, int(limit**0.5) + 1):
                    if sieve[i]:
                        sieve[i * i : limit + 1 : i] = False
                return numpy.where(sieve)[0].tolist()
            else:
                sieve = [True] * (limit + 1)  # Phân bổ trước bộ nhớ
                sieve[0] = sieve[1] = False
                for i in range(2, int(limit**0.5) + 1):
                    if sieve[i]:
                        for j in range(i * i, limit + 1, i):
                            sieve[j] = False
                return [i for i in range(limit + 1) if sieve[i]]
    except (ValueError, TypeError):
        raise InvalidInputError("Đầu vào không hợp lệ: Giới hạn không phải số nguyên")


def kiem_tra_so_emirp(number):
    """
    Kiểm tra xem một số có phải là số emirp (số nguyên tố đảo ngược cũng là nguyên tố) hay không.

    Tham số:
        - number (int hoặc float) - Số cần kiểm tra.

    Trả về:
        - True nếu là số emirp, False nếu không (bool).

    Ném lỗi:
        - InvalidInputError nếu đầu vào không phải số nguyên dương.
        - Ví dụ: kiem_tra_so_emirp(31) → True vì 31 cũng là số nguyên tố,
                 kiem_tra_so_emirp(3.5) → lỗi "Đầu vào không hợp lệ".
    """
    try:
        if isinstance(number, float) and not number.is_integer():
            raise InvalidInputError(
                "Đầu vào không hợp lệ: Số thực không được chấp nhận"
            )
        number = int(number)
        if number < 2:
            raise InvalidInputError("Đầu vào không hợp lệ: Số phải >= 2")
        if not kiem_tra_so_nguyen_to(number):
            return False
        reversed_number = int(str(number)[::-1])
        return kiem_tra_so_nguyen_to(reversed_number)
    except (ValueError, TypeError):
        raise InvalidInputError("Đầu vào không hợp lệ: Giá trị không phải số nguyên")


def tao_danh_sach_so_emirp(limit):
    """
    Tạo danh sách các số emirp từ 0 đến limit.

    Tham số:
        - limit (int hoặc float) - Giới hạn trên của danh sách.

    Trả về:
        - Danh sách các số emirp (list).

    Ném lỗi:
        - InvalidInputError nếu limit không phải số nguyên không âm.
    """
    try:
        if isinstance(limit, float) and not limit.is_integer():
            raise InvalidInputError("Đầu vào không hợp lệ: Giới hạn phải là số nguyên")
        limit = int(limit)
        if limit < 0:
            raise InvalidInputError("Đầu vào không hợp lệ: Giới hạn phải không âm")
        return [i for i in range(2, limit) if kiem_tra_so_emirp(i)]
    except (ValueError, TypeError):
        raise InvalidInputError("Đầu vào không hợp lệ: Giới hạn không phải số nguyên")


# Các hàm Fibonacci
def vi_tri_so_Fibonacci(index):
    """
    Tính số Fibonacci thứ index bằng phương pháp lặp và chỉ chấp nhận index kiểu int không âm.

    Tham số:
        - index (int) - Vị trí của số Fibonacci (bắt đầu từ 0).

    Trả về:
        - Số Fibonacci tại vị trí index (int).

    Ném lỗi:
        - InvalidInputError nếu index không phải số nguyên không âm.
    """
    if not isinstance(index, int) and not isinstance(index, bool):
        raise InvalidInputError("Đầu vào không hợp lệ: Phải là số nguyên")

    if index < 0:
        raise InvalidInputError("Đầu vào không hợp lệ: Phải là số nguyên không âm")

    a, b = 0, 1
    for _ in range(index):
        a, b = b, a + b
    return a


def tao_danh_sach_so_Fibonacci(count):
    """
    Tạo danh sách count số Fibonacci đầu tiên.

    Tham số:
        - count (int hoặc float) - Số lượng phần tử trong danh sách.

    Trả về:
        - Danh sách các số Fibonacci (list).

    Ném lỗi:
        - InvalidInputError nếu count không phải số nguyên không âm.
    """
    try:
        if isinstance(count, float) and not count.is_integer():
            raise InvalidInputError("Đầu vào không hợp lệ: Số lượng phải là số nguyên")
        count = int(count)
        if count < 0:
            raise InvalidInputError("Đầu vào không hợp lệ: Số lượng phải không âm")
        return [vi_tri_so_Fibonacci(i) for i in range(count)]
    except (ValueError, TypeError):
        raise InvalidInputError("Đầu vào không hợp lệ: Số lượng không phải số nguyên")


# Các hàm tính số hoàn thiện, tự mãn, hữu hảo, hoàn hào, thân thiết
def tong_uoc_so(number):
    """
    Tính tổng các ước số dương của number (không tính chính nó).

    Tham số:
        - number (int hoặc float) - Số cần tính tổng ước số.

    Trả về:
        - Tổng các ước số (int).

    Ném lỗi:
        - MathError nếu number <= 0, InvalidInputError nếu không phải số nguyên.
    """
    try:
        if isinstance(number, float) and not number.is_integer():
            raise InvalidInputError(
                "Đầu vào không hợp lệ: Số thực không được chấp nhận"
            )
        number = int(number)
        if number <= 0:
            raise MathError("Số phải lớn hơn 0 / Number must be greater than 0")
        return sum(i for i in range(1, number) if number % i == 0)
    except (ValueError, TypeError):
        raise InvalidInputError("Đầu vào không hợp lệ: Giá trị không phải số nguyên")


def tong_chu_so(number):
    """
    Tính tổng các chữ số của một số nguyên.

    Tham số:
        - number (int hoặc float) - Số cần tính tổng chữ số.
    Trả về:
        - Tổng các chữ số (int).

    Ném lỗi:
        - InvalidInputError nếu đầu vào không phải số nguyên hợp lệ.
    """
    try:
        if isinstance(number, float) and not number.is_integer():
            raise InvalidInputError(
                "Đầu vào không hợp lệ: Số thực có phần thập phân không được chấp nhận"
            )
        number = int(number)
        return sum(int(digit) for digit in str(abs(number)))
    except (ValueError, TypeError):
        raise InvalidInputError("Đầu vào không hợp lệ: Giá trị không phải số nguyên")


def kiem_tra_so_hoan_thien(number):
    """
    Kiểm tra xem một số có phải là số hoàn thiện hay không.

    Tham số:
        - number (int) - Số cần kiểm tra.

    Trả lại:
        - bool: True nếu number là số hoàn thiện, False nếu không.

    Ném lỗi:
        - MathError nếu number không lớn hơn 1.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Đầu vào phải là số nguyên")
        number = int(number)
        if number < 1:
            raise MathError("Số phải lớn hơn 0")
        return tong_uoc_so(number) == number
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def tao_danh_sach_so_hoan_thien(limit):
    """
    Tạo danh sách các số hoàn thiện từ 0 đến limit.

    Tham số:
        - limit (int) - Giới hạn trên của danh sách.

    Trả lại:
        - Danh sách các số hoàn thiện (list).

    Ném lỗi:
        - NotIntegerError nếu không phải số nguyên, InvalidInputError nếu không lớn hơn 1.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Giới hạn phải là số nguyên")
        limit = int(limit)
        if limit < 1:
            raise InvalidInputError("Giới hạn phải lớn hơn 0")
        return [i for i in range(1, limit + 1) if kiem_tra_so_hoan_thien(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def kiem_tra_so_tu_man(number):
    """
    Kiểm tra xem một số có phải là số tự mãn hay không.

    Tham số:
        - number (int) - Số cần kiểm tra.

    Trả lại:
        - bool: True nếu number là số tự mãn, False nếu không.

    Ném lỗi:
        - InvalidInputError nếu number không phải số nguyên >= 2.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Đầu vào phải là số nguyên")
        number = int(number)
        if number < 0:
            return False
        return sum(int(digit) ** 3 for digit in str(number)) == number
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def tao_danh_sach_so_tu_man(limit):
    """
    Tạo danh sách các số tự mãn từ 0 đến limit.

    Tham số:
        - limit (int) - Giới hạn trên của danh sách.

    Trả lại:
        - list - Danh sách các số tự mãn.

    Ném lỗi:
        - InvalidInputError nếu limit không phải số nguyên >= 2.
        - NotIntegerError nếu limit không phải là số nguyên.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Giới hạn phải là số nguyên")
        limit = int(limit)
        if limit < 2:
            raise InvalidInputError("Giới hạn phải lớn hơn hoặc bằng 2")
        return [i for i in range(2, limit) if kiem_tra_so_tu_man(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def cap_so_hua_hon(number1, number2):
    """
    Kiểm tra xem hai số có phải là cặp số hữu hảo hay không.

    Tham số:
        - number1 (int) - Số thứ nhất.
        - number2 (int) - Số thứ hai.

    Trả lại:
        - bool: True nếu number1 và number2 là cặp số hữu hảo, False nếu không.

    Ném lỗi:
        - MathError nếu các số âm.
        - InvalidInputError nếu các số không phải số nguyên.
    """
    try:
        if not (
            isinstance(number1, (int, float)) and isinstance(number2, (int, float))
        ) or not (float(number1).is_integer() and float(number2).is_integer()):
            raise NotIntegerError("Cả hai số phải là số nguyên")
        number1, number2 = int(number1), int(number2)
        if number1 < 0 or number2 < 0:
            raise MathError("Các số phải không âm")
        return (
            tong_uoc_so(number1) == number2 + 1 and tong_uoc_so(number2) == number1 + 1
        )
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def kiem_tra_so_hoan_hao(number):
    """
    Kiểm tra xem một số có phải là số hoàn hảo hay không.

    Tham số:
        - number (int) - Số cần kiểm tra.

    Trả lại:
        - bool: True nếu number là số hoàn hảo, False nếu không.

    Ném lỗi:
        - MathError nếu number < 1, InvalidInputError nếu không phải số nguyên.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Đầu vào phải là số nguyên")
        number = int(number)
        if number < 1:
            raise MathError("Số phải lớn hơn 0")
        return sum(i for i in range(1, number) if number % i == 0) == number
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def tao_danh_sach_so_hoan_hao(limit):
    """
    Tạo danh sách các số hoàn hảo từ 0 đến limit.

    Tham số:
        - limit (int): Giới hạn trên của danh sách.

    Trả lại:
        - list: Danh sách các số hoàn hảo.

    Ném lỗi:
        - InvalidInputError nếu limit không phải số nguyên > 0.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Giới hạn phải là số nguyên")
        limit = int(limit)
        if limit < 1:
            raise InvalidInputError("Giới hạn phải lớn hơn 0")
        return [i for i in range(1, limit) if kiem_tra_so_hoan_hao(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


# Các hàm số chính phương, mạnh mẽ, thân thiết
def kiem_tra_so_chinh_phuong(number):
    """
    Kiểm tra xem một số có phải là số chính phương hay không.

    Tham số:
        - number (int) - Số cần kiểm tra.

    Trả lại:
        - bool: True nếu number là số chính phương, False nếu không.

    Ném lỗi:
        - InvalidInputError nếu không phải số nguyên.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Đầu vào phải là số nguyên")
        number = int(number)
        if number < 0:
            return False
        sqrt_number = int(math.sqrt(number))
        return sqrt_number * sqrt_number == number
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def tao_danh_sach_so_chinh_phuong(limit):
    """
    Tạo danh sách các số chính phương từ 0 đến limit.

    Tham số:
        - limit (int) - Giới hạn trên của danh sách.

    Trả lại:
        - list: Danh sách các số chính phương.

    Ném lỗi:
        - InvalidInputError nếu limit không phải số nguyên không âm.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Giới hạn phải là số nguyên")
        limit = int(limit)
        if limit < 0:
            raise InvalidInputError("Giới hạn phải không âm")
        return [i for i in range(limit) if kiem_tra_so_chinh_phuong(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def cap_so_than_thiet(number1, number2):
    """
    Kiểm tra xem hai số có phải là cặp số thân thiết hay không.

    Tham số:
        - number1 (int) - Số thứ nhất.
        - number2 (int) - Số thứ hai.

    Trả lại:
        - bool: True nếu number1 và number2 là cặp số thân thiết, False nếu không.

    Ném lỗi:
        - MathError nếu các số không lớn hơn 1.
        - InvalidInputError nếu không phải số nguyên.
    """
    try:
        if not (
            isinstance(number1, (int, float)) and isinstance(number2, (int, float))
        ) or not (float(number1).is_integer() and float(number2).is_integer()):
            raise NotIntegerError("Cả hai số phải là số nguyên")
        number1, number2 = int(number1), int(number2)
        if number1 <= 1 or number2 <= 1:
            raise MathError("Các số phải lớn hơn 1")
        return tong_uoc_so(number1) == number2 and tong_uoc_so(number2) == number1
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def kiem_tra_so_manh_me(number, variant=1):
    """
    Kiểm tra xem một số có phải là số mạnh mẽ (tổng chữ số là nguyên tố) hay không.

    Tham số:
        - number (int) - Số cần kiểm tra.
        - variant (int) - 1 - Tổng chữ số là nguyên tố; 2 - Có thừa số nguyên tố bình phương.

    Trả lại:
        - bool: True nếu number là số mạnh mẽ, False nếu không.

    Ném lỗi:
        - InvalidInputError nếu không phải số nguyên.
    """
    try:
        if not isinstance(number, int) or number < 0:
            raise NotIntegerError("Đầu vào phải là số nguyên không âm")
        number = int(number)
        if variant == 1:
            return kiem_tra_so_nguyen_to(tong_chu_so(number))
        elif variant == 2:
            prime_list = [i for i in range(2, number) if kiem_tra_so_nguyen_to(i)]
            for prime in prime_list:
                if number % prime == 0 and number % (prime**2) == 0:
                    return True
            return False
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


# Các hàm về ước số và bội số
def tao_danh_sach_uoc_so(number, positive_only=True):
    """
    Tạo danh sách các ước số của number.

    Tham số:
        - number (int) - Số cần tạo danh sách ước số.
        - positive_only = True 'hoặc' False. Mặc định là True và các ước sẽ luôn dương, có thể thay đổi thành False và các ước âm sẽ được xuất hiện.

    Trả lại:
        - list: Danh sách các ước số của number.

    Ném lỗi:
        - MathError: Nếu number là 0.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Đầu vào phải là số nguyên")
        number = int(number)
        if number == 0:
            raise MathError("Không thể tạo danh sách ước số cho 0")
        number = abs(number)
        divisors = [i for i in range(1, number + 1) if number % i == 0]
        if not positive_only:
            divisors += [-i for i in divisors]
        return sorted(divisors)
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def tao_danh_sach_boi_so(number, positive_only=True):
    """
    Tạo danh sách bội số của number từ 0 đến 10 lần.

    Tham số:
        - number (int) - Số cần tạo danh sách bội số.
        - positive_only = True 'hoặc' False. Mặc định là True và các ước sẽ luôn dương, có thể thay đổi thành False và các ước âm sẽ được xuất hiện.

    Trả lại:
        - list: Danh sách bội số của number.

    Ném lỗi:
        - MathError: Nếu number là 0.
        - NotIntegerError: Đầu vào phải là số nguyên.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Đầu vào phải là số nguyên")
        number = int(number)
        if number == 0:
            raise MathError("Không thể tạo danh sách bội số cho 0")
        if not positive_only == True:
            return sorted([-number * i for i in range(1, 11)]) + [
                number * i for i in range(11)
            ]
        return [number * i for i in range(11)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def uoc_chung(numbers):
    """
    Tạo danh sách các ước chung của một danh sách các số.

    Tham số:
        - numbers (list) - Danh sách các số.

    Trả lại:
        - list: Danh sách các ước chung.

    Ném lỗi:
        - MathError: Nếu danh sách không đủ phần tử.
        - ListError: Đầu vào phải là danh sách hoặc tuple.
    """

    def get_divisors(n):
        try:
            n = abs(int(n))
            return set(
                [i for i in range(1, n + 1) if n % i == 0]
                + [-i for i in range(1, n + 1) if n % i == 0]
            )
        except (ValueError, TypeError):
            raise TypeErrorCustom("Phần tử trong danh sách không hợp lệ")

    try:
        numbers = list(set(numbers))
        for i in numbers:
            if i == 0:
                numbers.remove(i)
        if not isinstance(numbers, (list, tuple)):
            raise ListError("Đầu vào phải là danh sách hoặc tuple")
        if len(numbers) < 2:
            raise MathError("Danh sách phải có ít nhất 2 phần tử")
        for num in numbers:
            if not isinstance(num, (int, float)) or not float(num).is_integer():
                raise NotIntegerError("Tất cả phần tử phải là số nguyên")
        result = get_divisors(numbers[0])
        for num in numbers[1:]:
            result = result.intersection(get_divisors(num))
        return sorted(list(result))
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


def uoc_chung_lon_nhat(numbers):
    """
    Tính ước chung lớn nhất của một danh sách các số.

    Tham số:
        - numbers (list) - Danh sách các số.

    Trả lại:
        - int: Ước chung lớn nhất của danh sách.

    Ném lỗi:
        - MathError: Nếu danh sách không hợp lệ.
        - ListError: Nếu đầu vào không phải là danh sách hoặc tuple.
    """

    def get_UCLN(number1, number2):
        try:
            if not (
                isinstance(number1, (int, float)) and isinstance(number2, (int, float))
            ) or not (float(number1).is_integer() and float(number2).is_integer()):
                raise NotIntegerError("Cả hai số phải là số nguyên")
            number1, number2 = int(number1), int(number2)
            return math.gcd(number1, number2)
        except (ValueError, TypeError):
            raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")

    try:
        numbers = list(set(numbers))
        for i in numbers:
            if i == 0:
                numbers.remove(i)
        if not isinstance(numbers, (list, tuple)):
            raise ListError("Đầu vào phải là danh sách hoặc tuple")
        if len(numbers) < 2:
            raise MathError("Danh sách không hợp lệ")
        for num in numbers:
            if not isinstance(num, (int, float)) or not float(num).is_integer():
                raise NotIntegerError("Tất cả phần tử phải là số nguyên")
        result = int(numbers[0])
        for num in numbers[1:]:
            result = get_UCLN(result, int(num))
            if result == 1:
                break
        return result
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


def boi_chung_nho_nhat(numbers):
    """
    Tính bội chung nhỏ nhất của một danh sách các số.

    Tham số:
        - numbers (list) - Danh sách các số.

    Trả lại:
        - int: Bội chung nhỏ nhất của danh sách.

    Ném lỗi:
        - MathError: Nếu danh sách không hợp lệ.
        - ListError: Đầu vào phải là danh sách hoặc tuple.
    """

    def get_BCNN(number1, number2):
        try:
            if not (
                isinstance(number1, (int, float)) and isinstance(number2, (int, float))
            ) or not (float(number1).is_integer() and float(number2).is_integer()):
                raise NotIntegerError("Cả hai số phải là số nguyên")
            number1, number2 = int(number1), int(number2)
            if number1 == 0 or number2 == 0:
                raise DivisionByZeroError("Không thể tính LCM với 0")
            return math.lcm(number1, number2)
        except (ValueError, TypeError):
            raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")

    try:
        if not isinstance(numbers, (list, tuple)):
            raise ListError("Đầu vào phải là danh sách hoặc tuple")
        if len(numbers) < 2 or 0 in numbers:
            raise MathError("Danh sách không hợp lệ")
        for num in numbers:
            if not isinstance(num, (int, float)) or not float(num).is_integer():
                raise NotIntegerError("Tất cả phần tử phải là số nguyên")
        result = int(numbers[0])
        for num in numbers[1:]:
            result = get_BCNN(result, int(num))
        return result
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


# Các hàm số song tố và số phong phú
def kiem_tra_so_song_to(number):
    """
    Kiểm tra xem một số có phải là số song tố hay không.

    Tham số:
        - number (int) - Số cần kiểm tra.

    Trả lại:
        - bool: True nếu number là số song tố, False nếu không.

    Ném lỗi:
        - NotIntegerError: Đầu vào phải là số nguyên.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Đầu vào phải là số nguyên")
        number = int(number)
        return kiem_tra_so_nguyen_to(number) and kiem_tra_so_nguyen_to(
            tong_chu_so(number)
        )
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def tao_danh_sach_so_song_to(limit):
    """
    Tạo danh sách các số song tố từ 0 đến limit.

    Tham số:
        - limit (int) - Giới hạn trên của danh sách.

    Trả lại:
        - list: Danh sách các số song tố.

    Ném lỗi:
        - NotIntegerError: Đầu vào phải là số nguyên.
        - InvalidInputError: Giới hạn phải không âm.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Giới hạn phải là số nguyên")
        limit = int(limit)
        if limit < 0:
            raise InvalidInputError("Giới hạn phải không âm")
        return [i for i in range(limit) if kiem_tra_so_song_to(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def kiem_tra_so_phong_phu(number):
    """
    Kiểm tra xem một số có phải là số phong phú hay không.

    Tham số:
        - number (int) - Số cần kiểm tra.

    Trả lại:
        - bool: True nếu number là số phong phú, False nếu không.

    Ném lỗi:
        - NotIntegerError: Đầu vào phải là số nguyên.
        - InvalidInputError: Giới hạn phải không âm.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Đầu vào phải là số nguyên")
        number = int(number)
        if number <= 0:
            return False
        return sum(i for i in range(1, number) if number % i == 0) > number
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def tao_danh_sach_so_phong_phu(limit):
    """
    Tạo danh sách các số phong phú từ 0 đến limit.

    Tham số:
        - limit (int) - Giới hạn trên của danh sách.

    Trả lại:
        - list: Danh sách các số phong phú.

    Ném lỗi:
        - NotIntegerError: Đầu vào phải là số nguyên.
    """
    try:
        if not isinstance(limit, (int, float)) or not float(limit).is_integer():
            raise NotIntegerError("Giới hạn phải là số nguyên")
        limit = int(limit)
        if limit < 0:
            raise InvalidInputError("Giới hạn phải không âm")
        return [i for i in range(limit) if kiem_tra_so_phong_phu(i)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def thua_so_nguyen_to(number):
    """
    Phân tích một số thành danh sách các thừa số nguyên tố.

    Tham số:
        - number (int) - Số cần phân tích.

    Trả lại:
        - list: Danh sách các thừa số nguyên tố.

    Ném lỗi:
        - MathError: Nếu number không lớn hơn 1.
        - NotIntegerError: Đầu vào phải là số nguyên.
    """
    try:
        if not isinstance(number, (int, float)) or not float(number).is_integer():
            raise NotIntegerError("Đầu vào phải là số nguyên")
        number = int(number)
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
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def uoc_chung_nguyen_to_hai_so(number1, number2):
    """
    Tìm ước chung nguyên tố lớn nhất của hai số.

    Tham số:
        - number1 (int) - Số thứ nhất.
        - number2 (int) - Số thứ hai.

    Trả lại:
        - int: Ước chung nguyên tố lớn nhất của number1 và number2.

    Ném lỗi:
        - MathError: Nếu các số không lớn hơn 1 hoặc không có ước chung nguyên tố.
        - NotIntegerError: Cả hai số phải là số nguyên.
    """
    try:
        if not (
            isinstance(number1, (int, float)) and isinstance(number2, (int, float))
        ) or not (float(number1).is_integer() and float(number2).is_integer()):
            raise NotIntegerError("Cả hai số phải là số nguyên")
        number1, number2 = int(number1), int(number2)
        if number1 <= 1 or number2 <= 1:
            raise MathError("Các số phải lớn hơn 1")
        factors1 = set(thua_so_nguyen_to(number1))
        factors2 = set(thua_so_nguyen_to(number2))
        common_factors = factors1.intersection(factors2)
        if not common_factors:
            raise MathError("Không có ước chung nguyên tố")
        return max(common_factors)
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


# Hàm giải phương trình
def giai_phuong_trinh(degree, coefficients):
    """
    Giải phương trình từ bậc 1 đến bậc 10 theo hệ số.

    Tham số:
        - degree (int) - Bậc của phương trình.
        - coefficients (list) - Danh sách các hệ số của phương trình.

    Trả lại:
        - str: Kết quả nghiệm của phương trình.

    Ném lỗi:
        - ImportError: Nếu numpy không được cài đặt.
        - InvalidInputError: Nếu bậc hoặc hệ số không hợp lệ.
    """
    try:
        if numpy is None:
            raise ImportError(
                "Hàm này yêu cầu cài đặt numpy. Hãy chạy: pip install numpy"
            )
        if not isinstance(degree, (int, float)) or not float(degree).is_integer():
            raise NotIntegerError("Bậc phải là số nguyên")
        degree = int(degree)
        if degree < 1 or degree > 10:
            raise InvalidInputError("Bậc của phương trình phải từ 1 đến 10")
        if not isinstance(coefficients, (list, tuple)):
            raise ListError("Hệ số phải là danh sách hoặc tuple")
        if len(coefficients) != degree + 1:
            raise InvalidInputError(
                f"Phương trình bậc {degree} phải có {degree + 1} hệ số"
            )
        for coef in coefficients:
            if not isinstance(coef, (int, float)):
                raise TypeErrorCustom("Hệ số phải là số")
        roots = numpy.roots(coefficients)
        real_roots = [r for r in roots if numpy.isreal(r)]
        complex_roots = [r for r in roots if not numpy.isreal(r)]
        result = "Nghiệm của phương trình:\n"
        if real_roots:
            result += "\nNghiệm thực:\n" + "\n".join(
                f"x{i+1} = {r.real}" for i, r in enumerate(real_roots)
            )
        if complex_roots:
            result += "\nNghiệm phức:\n" + "\n".join(
                f"x{i+1} = {r}" for i, r in enumerate(complex_roots)
            )
        return (
            result.strip()
            if real_roots or complex_roots
            else "Phương trình không có nghiệm thực hoặc phức"
        )
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


# Các hàm xử lý danh sách và chuỗi
def danh_sach_khong_trung_lap(items):
    """
    Loại bỏ phần tử trùng lặp trong danh sách.

    Tham số:
        - items (list) - Danh sách cần xử lý.

    Trả lại:
        - list - Danh sách không có phần tử trùng lặp.

    Ném lỗi:
        - ListError: Đầu vào phải là danh sách hoặc tuple.
    """
    try:
        if not isinstance(items, (list, tuple)):
            raise ListError("Đầu vào phải là danh sách hoặc tuple")
        return sorted(list(set(items)), reverse=True)
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


def trich_xuat_chu_so_tu_chuoi(text):
    """
    Trích xuất chuỗi chữ số từ chuỗi. Ví dụ: "abc123" = [1,2,3].

    Tham số:
        - text (str) - Chuỗi đầu vào.

    Trả lại:
        - list: Danh sách các chữ số.

    Ném lỗi:
        - InvalidInputError: nếu chuỗi rỗng.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Đầu vào phải là chuỗi")
        if not text:
            raise InvalidInputError("Chuỗi không thể rỗng")
        return [int(digit) for digit in re.findall(r"\d", text)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


def trich_xuat_so_tu_chuoi(text):
    """
    Trích xuất chuỗi số từ chuỗi. Ví dụ: "abc123" = [123].

    Tham số:
        - text (str) - Chuỗi đầu vào.

    Trả lại:
        - list: Danh sách các số.

    Ném lỗi:
        - InvalidInputError: nếu chuỗi rỗng.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Đầu vào phải là chuỗi")
        if not text:
            raise InvalidInputError("Chuỗi không thể rỗng")
        return [int(number) for number in re.findall(r"\d+", text)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


def trich_xuat_ki_tu(text):
    """
    Trích xuất các ký tự không phải số từ chuỗi.

    Tham số:
        - text (str) - Chuỗi đầu vào.

    Trả lại:
        - list: Danh sách các ký tự không phải số.

    Ném lỗi:
        - TypeErrorCustom: Đầu vào phải là chuỗi.
        - InvalidInputError: Chuỗi không thể rỗng.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Đầu vào phải là chuỗi")
        if not text:
            raise InvalidInputError("Chuỗi không thể rỗng")
        return re.findall(r"\D", text)
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


def xau_duoc_nen(text, type):
    """
    Xâu được nén thành 2 loại.

    Tham số:
        - text (str) - Chuỗi đầu vào.
        - type = 1 hoặc 2. Nếu 1 thì "google" → "google", nếu 2 thì "google" → "google".

    Trả lại:
        - str: Chuỗi đã nén.

    Ném lỗi:
        - InvalidInputError: Loại nén chỉ có 1 hoặc 2.
    """

    def loai_1(text):
        try:
            if not isinstance(text, str):
                raise TypeErrorCustom("Đầu vào phải là chuỗi")
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
                        str(count) + sorted_chars[i - 1]
                        if count > 1
                        else sorted_chars[i - 1]
                    )
                    count = 1
            result += str(count) + sorted_chars[-1] if count > 1 else sorted_chars[-1]
            return result
        except (ValueError, TypeError):
            raise TypeErrorCustom("Đầu vào không hợp lệ")

    def loai_2(text):
        try:
            if not isinstance(text, str):
                raise TypeErrorCustom("Đầu vào phải là chuỗi")
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
        except (ValueError, TypeError):
            raise TypeErrorCustom("Đầu vào không hợp lệ")

    if type == 1:
        return loai_1(text)
    elif type == 2:
        return loai_2(text)
    else:
        raise InvalidInputError("Loại nén chỉ có 1 hoặc 2")


def xau_duoc_nen_khong_ghi_so(input_text):
    """
    Nén xâu bỏ số (ví dụ "hhhooccssiiinnhh" → "hocsinh").

    Tham số:
        - input_text (str): Chuỗi đầu vào.

    Trả lại:
        - str: Chuỗi đã nén.

    Ném lỗi:
        - InvalidInputError: Chuỗi không thể rỗng.
    """
    try:
        if not isinstance(input_text, str):
            raise TypeErrorCustom("Đầu vào phải là chuỗi")
        if not input_text:
            raise InvalidInputError("Chuỗi không thể rỗng")
        result = input_text[0]
        for char in input_text[1:]:
            if char != result[-1]:
                result += char
        return result
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


def xau_duoc_giai_nen(text):
    """
    Giải nén xâu (ví dụ g2ogle" → "google").

    Tham số:
        - text (str) - Chuỗi đầu vào.

    Trả lại:
        - str: Chuỗi đã giải nén.

    Ném lỗi:
        - InvalidInputError: Nếu chuỗi rỗng.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Đầu vào phải là chuỗi")
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
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc số không hợp lệ trong chuỗi")


def xau_ki_tu_khong_trung_lap(text):
    """
    Tạo xâu ký tự không trùng lặp (ví dụ "google" → gole").

    Tham số:
        - text (str) - Chuỗi đầu vào.

    Trả lại:
        - str: Chuỗi không có ký tự trùng lặp.

    Ném lỗi:
        - InvalidInputError: Nếu chuỗi rỗng.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Đầu vào phải là chuỗi")
        if not text:
            raise InvalidInputError("Chuỗi không thể rỗng")
        text = text.lower()
        unique_chars = ""
        for char in text:
            if char not in unique_chars:
                unique_chars += char
        return unique_chars
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


# Mật mã Caesar
def chuyen_hoa_caesar(text, shift):
    """
    Chuyển chuỗi thành dãy số mật mã Caesar.

    Tham số:
        - text (str) - Chuỗi đầu vào.
        - shift (int) - Số bước dịch chuyển.

    Trả lại:
        - list: Dãy số mật mã Caesar.

    Ném lỗi:
        - InvalidInputError: Nếu chuỗi rỗng, chuỗi phải chỉ chứa chữ cái.
        - NotIntegerError: Số bước dịch chuyển phải là số nguyên.
    """
    try:
        if not isinstance(text, str):
            raise TypeErrorCustom("Đầu vào phải là chuỗi")
        if not isinstance(shift, (int, float)) or not float(shift).is_integer():
            raise NotIntegerError("Số bước dịch chuyển phải là số nguyên")
        shift = int(shift)
        if not text:
            raise InvalidInputError("Chuỗi không thể rỗng")
        text = "".join([char for char in text.upper() if char != " "]).strip()
        if not text.isalpha():
            raise InvalidInputError("Chuỗi phải chỉ chứa chữ cái")
        char_map = {chr(65 + i): i for i in range(26)}
        shifted_map = [(i + shift) % 26 for i in range(26)]
        return [shifted_map[char_map[char]] for char in text]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


def ma_hoa_caesar(numbers, shift):
    """
    Mã hóa dãy số Caesar thành xâu.

    Tham số:
        - numbers (list) - Dãy số đầu vào.
        - shift (int) - Số bước dịch chuyển.

    Trả lại:
        - str: Chuỗi đã mã hóa.

    Ném lỗi:
        - InvalidInputError: Nếu chuỗi rỗng, các số phải là số nguyên từ 0 đến 25.
        - ListError: Đầu vào phải là danh sách hoặc tuple.
        - NotIntegerError: Số bước dịch chuyển phải là số nguyên.
    """
    try:
        if not isinstance(numbers, (list, tuple)):
            raise ListError("Đầu vào phải là danh sách hoặc tuple")
        if not isinstance(shift, (int, float)) or not float(shift).is_integer():
            raise NotIntegerError("Số bước dịch chuyển phải là số nguyên")
        shift = int(shift)
        if not numbers:
            raise InvalidInputError("Danh sách không thể rỗng")
        for num in numbers:
            if (
                not isinstance(num, (int, float))
                or not float(num).is_integer()
                or int(num) < 0
                or int(num) > 25
            ):
                raise InvalidInputError("Các số phải là số nguyên từ 0 đến 25")
        char_map = {i: chr(65 + i) for i in range(26)}
        shifted_map = [(i + shift) % 26 for i in range(26)]
        reverse_map = {shifted_map[i]: i for i in range(26)}
        decoded = [reverse_map[int(num)] for num in numbers]
        return "".join([char_map[i] for i in decoded])
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


# Teen Code Yahoo
def teen_code_yahoo(input_text):
    """
    Chuyển xâu thành Teen Code Yahoo.

    Tham số:
        - input_text (str) - Chuỗi đầu vào.

    Trả lại:
        - str: Chuỗi Teen Code Yahoo.
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

    try:
        if not isinstance(input_text, str):
            raise TypeErrorCustom("Đầu vào phải là chuỗi")
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
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


# Các hàm mô phỏng chỉ với string
def mp_tai_xuong(steps):
    """
    Mô phỏng quá trình tải xuống.

    Tham số:
        steps (int): Số bước tải xuống.

    Ném lỗi:
        OutOfRangeError: Nếu steps không nằm trong phạm vi hợp lệ.
    """
    try:
        if not isinstance(steps, (int, float)) or not float(steps).is_integer():
            raise NotIntegerError("Số bước phải là số nguyên")
        steps = int(steps)
        if steps < 0 or steps > 88 or steps <= 1:
            raise OutOfRangeError("Số bước phải từ 2 đến 88")
        for i in range(steps):
            sys.stdout.write(
                "Dang tai xuong [{}{}] {}%\r".format(
                    "■" * i, " " * (steps - 1 - i), (i + 1) * 100 // steps
                )
            )
            sys.stdout.flush()
            time.sleep(0.1)
        print("\nTai xuong hoan tat!")
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def mp_tinh_toan(steps):
    """
    Mô phỏng quá trình tính toán.

    Tham số:
        steps (int): Số bước tính toán.

    Ném lỗi:
        OutOfRangeError: Nếu steps không nằm trong phạm vi hợp lệ.
    """
    try:
        if not isinstance(steps, (int, float)) or not float(steps).is_integer():
            raise NotIntegerError("Số bước phải là số nguyên")
        steps = int(steps)
        if steps < 0 or steps >= 88:
            raise OutOfRangeError("Số bước phải từ 0 đến 87")
        for i in range(steps):
            sys.stdout.write(
                "    AD: Dang tinh toan [{}{}] {}%\r".format(
                    "■" * i, " " * (steps - 1 - i), (i + 1) * 100 // steps
                )
            )
            sys.stdout.flush()
            time.sleep(0.2)
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def mp_loading(count):
    """
    Mô phỏng quá trình loading.

    Tham số:
        count (int): Số lần lặp.
    """
    try:
        if not isinstance(count, (int, float)) or not float(count).is_integer():
            raise NotIntegerError("Số lần lặp phải là số nguyên")
        count = int(count)
        if count < 0:
            raise InvalidInputError("Số lần lặp phải không âm")
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
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def mp_christmas_tree(type):
    """
    Mô phỏng cây thông giáng sinh.

    Tham số:
        - type (int) = 1 hoặc 2. Nếu 1 là cây thông cho terminal VSCode, 2 là cho văn bản text.

    Trả lại:
        None: Yêu cầu nhập chiều cao cây thông.
    """

    def loai_1():
        try:
            height = input("- Nhập chiều cao cây thông: ")
            if not height.isdigit():
                raise NotIntegerError("Chiều cao phải là số nguyên")
            height = int(height)
            if height <= 0:
                raise InvalidInputError("Chiều cao phải lớn hơn 0")
            tree = []
            for i in range(height):
                tree.append(" " * (height - i - 1) + "* " * (i + 1))
            for i in range(height // 3):
                tree.append(" " * (height - 1) + "H")
            for line in tree:
                print(line)
        except (ValueError, TypeError):
            raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")

    def loai_2():
        try:
            height = input("- Nhập chiều cao cây thông: ")
            if not height.isdigit():
                raise NotIntegerError("Chiều cao phải là số nguyên")
            height = int(height)
            if height <= 0:
                raise InvalidInputError("Chiều cao phải lớn hơn 0")
            tree = []
            for i in range(height):
                tree.append("  " * (height - i - 1) + " * " * (i + 1))
            for i in range(height // 3):
                tree.append("  " * (height - 1) + "H")
            for line in tree:
                print(line)
        except (ValueError, TypeError):
            raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")

    if type == 1:
        return loai_1()
    elif type == 2:
        return loai_2()
    else:
        raise InvalidInputError("Loại nén chỉ có 1 hoặc 2")


def chuong_trinh_matrix():
    """
    Giới thiệu:
        - Chương trình này tạo và thao tác với ma trận ngẫu nhiên dựa trên đầu vào của người dùng.
        - Các chức năng bao gồm:
        - Tạo ma trận với kích thước và giá trị tối đa do người dùng chỉ định.
        - In ma trận.
        - Tính toán và hiển thị giá trị lớn nhất, nhỏ nhất, tổng, và trung bình của các phần tử trong ma trận.
        - Trích xuất và hiển thị hàng hoặc cột cụ thể.
        - Tìm kiếm một số trong ma trận và hiển thị các vị trí của nó.
        - Lọc ma trận để chỉ hiển thị các phần tử bằng với số được tìm kiếm.

    Ném lỗi:
        - ValueError: Nếu người dùng nhập các giá trị không hợp lệ, chẳng hạn như số hàng hoặc số cột không phải là số nguyên, không dương, lớn hơn 20, hoặc nếu giá trị tối đa lớn hơn 100.
        - IndexError: Nếu người dùng yêu cầu trích xuất hàng hoặc cột không tồn tại trong ma trận.
    """

    def tao_matrix(m, n, max_value=100):
        if not (isinstance(m, int) and isinstance(n, int)):
            raise ValueError("Số hàng và số cột phải là số nguyên.")
        if m <= 0 or n <= 0:
            raise ValueError("Số hàng và số cột phải là số nguyên dương.")
        if m > 20 or n > 20:
            raise ValueError("Số hàng và số cột không được lớn hơn 20.")
        return [
            [random.randrange(-9, max_value + 1) for _ in range(n)] for _ in range(m)
        ]

    def in_ra_matrix(matrix, title="Ma tran", align=">4"):
        print(f"{title}:\n")
        if not matrix or not matrix[0]:
            print("Ma tran rong.")
            return
        str_matrix = [[str(elem) for elem in row] for row in matrix]
        max_len = max(len(elem) for row in str_matrix for elem in row)
        align = f">{max_len}"
        for row in str_matrix:
            print(" ".join(f"{elem:{align}}" for elem in row))
        print()

    def thong_ke_matrix(matrix):
        flat_matrix = [elem for row in matrix for elem in row]
        if not flat_matrix:
            raise ValueError("Ma trận rỗng.")
        return {
            "max": max(flat_matrix),
            "min": min(flat_matrix),
            "sum": sum(flat_matrix),
            "avg": sum(flat_matrix) / len(flat_matrix),
        }

    def lay_hang(matrix, row_index):
        if not 0 <= row_index < len(matrix):
            raise IndexError(
                f"Hàng {row_index + 1} không hợp lệ (phải từ 1 đến {len(matrix)})."
            )
        return matrix[row_index]

    def lay_cot(matrix, col_index):
        if not 0 <= col_index < len(matrix[0]):
            raise IndexError(
                f"Cột {col_index + 1} không hợp lệ (phải từ 1 đến {len(matrix[0])})."
            )
        return [row[col_index] for row in matrix]

    def tim_so(matrix, num):
        positions = [
            (i, j)
            for i in range(len(matrix))
            for j in range(len(matrix[0]))
            if matrix[i][j] == num
        ]
        return positions if positions else None

    def loc_matrix(matrix, num, replace_with="––"):
        return [
            [elem if elem == num else replace_with for elem in row] for row in matrix
        ]

    try:
        if roman is None:
            raise ImportError(
                "Hàm này yêu cầu cài đặt roman. Hãy chạy: pip install roman"
            )
        print("=== Chuong trinh Ma tran ===")
        m = int(input("- Nhap so hang: "))
        n = int(input("- Nhap so cot: "))
        max_val = int(
            input("- Nhap gia tri toi da cho phan tu (mac dinh 100): ") or 100
        )

        if max_val > 100:
            raise ValueError("Giá trị tối đa không được lớn hơn 100.")

        matrix = tao_matrix(m, n, max_val)

        for row in matrix:
            for elem in row:
                if elem > 100:
                    raise ValueError("Có số lớn hơn 100 trong ma trận.")

        in_ra_matrix(matrix, "- Ma tran goc")

        stats = thong_ke_matrix(matrix)
        print(f">>> Gia tri lon nhat: {stats['max']}")
        print(f">>> Gia tri nho nhat: {stats['min']}")
        print(f">>> Tong cac phan tu: {stats['sum']}")
        print(f">>> Trung binh: {stats['avg']:.2f}\n")

        hang_bat_ky = int(input(f"- Nhap hang can lay (1 den {m}): ")) - 1
        row = lay_hang(matrix, hang_bat_ky)
        print(f">>> Hang {hang_bat_ky + 1}: {row}\n")

        cot_bat_ky = int(input(f"- Nhap cot can lay (1 den {n}): ")) - 1
        column = lay_cot(matrix, cot_bat_ky)
        print(f">>> Cot {cot_bat_ky + 1}: {column}\n")

        so_n = int(input("- Nhap so can tim: "))
        positions = tim_so(matrix, so_n)
        if positions:
            print(f"- So {so_n} xuat hien {len(positions)} lan trong ma tran.")
            in_ra_matrix(loc_matrix(matrix, so_n), "- Ma tran sau khi loc")
            print(">>> Vi tri cua so:")
            for idx, (i, j) in enumerate(positions, 1):
                print(f"[{roman.toRoman(idx)} - {idx}] Hang: {i + 1}, Cot: {j + 1}")
        else:
            print(f"- So {so_n} khong co trong ma tran.")

    except ValueError as e:
        print(f"Loi: {e}")
    except IndexError as e:
        print(f"Loi: {e}")
    except Exception as e:
        print(f"Loi khong xac dinh: {e}")
    finally:
        print("=== Ket thuc chuong trinh ===")


# Hàm hỗ trợ tính toán đặc biệt
def tinh_toan_tien_dien(old_reading, new_reading):
    """
    Tính toán tiền điện.

    Tham số:
        - old_reading (str) - Chỉ số cũ.
        - new_reading (str) - Chỉ số mới.

    Trả lại:
        - str: Kết quả tính toán.

    Ném lỗi:
        - MathError: Nếu chỉ số không hợp lệ.
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
            return f"- So Kwh dien tieu thu trong thang: {kwh} Kwh\n- So tien dien can tra trong thang: {total} VND"
        raise MathError("Chi so khong hop le")
    except (ValueError, TypeError):
        raise TypeErrorCustom("Chỉ số phải là số hợp lệ")


def tong_chu_so_lon_nhat_bang_n(digit_count, target_sum):
    """
    Tìm số lớn nhất có digit_count chữ số và tổng các chữ số bằng target_sum.

    Tham số:
        - digit_count (int) - Số chữ số.
        - target_sum (int) - Tổng các chữ số.

    Trả lại:
        - str: Số lớn nhất thỏa mãn điều kiện.

    Ném lỗi:
        - MathError: Nếu không thể tạo số thỏa mãn.
    """
    try:
        if not (
            isinstance(digit_count, (int, float))
            and isinstance(target_sum, (int, float))
        ) or not (float(digit_count).is_integer() and float(target_sum).is_integer()):
            raise NotIntegerError("Đầu vào phải là số nguyên")
        digits = abs(int(digit_count))
        total = abs(int(target_sum))
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
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def pythagore(side_a, side_b, side_c):
    """
    Tính cạnh còn lại trong tam giác vuông.

    Tham số:
        - side_a (float or bool) - Cạnh a.
        - side_b (float or bool) - Cạnh b.
        - side_c (float or bool) - Cạnh c.

    Trả lại:
        - str: Kết quả tính toán.

    Ném lỗi:
        - MathError: Nếu đầu vào không hợp lệ.
    """
    try:
        sides = [side_a, side_b, side_c]
        false_count = sides.count(False)
        if false_count > 1:
            raise MathError("Chỉ được để một cạnh là False")
        for side in sides:
            if side is not False and (not isinstance(side, (int, float)) or side < 0):
                raise MathError("Cạnh phải là số không âm")
        if side_a is False:
            if not (
                isinstance(side_b, (int, float)) and isinstance(side_c, (int, float))
            ):
                raise TypeErrorCustom("Cạnh phải là số")
            side_b, side_c = float(side_b), float(side_c)
            if side_c < side_b:
                raise MathError("Canh huyen phai lon hon canh goc vuong")
            result = math.sqrt(side_c**2 - side_b**2)
            return f"Canh goc vuong 1 = {result}"
        elif side_b is False:
            if not (
                isinstance(side_a, (int, float)) and isinstance(side_c, (int, float))
            ):
                raise TypeErrorCustom("Cạnh phải là số")
            side_a, side_c = float(side_a), float(side_c)
            if side_c < side_a:
                raise MathError("Canh huyen phai lon hon canh goc vuong")
            result = math.sqrt(side_c**2 - side_a**2)
            return f"Canh goc vuong 2 = {result}"
        elif side_c is False:
            if not (
                isinstance(side_a, (int, float)) and isinstance(side_b, (int, float))
            ):
                raise TypeErrorCustom("Cạnh phải là số")
            side_a, side_b = float(side_a), float(side_b)
            result = math.sqrt(side_a**2 + side_b**2)
            return f"Canh huyen = {result}"
        raise MathError("Dau vao khong hop le")
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


# Quy luật sinh dãy
def tao_danh_sach_quy_luat_1(total):
    """
    Tạo danh sách theo quy luật: 1 số ⋮ 1, 2 số ⋮ 2, 3 số ⋮ 3, ...

    Tham số:
        - total (int) - Tổng số lượng phần tử.

    Trả lại:
        - list: Danh sách theo quy luật.
    """
    try:
        if not isinstance(total, (int, float)) or not float(total).is_integer():
            raise NotIntegerError("Tổng số lượng phải là số nguyên")
        total = int(total)
        if total < 0:
            raise InvalidInputError("Tổng số lượng phải không âm")
        result = []
        step = 1
        while len(result) < total:
            for _ in range(step):
                if len(result) < total:
                    result.append(step)
            step += 1
        return result
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def tao_danh_sach_quy_luat_2(base, count):
    """
    Tạo danh sách các bội của base với count phần tử.

    Tham số:
        - base (int) - Số để tạo bội.
        - count (int) - Số phần tử.

    Trả lại:
        list: Danh sách các bội của base.
    """
    try:
        if not (
            isinstance(base, (int, float)) and isinstance(count, (int, float))
        ) or not (float(base).is_integer() and float(count).is_integer()):
            raise NotIntegerError("Cả hai tham số phải là số nguyên")
        base, count = int(base), int(count)
        if count < 0:
            raise InvalidInputError("Số phần tử phải không âm")
        return [base * i for i in range(count)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def tao_danh_sach_quy_luat_3(count, base):
    """
    Tạo danh sách lũy thừa của base từ 0 đến count.

    Tham số:
        - count (int) - Số lượng phần tử.
        - base (int) - Cơ số.

    Trả lại:
        - list: Danh sách lũy thừa của base.
    """
    try:
        if not (
            isinstance(count, (int, float)) and isinstance(base, (int, float))
        ) or not (float(count).is_integer() and float(base).is_integer()):
            raise NotIntegerError("Cả hai tham số phải là số nguyên")
        count, base = int(count), int(base)
        if count < 0:
            raise InvalidInputError("Số lượng phải không âm")
        return [base**i for i in range(count)]
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


# Đếm số nghịch thế
def dem_so_nghich_the(numbers):
    """
    Đếm số cặp nghịch thế trong danh sách.

    Tham số:
        - numbers (list) - Danh sách cần đếm.

    Trả lại:
        - int: Số cặp nghịch thế.
    """
    try:
        if not isinstance(numbers, (list, tuple)):
            raise ListError("Đầu vào phải là danh sách hoặc tuple")
        for num in numbers:
            if not isinstance(num, (int, float)):
                raise TypeErrorCustom("Phần tử phải là số")
        count = 0
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] > numbers[j]:
                    count += 1
        return count
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ")


def one_two_three():
    """
    Chơi kéo búa bao với A.I.

    Tham số:
        None

    Trả lại:
        None: In kết quả ra màn hình.

    Hướng dẫn:
        - Nhập số trận đấu.
        - Nhập lựa chọn của bạn (Keo, Bua, Bao).
    """
    choices = {1: "Keo", 2: "Bua", 3: "Bao"}
    human_score, ai_score = 0, 0
    try:
        matches = input("- Number of matches: ")
        if not matches.isdigit():
            raise NotIntegerError("Số trận đấu phải là số nguyên")
        matches = int(matches)
        if matches <= 0:
            raise InvalidInputError("Số trận đấu phải lớn hơn 0")
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
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")


def tao_day_chu(rows, columns, repeats):
    """
    Tạo dãy chữ với rows dòng, columns cột, 2 đường chéo, lặp lại repeats lần.

    Tham số:
        rows (int): Số dòng.
        columns (int): Số cột.
        repeats (int): Số lần lặp lại.

    Trả lại:
        None: In dãy chữ ra màn hình.

    Hướng dẫn:
        - Nhập chuỗi đầu tiên khi được yêu cầu.
    """
    try:
        if not (
            isinstance(rows, (int, float))
            and isinstance(columns, (int, float))
            and isinstance(repeats, (int, float))
        ) or not (
            float(rows).is_integer()
            and float(columns).is_integer()
            and float(repeats).is_integer()
        ):
            raise NotIntegerError("Tất cả tham số phải là số nguyên")
        rows, columns, repeats = int(rows), int(columns), int(repeats)
        if rows <= 0 or columns <= 0 or repeats < 0:
            raise InvalidInputError(
                "Số dòng, cột phải lớn hơn 0, số lần lặp phải không âm"
            )
        text = input("Nhap day dau tien: ")
        if not isinstance(text, str) or not text:
            raise InvalidInputError("Chuỗi đầu vào không thể rỗng")
        for _ in range(repeats):
            for _ in range(columns):
                for _ in range(rows):
                    print(text)
            for i in range(rows):
                print("  " * i + text)
            for i in range(rows - 1, -1, -1):
                print("  " * i + text)
    except (ValueError, TypeError):
        raise TypeErrorCustom("Đầu vào không hợp lệ hoặc không phải số")
