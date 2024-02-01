# Code của mình cung cấp những hàm mà mình đã sưu tầm 🐧 (*Lưu ý: có những sai sót trong quá trình mình làm, mong mọi người giúp đỡ).

# Vietnamese:
# Các hàm kiểm tra tính chất số nguyên tố và số nguyên tố liên quan:
// Hàm kiểm tra xem một số có phải là số nguyên tố hay không.
- kiem_tra_so_nguyen_to(n).
>> True/ False nếu (không) là số nguyên tố;

// Hàm tạo danh sách các số nguyên tố đến n.
- tao_danh_sach_so_nguyen_to(n).
>> Một danh sách các số nguyên tố nằm trong khoảng từ 0 tới số n đã nhập;

// Hàm kiểm tra số emirp (một số emirp là một số nguyên tố mà khi đảo ngược vị trí các chữ số của nó, ta cũng được một số nguyên tố, không kể những số nguyên tố đối xứng).
- kiem_tra_so_emirp(n).
>> True/ False nếu (không) là số emirp;

// Hàm tạo số emirp đến n.
- tao_danh_sach_so_emirp(n).
>> Một danh sách các số emirp nằm trong khoảng từ 0 tới số n đã nhập;

# Các hàm liên quan đến số Fibonacci:
// Hàm tính số Fibonacci thứ n.
- vi_tri_so_Fibonacci(n).
>> Vị trí của một số Fibonacci thứ n;

// Hàm tạo danh sách các số Fibonacci đến n.
- tao_danh_sach_so_Fibonacci(n).
>> Một danh sách các số Fibonacci trong khoảng từ 0 tới số n đã nhập;

# Các hàm số hoàn thiện, số tự mãn, hứa hôn, hoàn hảo, thân thiết và tính tổng các ước, chữ số:
// Hàm tính tổng các ước số của n không tính n và không âm.
- tong_uoc_so(n).
>> Tổng các ước số dương của số n;

// Hàm tính tổng các chữ số của một số.
- tong_chu_so(n).
>> Tổng các chữ số của số n;

// Hàm kiểm tra xem một số có phải là số hoàn thiện (một số hoàn thiện là một số nguyên dương mà tổng các ước nguyên dương của nó bằng chính nó).
- kiem_tra_so_hoan_thien(n).
>> True/ False nếu (không) là số hoàn thiện;

// Hàm tạo danh sách các số hoàn thiện.
- tao_danh_sach_so_hoan_thien(n).
>> Một danh sách các số hoàn thiện trong khoảng từ 0 tới số n đã nhập;

// Hàm kiểm tra số tự mãn (một số tự mãn là số bằng tổng các mũ bậc ba của mỗi chữ số của nó).
- kiem_tra_so_tu_man(n).
>> True/ False nếu (không) là một số tự mãn;

// Hàm tạo danh sách các số tự mãn.
- tao_danh_sach_so_tu_man(n).
>> Một danh sách các số tự mãn trong khoảng từ 0 tới số n đã nhập;

// Hàm kiểm tra cặp số hứa hôn (một cặp số hứa hôn là hai số nguyên dương mà tổng các ước của số này (không tính số đó) nhiều hơn số kia đúng 1 đơn vị).
- cap_so_hua_hon(a, b).
>> True/ False nếu a, b (không) là một cặp số hứa hôn.

// Hàm kiểm tra số hoàn hảo (một số hoàn hảo là khi tổng các ước số thực sự của n cũng bằng n).
- kiem_tra_so_hoan_hao(n).
>> True/ False nếu (không) là một số hoàn hảo;

// Hàm tạo danh sách số hoàn hảo.
- tao_danh_sach_so_hoan_hao(n).
>> Một danh sách các số hoàn hảo trong khoảng từ 0 tới số n đã nhập;

# Các hàm kiểm tra và tạo danh sách số chính phương, thân thiết, mạnh mẽ loại 1, 2:
// Hàm kiểm tra số chính phương (số chính phương là số mà nếu nó là bình phương của một số nguyên).
- kiem_tra_so_chinh_phuong(n).
>> True/ False nếu (không) là một số chính phương;

// Hàm tạo danh sách các số chính phương đến n.
- tao_danh_sach_so_chinh_phuong(n).
>> Một danh sách các số chính phương trong khoảng từ 0 tới số n đã nhập;

// Hàm kiểm tra xem hai số có phải là các số thân thiết (một cặp số thân thiết là khi chúng tuân theo quy luật: Số này bằng tổng tất cả các ước của số kia (trừ chính số đó) và ngược lại).
- cap_so_than_thiet(a, b).
>> True/ False nếu a, b (không) là các số thân thiết;

// Hàm kiểm tra số mạnh mẽ (nếu tổng chữ số nó là một số nguyên tố).
- kiem_tra_so_manh_me_1(n).
>> True/ False nếu (không) là một số mạnh mẽ;

// Hàm kiểm tra số mạnh mẽ (nếu một số vừa chia hết cho những số nguyên tố và bình phương của chúng trước nó).
- kiem_tra_so_manh_me_2(n).
>> True/ False nếu (không) là một số mạnh mẽ;

# Các hàm liên quan đến ước số và bội số:
// Hàm tạo danh sách các ước số của một số.
- tao_danh_sach_uoc_so(n).
>> Một danh sách các ước số của một số;

// Hàm tìm ước chung lớn nhất của 2 số.
- uoc_chung_lon_nhat(a, b).
>> Giá trị ước chung lớn nhất của a, b;

// Hàm tính ước số chung lớn của một danh sách các số (ước chung lớn nhất của nhiều số).
- uoc_chung_lon_nhat_cua_danh_sach(array).
>> Giá trị ước chung lớn nhất của array;

// Hàm tính bội số chung nhỏ nhất của hai số.
- boi_chung_nho_nhat(a, b).
>> Giá trị bội chung nhỏ nhất của a, b;

// Hàm tính bội số chung nhỏ nhất của một danh sách các số (bội chung nhỏ nhất của nhiều số).
- boi_chung_nho_nhat_cua_danh_sach(array).
>> Giá trị bội chung nhỏ nhất của array;

// Hàm tạo danh sách các bội số của một số lên đến 10 lần.
- tao_danh_sach_boi_so(n).
>> Một danh sách các số bội số của từ 0 tới 10 lần;

# Các hàm liên quan đến tính chất số song tố:
// Hàm kiểm tra các số song tố.
- kiem_tra_so_song_to(n).
>> True/ False nếu (không) là một số song tố;

// Hàm tạo danh sách các số song tố.
- tao_danh_sach_so_song_to(n).
>> Một danh sách các số song tố từ 0 tới n;

# Các hàm liên quan đến phân tích thừa số nguyên tố:
// Hàm tính các thừa số nguyên tố của một số (vip).
- thua_so_nguyen_to_day_du(n).
>> Trả về tích của những số nguyên tố (có số mũ) bằng số n;

// Hàm tính các thừa số nguyên tố của một số dạng list.
- thua_so_nguyen_to(n).
>> Trả về một danh sách các số nguyên tố có tích bằng n;

// Hàm tính ước số chung lớn nhất nguyên tố của hai số.
- uoc_chung_nguyen_to_2_so(a, b).
>> Giá trị ước chung nguyên tố lớn nhất của a, b;

# Các hàm liên quan đến phương trình và biểu thức toán học:
// Hàm giải phương trình bậc 1, 2 một ẩn và vài lưu ý, khi nhập: phuong_trinh = "12x^2 + 34 - 24 = 23x - 13".
- giai_pt_bac_1va2_dang_string(phuong_trinh).
>> Nghiệm của phương trình;

// Hàm giải phương trình bậc 1 - 10 bằng cách nhập hệ số.(bac = bậc của phương trình).
- giai_phuong_trinh(bac, he_so_phuong_trinh):
>> Nghiệm của phương trình;

# Các hàm liên quan đến trích xuất, xử lý chuỗi, danh sách:
// Hàm loại bỏ các phần tử trùng lặp từ một danh sách.
- danh_sach_khong_trung_lap(lst).
>> Danh sách với những phần tử không trùng lặp;

// Hàm loại bỏ các ký tự trùng lặp từ một chuỗi.
- ki_tu_khong_trung_lap(string).
>> Một chuỗi không trùng lặp;

// Hàm trích xuất các chữ số từ một chuỗi.
- trich_xuat_chu_so_tu_chuoi(s).
>> Một chuỗi chữ số có trong s;

// Hàm trích xuất các số từ một chuỗi.
- trich_xuat_so_tu_chuoi(s).
>> Một chuỗi các số có trong s;

// Hàm trích xuất các ký tự từ một chuỗi.
- trich_xuat_ki_tu(s).
>> Trích xuất kí tự có trong s;

// Hàm ẩn kí tự dạng "12/05/2010" == "••/••/••••".
- an_ki_tu(s).
>> Một dãy kí tự ẩn mà không thể truy lại s ban đầu;

// Hàm trích xuất các số từ chuỗi số. VD: "32/232343244" sẽ là "32.232343244".
- trich_xuat_cac_so_tu_so(s).
>> Trích xuất các số từ một dãy số nhưng lân với kí tự;

// Hàm nén xâu nhưng không ghi số. VD: "hhhooccsiinh" sẽ là "hocsinh".
- xau_duoc_nen_ko_so(chuoi_nhap).
>> Xâu được nén;

// Hàm giải nén xâu.
- xau_duoc_giai_nen(s).
>> Xâu được giải nén;

# Mật mã Caesar:
# Phương pháp mã hoá của Caesar được ví dụ cụ thể như sau: 
>> Dùng mật mã của Caesar chuyển bức thư “MEET YOU IN THE PARK” thành bức thư bí mật. 
>> Các chữ cái được biểu diễn thành số theo quy tắc sau.

- A B C D E F G H I J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
- 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

>> Khi đó bức thư gốc “MEET YOU IN THE PARK” trở thành (không tính khoảng trắng): “12 4 4 19 24 14 20 8 13 19 7 4 15 0 17 10”
>> Bây giờ ta sẽ quay chuỗi số 0 -> 25 sang trái k số (ví dụ trong trường hợp này k = 3) khi đó ta có bảng sau.

- 0 1 2 3 4 5 6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 
- 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25  0  1  2

>> Khi đó chuỗi số “12 4 4 19 24 14 20 8 13 19 7 4 15 0 17 10” sẽ  được mã hóa thành: “15 7 7 22 1 17 23 11 16 22 10 7 18 3 20 13”

// Hàm chuyển hóa chuỗi thành mật mã Caesar.
- chuyen_hoa_caesar(string, sang_trai_k_so).
>> Dãy số mật mã caesar;

// Hàm mã hóa dãy số Caesar.
- ma_hoa_caesar(array, sang_trai_k_so).
>> Xâu được mã hóa bởi dãy số mật mã;

# Các hàm mô phổng chỉ với string:
// Hàm mô phỏng quá trình "Tải xuống" (phạm vi số n là lớn hơn 0 và nhỏ hơn 88).
- mp_tai_xuong(n).
>> 
   Đang tải xuống [■■■■■■■■■■■■■■■■■■■■■■■■■] 100%
   Tải xuống hoàn tất!

// Hàm mô phỏng quá trình "tính toán" của "Admin" (giống như mô phổng tải xuống).
- mp_tinh_toan(n).
>> 
   AD: Đang tính toán [■■■■■■■■■■■■■■■■■■■■■■■■■] 100%

// Hàm mô phỏng quá trình "LOADING...".
- mp_loading(n).
>> LOADING...

// Hàm mô phỏng cây thông.
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

# Hàm hỗ trợ tính toán đặc biệt:
// Hàm tính toán các công thức vật lý.
- tinh_toan_vat_ly_8().
>> Một bảng lựa chọn các công thức vật lý 8 chương trình GDPT 2018 sách CTST HK1;

// Hàm tính toán tiền điện a là chỉ số cũ, b là chỉ số mới (b > a).
- tinh_toan_tien_dien(chi_so_cu, chi_so_moi).
>> Số Kwh đã tiêu thụ và số tiền phải trả;

// Hàm tìm một số lớn nhất có tổng các chữ "a" số bằng số "b". VD: 3,21 sẽ bằng 993.
- tong_chu_so_lon_nhat_bang_n(number_of_digits, int_number).
>> Số kết quả;

// Hàm định lý Pythagore (muốn tìm cạnh nào thì cho cạnh đó bằng False. VD a = 1, b = 2, c = False để tìm c và trong đó, a là cạnh góc vuông 1, b là cạnh góc vuông 2, c là cạnh huyền).
- pythagore(a, b, c).
>> Giá trị của cạnh cần tìm trong tam giác;

# Quy luật:
// Hàm tạo danh sách các số theo quy luật: 1 số :: 1, 2 số :: 2, 3 số :: 3, ... cho tới tổng số lượng là number (dấu :: là dấu chia hết)
- tao_danh_sach_quy_luat_1(number).
>> Một danh sách theo quy luật 1;

// Hàm tạo một dãy số theo quy luật: mỗi phần tử của dãy số vô hạn này tích với n đơn vị. VD: number = 10, n = 2 => array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18].
- tao_danh_sach_quy_luat_2(n, number).
>> Một danh sách theo quy luật 2;

// Hàm tạo dãy số theo quy luật: số mũ nâng tới n của số number. VD: number = 3, n = 10 => array = [3^0, 3^1, 3^2, ..., 3^10].
- tao_danh_sach_quy_luat_3(n, number).
>> Một danh sách theo quy luật 3;

# Khác:
// Hàm chuyển đổi số bình thường thành số La Mã.
- chuyen_doi_so_la_ma(num).
>> Số la mã của num;

// Hàm đếm số nghịch thế trong một danh sách (cho dãy số nguyên dương gồm n phần tử a1, a2 ,…, a{n} . Một cặp (a[i], a[j] ) được gọi là một nghịch thế nếu i < j và a[i] > a[j]).
- dem_so_nghich_the(danh_sach).
>> Số nghịch thế trong danh sách;