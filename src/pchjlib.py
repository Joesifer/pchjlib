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

Tác giả
---------------------------------------------------------
- Joesifer.

Phiên bản
---------------------------------------------------------
- 0.0.3.6.

Ngày đăng
---------------------------------------------------------
- ngày 14 tháng Hai, năm 2024.

Bản quyền
---------------------------------------------------------
- Copyright (c) 2024 Joesifer.

Phiên bản python được hỗ trợ
---------------------------------------------------------
- lớn hơn hoặc bằng 3.7.

Thư viện được thêm vào
---------------------------------------------------------
- cmath, collections, math, re, sys, time, numpy, roman.

License.
---------------------------------------------------------
- MIT License.

Thông tin
---------------------------------------------------------

Nếu bạn không biết cách dùng thì hãy::

  >>> Truy cập: `https://github.com/Joesifer/pchjlib/blob/main/README.md` .

Và bạn có thể góp ý hoặc ủng hộ bằng::

  >>> Gửi email : `phanchanhung12055@gmail.com` .


CẢM ƠN!
================================

"""

import cmath, collections, math, random, re, sys, time, numpy, roman


# # Cac ham kiem tra tinh chat so nguyen to va so nguyen to lien quan:
# Ham kiem tra xem mot so co phai la so nguyen to hay khong
def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


# Ham tao danh sach cac so nguyen to den n
def tao_danh_sach_so_nguyen_to(n):
    if n < 5:
        n = 10
        prime_list = [i for i in range(n) if kiem_tra_so_nguyen_to(i) is True]
    else:
        prime_list = [i for i in range(n) if kiem_tra_so_nguyen_to(i) is True]
    return prime_list


# Ham kiem tra so emirp (trai voi prime hay so nguyen to)
def kiem_tra_so_emirp(n):
    if kiem_tra_so_nguyen_to(n) is True:
        reverse_n = int(str(n)[::-1])
        if n != reverse_n and kiem_tra_so_nguyen_to(reverse_n):
            return True
    return False


# Ham tao so emirp den n (trai voi prime hay so nguyen to)
def tao_danh_sach_so_emirp(n):
    return [i for i in range(n) if kiem_tra_so_emirp(i) is True]


# # Cac ham lien quan den so Fibonacci:
# Ham tinh so Fibonacci thu n bang cach su dung memoization
def vi_tri_so_Fibonacci(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = vi_tri_so_Fibonacci(n - 1, memo) + vi_tri_so_Fibonacci(n - 2, memo)
    return memo[n]


# Ham tao danh sach cac so Fibonacci den n
def tao_danh_sach_so_Fibonacci(n):
    return [vi_tri_so_Fibonacci(i) for i in range(n)]


# # Cac ham so hoan thien, so tu man, hua hon, hoan hao, than thiet:
# Ham tinh tong cac uoc so cua n khong tinh n va khong am
def tong_uoc_so(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong


# Ham tinh tong cac chu so cua mot so
def tong_chu_so(n):
    return sum(int(digit) for digit in str(n))


# Ham kiem tra xem mot so co phai la so hoan thien
def kiem_tra_so_hoan_thien(n):
    if n < 1:
        return "LOI TOAN HOC"
    else:
        divisors_sum = sum(i for i in range(1, n) if n % i == 0)
        return True if divisors_sum == n else False


# Ham tao danh sach cac so hoan thien
def tao_danh_sach_so_hoan_thien(n):
    return [i for i in range(n) if kiem_tra_so_hoan_thien(i) is True]


# Ham kiem tra so tu man (so bang tong cac mu bac ba cua moi chu so cua no)
def kiem_tra_so_tu_man(n):
    n = str(n)
    tong = sum(int(i) ** 3 for i in n)
    if tong == int(n):
        return True
    else:
        return False


# Ham tao danh sach cac so tu man
def tao_danh_sach_so_tu_man(n):
    return [i for i in range(2, n) if kiem_tra_so_tu_man(i) is True]


# Ham kiem tra cap so hua hon
def cap_so_hua_hon(a, b):
    if a < 0 or b < 0:
        return "LOI TOAN HOC"
    else:
        sum_a = tong_uoc_so(a)
        sum_b = tong_uoc_so(b)
        return True if sum_a == b + 1 and sum_b == a + 1 else False


# Ham kiem tra so hoan hao
def kiem_tra_so_hoan_hao(number):
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == number


# Ham tao danh sach so hoan hao
def tao_danh_sach_so_hoan_hao(n):
    return [i for i in range(1, n) if kiem_tra_so_hoan_hao(i) is True]


# # Cac ham kiem tra va tao danh sach so chinh phuong:
# Ham kiem tra so chinh phuong
def kiem_tra_so_chinh_phuong(n):
    if n < 0:
        return False
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n


# Ham tao danh sach cac so chinh phuong den n
def tao_danh_sach_so_chinh_phuong(n):
    return [i for i in range(n) if kiem_tra_so_chinh_phuong(i) is True]


# Ham kiem tra xem hai so co phai la cac so than thiet
def cap_so_than_thiet(a, b):
    if a <= 1 or b <= 1:
        return "LOI TOAN HOC"
    else:
        sum_a = tong_uoc_so(a)
        sum_b = tong_uoc_so(b)
        return True if sum_a == b and sum_b == a else False


# Ham kiem tra so manh me (neu tong chu so no la mot so nguyen to)
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


# Ham kiem tra so manh me (neu mot so vua chia het cho nhung so nguyen to va binh phuong cua chung truoc no)
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


# # Cac ham lien quan den uoc so va boi so:
# Ham tao danh sach cac uoc so cua mot so
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


# Ham tim uoc chung lon nhat 2 so
def uoc_chung_lon_nhat(a, b):
    return math.gcd(a, b)


# Ham tinh uoc so chung lon cua mot danh sach cac so
def uoc_chung_lon_nhat_cua_danh_sach(array):
    numbers = array
    if len(numbers) < 2 or 0 in numbers:
        return "LOI TOAN HOC"
    else:
        kq = numbers[0]
        for i in range(1, len(numbers)):
            kq = uoc_chung_lon_nhat(kq, numbers[i])
            if kq == 1:
                break
        return kq


# Ham tinh boi so chung nho nhat cua hai so
def boi_chung_nho_nhat(a, b):
    return math.lcm(a, b)


# Ham tinh boi so chung nho nhat cua mot danh sach cac so
def boi_chung_nho_nhat_cua_danh_sach(array):
    numbers = array
    if len(numbers) < 2 or 0 in numbers:
        return "LOI TOAN HOC"
    else:
        kq = numbers[0]
        for i in range(1, len(numbers)):
            kq = boi_chung_nho_nhat(kq, numbers[i])
            if kq == 1:
                break
        return kq


# Ham tao danh sach cac boi so cua mot so len den 10 lan
def tao_danh_sach_boi_so(n):
    if n == 0:
        return "LOI TOAN HOC"
    else:
        boi = [n * i for i in range(11)]
        return boi


# Ham tao gia tri cac uoc chung cua mot danh sach
def uoc_chung_cua_danh_sach(arr):
    def ho_tro(n):
        if n == 0:
            return {1}
        else:
            n = abs(n)
            uoc = [i for i in range(1, n + 1) if n % i == 0] + [
                -i for i in range(1, n + 1) if n % i == 0
            ]
            return set(uoc)

    for i in range(len(arr) - 1):
        kq = ho_tro(arr[i]).intersection(ho_tro(arr[i + 1]))
    return sorted(list(kq), reverse=False)


# # Cac ham lien quan den tinh chat so song to va so phong phu:
# Ham kiem tra cac so song to
def kiem_tra_so_song_to(n):
    if kiem_tra_so_nguyen_to(n) and kiem_tra_so_nguyen_to(tong_chu_so(n)):
        return True
    else:
        return False


# Ham tao danh sach cac so song to
def tao_danh_sach_so_song_to(n):
    so = [i for i in range(n) if kiem_tra_so_nguyen_to(i) is True]
    return so


# Ham kiem tra cac so phong phu.
def kiem_tra_so_phong_phu(number):
    def uoc(so):
        return [i for i in range(1, so - 1) if so % i == 0]

    def sup(so):
        if sum(uoc(so)) > so:
            return True
        else:
            return False

    return sup(number)


# Ham tao danh sach cac so phong phu.
def tao_danh_sach_so_phong_phu(n):
    return [i for i in range(n) if kiem_tra_so_phong_phu(i) is True]


# # Cac ham lien quan den phan tich thua so nguyen to:
# Ham tinh cac thua so nguyen to cua mot so (vip)
def thua_so_nguyen_to_day_du(n):
    # Ham ho tro cho phan tich so mu (don gian hoa bieu thuc mu. VD: 2^1=2)
    def ho_tro_phan_tich_so_mu(s):
        yeu_to = s.split()
        dem_yeu_to = collections.defaultdict(int)
        for y in yeu_to:
            co_so, so_mu = y.split("^")
            so_mu = int(so_mu)
            dem_yeu_to[co_so] = max(dem_yeu_to[co_so], so_mu)
        yeu_to_don_gian_hoa = [
            co_so if so_mu == 1 else f"{co_so}^{so_mu}"
            for co_so, so_mu in dem_yeu_to.items()
        ]
        bieu_thuc_don_gian_hoa = " ".join(yeu_to_don_gian_hoa)
        return bieu_thuc_don_gian_hoa

    # Ham phan tich so mu
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
        return "- Phan tich: {}\n- Bo so mu: {}".format(phan_tich, uoc_so)
    else:
        return "LOI TOAN HOC"


# Ham tinh cac thua so nguyen to cua mot so (ds)
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
        return "LOI TOAN HOC"


# Ham tinh uoc so chung lon nhat nguyen to cua hai so
def uoc_chung_nguyen_to_2_so(a, b):
    thua_so_cua_a = set(thua_so_nguyen_to(a))
    thu_so_cua_b = set(thua_so_nguyen_to(b))
    uoc_chung_nguyen_to = thua_so_cua_a.intersection(thu_so_cua_b)
    if len(uoc_chung_nguyen_to) == 0:
        return "LOI TOAN HOC"
    else:
        return max(uoc_chung_nguyen_to)


# # Cac ham lien quan den phuong trinh va bieu thuc toan hoc:
# Ham giai phuong trinh bac 1, 2 mot an va vai luu y, VD nhap: "12x^2 + 34 - 24 = 23x - 13"
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
            return "LOI TOAN HOC"
        else:
            delta = b**2 - 4 * a * c
            if delta == 0:
                return "x = {}".format(-b / (2 * a))
            else:
                x1 = (-b + cmath.sqrt(delta)) / (2 * a)
                x2 = (-b - cmath.sqrt(delta)) / (2 * a)
                return "Nghiem cua phuong trinh la:\nx₁ = {}\nx₂ = {}".format(x1, x2)
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
                return "Phuong trinh vo so nghiem"
            else:
                return "Phuong trinh vo nghiem"
        else:
            return "x₁ = {}".format(-b / a)


# Ham giai phuong trinh bac 1 - 10 bang cach nhap he so
def giai_phuong_trinh(bac, he_so_phuong_trinh):
    def giai_phuong_trinh_bac_1(a, b):
        nghiem = numpy.roots([a, b])
        return "Nghiem cua phuong trinh la:\nx₁ = {}".format(nghiem[0])

    def giai_phuong_trinh_bac_2(a, b, c):
        nghiem = numpy.roots([a, b, c])
        return "Nghiem cua phuong trinh la:\nx₁ = {}\nx₂ = {}".format(
            nghiem[0], nghiem[1]
        )

    def giai_phuong_trinh_bac_3(a, b, c, d):
        nghiem = numpy.roots([a, b, c, d])
        return "Nghiem cua phuong trinh la:\nx₁ = {}\nx₂ = {}\nx₃ = {}".format(
            nghiem[0], nghiem[1], nghiem[2]
        )

    def giai_phuong_trinh_bac_4(a, b, c, d, e):
        nghiem = numpy.roots([a, b, c, d, e])
        return "Nghiem cua phuong trinh la:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}".format(
            nghiem[0], nghiem[1], nghiem[2], nghiem[3]
        )

    def giai_phuong_trinh_bac_5(a, b, c, d, e, f):
        nghiem = numpy.roots([a, b, c, d, e, f])
        return "Nghiem cua phuong trinh la:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}".format(
            nghiem[0], nghiem[1], nghiem[2], nghiem[3], nghiem[4]
        )

    def giai_phuong_trinh_bac_6(a, b, c, d, e, f, g):
        nghiem = numpy.roots([a, b, c, d, e, f, g])
        return "Nghiem cua phuong trinh la:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}\nx₆ = {}".format(
            nghiem[0], nghiem[1], nghiem[2], nghiem[3], nghiem[4], nghiem[5]
        )

    def giai_phuong_trinh_bac_7(a, b, c, d, e, f, g, h):
        nghiem = numpy.roots([a, b, c, d, e, f, g, h])
        return "Nghiem cua phuong trinh la:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}\nx₆ = {}\nx₇ = {}".format(
            nghiem[0], nghiem[1], nghiem[2], nghiem[3], nghiem[4], nghiem[5], nghiem[6]
        )

    def giai_phuong_trinh_bac_8(a, b, c, d, e, f, g, h, i):
        nghiem = numpy.roots([a, b, c, d, e, f, g, h, i])
        return "Nghiem cua phuong trinh la:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}\nx₆ = {}\nx₇ = {}\nx₈ = {}".format(
            nghiem[0],
            nghiem[1],
            nghiem[2],
            nghiem[3],
            nghiem[4],
            nghiem[5],
            nghiem[6],
            nghiem[7],
        )

    def giai_phuong_trinh_bac_9(a, b, c, d, e, f, g, h, i, j):
        nghiem = numpy.roots([a, b, c, d, e, f, g, h, i, j])
        return "Nghiem cua phuong trinh la:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}\nx₆ = {}\nx₇ = {}\nx₈ = {}\nx₉ = {}".format(
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

    def giai_phuong_trinh_bac_10(a, b, c, d, e, f, g, h, i, j, k):
        nghiem = numpy.roots([a, b, c, d, e, f, g, h, i, j, k])
        return "Nghiem cua phuong trinh la:\nx₁ = {}\nx₂ = {}\nx₃ = {}\nx₄ = {}\nx₅ = {}\nx₆ = {}\nx₇ = {}\nx₈ = {}\nx₉ = {}\nx₁₀= {}".format(
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
        return "CHUA CO!"


# Ham tinh can bac n cua mot so
def can_bac(n, so_can):
    if so_can != 0:
        return n ** (1 / so_can)
    else:
        return "LOI TOAN HOC"


# # Cac ham lien quan den trich xuat va xu ly chuoi:
# Ham loai bo cac phan tu trung lap tu mot danh sach
def danh_sach_khong_trung_lap(lst):
    return sorted(list(set(lst)), reverse=True)


# Ham trich xuat cac chu so tu mot chuoi
def trich_xuat_chu_so_tu_chuoi(s):
    return [int(digit) for digit in re.findall(r"\d", s)]


# Ham trich xuat cac so tu mot chuoi
def trich_xuat_so_tu_chuoi(s):
    return [int(number) for number in re.findall(r"\d+", s)]


# Ham trich xuat cac ky tu khong phai la chu so tu mot chuoi
def trich_xuat_ki_tu(s):
    return re.findall(r"\D", s)


# Ham an ki tu dang "234343" == "••••••"
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


# Ham trich xuat cac so tu chuoi so. VD: "32/232343244" se la 32.232343244
def trich_xuat_cac_so_tu_so(s):
    s = str(s)
    if len(s) == 0:
        return 0
    if len(re.findall(r"\d+", s)) == 0:
        return 0
    if "-" in re.findall(
        r"\D", s
    ):  # Ho tro cho tinh toan vat ly 8, tien dien. Khong can thi an
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


# Ham nen xau
def xau_duoc_nen_1(s):
    s = sorted([i for i in s], reverse=True)
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


# Ham nen xau
def xau_duoc_nen_2(s):
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


# Ham tao ra xau ki tu khong trung lap. VD: "Google" se la "gole"
def xau_ki_tu_khong_trung_lap(s):
    s = s.lower()
    chuoi = ""
    for i in s:
        if i not in chuoi:
            chuoi += i
    return chuoi


# Ham nen xau nhung khong ghi so. VD: "hhhooccsiinh" == "hocsinh"
def xau_duoc_nen_khong_so(chuoi_nhap):
    ket_qua = chuoi_nhap[0]
    for ky_tu in chuoi_nhap[1:]:
        if ky_tu != ket_qua[-1]:
            ket_qua += ky_tu
    return ket_qua


# Ham giai nen xau
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


# # Khac
# Ham chuyen doi so binh thuong thanh so La Ma
def chuyen_doi_so_la_ma(num):
    return roman.toRoman(num)


# Ham dem so nghich the trong mot danh sach
def dem_so_nghich_the(danh_sach):
    dem = 0
    i = 0
    while i < len(danh_sach):
        for j in range(len(danh_sach)):
            if (i < j) and (danh_sach[i] > danh_sach[j]):
                dem += 1
        i += 1
    return dem


# Ham dinh ly Pythagore
def pythagore(a, b, c):
    sides = [a, b, c]
    if sides.count(False) > 1 or any(side < 0 for side in sides):
        return "LOI TOAN HOC"
    if a is False:
        if c < b:
            return "LOI TOAN HOC"
        else:
            side = math.sqrt(c**2 - b**2)
            return "Canh goc vuong 1 = {}".format(side)
    elif b is False:
        if c < a:
            return "LOI TOAN HOC"
        else:
            side = math.sqrt(c**2 - a**2)
            return "Canh goc vuong 2 = {}".format(side)
    elif c is False:
        side = math.sqrt(a**2 + b**2)
        return "Canh huyen = {}".format(side)


# Ham mo phong qua trinh "Tai xuong"
def mp_tai_xuong(n):
    if n < 0 or n > 88 or n <= 1:
        print("AGAIN")
    else:
        n = int(n)
        for i in range(n):
            sys.stdout.write(
                "Dang tai xuong [{}{}] {}%\r".format(
                    "■" * i, " " * (n - 1 - i), (i + 1) * 100 // n
                )
            )
            sys.stdout.flush()
            time.sleep(0.1)
        print("\n{}".format("Tai xuong hoan tat!"))


# Ham mo phong qua trinh "tinh toan"
def mp_tinh_toan(n):
    if n < 0 or n >= 88:
        print("NO")
    else:
        n = int(n)
        for i in range(n):
            sys.stdout.write(
                "    AD: Dang tinh toan [{}{}] {}%\r".format(
                    "■" * i, " " * (n - 1 - i), (i + 1) * 100 // n
                )
            )
            sys.stdout.flush()
            time.sleep(0.2)


# Ham mo phong qua trinh "LOADING..."
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


# Ham mo phong cay thong
def mp_christmas_tree():
    n = 9  # De tao cay thong dep thi cho n = 9
    for i in range(1, n + 1):
        for __ in range(n - i + 5):
            print(" ", end=" ")
        for _ in range(2 * i - 5):
            print("*", end=" ")
        print()
    for i in range(3):
        print("                     ", end="")
        print(" * ")


# # Ham ho tro tinh toan dac biet
# Ham tinh toan cac cong thuc vat ly
def tinh_toan_vat_ly_8():
    print(
        "\n",
        " —————————————————————————————————————————————————————————————————————————————————————",
        "\n",
        "|                 >>>>> NHAP TEN CONG THUC BAN MUON DE ADMIN TINH <<<<<               |",
        "\n",
        "|                         ~~~ ! Luu y: Nhap theo yeu cau ! ~~~                        |",
        "\n",
        "|                                                                                     |",
        "\n",
        "|        --> 1. Cong thuc tinh: Khoi luong rieng      (ki hieu D, Kg/m^3)             |",
        "\n",
        "|        --> 2. Cong thuc tinh: Trong luong rieng     (ki hieu d, don vi N/m^3)       |",
        "\n",
        "|        --> 3. Cong thuc tinh: Luc day Archimedes    (ki hieu Fa, don vi N)          |",
        "\n",
        "|        --> 4. Cong thuc tinh: Trong luong           (ki hieu P, don vi N)           |",
        "\n",
        "|        --> 5. Cong thuc tinh: Ap suat chat ran      (ki hieu p, N/m^2)              |",
        "\n",
        "|        --> 6. Cong thuc tinh: Ap suat chat long     (ki hieu p, N/m^2)              |",
        "\n",
        " ———————————————————————————————————————————————————————————————————————————————————--",
    )
    n = str(input("    AD: Nhap cong thuc ban chon de AD tinh: "))
    chuoi_so = [i for i in n]
    if chuoi_so[0].isdigit() is True:
        n = int(chuoi_so[0])
    if n == 1:
        h = int(
            input(
                "    AD: Co trong luong nhung khong co khoi luong thi nhap (1 la Co, 2 la Khong): ",
            )
        )
        if h != 1 and h != 2:
            print("    AD: Nhap so 1 va 2 co ma🤨", "\n")
        if h == 1:
            P = str(input("- Nhap trong luong cua chat (N): "))
            V = str(input("- Nhap the tich cua chat (m^3): "))
            P = trich_xuat_cac_so_tu_so(P)
            V = trich_xuat_cac_so_tu_so(V)
            m = P / 9.8  # type: ignore
            D = m / V
            if D > 0:
                mp_tinh_toan(30)
                print("\n", "   AD: Khoi luong rieng cua chat la: ", D, "kg/m^3", "\n")
            else:
                print("    AD: Ba cho so am chi dzay", "\n")
        if h == 2:
            m = str(input("- Nhap khoi luong cua chat (kg): "))
            V = str(input("- Nhap the tich cua chat (m^3): "))
            m = trich_xuat_cac_so_tu_so(m)
            V = trich_xuat_cac_so_tu_so(V)
            D = m / V  # type: ignore
            if D >= 0:
                mp_tinh_toan(30)
                print("\n", "   AD: Khoi luong rieng cua chat la: ", D, "kg/m^3", "\n")
            else:
                print("    AD: Ba cho so am chi dzay", "\n")
    elif n == 2:
        h = int(
            input(
                "    AD: Co khoi luong nhung khong co trong luong thi nhap (1 la Co, 2 la Khong): "
            )
        )
        if h != 1 and h != 2:
            print("    AD: Nhap so 1 va 2 co ma🤨", "\n")
        elif h == 2:
            P = str(input("- Nhap trong luong cua chat (N): "))
            V = str(input("- Nhap the tich cua chat (m^3): "))
            P = trich_xuat_cac_so_tu_so(P)
            V = trich_xuat_cac_so_tu_so(V)
            d = P / V  # type: ignore
            if d >= 0:
                mp_tinh_toan(30)
                print(
                    "\n", "   AD: Trong luong rieng cua chat do la: ", d, "N/m^3", "\n"
                )
            else:
                print("    AD: Ba cho so am chi dzay", "\n")
        elif h == 1:
            m = str(input("- Nhap khoi luong cua chat (kg): "))
            V = str(input("- Nhap the tich cua chat (m^3): "))
            m = trich_xuat_cac_so_tu_so(m)
            V = trich_xuat_cac_so_tu_so(V)
            d = 9.8 * m / V  # type: ignore
            if d >= 0:
                mp_tinh_toan(30)
                print(
                    "\n", "   AD: Trong luong rieng cua chat do la: ", d, "N/m^3", "\n"
                )
            else:
                print("    AD: Ba cho so am chi dzay", "\n")
    elif n == 3:
        d = str(input("- Nhap trong luong rieng cua chat long (N/m^3): "))
        V = str(input("- Nhap the tich ma chat long bi chiem boi vat (m^3): "))
        d = trich_xuat_cac_so_tu_so(d)
        V = trich_xuat_cac_so_tu_so(V)
        Fa = d * V  # type: ignore
        if Fa >= 0:
            mp_tinh_toan(30)
            print(
                "\n", "   AD: Luc day Archimedes tac dung len vat la: ", Fa, "N", "\n"
            )
        else:
            print("    AD: Ba cho so am chi dzay", "\n")
    elif n == 4:
        m = str(input("- Nhap khoi luong cua vat (kg): "))
        m = trich_xuat_cac_so_tu_so(m)
        P = m * 9.8  # type: ignore
        if P >= 0:
            mp_tinh_toan(30)
            print("\n", "   AD: Trong luong cua chat do la: ", P, "N", "\n")
        else:
            print("    AD: Ba cho so am chi dzay", "\n")
    elif n == 5:
        F = str(input("- Nhap ap luc len be mat do (ki hieu F hoac P, don vi N): "))
        S = str(input("- Nhap dien tich be mat tiep xuc (m^2): "))
        F = trich_xuat_cac_so_tu_so(F)
        S = trich_xuat_cac_so_tu_so(S)
        p = F / S  # type: ignore
        if p >= 0:
            mp_tinh_toan(30)
            print(
                "\n",
                "   AD: Ap suat cua vat len be mat la (Ap suat chat ran): ",
                p,
                "N/m^2",
                "\n",
            )
        else:
            print("    AD: Ba cho so am chi dzay", "\n")
    elif n == 6:
        d = str(input("- Nhap trong luong rieng chat long do (N/m^3): "))
        h = str(
            input("- Nhap chieu sau tu tren xuong cua vat trong chat long do (m): ")
        )
        d = trich_xuat_cac_so_tu_so(d)
        h = trich_xuat_cac_so_tu_so(h)
        p = d * h  # type: ignore
        if p >= 0:
            mp_tinh_toan(30)
            print("\n", "   AD: Ap suat chat long la: ", p, "N/m^2", "\n")
        else:
            print("    AD: Ba cho so am chi dzay", "\n")
    else:
        print("    AD: Chon lai gium tuiii😒", "\n")


# Ham tinh toan tien dien a la chi so cu, b la chi so moi (b > a)
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
        return "- So Kwh dien tieu thu trong thang: {} Kwh\n- So tien dien can tra trong thang: {} VND".format(
            skw, TT  # type: ignore
        )
    else:
        return "KHONG DUOC"


# Ham tim mot so lon nhat co tong cac chu "a" so bang so "b". VD: 3,21 se bang 993
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


# Ham chuyen hoa chuoi thanh mat ma Caesar
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


# Ham ma hoa day so Caesar
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


# # Quy luat.
# Ham tao danh sach cac so theo quy luat: 1 so ⋮ 1, 2 so ⋮ 2, 3 so ⋮ 3, ... cho toi tong so luong la number.
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


# Ham tao mot day so theo quy luat: moi phan tu cua day so vo han nay tich voi n don vi.
def tao_danh_sach_quy_luat_2(m, n):
    return [i * m for i in range(n)]


# Ham tao day so theo quy luat: so mu nang toi n cua so number.
def tao_danh_sach_quy_luat_3(n, m):
    return [m**i for i in range(n)]


# Ham choi keo bua bao voi "A.I"
def one_two_three():
    set = {1: "Keo", 2: "Bua", 3: "Bao"}
    dem_human, dem_ai = 0, 0
    n = int(input("- So man choi: "))

    for _ in range(n):
        AI_choose = set[random.randint(1, 3)]
        User_choose = str(input("- Lua chon cua ban: "))
        User = User_choose.title()

        print(f"- Lua chon cua ban = {User}, lua chon cua A.I = {AI_choose};")

        if User == "Keo" or User == "Keo":
            if AI_choose == "Keo":
                print(">>> HOA;")
                dem_ai += 1
                dem_human += 1
            if AI_choose == "Bua":
                print(">>> A.I THANG;")
                dem_ai += 1
            if AI_choose == "Bao":
                print(">>> BAN THANG;")
                dem_human += 1

        elif User == "Bua" or User == "Bua":
            if AI_choose == "Bua":
                print(">>> HOA;")
                dem_human += 1
                dem_ai += 1
            if AI_choose == "Bao":
                print(">>> A.I THANG;")
                dem_ai += 1
            if AI_choose == "Keo":
                print(">>> BAN THANG;")
                dem_human += 1

        elif User == "Bao":
            if AI_choose == "Bao":
                print(">>> HOA;")
                dem_ai += 1
                dem_human += 1
            if AI_choose == "Keo":
                print(">>> A.I THANG;")
                dem_ai += 1
            if AI_choose == "Bua":
                print(">>> USER THANG;")
                dem_human += 1

        else:
            print(">>> ! LOI NHE (BAN BI TRU 1 DIEM) !")
            dem_human -= 1
            dem_ai += 1
        print()

    print("- KET QUA:")
    if dem_ai < dem_human:
        print(f">>> Ban thang voi {dem_human} diem, A.I thua voi {dem_ai} diem.")
    elif dem_ai > dem_human:
        print(f">>> A.i thang voi {dem_ai} diem, ban thua voi {dem_human} diem.")
    elif dem_ai == dem_human:
        print(f">>> Ban hoa voi A.I va so diem la {dem_ai}.")
