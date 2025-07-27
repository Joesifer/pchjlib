<h1 align="center">
<img src="https://i.imgur.com/AUXxUzd.png" width="500" alt="PCHJLIB - Joesifer">
</h1><br>


[![PyPI Downloads](https://img.shields.io/badge/pchjlib-PyPI_downloads?style=plastic&logo=pchjlib&label=PyPI%20downloads)](https://pypi.org/project/pchjlib/)
[![GitHub](https://img.shields.io/badge/pchjlib-Joesifer_GitHub?style=plastic&logo=GitHub&label=GitHub)](https://github.com/Joesifer/pchjlib)
[![Python](https://img.shields.io/badge/Version_%3E_3.7-1?style=plastic&label=Python)](https://www.python.org/)
[![Owner](https://img.shields.io/badge/Joesifer-1?style=plastic&label=PCHJLIB&labelColor=%2300fff7&color=%23ffe600)](https://github.com/Joesifer)


# Cac ham kiem tra tinh chat so nguyen to va so nguyen to lien quan:
### Ham kiem tra xem mot so co phai la so nguyen to hay khong.
``` python
- kiem_tra_so_nguyen_to(n).
>> True/ False neu (khong) la so nguyen to;
```

### Ham tao danh sach cac so nguyen to den n.
``` python
- tao_danh_sach_so_nguyen_to(n).
>> Mot danh sach cac so nguyen to nam trong khoang tu 0 toi so n da nhap;
```

### Ham kiem tra so emirp (mot so emirp la mot so nguyen to ma khi dao nguoc vi tri cac chu so cua no, ta cung duoc mot so nguyen to, khong ke nhung so nguyen to doi xung).
``` python
- kiem_tra_so_emirp(n).
>> True/ False neu (khong) la so emirp;
```

### Ham tao so emirp den n.
``` python
- tao_danh_sach_so_emirp(n).
>> Mot danh sach cac so emirp nam trong khoang tu 0 toi so n da nhap;
```

# Cac ham lien quan den so Fibonacci:
### Ham tinh so Fibonacci thu n.
``` python
- vi_tri_so_Fibonacci(n).
>> Vi tri cua mot so Fibonacci thu n;
```

### Ham tao danh sach cac so Fibonacci den n.
``` python
- tao_danh_sach_so_Fibonacci(n).
>> Mot danh sach cac so Fibonacci trong khoang tu 0 toi so n da nhap;
```

# Cac ham so hoan thien, so tu man, hua hon, hoan hao, than thiet va tinh tong cac uoc, chu so:
### Ham tinh tong cac uoc so cua n khong tinh n va khong am.
``` python
- tong_uoc_so(n).
>> Tong cac uoc so duong cua so n;
```

### Ham tinh tong cac chu so cua mot so.
``` python
- tong_chu_so(n).
>> Tong cac chu so cua so n;
```

### Ham kiem tra xem mot so co phai la so hoan thien (mot so hoan thien la mot so nguyen duong ma tong cac uoc nguyen duong cua no bang chinh no).
``` python
- kiem_tra_so_hoan_thien(n).
>> True/ False neu (khong) la so hoan thien;
```

### Ham tao danh sach cac so hoan thien.
``` python
- tao_danh_sach_so_hoan_thien(n).
>> Mot danh sach cac so hoan thien trong khoang tu 0 toi so n da nhap;
```

### Ham kiem tra so tu man (mot so tu man la so bang tong cac mu bac ba cua moi chu so cua no).
``` python
- kiem_tra_so_tu_man(n).
>> True/ False neu (khong) la mot so tu man;
```

### Ham tao danh sach cac so tu man.
``` python
- tao_danh_sach_so_tu_man(n).
>> Mot danh sach cac so tu man trong khoang tu 0 toi so n da nhap;
```

### Ham kiem tra cap so hua hon (mot cap so hua hon la hai so nguyen duong ma tong cac uoc cua so nay (khong tinh so do) nhieu hon so kia dung 1 don vi).
``` python
- cap_so_hua_hon(a, b).
>> True/ False neu a, b (khong) la mot cap so hua hon.
```

### Ham kiem tra so hoan hao (mot so hoan hao la khi tong cac uoc so thuc su cua n cung bang n).
``` python
- kiem_tra_so_hoan_hao(n).
>> True/ False neu (khong) la mot so hoan hao;
```

### Ham tao danh sach so hoan hao.
``` python
- tao_danh_sach_so_hoan_hao(n).
>> Mot danh sach cac so hoan hao trong khoang tu 0 toi so n da nhap;
```

# Cac ham kiem tra va tao danh sach so chinh phuong, than thiet, manh me loai 1, 2:
### Ham kiem tra so chinh phuong (so chinh phuong la so ma neu no la binh phuong cua mot so nguyen).
``` python
- kiem_tra_so_chinh_phuong(n).
>> True/ False neu (khong) la mot so chinh phuong;
```

### Ham tao danh sach cac so chinh phuong den n.
``` python
- tao_danh_sach_so_chinh_phuong(n).
>> Mot danh sach cac so chinh phuong trong khoang tu 0 toi so n da nhap;
```

### Ham kiem tra xem hai so co phai la cac so than thiet (mot cap so than thiet la khi chung tuan theo quy luat: So nay bang tong tat ca cac uoc cua so kia (tru chinh so do) va nguoc lai).
``` python
- cap_so_than_thiet(a, b).
>> True/ False neu a, b (khong) la cac so than thiet;
```

### Ham kiem tra so manh me (neu tong chu so no la mot so nguyen to).
``` python
- kiem_tra_so_manh_me_1(n).
>> True/ False neu (khong) la mot so manh me;
```

### Ham kiem tra so manh me (neu mot so vua chia het cho nhung so nguyen to va binh phuong cua chung truoc no).
``` python
- kiem_tra_so_manh_me_2(n).
>> True/ False neu (khong) la mot so manh me;
```

# Cac ham lien quan den uoc so va boi so:
### Ham tao danh sach cac uoc so cua mot so.
``` python
- tao_danh_sach_uoc_so(n).
>> Mot danh sach cac uoc so cua mot so;
```

### Ham tim uoc chung lon nhat cua 2 so.
``` python
- uoc_chung_lon_nhat(a, b).
>> Gia tri uoc chung lon nhat cua a, b;
```

### Ham tinh uoc so chung lon cua mot danh sach cac so (uoc chung lon nhat cua nhieu so).
``` python
- uoc_chung_lon_nhat_cua_danh_sach(array).
>> Gia tri uoc chung lon nhat cua array;
```

### Ham tinh boi so chung nho nhat cua hai so.
``` python
- boi_chung_nho_nhat(a, b).
>> Gia tri boi chung nho nhat cua a, b;
```

### Ham tinh boi so chung nho nhat cua mot danh sach cac so (boi chung nho nhat cua nhieu so).
``` python
- boi_chung_nho_nhat_cua_danh_sach(array).
>> Gia tri boi chung nho nhat cua array;
```

### Ham tao danh sach cac boi so cua mot so len den 10 lan.
``` python
- tao_danh_sach_boi_so(n).
>> Mot danh sach cac so boi so cua tu 0 toi 10 lan;
```

# Ham tao gia tri cac uoc chung cua mot danh sach.
``` python
- uoc_chung_cua_danh_sach(arr).
>> Mot danh sach cac uoc chung cua danh sach.
```

# Cac ham lien quan den tinh chat so song to va so phong phu:
### Ham kiem tra cac so song to.
``` python
- kiem_tra_so_song_to(n).
>> True/ False neu (khong) la mot so song to;
```

### Ham tao danh sach cac so song to.
``` python
- tao_danh_sach_so_song_to(n).
>> Mot danh sach cac so song to tu 0 toi n;
```

### Ham kiem tra cac so phong phu. (So tu nhien N duoc goi la so phong phu neu tong cac uoc cua N (khong ke N) lon hon N).
``` python
- kiem_tra_so_phong_phu(number).
>>  True/ False neu (khong) la mot so phong phu;
```

### Ham tao danh sach cac so phong phu.
``` python
- tao_danh_sach_so_phong_phu(n).
>> Mot danh sach cac so phong phu tu 0 toi n;
```
# Cac ham lien quan den phan tich thua so nguyen to:
### Ham tinh cac thua so nguyen to cua mot so (vip).
``` python
- thua_so_nguyen_to_day_du(n).
>> Tra ve tich cua nhung so nguyen to (co so mu) bang so n;
```

### Ham tinh cac thua so nguyen to cua mot so dang list.
``` python
- thua_so_nguyen_to(n).
>> Tra ve mot danh sach cac so nguyen to co tich bang n;
```

### Ham tinh uoc so chung lon nhat nguyen to cua hai so.
``` python
- uoc_chung_nguyen_to_2_so(a, b).
>> Gia tri uoc chung nguyen to lon nhat cua a, b;
```

# Cac ham lien quan den phuong trinh va bieu thuc toan hoc:
### Ham giai phuong trinh bac 1, 2 mot an va vai luu y, khi nhap: phuong_trinh = "12x^2 + 34 - 24 = 23x - 13".
``` python
- giai_pt_bac_1va2_dang_string(phuong_trinh).
>> Nghiem cua phuong trinh;
```

### Ham giai phuong trinh bac 1 - 10 bang cach nhap he so.(bac = bac cua phuong trinh).
``` python
- giai_phuong_trinh(bac, he_so_phuong_trinh):
>> Nghiem cua phuong trinh;
```

# Cac ham lien quan den trich xuat, xu ly chuoi, danh sach:
### Ham loai bo cac phan tu trung lap tu mot danh sach.
``` python
- danh_sach_khong_trung_lap(lst).
>> Danh sach voi nhung phan tu khong trung lap;
```

### Ham trich xuat cac chu so tu mot chuoi.
``` python
- trich_xuat_chu_so_tu_chuoi(s).
>> Mot chuoi chu so co trong s;
```

### Ham trich xuat cac so tu mot chuoi.
``` python
- trich_xuat_so_tu_chuoi(s).
>> Mot chuoi cac so co trong s;
```

### Ham trich xuat cac ky tu tu mot chuoi.
``` python
- trich_xuat_ki_tu(s).
>> Trich xuat ki tu co trong s;
```

### Ham trich xuat cac so tu chuoi so. VD: "32/232343244" se la "32.232343244".
``` python
- trich_xuat_cac_so_tu_so(s).
>> Trich xuat cac so tu mot day so nhung lan voi ki tu;
```

### Ham nen xau loai 1. VD: "google" se la "2ol2ge".
``` python
- xau_duoc_nen_1(s).
>> Xau duoc nen;
```
### Ham nen xau loai 2. VD: "google" se la "g2ogle".
``` python
- xau_duoc_nen_2(s).
>> Xau duoc nen;
```

### Ham nen xau nhung khong ghi so. VD: "hhhooccsiinh" se la "hocsinh".
``` python
- xau_duoc_nen_khong_so(chuoi_nhap).
>> Xau duoc nen;
```

### Ham giai nen xau. VD: "3ab3c" se la "aaabccc"
``` python
- xau_duoc_giai_nen(s).
>> Xau duoc giai nen;
```

### Ham tao ra xau ki tu khong trung lap. VD: "Google" se la "gole".
``` python
- xau_ki_tu_khong_trung_lap(s).
>> Xau ki tu khong trung lap;
```

# Mat ma Caesar:
# Phuong phap ma hoa cua Caesar duoc vi du cu the nhu sau:
``` python

- Dung mat ma cua Caesar chuyen buc thu "MEET YOU IN THE PARK" thanh buc thu bi mat. 
- Cac chu cai duoc bieu dien thanh so theo quy tac sau.

>> A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
>> 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

- Khi do buc thu goc "MEET YOU IN THE PARK" tro thanh (khong tinh khoang trang): "12 4 4 19 24 14 20 8 13 19 7 4 15 0 17 10"
- Bay gio ta se quay chuoi so 0 -> 25 sang trai k so (vi du trong truong hop nay k = 3) khi do ta co bang sau.

>> 0 1 2 3 4 5 6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 
>> 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25  0  1  2

- Khi do chuoi so "12 4 4 19 24 14 20 8 13 19 7 4 15 0 17 10" se duoc ma hoa thanh: "15 7 7 22 1 17 23 11 16 22 10 7 18 3 20 13"

```

### Ham chuyen hoa chuoi thanh mat ma Caesar.
``` python
- chuyen_hoa_caesar(string, sang_trai_k_so).
>> Day so mat ma caesar;
```

### Ham ma hoa day so Caesar.
``` python
- ma_hoa_caesar(array, sang_trai_k_so).
>> Xau duoc ma hoa boi day so mat ma;
```
# Teen code Yahoo. "Đây là ví dụ" -> "+)4¥ 14` √!' |)⊔."
``` python
- teen_code_yahoo(dau_vao).
>> Xau duoc chuyen hoa;

```

# Cac ham mo phong chi voi string:
### Ham mo phong qua trinh "Tai xuong" (pham vi so n la lon hon 0 va nho hon 88).
``` python
- mp_tai_xuong(n):
  Dang tai xuong [=====================================] 100%
  Tai xuong hoan tat!
```
### Ham mo phong qua trinh "tinh toan" cua "Admin" (giong nhu mo phong tai xuong).
``` python
- mp_tinh_toan(n):
  AD: Dang tinh toan [=====================================] 100%
```

### Ham mo phong qua trinh "LOADING...".
``` python
- mp_loading(n):
>> LOADING...
```

### Ham mo phong cay thong cho VSCode.
``` python
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

### Ham mo phong cay thong cho TEXT.
``` python
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

# Ham ho tro tinh toan dac biet:
### Ham tinh toan cac cong thuc vat ly.
``` python
- tinh_toan_vat_ly_8().
>> Mot bang lua chon cac cong thuc vat ly 8 chuong trinh GDPT 2018 sach CTST HK1;
>>



                   >>>>> NHAP TEN CONG THUC BAN MUON DE ADMIN TINH <<<<<               
                           ~~~ ! Luu y: Nhap theo yeu cau ! ~~~                        
                                                                                       
          --> 1. Cong thuc tinh: Khoi luong rieng      (ki hieu D, Kg/m^3)             
          --> 2. Cong thuc tinh: Trong luong rieng     (ki hieu d, don vi N/m^3)       
          --> 3. Cong thuc tinh: Luc day Archimedes    (ki hieu Fa, don vi N)         
          --> 4. Cong thuc tinh: Trong luong           (ki hieu P, don vi N)           
          --> 5. Cong thuc tinh: Ap suat chat ran      (ki hieu p, N/m^2)             
          --> 6. Cong thuc tinh: Ap suat chat long     (ki hieu p, N/m^2)              

      AD: Nhap cong thuc ban chon de AD tinh: 4
  - Nhap khoi luong cua vat (kg): 3.4
      AD: Dang tinh toan [=====================================] 100%
      AD: Trong luong cua chat do la:  33.32 N 
```

### Ham tinh toan tien dien a la chi so cu, b la chi so moi (b > a).
``` python
- tinh_toan_tien_dien(chi_so_cu, chi_so_moi).
>> So Kwh da tieu thu va so tien phai tra;
```

### Ham tim mot so lon nhat co tong cac chu "a" so bang so "b". VD: 3, 21 se bang 993.
``` python
- tong_chu_so_lon_nhat_bang_n(number_of_digits, int_number).
>> So ket qua;
```

### Ham dinh ly Pythagore (muon tim canh nao thi cho canh do bang False. VD a = 1, b = 2, c = False de tim c va trong do, a la canh goc vuong 1, b la canh goc vuong 2, c la canh huyen).
``` python
- pythagore(a, b, c).
>> Gia tri cua canh can tim trong tam giac;
```

# Quy luat:
### Ham tao danh sach cac so theo quy luat: 1 so chia het 1, 2 so chia het 2, 3 so chia het 3, ... cho toi tong so luong la number.
``` python
- tao_danh_sach_quy_luat_1(number).
>> Mot danh sach theo quy luat 1;
```

### Ham tao mot day so theo quy luat: cap so nhan voi n phan tu va m. VD: n = 10, m = 2 -> array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18].
``` python
- tao_danh_sach_quy_luat_2(m, n).
>> Mot danh sach theo quy luat 2;
```

### Ham tao day so theo quy luat: so mu nang toi lan thu n cua so m. VD: m = 3, n = 10 -> array = [3^0, 3^1, 3^2, ... , 3^10].
``` python
- tao_danh_sach_quy_luat_3(n, m).
>> Mot danh sach theo quy luat 3;
```

# Khac:
### Ham chuyen doi so binh thuong thanh so La Ma.
``` python
- chuyen_doi_so_la_ma(num).
>> So la ma cua num;
```

### Ham dem so nghich the trong mot danh sach (cho day so nguyen duong gom n phan tu a1, a2 ,…, a{n} . Mot cap (a[i], a[j] ) duoc goi la mot nghich the neu i < j va a[i] > a[j]).
``` python
- dem_so_nghich_the(danh_sach).
>> So nghich the trong danh sach;
```

### Ham choi keo bua bao voi "A.I".
``` python
- one_two_three().
>> Nhung su lua chon de ban choi keo bua bao voi A.I;
```

### Ham tao dong ho dem nguoc. (n la so dong moi cot va duong cheo, r la so tong cot va 2 duong cheo, x la so lan lap lai).
``` python
- tao_day_chu(n, r, x):
>> Nhap day dau tien: I love you❤️
I love you❤️
I love you❤️
I love you❤️
I love you❤️
I love you❤️
I love you❤️
I love you❤️
I love you❤️
I love you❤️
I love you❤️
I love you❤️
  I love you❤️
    I love you❤️
      I love you❤️
        I love you❤️
          I love you❤️
            I love you❤️
              I love you❤️
                I love you❤️
                  I love you❤️
                    I love you❤️
                  I love you❤️
                I love you❤️
              I love you❤️
            I love you❤️
          I love you❤️
        I love you❤️
      I love you❤️
    I love you❤️
  I love you❤️
```

# NHUNG BAN CAP NHAT

### 0.0.5.1 - (27/7/2025).
- ***Cap nhat teen_code_yahoo.***

### 0.0.5.0 - (26/7/2025).
- ***Xoa an_ki_tu.***

### 0.0.4.1 - (17/10/2024).
- ***Cap nhat "one_two_three" va bo sung "tao day chu".***

### 0.0.4.0 - (5/5/2024).
- ***Sua README.***

### 0.0.3.9 - (5/5/2024).
- ***Sua loi.***

### 0.0.3.8 - (5/5/2024).
- ***Cap nhat "mp_christmas_tree_cho_VSCode" va "mp_christmas_tree_cho_TEXT".***
### 0.0.3.8 - (5/5/2024).
- ***Cap nhat "mp_christmas_tree_cho_VSCode" va "mp_christmas_tree_cho_TEXT".***

### 0.0.3.7 - (4/5/2024).
- ***Cap nhat "mp_christmas_tree".***

### 0.0.3.6 - (03/03/2024).
- ***Thu nghiem.***

### 0.0.3.5 - (01/03/2024).
- ***Thu nghiem.***

### 0.0.3.4 - (26/02/2024).
- ***Bo sung "ham uoc_chung_cua_danh_sach" (de tim cac uoc chung trong mot array).***

### 0.0.3.3 - (21/02/2024).
- ***Nang cap info library, README.***

### 0.0.3.2 - (20/02/2024).
- ***Bo sung so phong phu.***

### 0.0.3.1 - (20/02/2024).
- ***Nang cap info library.***

### 0.0.3 - (20/02/2024).
- ***Bo sung "xau_ki_tu_khong_trung_lap" (khong theo thu tu bang chu cai) va loai bo "ki_tu_trung_lap" (theo thu tu bang chu cai).***

### 0.0.2.10 - (19/02/2024).
- ***Nang cap README.***

### 0.0.2.9 - (19/02/2024).
- ***Thu nghiem.***

### 0.0.2.8 - (19/02/2024).
- ***Thu nghiem.***

### 0.0.2.7 - (18/02/2024).
- ***Nang cap README.***

### 0.0.2.6 - (18/02/2024).
- ***Thay doi sang MIT License.***

### 0.0.2.5 - (18/02/2024).
- ***Nang cap README.***

### 0.0.2.4 - (18/02/2024).
- ***Nang cap README.***

### 0.0.2.3 - (18/02/2024).
- ***Thu nghiem.***

### 0.0.2.2 - (14/02/2024).
- ***Thu nghiem.***

### 0.0.2.1 - (14/02/2024).
- ***Thu nghiem.***

### 0.0.2 - (14/02/2024).
- ***Sua loi khong them cac phu thuoc.***

### 0.0.1.2 - (14/02/2024).
- ***Thu nghiem.***

### 0.0.1.1 - (14/2/2024).
- ***Thu nghiem.***

### 0.0.1 - (14/02/2024).
- ***Phien ban dau tien.***

### 0.0.0.1 - (14/02/2024).
- ***Thu nghiem.***