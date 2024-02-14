# Minh cung cap nhung ham con minh suu tam (co nhung sai sot trong qua trinh minh lam, mong moi nguoi giup do).

# Cac ham kiem tra tinh chat so nguyen to va so nguyen to lien quan:
// Ham kiem tra xem mot so co phai la so nguyen to hay khong.
- kiem_tra_so_nguyen_to(n).
>> True/ False neu (khong) la so nguyen to;

// Ham tao danh sach cac so nguyen to den n.
- tao_danh_sach_so_nguyen_to(n).
>> Mot danh sach cac so nguyen to nam trong khoang tu 0 toi so n da nhap;

// Ham kiem tra so emirp (mot so emirp la mot so nguyen to ma khi dao nguoc vi tri cac chu so cua no, ta cung duoc mot so nguyen to, khong ke nhung so nguyen to doi xung).
- kiem_tra_so_emirp(n).
>> True/ False neu (khong) la so emirp;

// Ham tao so emirp den n.
- tao_danh_sach_so_emirp(n).
>> Mot danh sach cac so emirp nam trong khoang tu 0 toi so n da nhap;

# Cac ham lien quan den so Fibonacci:
// Ham tinh so Fibonacci thu n.
- vi_tri_so_Fibonacci(n).
>> Vi tri cua mot so Fibonacci thu n;

// Ham tao danh sach cac so Fibonacci den n.
- tao_danh_sach_so_Fibonacci(n).
>> Mot danh sach cac so Fibonacci trong khoang tu 0 toi so n da nhap;

# Cac ham so hoan thien, so tu man, hua hon, hoan hao, than thiet va tinh tong cac uoc, chu so:
// Ham tinh tong cac uoc so cua n khong tinh n va khong am.
- tong_uoc_so(n).
>> Tong cac uoc so duong cua so n;

// Ham tinh tong cac chu so cua mot so.
- tong_chu_so(n).
>> Tong cac chu so cua so n;

// Ham kiem tra xem mot so co phai la so hoan thien (mot so hoan thien la mot so nguyen duong ma tong cac uoc nguyen duong cua no bang chinh no).
- kiem_tra_so_hoan_thien(n).
>> True/ False neu (khong) la so hoan thien;

// Ham tao danh sach cac so hoan thien.
- tao_danh_sach_so_hoan_thien(n).
>> Mot danh sach cac so hoan thien trong khoang tu 0 toi so n da nhap;

// Ham kiem tra so tu man (mot so tu man la so bang tong cac mu bac ba cua moi chu so cua no).
- kiem_tra_so_tu_man(n).
>> True/ False neu (khong) la mot so tu man;

// Ham tao danh sach cac so tu man.
- tao_danh_sach_so_tu_man(n).
>> Mot danh sach cac so tu man trong khoang tu 0 toi so n da nhap;

// Ham kiem tra cap so hua hon (mot cap so hua hon la hai so nguyen duong ma tong cac uoc cua so nay (khong tinh so do) nhieu hon so kia dung 1 don vi).
- cap_so_hua_hon(a, b).
>> True/ False neu a, b (khong) la mot cap so hua hon.

// Ham kiem tra so hoan hao (mot so hoan hao la khi tong cac uoc so thuc su cua n cung bang n).
- kiem_tra_so_hoan_hao(n).
>> True/ False neu (khong) la mot so hoan hao;

// Ham tao danh sach so hoan hao.
- tao_danh_sach_so_hoan_hao(n).
>> Mot danh sach cac so hoan hao trong khoang tu 0 toi so n da nhap;

# Cac ham kiem tra va tao danh sach so chinh phuong, than thiet, manh me loai 1, 2:
// Ham kiem tra so chinh phuong (so chinh phuong la so ma neu no la binh phuong cua mot so nguyen).
- kiem_tra_so_chinh_phuong(n).
>> True/ False neu (khong) la mot so chinh phuong;

// Ham tao danh sach cac so chinh phuong den n.
- tao_danh_sach_so_chinh_phuong(n).
>> Mot danh sach cac so chinh phuong trong khoang tu 0 toi so n da nhap;

// Ham kiem tra xem hai so co phai la cac so than thiet (mot cap so than thiet la khi chung tuan theo quy luat: So nay bang tong tat ca cac uoc cua so kia (tru chinh so do) va nguoc lai).
- cap_so_than_thiet(a, b).
>> True/ False neu a, b (khong) la cac so than thiet;

// Ham kiem tra so manh me (neu tong chu so no la mot so nguyen to).
- kiem_tra_so_manh_me_1(n).
>> True/ False neu (khong) la mot so manh me;

// Ham kiem tra so manh me (neu mot so vua chia het cho nhung so nguyen to va binh phuong cua chung truoc no).
- kiem_tra_so_manh_me_2(n).
>> True/ False neu (khong) la mot so manh me;

# Cac ham lien quan den uoc so va boi so:
// Ham tao danh sach cac uoc so cua mot so.
- tao_danh_sach_uoc_so(n).
>> Mot danh sach cac uoc so cua mot so;

// Ham tim uoc chung lon nhat cua 2 so.
- uoc_chung_lon_nhat(a, b).
>> Gia tri uoc chung lon nhat cua a, b;

// Ham tinh uoc so chung lon cua mot danh sach cac so (uoc chung lon nhat cua nhieu so).
- uoc_chung_lon_nhat_cua_danh_sach(array).
>> Gia tri uoc chung lon nhat cua array;

// Ham tinh boi so chung nho nhat cua hai so.
- boi_chung_nho_nhat(a, b).
>> Gia tri boi chung nho nhat cua a, b;

// Ham tinh boi so chung nho nhat cua mot danh sach cac so (boi chung nho nhat cua nhieu so).
- boi_chung_nho_nhat_cua_danh_sach(array).
>> Gia tri boi chung nho nhat cua array;

// Ham tao danh sach cac boi so cua mot so len den 10 lan.
- tao_danh_sach_boi_so(n).
>> Mot danh sach cac so boi so cua tu 0 toi 10 lan;

# Cac ham lien quan den tinh chat so song to:
// Ham kiem tra cac so song to.
- kiem_tra_so_song_to(n).
>> True/ False neu (khong) la mot so song to;

// Ham tao danh sach cac so song to.
- tao_danh_sach_so_song_to(n).
>> Mot danh sach cac so song to tu 0 toi n;

# Cac ham lien quan den phan tich thua so nguyen to:
// Ham tinh cac thua so nguyen to cua mot so (vip).
- thua_so_nguyen_to_day_du(n).
>> Tra ve tich cua nhung so nguyen to (co so mu) bang so n;

// Ham tinh cac thua so nguyen to cua mot so dang list.
- thua_so_nguyen_to(n).
>> Tra ve mot danh sach cac so nguyen to co tich bang n;

// Ham tinh uoc so chung lon nhat nguyen to cua hai so.
- uoc_chung_nguyen_to_2_so(a, b).
>> Gia tri uoc chung nguyen to lon nhat cua a, b;

# Cac ham lien quan den phuong trinh va bieu thuc toan hoc:
// Ham giai phuong trinh bac 1, 2 mot an va vai luu y, khi nhap: phuong_trinh = "12x^2 + 34 - 24 = 23x - 13".
- giai_pt_bac_1va2_dang_string(phuong_trinh).
>> Nghiem cua phuong trinh;

// Ham giai phuong trinh bac 1 - 10 bang cach nhap he so.(bac = bac cua phuong trinh).
- giai_phuong_trinh(bac, he_so_phuong_trinh):
>> Nghiem cua phuong trinh;

# Cac ham lien quan den trich xuat, xu ly chuoi, danh sach:
// Ham loai bo cac phan tu trung lap tu mot danh sach.
- danh_sach_khong_trung_lap(lst).
>> Danh sach voi nhung phan tu khong trung lap;

// Ham loai bo cac ky tu trung lap tu mot chuoi.
- ki_tu_khong_trung_lap(string).
>> Mot chuoi khong trung lap;

// Ham trich xuat cac chu so tu mot chuoi.
- trich_xuat_chu_so_tu_chuoi(s).
>> Mot chuoi chu so co trong s;

// Ham trich xuat cac so tu mot chuoi.
- trich_xuat_so_tu_chuoi(s).
>> Mot chuoi cac so co trong s;

// Ham trich xuat cac ky tu tu mot chuoi.
- trich_xuat_ki_tu(s).
>> Trich xuat ki tu co trong s;

// Ham an ki tu dang "12/05/2010" == "**/**/***".
- an_ki_tu(s).
>> Mot day ki tu an ma khong the truy lai s ban dau;

// Ham trich xuat cac so tu chuoi so. VD: "32/232343244" se la "32.232343244".
- trich_xuat_cac_so_tu_so(s).
>> Trich xuat cac so tu mot day so nhung lan voi ki tu;

// Ham nen xau nhung khong ghi so. VD: "hhhooccsiinh" se la "hocsinh".
- xau_duoc_nen_ko_so(chuoi_nhap).
>> Xau duoc nen;

// Ham giai nen xau.
- xau_duoc_giai_nen(s).
>> Xau duoc giai nen;

# Mat ma Caesar:
# Phuong phap ma hoa cua Caesar duoc vi du cu the nhu sau: 
>> Dung mat ma cua Caesar chuyen buc thu "MEET YOU IN THE PARK" thanh buc thu bi mat. 
>> Cac chu cai duoc bieu dien thanh so theo quy tac sau.

- A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
- 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

>> Khi do buc thu goc "MEET YOU IN THE PARK" tro thanh (khong tinh khoang trang): "12 4 4 19 24 14 20 8 13 19 7 4 15 0 17 10"
>> Bay gio ta se quay chuoi so 0 -> 25 sang trai k so (vi du trong truong hop nay k = 3) khi do ta co bang sau.

- 0 1 2 3 4 5 6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 
- 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25  0  1  2

>> Khi do chuoi so "12 4 4 19 24 14 20 8 13 19 7 4 15 0 17 10" se duoc ma hoa thanh: "15 7 7 22 1 17 23 11 16 22 10 7 18 3 20 13"

// Ham chuyen hoa chuoi thanh mat ma Caesar.
- chuyen_hoa_caesar(string, sang_trai_k_so).
>> Day so mat ma caesar;

// Ham ma hoa day so Caesar.
- ma_hoa_caesar(array, sang_trai_k_so).
>> Xau duoc ma hoa boi day so mat ma;

# Cac ham mo phong chi voi string:
// Ham mo phong qua trinh "Tai xuong" (pham vi so n la lon hon 0 va nho hon 88).
- mp_tai_xuong(n).
>> 
  Dang tai xuong [■■■■■■■■■■■■■■■■■■■■■■■■■] 100%
  Tai xuong hoan tat!

// Ham mo phong qua trinh "tinh toan" cua "Admin" (giong nhu mo phong tai xuong).
- mp_tinh_toan(n).
>> 
  AD: Dang tinh toan [■■■■■■■■■■■■■■■■■■■■■■■■■] 100%

// Ham mo phong qua trinh "LOADING...".
- mp_loading(n).
>> LOADING...

// Ham mo phong cay thong.
- mp_christmas_tree():
>>
                      * 
                    * * * 
                  * * * * * 
                * * * * * * * 
              * * * * * * * * * 
            * * * * * * * * * * * 
          * * * * * * * * * * * * * 
                      * 
                      * 
                      * 

# Ham ho tro tinh toan dac biet:
// Ham tinh toan cac cong thuc vat ly.
- tinh_toan_vat_ly_8().
>> Mot bang lua chon cac cong thuc vat ly 8 chuong trinh GDPT 2018 sach CTST HK1;

// Ham tinh toan tien dien a la chi so cu, b la chi so moi (b > a).
- tinh_toan_tien_dien(chi_so_cu, chi_so_moi).
>> So Kwh da tieu thu va so tien phai tra;

// Ham tim mot so lon nhat co tong cac chu "a" so bang so "b". VD: 3, 21 se bang 993.
- tong_chu_so_lon_nhat_bang_n(number_of_digits, int_number).
>> So ket qua;

// Ham dinh ly Pythagore (muon tim canh nao thi cho canh do bang False. VD a = 1, b = 2, c = False de tim c va trong do, a la canh goc vuong 1, b la canh goc vuong 2, c la canh huyen).
- pythagore(a, b, c).
>> Gia tri cua canh can tim trong tam giac;

# Quy luat:
// Ham tao danh sach cac so theo quy luat: 1 so chia het 1, 2 so chia het 2, 3 so chia het 3, ... cho toi tong so luong la number.
- tao_danh_sach_quy_luat_1(number).
>> Mot danh sach theo quy luat 1;

// Ham tao mot day so theo quy luat: cap so nhan voi n phan tu va m. VD: n = 10, m = 2 -> array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18].
- tao_danh_sach_quy_luat_2(m, n).
>> Mot danh sach theo quy luat 2;

// Ham tao day so theo quy luat: so mu nang toi lan thu n cua so m. VD: m = 3, n = 10 -> array = [3^0, 3^1, 3^2, ... , 3^10].
- tao_danh_sach_quy_luat_3(n, m).
>> Mot danh sach theo quy luat 3;

# Khac:
// Ham chuyen doi so binh thuong thanh so La Ma.
- chuyen_doi_so_la_ma(num).
>> So la ma cua num;

// Ham dem so nghich the trong mot danh sach (cho day so nguyen duong gom n phan tu a1, a2 ,…, a{n} . Mot cap (a[i], a[j] ) duoc goi la mot nghich the neu i < j va a[i] > a[j]).
- dem_so_nghich_the(danh_sach).
>> So nghich the trong danh sach;

// Ham choi keo bua bao voi "A.I".
- one_two_three().
>> Nhung su lua chon de ban choi keo bua bao voi A.I;