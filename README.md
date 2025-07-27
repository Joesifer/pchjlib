<h1 align="center">
<img src="https://i.imgur.com/AUXxUzd.png" width="500" alt="PCHJLIB - Joesifer">
</h1><br>


[![PyPI Downloads](https://img.shields.io/badge/pchjlib-PyPI_downloads?style=plastic&logo=pchjlib&label=PyPI%20downloads)](https://pypi.org/project/pchjlib/)
[![GitHub](https://img.shields.io/badge/pchjlib-Joesifer_GitHub?style=plastic&logo=GitHub&label=GitHub)](https://github.com/Joesifer/pchjlib)
[![Python](https://img.shields.io/badge/Version_%3E_3.7-1?style=plastic&label=Python)](https://www.python.org/)
[![Owner](https://img.shields.io/badge/Joesifer-1?style=plastic&label=PCHJLIB&labelColor=%2300fff7&color=%23ffe600)](https://github.com/Joesifer)


# Mục Lục

- [Các hàm kiểm tra số nguyên tố và số liên quan](#các-hàm-kiểm-tra-số-nguyên-tố-và-số-liên-quan)  
- [Các hàm Fibonacci](#các-hàm-fibonacci)  
- [Các hàm tính số hoàn thiện, tự mãn, hữu hảo, hoàn hào, thân thiết](#các-hàm-tính-số-hoàn-thiện-tự-mãn-hữu-hảo-hoàn-hào-thân-thiết)  
- [Các hàm số chính phương, mạnh mẽ, thân thiết](#các-hàm-số-chính-phương-mạnh-mẽ-thân-thiết)  
- [Các hàm về ước số và bội số](#các-hàm-về-ước-số-và-bội-số)  
- [Các hàm số song tố và số phong phú](#các-hàm-số-song-tố-và-số-phong-phú)  
- [Các hàm phân tích thừa số nguyên tố](#các-hàm-phân-tích-thừa-số-nguyên-tố)  
- [Các hàm giải phương trình](#các-hàm-giải-phương-trình)  
- [Các hàm xử lý danh sách và chuỗi](#các-hàm-xử-lý-danh-sách-và-chuỗi)  
- [Mật mã Caesar](#mật-mã-caesar)  
- [Teen Code Yahoo](#teen-code-yahoo)  
- [Các hàm mô phỏng chỉ với string](#các-hàm-mô-phỏng-chỉ-với-string)  
- [Hàm hỗ trợ tính toán đặc biệt](#hàm-hỗ-trợ-tính-toán-đặc-biệt)  
- [Quy luật sinh dãy](#quy-luật-sinh-dãy)  
- [Chuyển đổi và đếm](#chuyển-đổi-và-đếm)  
- [Khác](#khác)  
- [Những bản cập nhật](#những-bản-cập-nhật) 

---

## Các hàm kiểm tra số nguyên tố và số liên quan

- **kiem_tra_so_nguyen_to(n)**  
  True/False nếu n (không) là số nguyên tố.

- **tao_danh_sach_so_nguyen_to(n)**  
  Danh sách các số nguyên tố từ 0 đến n.

- **kiem_tra_so_emirp(n)**  
  True/False nếu n (không) là số emirp.

- **tao_danh_sach_so_emirp(n)**  
  Danh sách các số emirp từ 0 đến n.

---

## Các hàm Fibonacci

- **vi_tri_so_Fibonacci(n)**  
  Tính số Fibonacci thứ n.

- **tao_danh_sach_so_Fibonacci(n)**  
  Danh sách các số Fibonacci trong khoảng 0 đến n.

---

## Các hàm tính số hoàn thiện, tự mãn, hữu hảo, hoàn hào, thân thiết

- **tong_uoc_so(n)**  
  Tổng các ước số dương (không tính n) của n.

- **tong_chu_so(n)**  
  Tổng các chữ số của n.

- **kiem_tra_so_hoan_thien(n)**  
  True/False nếu n (không) là số hoàn thiện.

- **tao_danh_sach_so_hoan_thien(n)**  
  Danh sách số hoàn thiện từ 0 đến n.

- **kiem_tra_so_tu_man(n)**  
  True/False nếu n (không) là số tự mãn.

- **tao_danh_sach_so_tu_man(n)**  
  Danh sách số tự mãn từ 0 đến n.

- **cap_so_hua_hon(a, b)**  
  True/False nếu a, b (không) là cặp số hữu hảo.

- **kiem_tra_so_hoan_hao(n)**  
  True/False nếu n (không) là số hoàn hào.

- **tao_danh_sach_so_hoan_hao(n)**  
  Danh sách số hoàn hào từ 0 đến n.

---

## Các hàm số chính phương, mạnh mẽ, thân thiết

- **kiem_tra_so_chinh_phuong(n)**  
  True/False nếu n (không) là số chính phương.

- **tao_danh_sach_so_chinh_phuong(n)**  
  Danh sách số chính phương từ 0 đến n.

- **cap_so_than_thiet(a, b)**  
  True/False nếu a, b (không) là cặp số thân thiết.

- **kiem_tra_so_manh_me_1(n)**  
  True/False nếu n (không) là số mạnh mẽ (tổng chữ số là nguyên tố).

- **kiem_tra_so_manh_me_2(n)**  
  True/False nếu n (không) là số mạnh mẽ loại 2.

---

## Các hàm về ước số và bội số

- **tao_danh_sach_uoc_so(n)**  
  Danh sách các ước số của n.

- **uoc_chung_lon_nhat(a, b)**  
  Giá trị ước chung lớn nhất của a, b.

- **uoc_chung_lon_nhat_cua_danh_sach(array)**  
  Giá trị ước chung lớn nhất của dãy.

- **boi_chung_nho_nhat(a, b)**  
  Giá trị bội số chung nhỏ nhất của a, b.

- **boi_chung_nho_nhat_cua_danh_sach(array)**  
  Giá trị bội số chung nhỏ nhất của dãy.

- **tao_danh_sach_boi_so(n)**  
  Danh sách bội số của n từ 0 đến 10 lần.

- **uoc_chung_cua_danh_sach(arr)**  
  Danh sách các ước chung của dãy.

---

## Các hàm số song tố và số phong phú

- **kiem_tra_so_song_to(n)**  
  True/False nếu n (không) là số song tố.

- **tao_danh_sach_so_song_to(n)**  
  Danh sách số song tố từ 0 đến n.

- **kiem_tra_so_phong_phu(number)**  
  True/False nếu n (không) là số phong phú.

- **tao_danh_sach_so_phong_phu(n)**  
  Danh sách số phong phú từ 0 đến n.

---

## Các hàm phân tích thừa số nguyên tố

- **thua_so_nguyen_to_day_du(n)**  
  Trả về tích các thừa số nguyên tố (có số mũ) bằng n.

- **thua_so_nguyen_to(n)**  
  Trả về danh sách các thừa số nguyên tố của n.

- **uoc_chung_nguyen_to_2_so(a, b)**  
  Giá trị ước chung nguyên tố lớn nhất của a, b.

---

## Các hàm giải phương trình

- **giai_pt_bac_1va2_dang_string(phuong_trinh)**  
  Giải phương trình bậc 1, 2 nhập dạng chuỗi.

- **giai_phuong_trinh(bac, he_so_phuong_trinh)**  
  Giải phương trình bậc 1–10 theo hệ số.

---

## Các hàm xử lý danh sách và chuỗi

- **danh_sach_khong_trung_lap(lst)**  
  Loại bỏ phần tử trùng lặp trong danh sách.

- **trich_xuat_chu_so_tu_chuoi(s)**  
  Trích xuất chuỗi chữ số từ s.

- **trich_xuat_so_tu_chuoi(s)**  
  Trích xuất chuỗi số từ s.

- **trich_xuat_ki_tu(s)**  
  Trích xuất các ký tự từ s.

- **trich_xuat_cac_so_tu_so(s)**  
  Trích xuất các số từ chuỗi số (ví dụ “32/232343244” → “32.232343244”).

- **xau_duoc_nen_1(s)**  
  Nén xâu loại 1 (ví dụ “google” → “2ol2ge”).

- **xau_duoc_nen_2(s)**  
  Nén xâu loại 2 (ví dụ “google” → “g2ogle”).

- **xau_duoc_nen_khong_so(chuoi_nhap)**  
  Nén xâu bỏ số (ví dụ “hhhooccsiinh” → “hocsinh”).

- **xau_duoc_giai_nen(s)**  
  Giải nén xâu (ví dụ “3ab3c” → “aaabccc”).

- **xau_ki_tu_khong_trung_lap(s)**  
  Tạo xâu ký tự không trùng lặp (ví dụ “Google” → “gole”).

---

## Mật mã Caesar

- **chuyen_hoa_caesar(string, sang_trai_k_so)**  
  Chuyển chuỗi thành dãy số mật mã Caesar.

- **ma_hoa_caesar(array, sang_trai_k_so)**  
  Mã hóa dãy số Caesar thành xâu.

---

## Teen Code Yahoo

- **teen_code_yahoo(dau_vao)**  
  Chuyển xâu thành Teen Code Yahoo.

---

## Các hàm mô phỏng chỉ với string

### mp_tai_xuong(n)
Phạm vi 0 < n < 88  
```python
- mp_tai_xuong(n):
  Dang tai xuong [=====================================] 100%
  Tai xuong hoan tat!
```

### mp_tinh_toan(n)
```python
- mp_tinh_toan(n):
  AD: Dang tinh toan [=====================================] 100%
```

### mp_loading(n)
```python
- mp_loading(n):
>> LOADING...
```

### mp_christmas_tree_cho_VSCode()
```python
- mp_christmas_tree_cho_VSCode():
- Nhap chieu cao cay thong: 8

        *
       * *
      * * *
     * * * *
    * * * * *
   * * * * * *
  * * * * * * *
 * * * * * * * *
        H
        H
```

### mp_christmas_tree_cho_TEXT()
```python
- mp_christmas_tree_cho_TEXT():
- Nhap chieu cao cay thong: 8

                 *  
               *  *   
             *  *  *    
           *  *  *  *     
         *  *  *  *  *      
       *  *  *  *  *  *       
     *  *  *  *  *  *  *        
   *  *  *  *  *  *  *  *
                H
                H
```

---

## Hàm hỗ trợ tính toán đặc biệt

### tinh_toan_vat_ly_8()
```python
- tinh_toan_vat_ly_8():
>> 
  ————————————————————————————————————————————————————————————————————————————————————— 
 |                 >>>>> NHAP TEN CONG THUC BAN MUON DE ADMIN TINH <<<<<               | 
 |                         ~~~ ! Luu y: Nhap theo yeu cau ! ~~~                        | 
 |                                                                                     | 
 |        --> 1. Cong thuc tinh: Khoi luong rieng      (ki hieu D, Kg/m^3)             | 
 |        --> 2. Cong thuc tinh: Trong luong rieng     (ki hieu d, don vi N/m^3)       | 
 |        --> 3. Cong thuc tinh: Luc day Archimedes    (ki hieu Fa, don vi N)          | 
 |        --> 4. Cong thuc tinh: Trong luong           (ki hieu P, don vi N)           | 
 |        --> 5. Cong thuc tinh: Ap suat chat ran      (ki hieu p, N/m^2)              | 
 |        --> 6. Cong thuc tinh: Ap suat chat long     (ki hieu p, N/m^2)              | 
  ———————————————————————————————————————————————————————————————————————————————————--
    AD: Nhap cong thuc ban chon de AD tinh: 4
- Nhap khoi luong cua vat (kg): 3,4
    AD: Dang tinh toan [■■■■■■■■■■■■■■■■■■■■■■■■■■■■■] 100%
    AD: Trong luong cua chat do la:  33.32 N 

```

### tinh_toan_tien_dien(chi_so_cu, chi_so_moi)
```python
- tinh_toan_tien_dien(chi_so_cu, chi_so_moi):
>> Số Kwh đã tiêu thụ và số tiền phải trả;
```

### tong_chu_so_lon_nhat_bang_n(number_of_digits, int_number)
```python
- tong_chu_so_lon_nhat_bang_n(number_of_digits, int_number):
>> Số lớn nhất number_of_digits chữ số và tổng bằng int_number
# Vi du: 3, 21 → 993
```

### pythagore(a, b, c)
```python
- pythagore(a, b, c):
>> Tính cạnh còn lại trong tam giác vuông
# Cạnh cần tìm thì cho = False
```

---

## Quy luật sinh dãy

### tao_danh_sach_quy_luat_1(number)
```python
- tao_danh_sach_quy_luat_1(number):
>> Một danh sách: 1 số chia hết cho 1, 2 số chia hết cho 2, … cho tổng số lượng number
```

### tao_danh_sach_quy_luat_2(m, n)
```python
- tao_danh_sach_quy_luat_2(m, n):
>> Một danh sách các số bội m, số phần tử n
# Vi du: m=2, n=10 → [0,2,4,6,8,10,12,14,16,18]
```

### tao_danh_sach_quy_luat_3(n, m)
```python
- tao_danh_sach_quy_luat_3(n, m):
>> Danh sách lũy thừa của m^0 đến m^n
# Vi du: m=3, n=10 → [1,3,9,…,3^10]
```

---

## Chuyển đổi và đếm

### chuyen_doi_so_la_ma(num)
```python
- chuyen_doi_so_la_ma(num):
>> Số La Mã của num
```

### dem_so_nghich_the(danh_sach)
```python
- dem_so_nghich_the(danh_sach):
>> Số cặp nghịch thế trong danh sách.
# (i<j va a[i]>a[j])
```

### one_two_three()
```python
- one_two_three():
>> Lua chon keo bua bao voi A.I: ['Keo','Bua','Bao']
```

### tao_day_chu(n, r, x)
```python
- tao_day_chu(n, r, x):
>> Tạo dòng chữ với n dòng, r cột, 2 đường chéo, lăp lại x lần.
- Ví dụ:
- tao_day_chu(5, 5, 10)
Nhap day dau tien: I Love U💞💞 
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
I Love U💞💞
  I Love U💞💞
    I Love U💞💞
      I Love U💞💞
        I Love U💞💞
          I Love U💞💞
        I Love U💞💞
      I Love U💞💞
    I Love U💞💞
  I Love U💞💞
```

---

## Khác

*(Chưa có hàm bổ sung)*

# NHỮNG BẢN CẬP NHẬT

### 0.0.5.2.1 - (27/07/2025)
- ***Sửa README.***

### 0.0.5.2 - (27/07/2025)
- ***Sửa README.***

### 0.0.5.1 - (27/07/2025)
- ***Cập nhật teen_code_yahoo.***

### 0.0.5.0 - (26/07/2025)
- ***Xóa an_ký_tự.***

### 0.0.4.1 - (17/10/2024)
- ***Cập nhật "one_two_three" và bổ sung "tạo_dãy_chữ".***

### 0.0.4.0 - (05/05/2024)
- ***Sửa README.***

### 0.0.3.9 - (05/05/2024)
- ***Sửa README.***

### 0.0.3.8 - (05/05/2024)
- ***Cập nhật "mp_christmas_tree_cho_VSCode" và "mp_christmas_tree_cho_TEXT".***

### 0.0.3.7 - (04/05/2024)
- ***Cập nhật "mp_christmas_tree".***

### 0.0.3.6 - (03/03/2024)
- ***Thử nghiệm.***

### 0.0.3.5 - (01/03/2024)
- ***Thử nghiệm.***

### 0.0.3.4 - (26/02/2024)
- ***Bổ sung hàm "uoc_chung_cua_danh_sach" (để tìm các ước chung trong một mảng).***

### 0.0.3.3 - (21/02/2024)
- ***Nâng cấp thông tin thư viện và README.***

### 0.0.3.2 - (20/02/2024)
- ***Bổ sung số phong phú.***

### 0.0.3.1 - (20/02/2024)
- ***Nâng cấp thông tin thư viện.***

### 0.0.3 - (20/02/2024)
- ***Bổ sung "xau_ki_tu_khong_trung_lap" (không theo thứ tự bảng chữ cái) và loại bỏ "ki_tu_trung_lap" (theo thứ tự bảng chữ cái).***

### 0.0.2.10 - (19/02/2024)
- ***Nâng cấp README.***

### 0.0.2.9 - (19/02/2024)
- ***Thử nghiệm.***

### 0.0.2.8 - (19/02/2024)
- ***Thử nghiệm.***

### 0.0.2.7 - (18/02/2024)
- ***Nâng cấp README.***

### 0.0.2.6 - (18/02/2024)
- ***Thay đổi sang giấy phép MIT License.***

### 0.0.2.5 - (18/02/2024)
- ***Nâng cấp README.***

### 0.0.2.4 - (18/02/2024)
- ***Nâng cấp README.***

### 0.0.2.3 - (18/02/2024)
- ***Thử nghiệm.***

### 0.0.2.2 - (14/02/2024)
- ***Thử nghiệm.***

### 0.0.2.1 - (14/02/2024)
- ***Thử nghiệm.***

### 0.0.2 - (14/02/2024)
- ***Sửa lỗi không thêm các phụ thuộc.***

### 0.0.1.2 - (14/02/2024)
- ***Thử nghiệm.***

### 0.0.1.1 - (14/02/2024)
- ***Thử nghiệm.***

### 0.0.1 - (14/02/2024)
- ***Phiên bản đầu tiên.***

### 0.0.0.1 - (14/02/2024)
- ***Thử nghiệm.***