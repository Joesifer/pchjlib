################################################################################################
#
# Copyright (c) 2024 PCH_125
# Any act of hitting a subordinate will result in a beating
# Supported python versions = {"all"}
# Imported library = {"cmath", "collections", "math", "re", "sys", "time", "numpy", "roman"}
#
# MIT License
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


# __author__ = "PCH_125"
# __version__ = "Last version"
# __date__ = "28/1/2024"
# __copyright__ = "Copyright (c) 2024 PCH_125"
# __sumdef__= "57"

import cmath
import collections
import math
import re
import sys
import time

import numpy
import roman


# # Các hàm kiểm tra tính chất số nguyên tố và số nguyên tố liên quan:
# Hàm kiểm tra xem một số có phải là số nguyên tố hay không
def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


# Hàm tạo danh sách các số nguyên tố đến n
def tao_danh_sach_so_nguyen_to(n):
    if n < 5:
        n = 10
        prime_list = [i for i in range(n) if kiem_tra_so_nguyen_to(i) is True]
    else:
        prime_list = [i for i in range(n) if kiem_tra_so_nguyen_to(i) is True]
    return prime_list


# Hàm kiểm tra số emirp (trái với prime hay số nguyên tố)
def kiem_tra_so_emirp(n):
    if kiem_tra_so_nguyen_to(n) is True:
        reverse_n = int(str(n)[::-1])
        if n != reverse_n and kiem_tra_so_nguyen_to(reverse_n):
            return True
    return False


# Hàm tạo số emirp đến n (trái với prime hay số nguyên tố)
def tao_danh_sach_so_emirp(n):
    return [i for i in range(n) if kiem_tra_so_emirp(i) is True]


# # Các hàm liên quan đến số Fibonacci:
# Hàm tính số Fibonacci thứ n bằng cách sử dụng memoization
def vi_tri_so_Fibonacci(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = vi_tri_so_Fibonacci(n - 1, memo) + vi_tri_so_Fibonacci(n - 2, memo)
    return memo[n]


# Hàm tạo danh sách các số Fibonacci đến n
def tao_danh_sach_so_Fibonacci(n):
    return [vi_tri_so_Fibonacci(i) for i in range(n)]


# # Các hàm số hoàn thiện, số tự mãn, hứa hôn, hoàn hảo, thân thiết:
# Hàm tính tổng các ước số của n không tính n và không âm
def tong_uoc_so(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong


# Hàm tính tổng các chữ số của một số
def tong_chu_so(n):
    return sum(int(digit) for digit in str(n))


# Hàm kiểm tra xem một số có phải là số hoàn thiện
def kiem_tra_so_hoan_thien(n):
    if n < 1:
        return "LỖI TOÁN HỌC"
    else:
        divisors_sum = sum(i for i in range(1, n) if n % i == 0)
        return True if divisors_sum == n else False


# Hàm tạo danh sách các số hoàn thiện
def tao_danh_sach_so_hoan_thien(n):
    return [i for i in range(n) if kiem_tra_so_hoan_thien(i) is True]


# Hàm kiểm tra số tự mãn (số bằng tổng các mũ bậc ba của mỗi chữ số của nó)
def kiem_tra_so_tu_man(n):
    n = str(n)
    tong = sum(int(i) ** 3 for i in n)
    if tong == int(n):
        return True
    else:
        return False


# Hàm tạo danh sách các số tự mãn
def tao_danh_sach_so_tu_man(n):
    return [i for i in range(2, n) if kiem_tra_so_tu_man(i) is True]


# Hàm kiểm tra cặp số hứa hôn
def cap_so_hua_hon(a, b):
    if a < 0 or b < 0:
        return "LỖI TOÁN HỌC"
    else:
        sum_a = tong_uoc_so(a)
        sum_b = tong_uoc_so(b)
        return True if sum_a == b + 1 and sum_b == a + 1 else False


# Hàm kiểm tra số hoàn hảo
def kiem_tra_so_hoan_hao(number):
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == number


# Hàm tạo danh sách số hoàn hảo
def tao_danh_sach_so_hoan_hao(n):
    return [i for i in range(1, n) if kiem_tra_so_hoan_hao(i) is True]


# # Các hàm kiểm tra và tạo danh sách số chính phương:
# Hàm kiểm tra số chính phương
def kiem_tra_so_chinh_phuong(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n


# Hàm tạo danh sách các số chính phương đến n
def tao_danh_sach_so_chinh_phuong(n):
    return [i for i in range(n) if kiem_tra_so_chinh_phuong(i) is True]


# Hàm kiểm tra xem hai số có phải là các số thân thiết
def cap_so_than_thiet(a, b):
    if a <= 1 or b <= 1:
        return "LỖI TOÁN HỌC"
    else:
        sum_a = tong_uoc_so(a)
        sum_b = tong_uoc_so(b)
        return True if sum_a == b and sum_b == a else False


# Hàm kiểm tra số mạnh mẽ (nếu tổng chữ số nó là một số nguyên tố)
def kiem_tra_so_manh_me_1(n):
    n = str(n)
    if len(n) == 0:
        return False
    if len(n) > 0:
        n = int(n)
        if n < 0:
            return False
        else:
            if kiem_tra_so_nguyen_to(tong_chu_so(n)) is True:
                return True
            else:
                return False


# Hàm kiểm tra số mạnh mẽ (nếu một số vừa chia hết cho những số nguyên tố và bình phương của chúng trước nó)
def kiem_tra_so_manh_me_2(n):
    if n < 0:
        return False
    else:
        ds_snt = [i for i in range(n) if kiem_tra_so_nguyen_to(i) is True]
        ds_sntbp = [i**2 for i in ds_snt]
        t = len(ds_snt)
        if n == 1:
            return True
        for i in range(t):
            if n % ds_snt[i] == 0 and n % ds_sntbp[i] == 0:
                return True
            else:
                return False


# # Các hàm liên quan đến ước số và bội số:
# Hàm tạo danh sách các ước số của một số
def tao_danh_sach_uoc_so(n):
    if n == 0:
        return -1
    elif n != 0:
        n = abs(n)
        uoc = sorted(
            [i for i in range(1, n + 1) if n % i == 0]
            + [-i for i in range(1, n + 1) if n % i == 0]
        )
        return uoc


# Hàm tìm ước chung lớn nhất 2 số
def uoc_chung_lon_nhat(a, b):
    return math.gcd(a, b)


# Hàm tính ước số chung lớn của một danh sách các số
def uoc_chung_lon_nhat_cua_danh_sach(array):
    numbers = array
    if len(numbers) < 2 or 0 in numbers:
        return "LỖI TOÁN HỌC"
    else:
        kq = numbers[0]
        for i in range(1, len(numbers)):
            kq = uoc_chung_lon_nhat(kq, numbers[i])
            if kq == 1:
                break
        return kq


# Hàm tính bội số chung nhỏ nhất của hai số
def boi_chung_nho_nhat(a, b):
    return math.lcm(a, b)


# Hàm tính bội số chung nhỏ nhất của một danh sách các số
def boi_chung_nho_nhat_cua_danh_sach(array):
    numbers = array
    if len(numbers) < 2 or 0 in numbers:
        return "LỖI TOÁN HỌC"
    else:
        kq = numbers[0]
        for i in range(1, len(numbers)):
            kq = boi_chung_nho_nhat(kq, numbers[i])
            if kq == 1:
                break
        return kq


# Hàm tạo danh sách các bội số của một số lên đến 10 lần
def tao_danh_sach_boi_so(n):
    if n == 0:
        return "LỖI TOÁN HỌC"
    else:
        boi = [n * i for i in range(11)]
        return boi


# # Các hàm liên quan đến tính chất số song tố:
# Hàm kiểm tra các số song tố
def kiem_tra_so_song_to(n):
    if kiem_tra_so_nguyen_to(n) and kiem_tra_so_nguyen_to(tong_chu_so(n)):
        return True
    else:
        return False


# Hàm tạo danh sách các số song tố
def tao_danh_sach_so_song_to(n):
    so = [i for i in range(n) if kiem_tra_so_nguyen_to(i) is True]
    return so


# # Các hàm liên quan đến phân tích thừa số nguyên tố:
# Hàm tính các thừa số nguyên tố của một số (vip)
def thua_so_nguyen_to_day_du(n):
    # Hàm hỗ trợ cho phân tích số mũ (đơn giản hóa biểu thức mũ. VD: 2^1=2)
    def ho_tro_phan_tich_so_mu(s):
        yếu_tố = s.split()
        đếm_yếu_tố = collections.defaultdict(int)
        for y in yếu_tố:
            cơ_số, số_mũ = y.split("^")
            số_mũ = int(số_mũ)
            đếm_yếu_tố[cơ_số] = max(đếm_yếu_tố[cơ_số], số_mũ)
        yếu_tố_đơn_giản_hóa = [
            cơ_số if số_mũ == 1 else f"{cơ_số}^{số_mũ}"
            for cơ_số, số_mũ in đếm_yếu_tố.items()
        ]
        biểu_thức_đơn_giản_hóa = " ".join(yếu_tố_đơn_giản_hóa)
        return biểu_thức_đơn_giản_hóa

    # Hàm phân tích số mũ
    def phan_tich_so_mu(ds):
        dem = collections.Counter(ds)
        kq = " ".join([f"{num}^{exp}" for num, exp in dem.items()])
        return ho_tro_phan_tich_so_mu(kq)

    if n > 1:
        cac_uoc_so = []
        i = 2
        while n > 1:
            while n % i == 0:
                cac_uoc_so.append(i)
                n //= i
            i += 1
        ket_qua = phan_tich_so_mu(cac_uoc_so).split()
        phan_tich = " x ".join(ket_qua)
        uoc_so = " x ".join(str(i) for i in cac_uoc_so)
        return "- Phân tích: {}\n- Bỏ số mũ: {}".format(phan_tich, uoc_so)
    else:
        return "LỖI TOÁN HỌC"


# Hàm tính các thừa số nguyên tố của một số (ds)
def thua_so_nguyen_to(n):
    if n > 1:
        thua_so = []
        i = 2
        while n > 1:
            while n % i == 0:
                thua_so.append(i)
                n //= i
            i += 1
        return thua_so
    else:
        return "LỖI TOÁN HỌC"


# Hàm tính ước số chung lớn nhất nguyên tố của hai số
def uoc_chung_nguyen_to_2_so(a, b):
    thua_so_cua_a = set(thua_so_nguyen_to(a))
    thu_so_cua_b = set(thua_so_nguyen_to(b))
    uoc_chung_nguyen_to = thua_so_cua_a.intersection(thu_so_cua_b)
    if len(uoc_chung_nguyen_to) == 0:
        return "LỖI TOÁN HỌC"
    else:
        return max(uoc_chung_nguyen_to)


# # Các hàm liên quan đến phương trình và biểu thức toán học:
# Hàm giải phương trình bậc 1, 2 một ẩn và vài lưu ý, VD nhập: "12x^2 + 34 - 24 = 23x - 13"
def giai_pt_bac_1va2_dang_string(phuong_trinh):
    cac_tu_tach = [i for i in phuong_trinh]
    vt_hs_x = [i - 1 for i in range(len(phuong_trinh)) if phuong_trinh[i] == "x"]
    for i in range(len(vt_hs_x)):
        cac_tu_tach[vt_hs_x[i]] += " "
    cac_tu = ("".join(cac_tu_tach)).split()
    hs_dau_cong = [i + 1 for i in range(len(cac_tu)) if cac_tu[i] == "+"]
    hs_dau_tru = [i + 1 for i in range(len(cac_tu)) if cac_tu[i] == "-"]
    for i in range(len(hs_dau_cong)):
        cac_tu[hs_dau_cong[i]] = "+" + cac_tu[hs_dau_cong[i]]
    for i in range(len(hs_dau_tru)):
        cac_tu[hs_dau_tru[i]] = "-" + cac_tu[hs_dau_tru[i]]
    for i in range(len(cac_tu)):
        if cac_tu[i] == "+" or cac_tu[i] == "-":
            cac_tu[i] = ""
    cac_tu = (" ".join(cac_tu)).split()
    if "=" in cac_tu:
        dau_bang = cac_tu.index("=")
        ve_phai = cac_tu[dau_bang + 1 :]
        vt_cac_so_ve_phai = [
            ve_phai.index(i) for i in ve_phai if i != "x" and i != "x^2"
        ]
        cac_so_ve_phai = [str(-int(i)) for i in ve_phai if i != "x" and i != "x^2"]
        for i in range(len(vt_cac_so_ve_phai)):
            ve_phai[vt_cac_so_ve_phai[i]] = cac_so_ve_phai[i]  # type: ignore
        ve_trai = cac_tu[:dau_bang]
        pt = " ".join(ve_trai) + " " + " ".join(ve_phai)
        cac_tu = pt.split()
    else:
        cac_tu = (" ".join(cac_tu)).split()
    if "x^2" in cac_tu:
        he_so_x_bac_2 = [i - 1 for i in range(len(cac_tu)) if cac_tu[i] == "x^2"]
        he_so_x_bac_1 = [i - 1 for i in range(len(cac_tu)) if cac_tu[i] == "x"]
        a = sum([int(cac_tu[i]) for i in he_so_x_bac_2])
        b = sum([int(cac_tu[i]) for i in he_so_x_bac_1])
        for i in range(len(he_so_x_bac_1)):
            for j in range(len(he_so_x_bac_2)):
                cac_tu[he_so_x_bac_1[i]] = ""
                cac_tu[he_so_x_bac_2[j]] = ""
        chuoi_cuoi = [float(i) for i in cac_tu if i != "x" and i != "x^2" and i != ""]
        if len(chuoi_cuoi) == 0:
            c = 0
        else:
            c = sum(chuoi_cuoi)
        if a == 0:
            return "LỖI TOÁN HỌC"
        else:
            delta = b**2 - 4 * a * c
            if delta == 0:
                return "x = {}".format(-b / (2 * a))
            else:
                x1 = (-b + cmath.sqrt(delta)) / (2 * a)
                x2 = (-b - cmath.sqrt(delta)) / (2 * a)
                return "Nghiệm của phương trình là:\nx₁ = {}\nx₂ = {}".format(x1, x2)
    elif "x^2" not in cac_tu:
        he_so_x_bac_1 = [i - 1 for i in range(len(cac_tu)) if cac_tu[i] == "x"]
        a = sum([int(cac_tu[i]) for i in he_so_x_bac_1])
        for i in he_so_x_bac_1:
            cac_tu[i] = ""
        chuoi_cuoi = [float(i) for i in cac_tu if i != "x" and i != ""]
        if len(chuoi_cuoi) == 0:
            b = 0
        else:
            b = sum(i for i in chuoi_cuoi)
        if a == 0:
            if b == 0:
                return "Phương trình vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            return "x₁ = {}".format(-b / a)


# Hàm giải phương trình bậc 1 - 10 bằng cách nhập hệ số
def giai_phuong_trinh(bac, he_so_phuong_trinh):
    # Hàm giải phương trình bậc 1 bằng cách nhập hệ số
    def giai_phuong_trinh_bac_1(a, b):
        nghiem = numpy.roots([a, b])
        return "Nghiệm của phương trình là:\nx₁ = {}".format(nghiem[0])

    # Hàm giải phương trình bậc 2 bằng cách nhập hệ số
    def giai_phuong_trinh_bac_2(a, b, c):
        nghiem = numpy.roots([a, b, c])
        return "Nghiệm của phương trình là:\nx₁ = {}\nx₂ = {}".format(
            nghiem[0], nghiem[1]
        )

    # Hàm giải phương trình bậc 3 bằng cách nhập hệ số
    def giai_phuong_trinh_bac_3(a, b, c, d):
        nghiem = numpy.roots([a, b, c, d])
        return "Nghiệm của phương trình là:\nx₁ = {}\nx₂ = {}\nx₃ = {}".format(
            nghiem[0], nghiem[1], nghiem[2]
        )

    # Hàm giải phương trình bậc 4 bằng cách nhập hệ số
    def giai_phuong_trinh_bac_4(a, b, c, d, e):
        nghiem = numpy.roots([a, b, c, d, e])
        return "Nghiệm của phương trình là:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}".format(
            nghiem[0], nghiem[1], nghiem[2], nghiem[3]
        )

    # Hàm giải phương trình bậc 5 bằng cách nhập hệ số
    def giai_phuong_trinh_bac_5(a, b, c, d, e, f):
        nghiem = numpy.roots([a, b, c, d, e, f])
        return "Nghiệm của phương trình là:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}".format(
            nghiem[0], nghiem[1], nghiem[2], nghiem[3], nghiem[4]
        )

    # Hàm giải phương trình bậc 6 bằng cách nhập hệ số
    def giai_phuong_trinh_bac_6(a, b, c, d, e, f, g):
        nghiem = numpy.roots([a, b, c, d, e, f, g])
        return "Nghiệm của phương trình là:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}\nx₆ = {}".format(
            nghiem[0], nghiem[1], nghiem[2], nghiem[3], nghiem[4], nghiem[5]
        )

    # Hàm giải phương trình bậc 7 bằng cách nhập hệ số
    def giai_phuong_trinh_bac_7(a, b, c, d, e, f, g, h):
        nghiem = numpy.roots([a, b, c, d, e, f, g, h])
        return "Nghiệm của phương trình là:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}\nx₆ = {}\nx₇ = {}".format(
            nghiem[0], nghiem[1], nghiem[2], nghiem[3], nghiem[4], nghiem[5], nghiem[6]
        )

    # Hàm giải phương trình bậc 8 bằng cách nhập hệ số
    def giai_phuong_trinh_bac_8(a, b, c, d, e, f, g, h, i):
        nghiem = numpy.roots([a, b, c, d, e, f, g, h, i])
        return "Nghiệm của phương trình là:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}\nx₆ = {}\nx₇ = {}\nx₈ = {}".format(
            nghiem[0],
            nghiem[1],
            nghiem[2],
            nghiem[3],
            nghiem[4],
            nghiem[5],
            nghiem[6],
            nghiem[7],
        )

    # Hàm giải phương trình bậc 9 bằng cách nhập hệ số
    def giai_phuong_trinh_bac_9(a, b, c, d, e, f, g, h, i, j):
        nghiem = numpy.roots([a, b, c, d, e, f, g, h, i, j])
        return "Nghiệm của phương trình là:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}\nx₆ = {}\nx₇ = {}\nx₈ = {}\nx₉ = {}".format(
            nghiem[0],
            nghiem[1],
            nghiem[2],
            nghiem[3],
            nghiem[4],
            nghiem[5],
            nghiem[6],
            nghiem[7],
            nghiem[8],
        )

    # Hàm giải phương trình bậc 10 bằng cách nhập hệ số
    def giai_phuong_trinh_bac_10(a, b, c, d, e, f, g, h, i, j, k):
        nghiem = numpy.roots([a, b, c, d, e, f, g, h, i, j, k])
        return "Nghiệm của phương trình là:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}\nx₆ = {}\nx₇ = {}\nx₈ = {}\nx₉ = {}\nx₁₀= {}".format(
            nghiem[0],
            nghiem[1],
            nghiem[2],
            nghiem[3],
            nghiem[4],
            nghiem[5],
            nghiem[6],
            nghiem[7],
            nghiem[8],
            nghiem[9],
        )

    if bac == 1:
        return giai_phuong_trinh_bac_1(he_so_phuong_trinh[0], he_so_phuong_trinh[1])
    elif bac == 2:
        return giai_phuong_trinh_bac_2(
            he_so_phuong_trinh[0], he_so_phuong_trinh[1], he_so_phuong_trinh[2]
        )
    elif bac == 3:
        return giai_phuong_trinh_bac_3(
            he_so_phuong_trinh[0],
            he_so_phuong_trinh[1],
            he_so_phuong_trinh[2],
            he_so_phuong_trinh[3],
        )
    elif bac == 4:
        return giai_phuong_trinh_bac_4(
            he_so_phuong_trinh[0],
            he_so_phuong_trinh[1],
            he_so_phuong_trinh[2],
            he_so_phuong_trinh[3],
            he_so_phuong_trinh[4],
        )
    elif bac == 5:
        return giai_phuong_trinh_bac_5(
            he_so_phuong_trinh[0],
            he_so_phuong_trinh[1],
            he_so_phuong_trinh[2],
            he_so_phuong_trinh[3],
            he_so_phuong_trinh[4],
            he_so_phuong_trinh[5],
        )
    elif bac == 6:
        return giai_phuong_trinh_bac_6(
            he_so_phuong_trinh[0],
            he_so_phuong_trinh[1],
            he_so_phuong_trinh[2],
            he_so_phuong_trinh[3],
            he_so_phuong_trinh[4],
            he_so_phuong_trinh[5],
            he_so_phuong_trinh[6],
        )
    elif bac == 7:
        return giai_phuong_trinh_bac_7(
            he_so_phuong_trinh[0],
            he_so_phuong_trinh[1],
            he_so_phuong_trinh[2],
            he_so_phuong_trinh[3],
            he_so_phuong_trinh[4],
            he_so_phuong_trinh[5],
            he_so_phuong_trinh[6],
            he_so_phuong_trinh[7],
        )
    elif bac == 8:
        return giai_phuong_trinh_bac_8(
            he_so_phuong_trinh[0],
            he_so_phuong_trinh[1],
            he_so_phuong_trinh[2],
            he_so_phuong_trinh[3],
            he_so_phuong_trinh[4],
            he_so_phuong_trinh[5],
            he_so_phuong_trinh[6],
            he_so_phuong_trinh[7],
            he_so_phuong_trinh[8],
        )
    elif bac == 9:
        return giai_phuong_trinh_bac_9(
            he_so_phuong_trinh[0],
            he_so_phuong_trinh[1],
            he_so_phuong_trinh[2],
            he_so_phuong_trinh[3],
            he_so_phuong_trinh[4],
            he_so_phuong_trinh[5],
            he_so_phuong_trinh[6],
            he_so_phuong_trinh[7],
            he_so_phuong_trinh[8],
            he_so_phuong_trinh[9],
        )
    elif bac == 10:
        return giai_phuong_trinh_bac_10(
            he_so_phuong_trinh[0],
            he_so_phuong_trinh[1],
            he_so_phuong_trinh[2],
            he_so_phuong_trinh[3],
            he_so_phuong_trinh[4],
            he_so_phuong_trinh[5],
            he_so_phuong_trinh[6],
            he_so_phuong_trinh[7],
            he_so_phuong_trinh[8],
            he_so_phuong_trinh[9],
            he_so_phuong_trinh[10],
        )
    else:
        return "CHƯA CÓ!"


# Hàm tính căn bậc n của một số
def can_bac(n, so_can):
    if so_can != 0:
        return n ** (1 / so_can)
    else:
        return "LỖI TOÁN HỌC"


# # Các hàm liên quan đến trích xuất và xử lý chuỗi:
# Hàm loại bỏ các phần tử trùng lặp từ một danh sách
def danh_sach_khong_trung_lap(lst):
    return sorted(list(set(lst)), reverse=True)


# Hàm loại bỏ các ký tự trùng lặp từ một chuỗi
def ki_tu_khong_trung_lap(string):
    return "".join(sorted(set(string), reverse=False))


# Hàm trích xuất các chữ số từ một chuỗi
def trich_xuat_chu_so_tu_chuoi(s):
    return [int(digit) for digit in re.findall(r"\d", s)]


# Hàm trích xuất các số từ một chuỗi
def trich_xuat_so_tu_chuoi(s):
    return [int(number) for number in re.findall(r"\d+", s)]


# Hàm trích xuất các ký tự không phải là chữ số từ một chuỗi
def trich_xuat_ki_tu(s):
    return re.findall(r"\D", s)


# Hàm ẩn kí tự dạng "234343" == "••••••"
def an_ki_tu(s):
    danh_sach = [i for i in s]
    if len(danh_sach) == 0:
        return "•"
    if len(danh_sach) > 0:
        if "/" not in danh_sach:
            return "".join("•" for i in range(len(s)))
        else:
            an = ["•" for _ in ("".join([i for i in danh_sach if i != "/"]))]
            vt = [i for i in range(len(s)) if danh_sach[i] == "/"]
            for i in range(len(vt)):
                an.insert(vt[i], "/")
            return "".join(an)


# Hàm trích xuất các số từ chuỗi số. VD: "32/232343244" sẽ là 32.232343244
def trich_xuat_cac_so_tu_so(s):
    s = str(s)
    if len(s) == 0:
        return 0
    if len(re.findall(r"\d+", s)) == 0:
        return 0
    if "-" in re.findall(
        r"\D", s
    ):  # Hỗ trợ cho tính toán vật lý 8, tiền điện. Không cần thì ẩn
        return -1
    if len(re.findall(r"\D", s)) > 0:
        D = re.findall(r"\D", s)
        if "." in D:
            c = len([i for i in D if i == "."])
            if c == 1:
                dau_cham = s.index(".")
                s1 = "".join(re.findall(r"\d", s[:dau_cham]))
                st = "".join(re.findall(r"\d", s[dau_cham + 1 :]))
                return float(s1 + "." + st)
            if s[-1] == ".":
                if c == 1:
                    chuoi_so = float("".join(re.findall(r"\d+", s)))
                    return chuoi_so
                if c > 1:
                    chuoi_so = str(".".join(re.findall(r"\d+", s)))
                    dau_cham = chuoi_so.index(".")
                    s1 = chuoi_so[:dau_cham]
                    st = str("".join(re.findall(r"\d", chuoi_so[dau_cham + 1 :])))
                    return float(s1 + "." + st)
            if s[0] == ".":
                chuoi_so = int("".join(re.findall(r"\d+", s)))
                return float("0." + str(chuoi_so))
            if s[-1] != ".":
                chuoi_so = str(".".join(re.findall(r"\d+", s)))
                dau_cham = chuoi_so.index(".")
                s1 = chuoi_so[:dau_cham]
                st = str("".join(re.findall(r"\d", chuoi_so[dau_cham + 1 :])))
                return float(s1 + "." + st)
            if c == 0 and len(D) == 0:
                chuoi_so = float("".join(re.findall(r"\d+", s)))
                return chuoi_so
        elif "." not in D:
            if len(D) == 0:
                chuoi_so = float("".join(re.findall(r"\d+", s)))
                return chuoi_so
            if len(D) != 0:
                if len([i for i in D if i == "."]) == 0:
                    chuoi_so = str(".".join(re.findall(r"\d+", s)))
                    dau_cham = chuoi_so.index(".")
                    s1 = chuoi_so[:dau_cham]
                    st = str("".join(re.findall(r"\d", chuoi_so[dau_cham + 1 :])))
                    return float(s1 + "." + st)
            if (
                s[0] != "."
                and len(re.findall(r"\d+", s)) != 0
                and len(D) == 1
                and s[0].isdigit() is False
            ):
                chuoi_so = "0" + s
                chuoi = ".".join(re.findall(r"\d+", chuoi_so))
                dau_cham = chuoi.index(".")
                s1 = chuoi[:dau_cham]
                st = str("".join(re.findall(r"\d", chuoi[dau_cham + 1 :])))
                return float(s1 + "." + st)
            if (
                s[-1] != "."
                and len(re.findall(r"\d+", s)) != 0
                and len(D) == 1
                and s[-1].isdigit() is False
            ):
                chuoi_so = s + "0"
                chuoi = ".".join(re.findall(r"\d+", chuoi_so))
                dau_cham = chuoi.index(".")
                s1 = chuoi[:dau_cham]
                st = str("".join(re.findall(r"\d", chuoi[dau_cham + 1 :])))
                return float(s1 + "." + st)
            if len([i for i in D if i == "."]) == 0:
                chuoi_so = float("".join(re.findall(r"\d+", s)))
                return chuoi_so
    elif len(re.findall(r"\D", s)) == 0:
        chuoi_so = float("".join([i for i in s]))
        return chuoi_so


# Hàm nén xâu
def xau_duoc_nen(s):
    ket_qua = ""
    dem = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            dem += 1
        else:
            if dem > 1:
                ket_qua += str(dem) + s[i - 1]
            else:
                ket_qua += s[i - 1]
            dem = 1
    if dem > 1:
        ket_qua += str(dem) + s[-1]
    else:
        ket_qua += s[-1]
    return ket_qua


# Hàm nén xâu nhưng không ghi số. VD: "hhhooccsiinh" == "hocsinh"
def xau_duoc_nen_ko_so(chuoi_nhap):
    ket_qua = chuoi_nhap[0]
    for ky_tu in chuoi_nhap[1:]:
        if ky_tu != ket_qua[-1]:
            ket_qua += ky_tu
    return ket_qua


# Hàm giải nén xâu
def xau_duoc_giai_nen(s):
    ket_qua = ""
    so_luong = ""
    for i in s:
        if i.isdigit():
            so_luong += i
        else:
            if so_luong == "":
                ket_qua += i
            else:
                ket_qua += int(so_luong) * i
                so_luong = ""
    return ket_qua


# # Khác
# Hàm chuyển đổi số bình thường thành số La Mã
def chuyen_doi_so_la_ma(num):
    return roman.toRoman(num)


# Hàm đếm số nghịch thế trong một danh sách
def dem_so_nghich_the(danh_sach):
    dem = 0
    i = 0
    while i < len(danh_sach):
        for j in range(len(danh_sach)):
            if (i < j) and (danh_sach[i] > danh_sach[j]):
                dem += 1
        i += 1
    return dem


# Hàm định lý Pythagore
def pythagore(a, b, c):
    sides = [a, b, c]
    if sides.count(False) > 1 or any(side < 0 for side in sides):
        return "LỖI TOÁN HỌC"
    if a is False:
        if c < b:
            return "LỖI TOÁN HỌC"
        else:
            side = math.sqrt(c**2 - b**2)
            return "Cạnh góc vuông 1 = {}".format(side)
    elif b is False:
        if c < a:
            return "LỖI TOÁN HỌC"
        else:
            side = math.sqrt(c**2 - a**2)
            return "Cạnh góc vuông 2 = {}".format(side)
    elif c is False:
        side = math.sqrt(a**2 + b**2)
        return "Cạnh huyền = {}".format(side)


# Hàm mô phỏng quá trình "Tải xuống"
def mp_tai_xuong(n):
    if n < 0 or n > 88 or n <= 1:
        print("AGAIN")
    else:
        n = int(n)
        for i in range(n):
            sys.stdout.write(
                "Đang tải xuống [{}{}] {}%\r".format(
                    "■" * i, " " * (n - 1 - i), (i + 1) * 100 // n
                )
            )
            sys.stdout.flush()
            time.sleep(0.1)
        print("\n{}".format("Tải xuống hoàn tất!"))


# Hàm mô phỏng quá trình "tính toán"
def mp_tinh_toan(n):
    if n < 0 or n >= 88:
        print("NO")
    else:
        n = int(n)
        for i in range(n):
            sys.stdout.write(
                "    AD: Đang tính toán [{}{}] {}%\r".format(
                    "■" * i, " " * (n - 1 - i), (i + 1) * 100 // n
                )
            )
            sys.stdout.flush()
            time.sleep(0.2)


# Hàm mô phỏng quá trình "LOADING..."
def mp_loading(n):
    sys.stdout.write("LOADING")
    sys.stdout.flush()
    time.sleep(0.5)
    for __ in range(n):
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.4)
        sys.stdout.write("\b\b\b   \b\b\b")
        sys.stdout.flush()


# Hàm mô phỏng cây thông
def mp_christmas_tree():
    n = 9  # Để tạo cây thông đẹp thì cho n = 9
    for i in range(1, n + 1):
        for __ in range(n - i + 5):
            print(" ", end=" ")
        for _ in range(2 * i - 5):
            print("*", end=" ")
        print()
    for i in range(3):
        print("                     ", end="")
        print(" * ")


# # Hàm hỗ trợ tính toán đặc biệt
# Hàm tính toán các công thức vật lý
def tinh_toan_vat_ly_8():
    print(
        "\n",
        " —————————————————————————————————————————————————————————————————————————————————————",
        "\n",
        "|                 >>>>> NHẬP TÊN CÔNG THỨC BẠN MUỐN ĐỂ ADMIN TÍNH <<<<<               |",
        "\n",
        "|                         ~~~ ! Lưu ý: Nhập theo yêu cầu ! ~~~                        |",
        "\n",
        "|                                                                                     |",
        "\n",
        "|        --> 1. Công thức tính: Khối lượng riêng      (kí hiệu D, Kg/m^3)             |",
        "\n",
        "|        --> 2. Công thức tính: Trọng lượng riêng     (kí hiệu d, đơn vị N/m^3)       |",
        "\n",
        "|        --> 3. Công thức tính: Lực đẩy Archimedes    (kí hiệu Fa, đơn vị N)          |",
        "\n",
        "|        --> 4. Công thức tính: Trọng lượng           (kí hiệu P, đơn vị N)           |",
        "\n",
        "|        --> 5. Công thức tính: Áp suất chất rắn      (kí hiệu p, N/m^2)              |",
        "\n",
        "|        --> 6. Công thức tính: Áp suất chất lỏng     (kí hiệu p, N/m^2)              |",
        "\n",
        " ———————————————————————————————————————————————————————————————————————————————————--",
    )
    n = str(input("    AD: Nhập công thức bạn chọn để AD tính: "))
    chuoi_so = [i for i in n]
    if chuoi_so[0].isdigit() is True:
        n = int(chuoi_so[0])
    if n == 1:
        h = int(
            input(
                "    AD: Có trọng lượng nhưng không có khối lượng thì nhập (1 là Có, 2 là Không): ",
            )
        )
        if h != 1 and h != 2:
            print("    AD: Nhập số 1 và 2 cơ mà🤨", "\n")
        if h == 1:
            P = str(input("- Nhập trọng lượng của chất (N): "))
            V = str(input("- Nhập thể tích của chất (m^3): "))
            P = trich_xuat_cac_so_tu_so(P)
            V = trich_xuat_cac_so_tu_so(V)
            m = P / 9.8  # type: ignore
            D = m / V
            if D > 0:
                mp_tinh_toan(30)
                print("\n", "   AD: Khối lượng riêng của chất là: ", D, "kg/m^3", "\n")
            else:
                print("    AD: Bà cho số âm chi dzẫy", "\n")
        if h == 2:
            m = str(input("- Nhập khối lượng của chất (kg): "))
            V = str(input("- Nhập thể tích của chất (m^3): "))
            m = trich_xuat_cac_so_tu_so(m)
            V = trich_xuat_cac_so_tu_so(V)
            D = m / V  # type: ignore
            if D >= 0:
                mp_tinh_toan(30)
                print("\n", "   AD: Khối lượng riêng của chất là: ", D, "kg/m^3", "\n")
            else:
                print("    AD: Bà cho số âm chi dzẫy", "\n")
    elif n == 2:
        h = int(
            input(
                "    AD: Có khối lượng nhưng không có trọng lượng thì nhập (1 là Có, 2 là Không): "
            )
        )
        if h != 1 and h != 2:
            print("    AD: Nhập số 1 và 2 cơ mà🤨", "\n")
        elif h == 2:
            P = str(input("- Nhập trọng lượng của chất (N): "))
            V = str(input("- Nhập thể tích của chất (m^3): "))
            P = trich_xuat_cac_so_tu_so(P)
            V = trich_xuat_cac_so_tu_so(V)
            d = P / V  # type: ignore
            if d >= 0:
                mp_tinh_toan(30)
                print(
                    "\n", "   AD: Trọng lượng riêng của chất đó là: ", d, "N/m^3", "\n"
                )
            else:
                print("    AD: Bà cho số âm chi dzẫy", "\n")
        elif h == 1:
            m = str(input("- Nhập khối lượng của chất (kg): "))
            V = str(input("- Nhập thể tích của chất (m^3): "))
            m = trich_xuat_cac_so_tu_so(m)
            V = trich_xuat_cac_so_tu_so(V)
            d = 9.8 * m / V  # type: ignore
            if d >= 0:
                mp_tinh_toan(30)
                print(
                    "\n", "   AD: Trọng lượng riêng của chất đó là: ", d, "N/m^3", "\n"
                )
            else:
                print("    AD: Bà cho số âm chi dzẫy", "\n")
    elif n == 3:
        d = str(input("- Nhập trọng lượng riêng của chất lỏng (N/m^3): "))
        V = str(input("- Nhập thể tích mà chất lỏng bị chiếm bởi vật (m^3): "))
        d = trich_xuat_cac_so_tu_so(d)
        V = trich_xuat_cac_so_tu_so(V)
        Fa = d * V  # type: ignore
        if Fa >= 0:
            mp_tinh_toan(30)
            print(
                "\n", "   AD: Lực đẩy Archimedes tác dụng lên vật là: ", Fa, "N", "\n"
            )
        else:
            print("    AD: Bà cho số âm chi dzẫy", "\n")
    elif n == 4:
        m = str(input("- Nhập khối lượng của vật (kg): "))
        m = trich_xuat_cac_so_tu_so(m)
        P = m * 9.8  # type: ignore
        if P >= 0:
            mp_tinh_toan(30)
            print("\n", "   AD: Trọng lượng của chất đó là: ", P, "N", "\n")
        else:
            print("    AD: Bà cho số âm chi dzẫy", "\n")
    elif n == 5:
        F = str(input("- Nhập áp lực lên bề mặt đó (kí hiệu F hoặc P, đơn vị N): "))
        S = str(input("- Nhập diện tích bề mặt tiếp xúc (m^2): "))
        F = trich_xuat_cac_so_tu_so(F)
        S = trich_xuat_cac_so_tu_so(S)
        p = F / S  # type: ignore
        if p >= 0:
            mp_tinh_toan(30)
            print(
                "\n",
                "   AD: Áp suất của vật lên bề mặt là (Áp suất chất rắn): ",
                p,
                "N/m^2",
                "\n",
            )
        else:
            print("    AD: Bà cho số âm chi dzẫy", "\n")
    elif n == 6:
        d = str(input("- Nhập trọng lượng riêng chất lỏng đó (N/m^3): "))
        h = str(
            input("- Nhập chiều sâu từ trên xuống của vật trong chất lỏng đó (m): ")
        )
        d = trich_xuat_cac_so_tu_so(d)
        h = trich_xuat_cac_so_tu_so(h)
        p = d * h  # type: ignore
        if p >= 0:
            mp_tinh_toan(30)
            print("\n", "   AD: Áp suất chất lỏng là: ", p, "N/m^2", "\n")
        else:
            print("    AD: Bà cho số âm chi dzẫy", "\n")
    else:
        print("    AD: Chọn lại giùm tuiii😒", "\n")


# Hàm tính toán tiền điện a là chỉ số cũ, b là chỉ số mới (b > a)
def tinh_toan_tien_dien(chi_so_cu, chi_so_moi):
    a = trich_xuat_cac_so_tu_so(chi_so_cu)
    b = trich_xuat_cac_so_tu_so(chi_so_moi)
    if b > a and a > 0 and b > 0:  # type: ignore
        skw = b - a  # type: ignore
        if 0 <= skw < 51:
            TT = skw * 1678
        elif 50 < skw < 101:
            TT = ((skw - 50) * 1734) + 50 * 1678
        elif 100 < skw < 201:
            TT = ((skw - 100) * 2014) + 50 * 1734 + 50 * 1678
        elif 200 < skw < 301:
            TT = ((skw - 200) * 2536) + 100 * 2014 + 50 * 1734 + 50 * 1678
        elif 300 < skw < 401:
            TT = ((skw - 300) * 2834) + 100 * 2536 + 100 * 2014 + 50 * 1734 + 50 * 1678
        elif 400 < skw:
            TT = (
                ((skw - 400) * 2927)
                + 100 * 2834
                + 100 * 2536
                + 100 * 2014
                + 50 * 1734
                + 50 * 1678
            )
        return "- Số Kwh điện tiêu thụ trong tháng: {} Kwh\n- Số tiền điện cần trả trong tháng: {} VNĐ".format(
            skw, TT  # type: ignore
        )
    else:
        return "KHÔNG ĐƯỢC"


# Hàm tìm một số lớn nhất có tổng các chữ "a" số bằng số "b". VD: 3,21 sẽ bằng 993
def tong_chu_so_lon_nhat_bang_n(number_of_digits, int_number):
    sct = []
    a = int(abs(number_of_digits))
    b = int(abs(int_number))
    if a != 0 and b != 0:
        if b < 10:
            if a == 1:
                return b
            if a == 2:
                if b == 2:
                    return 20
                else:
                    for i in range(1, 10):
                        for j in range(10, 1, -1):
                            if i + j == b:
                                sct.append(j)
                                sct.append(i)
                        break
                    return "{}{}".format(sct[0], sct[1])
            if a > 2:
                sct.append(str(b))
                a -= len(sct)
                for i in range(a):
                    sct.append("0")
                return "".join(sct)
        if 9 < b < 19:
            if a == 2:
                for i in range(1, 10):
                    if i + 9 == b:
                        return "9" + str(i)
            if a > 2:
                for i in range(1, 10):
                    if i + 9 == b:
                        sct.append("9")
                        sct.append(str(i))
                        break
                a -= len(sct)
                for i in range(a):
                    sct.append("0")
                return "".join(sct)
            if a < 2:
                return False
        if 18 < b:
            if a == 2:
                return False
            if a > 2:
                for i in range(b // 9):
                    if i * 9 < b:
                        sct.append(9)
                tinh = "".join([str(i) for i in sct])
                tong_sct = sum(sct)
                if tong_sct < b:
                    tru = str(b - tong_sct)
                elif tong_sct == b:
                    tru = ""
                tinh += tru  # type: ignore
                len_tinh = len(tinh)
                if a == len_tinh:
                    return tinh
                elif a > len_tinh:
                    tam_a = a - len_tinh
                    for i in range(tam_a):
                        tinh += "0"
                    return tinh
                elif a < len_tinh:
                    return False
            if a < 2:
                return False
    else:
        return False


# Hàm chuyển hóa chuỗi thành mật mã Caesar
def chuyen_hoa_caesar(string, sang_trai_k_so):
    string = "".join([i for i in string.upper() if i != " "]).strip()
    s_ = {}
    ss_ = {}
    kq = []
    kq_ = []
    ds = [i + sang_trai_k_so for i in range(0, 26) if i + sang_trai_k_so < 26] + [
        i
        for i in range(
            25
            - len([i + sang_trai_k_so for i in range(0, 26) if i + sang_trai_k_so < 26])
            + 1
        )
    ]

    for i in range(26):
        s__ = {[chr(j) for j in range(65, 65 + 26)][i]: i}
        s_.update(s__)

    for i in range(26):
        ss__ = {i: ds[i]}
        ss_.update(ss__)

    for i in string:
        kq.append(s_[i])

    for i in kq:
        kq_.append(ss_[i])

    return kq_


# Hàm mã hóa dãy số Caesar
def ma_hoa_caesar(array, sang_trai_k_so):
    s_ = {}
    ss_ = {}
    kq = []
    kq_ = []
    ds = [i + sang_trai_k_so for i in range(0, 26) if i + sang_trai_k_so < 26] + [
        i
        for i in range(
            25
            - len([i + sang_trai_k_so for i in range(0, 26) if i + sang_trai_k_so < 26])
            + 1
        )
    ]

    for i in range(26):
        s__ = {i: [chr(j) for j in range(65, 65 + 26)][i]}
        s_.update(s__)

    for i in range(26):
        ss__ = {ds[i]: i}
        ss_.update(ss__)

    for i in array:
        kq.append(ss_[i])

    for i in kq:
        kq_.append(str(s_[i]))

    return "".join(kq_)


# # Quy luật.
# Hàm tạo danh sách các số theo quy luật: 1 số :: 1, 2 số :: 2, 3 số :: 3, ... cho tới tổng số lượng là number (dấu :: là dấu chia hết)
def tao_danh_sach_quy_luat_1(number):
    def ho_tro(number):
        if number == 1:
            return 1
        socantim = 1
        vi_tri = 0
        for i in range(1, 1000):
            socantim = (socantim // i + 1) * i
            vi_tri += 1
            if vi_tri == number:
                return socantim
            for _ in range(0, i - 1):
                socantim += i
                vi_tri += 1
                if vi_tri == number:
                    return socantim

    return [ho_tro(i) for i in range(1, number + 1)]


# Hàm tạo một dãy số theo quy luật: mỗi phần tử của dãy số vô hạn này tăng theo n đơn vị.
def tao_danh_sach_quy_luat_2(number, n):
    return [i + n for i in range(number)]


# Hàm tạo dãy số theo quy luật: số mũ nâng tới n của số number.
def tao_danh_sach_quy_luat_3(number, n):
    return [number**i for i in range(n)]
