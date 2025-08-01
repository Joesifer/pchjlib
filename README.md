<h1 align="center">
<img src="https://i.imgur.com/AUXxUzd.png" width="500" alt="PCHJLIB - Joesifer">
</h1><br>


[![PyPI Downloads](https://img.shields.io/badge/pchjlib-PyPI_downloads?style=plastic&logo=pchjlib&label=PyPI%20downloads)](https://pypi.org/project/pchjlib/)
[![GitHub](https://img.shields.io/badge/pchjlib-Joesifer_GitHub?style=plastic&logo=GitHub&label=GitHub)](https://github.com/Joesifer/pchjlib)
[![Python](https://img.shields.io/badge/Version_%3E_3.7-1?style=plastic&label=Python)](https://www.python.org/)
[![Owner](https://img.shields.io/badge/Joesifer-1?style=plastic&label=PCHJLIB&labelColor=%2300fff7&color=%23ffe600)](https://github.com/Joesifer)

# 📚 Yêu cầu

- **Python**: >= 3.7
- **numpy**: Tùy chọn, cho hàm `giai_phuong_trinh` và `tao_danh_sach_so_nguyen_to`. Cài bằng `pip install pchjlib[numpy]` hoặc `pip install numpy`.
- **roman**: Tùy chọn, chỉ cần cho hàm `chuyen_doi_so_la_ma`. Cài bằng `pip install pchjlib[roman]` hoặc `pip install roman`.
- Để cài đặt đầy đủ: `pip install pchjlib[full]`.

# 🛠️ Cài đặt

Bạn có thể cài đặt thư viện cơ bản mà không cần các phụ thuộc tùy chọn:

```bash
pip install pchjlib
```

Nếu bạn cần sử dụng hàm `giai_phuong_trinh` và `tao_danh_sach_so_nguyen_to`, hãy cài đặt với `numpy`:

```bash
pip install pchjlib[numpy]
```

Tương tự, cho hàm `chuyen_doi_so_la_ma`, cài đặt với `roman`:

```bash
pip install pchjlib[roman]
```

Để cài đặt đầy đủ với tất cả các phụ thuộc:

```bash
pip install pchjlib[full]
```

---


# 🌟 Tính năng chính

- 🔍 **Kiểm tra và tạo danh sách các loại số đặc biệt:**  
  Hỗ trợ số nguyên tố, số emirp, số Fibonacci, số hoàn thiện, số tự mãn, số hữu hảo, số chính phương, số mạnh mẽ, số song tố, số phong phú, v.v.

- 🔗 **Xử lý ước số và bội số:**  
  Tạo danh sách ước số, tính ước chung lớn nhất (UCLN), bội chung nhỏ nhất (BCNN), phân tích thừa số nguyên tố.

- 🧮 **Giải phương trình:**  
  Giải các phương trình đa thức từ bậc 1 đến bậc 10.

- 🧹 **Xử lý danh sách và chuỗi:**  
  Loại bỏ phần tử trùng lặp, trích xuất chữ số/số/ký tự từ chuỗi, nén và giải nén chuỗi.

- 🔐 **Mã hóa và giải mã:**  
  Mã hóa Caesar (mã hóa Caesar chỉ mang tính giáo dục, không dùng cho bảo mật thực tế), chuyển đổi chuỗi thành Teen Code Yahoo.

- 🧪 **Mô phỏng:**  
  Mô phỏng quá trình tải xuống, tính toán, loading, và tạo cây thông Giáng sinh.

- ✨ **Tính toán đặc biệt:**  
  Tính tiền điện, tìm số lớn nhất với tổng chữ số cho trước, tính cạnh tam giác vuông.

- 🔢 **Tạo dãy theo quy luật:**  
  Tạo các dãy số theo các quy luật cụ thể.

- 🔄 **Chuyển đổi và đếm:**  
  Chuyển số thành số La Mã, đếm số cặp nghịch thế trong danh sách.

- 🎮 **Trò chơi:**  
  Chơi kéo búa bao với AI.

# 📚 MỤC LỤC

- 🔢 [Các hàm kiểm tra số nguyên tố và số liên quan](#các-hàm-kiểm-tra-số-nguyên-tố-và-số-liên-quan)  
- 🌀 [Các hàm Fibonacci](#các-hàm-fibonacci)  
- 🧠 [Các hàm tính số hoàn thiện, tự mãn, hữu hảo, hoàn hào, thân thiết](#các-hàm-tính-số-hoàn-thiện-tự-mãn-hữu-hảo-hoàn-hào-thân-thiết)  
- 📐 [Các hàm số chính phương, mạnh mẽ, thân thiết](#các-hàm-số-chính-phương-mạnh-mẽ-thân-thiết)  
- 📊 [Các hàm về ước số và bội số](#các-hàm-về-ước-số-và-bội-số)  
- 👯 [Các hàm số song tố và số phong phú](#các-hàm-số-song-tố-và-số-phong-phú)  
- 🔍 [Các hàm phân tích thừa số nguyên tố](#các-hàm-phân-tích-thừa-số-nguyên-tố)  
- 🧮 [Các hàm giải phương trình](#các-hàm-giải-phương-trình)  
- 🧵 [Các hàm xử lý danh sách và chuỗi](#các-hàm-xử-lý-danh-sách-và-chuỗi)  
- 🏛️ [Mật mã Caesar](#mật-mã-caesar)  
- 👶 [Teen Code Yahoo](#teen-code-yahoo)  
- 🧬 [Các hàm mô phỏng chỉ với string](#các-hàm-mô-phỏng-chỉ-với-string)  
- 💥 [Hàm hỗ trợ tính toán đặc biệt](#hàm-hỗ-trợ-tính-toán-đặc-biệt)  
- 🔁 [Quy luật sinh dãy](#quy-luật-sinh-dãy)  
- 🔄 [Chuyển đổi và đếm](#chuyển-đổi-và-đếm)  
- 🧩 [Khác](#khác)  
- 🛠️ [Những bản cập nhật](#những-bản-cập-nhật)

---

## 🔢 Các hàm kiểm tra số nguyên tố và số liên quan

- **kiem_tra_so_nguyen_to(number)**  
  Kiểm tra xem một số có phải là số nguyên tố hay không. Trả về `True` nếu là số nguyên tố, `False` nếu không.  
  - Tham số: `number` (int) - Số cần kiểm tra.  
  - Ném lỗi: `InvalidInputError` nếu đầu vào không phải số nguyên.

- **tao_danh_sach_so_nguyen_to(limit)**  
  Tạo danh sách các số nguyên tố từ 0 đến `limit`.  
  - Tham số: `limit` (int) - Giới hạn trên của danh sách.  
  - Trả về: Danh sách các số nguyên tố.  
  - Ném lỗi: `InvalidInputError` nếu `limit` không phải số nguyên >= 2.

- **kiem_tra_so_emirp(number)**  
  Kiểm tra xem một số có phải là số emirp (số nguyên tố đảo ngược cũng là nguyên tố) hay không.  
  - Tham số: `number` (int) - Số cần kiểm tra.  
  - Trả về: `True` nếu là số emirp, `False` nếu không.  
  - Ném lỗi: `InvalidInputError` nếu `number` không phải số nguyên dương.

- **tao_danh_sach_so_emirp(limit)**  
  Tạo danh sách các số emirp từ 0 đến `limit`.  
  - Tham số: `limit` (int) - Giới hạn trên của danh sách.  
  - Trả về: Danh sách các số emirp.  
  - Ném lỗi: `InvalidInputError` nếu `limit` không phải số nguyên không âm.

---

## 🌀 Các hàm Fibonacci

- **vi_tri_so_Fibonacci(index)**  
  Tính số Fibonacci thứ `index` bằng phương pháp lặp.  
  - Tham số: `index` (int) - Vị trí của số Fibonacci (bắt đầu từ 0).  
  - Trả về: Số Fibonacci tại vị trí `index`.  
  - Ném lỗi: `InvalidInputError` nếu `index` không phải số nguyên không âm.

- **tao_danh_sach_so_Fibonacci(count)**  
  Tạo danh sách `count` số Fibonacci đầu tiên.  
  - Tham số: `count` (int) - Số lượng phần tử trong danh sách.  
  - Trả về: Danh sách các số Fibonacci.  
  - Ném lỗi: `InvalidInputError` nếu `count` không phải số nguyên không âm.

---

## 🧠 Các hàm tính số hoàn thiện, tự mãn, hữu hảo, hoàn hào, thân thiết

- **tong_uoc_so(number)**  
  Tính tổng các ước số dương của `number` (không tính chính nó).  
  - Tham số: `number` (int) - Số cần tính.  
  - Trả về: Tổng các ước số.  
  - Ném lỗi: `MathError` nếu `number <= 0`, `InvalidInputError` nếu không phải số nguyên.

- **tong_chu_so(number)**  
  Tính tổng các chữ số của `number`.  
  - Tham số: `number` (int) - Số cần tính.  
  - Trả về: Tổng các chữ số.  
  - Ném lỗi: `InvalidInputError` nếu không phải số nguyên.

- **kiem_tra_so_hoan_thien(number)**  
  Kiểm tra xem `number` có phải là số hoàn thiện hay không.  
  - Tham số: `number` (int) - Số cần kiểm tra.  
  - Trả về: `True` nếu là số hoàn thiện, `False` nếu không.  
  - Ném lỗi: `MathError` nếu `number < 1`, `InvalidInputError` nếu không phải số nguyên.

- **tao_danh_sach_so_hoan_thien(limit)**  
  Tạo danh sách các số hoàn thiện từ 1 đến `limit`.  
  - Tham số: `limit` (int) - Giới hạn trên của danh sách.  
  - Trả về: Danh sách các số hoàn thiện.  
  - Ném lỗi: `InvalidInputError` nếu `limit` không phải số nguyên > 0, `InvalidInputError` nếu `limit` không lớn hơn 1.

- **kiem_tra_so_tu_man(number)**  
  Kiểm tra xem `number` có phải là số tự mãn hay không.  
  - Tham số: `number` (int) - Số cần kiểm tra.  
  - Trả về: `True` nếu là số tự mãn, `False` nếu không.  
  - Ném lỗi: `InvalidInputError` nếu `number` không phải số nguyên >= 2.

- **tao_danh_sach_so_tu_man(limit)**  
  Tạo danh sách các số tự mãn từ 2 đến `limit`.  
  - Tham số: `limit` (int) - Giới hạn trên của danh sách.  
  - Trả về: Danh sách các số tự mãn.  
  - Ném lỗi: `InvalidInputError` nếu `limit` không phải số >= 2. `NotIntegerError` nếu `limit` không phải là số nguyên.

- **cap_so_hua_hon(number1, number2)**  
  Kiểm tra xem `number1` và `number2` có phải là cặp số hữu hảo hay không.  
  - Tham số: `number1`, `number2` (int) - Hai số cần kiểm tra.  
  - Trả về: `True` nếu là cặp hữu hảo, `False` nếu không.  
  - Ném lỗi: `MathError` nếu các số âm, `InvalidInputError` nếu không phải số nguyên.

- **kiem_tra_so_hoan_hao(number)**  
  Kiểm tra xem `number` có phải là số hoàn hảo hay không.  
  - Tham số: `number` (int) - Số cần kiểm tra.  
  - Trả về: `True` nếu là số hoàn hảo, `False` nếu không.  
  - Ném lỗi: `MathError` nếu `number < 1`, `InvalidInputError` nếu không phải số nguyên.

- **tao_danh_sach_so_hoan_hao(limit)**  
  Tạo danh sách các số hoàn hảo từ 1 đến `limit`.  
  - Tham số: `limit` (int) - Giới hạn trên của danh sách.  
  - Trả về: Danh sách các số hoàn hảo.  
  - Ném lỗi: `InvalidInputError` nếu `limit` không phải số nguyên > 0.

---

## 📐 Các hàm số chính phương, mạnh mẽ, thân thiết

- **kiem_tra_so_chinh_phuong(number)**  
  Kiểm tra xem `number` có phải là số chính phương hay không.  
  - Tham số: `number` (int) - Số cần kiểm tra.  
  - Trả về: `True` nếu là số chính phương, `False` nếu không.  
  - Ném lỗi: `InvalidInputError` nếu không phải số nguyên.

- **tao_danh_sach_so_chinh_phuong(limit)**  
  Tạo danh sách các số chính phương từ 0 đến `limit`.  
  - Tham số: `limit` (int) - Giới hạn trên của danh sách.  
  - Trả về: Danh sách các số chính phương.  
  - Ném lỗi: `InvalidInputError` nếu `limit` không phải số nguyên không âm.

- **cap_so_than_thiet(number1, number2)**  
  Kiểm tra xem `number1` và `number2` có phải là cặp số thân thiết hay không.  
  - Tham số: `number1`, `number2` (int) - Hai số cần kiểm tra.  
  - Trả về: `True` nếu là cặp thân thiết, `False` nếu không.  
  - Ném lỗi: `MathError` nếu các số không lớn hơn 1, `InvalidInputError` nếu không phải số nguyên.

- **kiem_tra_so_manh_me(number)**  
  Kiểm tra xem `number` có phải là số mạnh mẽ (tổng chữ số là nguyên tố) hay không.  
  - Tham số: `number` (int): Số cần kiểm tra.
             `variant` (int): 1 - Tổng chữ số là nguyên tố; 2 - Có thừa số nguyên tố bình phương.
  - Trả về: `True` nếu là số mạnh mẽ, `False` nếu không.  
  - Ném lỗi: `InvalidInputError` nếu không phải số nguyên.

---

## 📊 Các hàm về ước số và bội số

- **tao_danh_sach_uoc_so(number, positive_only=True)**  
  Tạo danh sách các ước số của `number`.  
  - Tham số: `number` (int) - Số cần tạo danh sách ước số. `positive_only` (bool) - Nếu True, chỉ trả về ước số dương.  
  - Trả về: Danh sách các ước số.  
  - Ném lỗi: `MathError` nếu `number = 0`.

- **tao_danh_sach_boi_so(number)**  
  Tạo danh sách bội số của `number` từ 0 đến 10 lần.  
  - Tham số: `number` (int) - Số cần tạo danh sách bội số.
  - positive_only = True 'hoặc' False. Mặc định là True và các ước sẽ luôn dương, có thể thay đổi thành False và các ước âm sẽ được xuất hiện.
  - Trả về: Danh sách bội số.  
  - Ném lỗi: `MathError` nếu `number = 0`, `NotIntegerError` nếu đầu vào không phải là số nguyên.

- **uoc_chung(numbers)**
  Tạo danh sách các ước chung của một danh sách các số.  
  - Tham số: `numbers` (list) - Danh sách các số.  
  - Trả về: Danh sách các ước chung.  
  - Ném lỗi: `MathError` nếu danh sách không đủ phần tử, `ListError` nếu đầu vào không phải là danh sách hoặc tuple.


- **uoc_chung_lon_nhat(numbers)**  
  Tính ước chung lớn nhất của một danh sách các số.  
  - Tham số: `numbers` (list) - Danh sách các số.  
  - Trả về: Giá trị ước chung lớn nhất.  
  - Ném lỗi: `MathError` nếu danh sách không hợp lệ, `ListError` nếu đầu vào không phải là danh sách hoặc tuple.


- **boi_chung_nho_nhat(numbers)**  
  Tính bội chung nhỏ nhất của một danh sách các số.  
  - Tham số: `numbers` (list) - Danh sách các số.  
  - Trả về: Giá trị bội chung nhỏ nhất.  
  - Ném lỗi: `MathError` nếu danh sách không hợp lệ, `ListError` nếu đầu vào không phải là danh sách hoặc tuple.

---

## 👯 Các hàm số song tố và số phong phú

- **kiem_tra_so_song_to(number)**  
  Kiểm tra xem `number` có phải là số song tố hay không.  
  - Tham số: `number` (int) - Số cần kiểm tra.  
  - Trả về: `True` nếu là số song tố, `False` nếu không.
  - Ném lỗi: `NotIntegerError` nếu đầu vào không phải là số nguyên.

- **tao_danh_sach_so_song_to(limit)**  
  Tạo danh sách các số song tố từ 0 đến `limit`.  
  - Tham số: `limit` (int) - Giới hạn trên của danh sách.  
  - Trả về: Danh sách các số song tố.
  - Ném lỗi: `NotIntegerError` đầu vào phải là số nguyên, `InvalidInputError` giới hạn phải không âm.

- **kiem_tra_so_phong_phu(number)**  
  Kiểm tra xem `number` có phải là số phong phú hay không.  
  - Tham số: `number` (int) - Số cần kiểm tra.  
  - Trả về: `True` nếu là số phong phú, `False` nếu không.
  - Ném lỗi: `NotIntegerError` đầu vào phải là số nguyên.

- **tao_danh_sach_so_phong_phu(limit)**  
  Tạo danh sách các số phong phú từ 0 đến `limit`.  
  - Tham số: `limit` (int) - Giới hạn trên của danh sách.  
  - Trả về: Danh sách các số phong phú.
  - Ném lỗi: `NotIntegerError` đầu vào phải là số nguyên, `InvalidInputError` giới hạn phải không âm.

---

## 🔍 Các hàm phân tích thừa số nguyên tố

- **thua_so_nguyen_to(number)**  
  Phân tích `number` thành danh sách các thừa số nguyên tố.  
  - Tham số: `number` (int) - Số cần phân tích.  
  - Trả về: Danh sách các thừa số nguyên tố.  
  - Ném lỗi: `MathError` nếu `number <= 1`, `NotIntegerError` đầu vào phải là số nguyên.

- **uoc_chung_nguyen_to_hai_so(number1, number2)**  
  Tìm ước chung nguyên tố lớn nhất của hai số.  
  - Tham số: `number1`, `number2` (int) - Hai số cần tính.  
  - Trả về: Giá trị ước chung nguyên tố lớn nhất.  
  - Ném lỗi: `MathError` nếu không có ước chung nguyên tố hoặc số không lớn hơn 1, `NotIntegerError` cả hai số phải là số nguyên.

---

## 🧮 Các hàm giải phương trình

- **giai_phuong_trinh(degree, coefficients)**  
  Giải phương trình từ bậc 1 đến bậc 10 theo hệ số.  
  - Tham số: `degree` (int) - Bậc của phương trình; `coefficients` (list) - Danh sách các hệ số.  
  - Trả về: Chuỗi kết quả nghiệm của phương trình.  
  - Ném lỗi: `InvalidInputError` nếu bậc hoặc hệ số không hợp lệ, `ImportError` nếu numpy không được cài đặt.

---

## 🧵 Các hàm xử lý danh sách và chuỗi

- **danh_sach_khong_trung_lap(items)**  
  Loại bỏ phần tử trùng lặp trong danh sách và sắp xếp giảm dần.  
  - Tham số: `items` (list) - Danh sách cần xử lý.  
  - Trả về: Danh sách không có phần tử trùng lặp.
  - Ném lỗi: `ListError` đầu vào phải là danh sách hoặc tuple.

- **trich_xuat_chu_so_tu_chuoi(text)**  
  Trích xuất các chữ số từ chuỗi. Ví dụ: "abc123" = [1,2,3].  
  - Tham số: `text` (str) - Chuỗi đầu vào.  
  - Trả về: Danh sách các chữ số.  
  - Ném lỗi: `InvalidInputError` nếu chuỗi rỗng.

- **trich_xuat_so_tu_chuoi(text)**  
  Trích xuất các số từ chuỗi. Ví dụ: "abc123" = [123].
  - Tham số: `text` (str) - Chuỗi đầu vào.  
  - Trả về: Danh sách các số.  
  - Ném lỗi: `InvalidInputError` nếu chuỗi rỗng.

- **trich_xuat_ki_tu(text)**  
  Trích xuất các ký tự không phải số từ chuỗi.  
  - Tham số: `text` (str) - Chuỗi đầu vào.  
  - Trả về: Danh sách các ký tự.  
  - Ném lỗi: `TypeErrorCustom` Đầu vào phải là chuỗi, `InvalidInputError` nếu chuỗi rỗng.

- **xau_duoc_nen(text)**
  Xâu được nén thành 2 loại.
  - Tham số: `text` (str) - Chuỗi đầu vào, `type` = 1 hoặc 2. Nếu 1 thì "google" → "google", nếu 2 thì "google" → "google".
  - Trả về: Chuỗi đã nén.
  - Ném lỗi: `InvalidInputError` loại nén chỉ có 1 hoặc 2.

- **xau_duoc_nen_khong_ghi_so(input_text)**  
  Nén chuỗi bỏ số. Ví dụ "hhhoocssssiiinnnhhhhh" → "hocsinh".
  - Tham số: `input_text` (str) - Chuỗi đầu vào.  
  - Trả về: Chuỗi đã nén.  
  - Ném lỗi: `InvalidInputError` nếu chuỗi rỗng.

- **xau_duoc_giai_nen(text)**  
  Giải nén chuỗi. Ví dụ "g2ogle" → "google".
  - Tham số: `text` (str) - Chuỗi đầu vào.  
  - Trả về: Chuỗi đã giải nén.  
  - Ném lỗi: `InvalidInputError` nếu chuỗi rỗng.

- **xau_ki_tu_khong_trung_lap(text)**  
  Tạo chuỗi ký tự không trùng lặp. Ví dụ "google" → gole".
  - Tham số: `text` (str) - Chuỗi đầu vào.  
  - Trả về: Chuỗi không có ký tự trùng lặp.  
  - Ném lỗi: `InvalidInputError` nếu chuỗi rỗng.

---

## 🏛️ Mật mã Caesar

- **chuyen_hoa_caesar(text, shift)**  
  Chuyển chuỗi thành dãy số mật mã Caesar.  
  - Tham số: `text` (str) - Chuỗi đầu vào; `shift` (int) - Số bước dịch chuyển.  
  - Trả về: Dãy số mật mã Caesar.  
  - Ném lỗi: `InvalidInputError` nếu chuỗi rỗng, chuỗi phải chỉ chứa chữ cái, `NotIntegerError` số bước dịch chuyển phải là số nguyên.

- **ma_hoa_caesar(numbers, shift)**  
  Mã hóa dãy số Caesar thành chuỗi.  
  - Tham số: `numbers` (list) - Dãy số đầu vào; `shift` (int) - Số bước dịch chuyển.  
  - Trả về: Chuỗi đã mã hóa.
  - Ném lỗi: `InvalidInputError` nếu chuỗi rỗng, các số phải là số nguyên từ 0 đến 25, `ListError` đầu vào phải là danh sách hoặc tuple, `NotIntegerError` số bước dịch chuyển phải là số nguyên.

---

## 👶 Teen Code Yahoo

- **teen_code_yahoo(input_text)**  
  Chuyển chuỗi thành Teen Code Yahoo.  
  - Tham số: `input_text` (str) - Chuỗi đầu vào.  
  - Trả về: Chuỗi Teen Code Yahoo.

---

## 🧬 Các hàm mô phỏng chỉ với string

- **mp_tai_xuong(steps)**  
  Mô phỏng quá trình tải xuống.  
  - Tham số: `steps` (int) - Số bước tải xuống (2 ≤ steps ≤ 88).  
  - Ném lỗi: `OutOfRangeError` nếu `steps` không nằm trong phạm vi hợp lệ.

- **mp_tinh_toan(steps)**  
  Mô phỏng quá trình tính toán.  
  - Tham số: `steps` (int) - Số bước tính toán (0 ≤ steps < 88).  
  - Ném lỗi: `OutOfRangeError` nếu `steps` không nằm trong phạm vi hợp lệ.

- **mp_loading(count)**  
  Mô phỏng quá trình loading với `count` lần lặp.  
  - Tham số: `count` (int) - Số lần lặp.

- **mp_christmas_tree()**  
  Mô phỏng cây thông giáng sinh.
  - Tham số: type (int) = 1 hoặc 2. Nếu 1 là cây thông cho terminal VSCode, 2 là cho văn bản text.
  - Trả về: Yêu cầu nhập chiều cao cây thông.

---

## 💥 Hàm hỗ trợ tính toán đặc biệt

- **tinh_toan_tien_dien(old_reading, new_reading)**  
  Tính toán tiền điện dựa trên chỉ số cũ và mới.  
  - Tham số: `old_reading`, `new_reading` (str) - Chỉ số cũ và mới.  
  - Trả về: Chuỗi kết quả tính toán.  
  - Ném lỗi: `MathError` nếu chỉ số không hợp lệ.

- **tong_chu_so_lon_nhat_bang_n(digit_count, target_sum)**  
  Tìm số lớn nhất có `digit_count` chữ số và tổng các chữ số bằng `target_sum`.  
  - Tham số: `digit_count` (int) - Số chữ số; `target_sum` (int) - Tổng các chữ số.  
  - Trả về: Chuỗi số lớn nhất.  
  - Ném lỗi: `MathError` nếu không thể tạo số thỏa mãn.

- **pythagore(side_a, side_b, side_c)**  
  Tính cạnh còn lại trong tam giác vuông (cạnh cần tìm = `False`).  
  - Tham số: `side_a`, `side_b`, `side_c` (float hoặc bool) - Các cạnh.  
  - Trả về: Chuỗi kết quả tính toán.  
  - Ném lỗi: `MathError` nếu đầu vào không hợp lệ.

---

## 🔁 Quy luật sinh dãy

- **tao_danh_sach_quy_luat_1(total)**  
  Tạo danh sách theo quy luật: 1 số ⋮ 1, 2 số ⋮ 2, … với tổng số lượng `total`.  
  - Tham số: `total` (int) - Tổng số lượng phần tử.  
  - Trả về: Danh sách theo quy luật.

- **tao_danh_sach_quy_luat_2(base, count)**  
  Tạo danh sách các bội của `base` với `count` phần tử.  
  - Tham số: `base` (int) - Số để tạo bội; `count` (int) - Số phần tử.  
  - Trả về: Danh sách các bội.

- **tao_danh_sach_quy_luat_3(count, base)**  
  Tạo danh sách lũy thừa của `base` từ 0 đến `count`.  
  - Tham số: `count` (int) - Số lượng phần tử; `base` (int) - Cơ số.  
  - Trả về: Danh sách lũy thừa.

---

## 🔄 Chuyển đổi và đếm

- **chuyen_doi_so_la_ma(number)**  
  Chuyển đổi `number` thành số La Mã.  
  - Tham số: `number` (int) - Số cần chuyển đổi.  
  - Trả về: Chuỗi số La Mã.  
  - Ném lỗi: `ImportError` nếu roman không được cài đặt, `OutOfRangeError` nếu `number` không từ 1 đến 3999.

- **dem_so_nghich_the(numbers)**  
  Đếm số cặp nghịch thế trong danh sách.  
  - Tham số: `numbers` (list) - Danh sách cần đếm.  
  - Trả về: Số cặp nghịch thế.

---

## 🧩 Khác

- **one_two_three()**  
  Chơi kéo búa bao với AI.  
  - Yêu cầu nhập số trận đấu và lựa chọn (Keo, Bua, Bao).

---

## 🛠️ Những bản cập nhật

> **📅 Ngày cập nhật gần nhất:** 02/08/2025  
> **📦 Tổng số bản phát hành:** 49

---

### 📌 2025
- **0.1.4** – *(02/08/2025)*
  ✅ Cập nhật tính năng lựa chọn bội/ ước âm cho `tao_danh_sach_boi_so` và `tao_danh_sach_uoc_so`.
  🔧 Sửa lỗi `uoc_chung_cua_danh_sach`.
  ❌ Xóa `uoc_chung_lon_nhat`, `trich_xuat_cac_so_tu_so`.
  ✅ Gộp hai hàm xâu được nén thành một.

- **0.1.3.2** – *(01/08/2025)*
  🔧 Sửa lỗi nhỏ.

- **0.1.3.1** – *(01/08/2025)*
  🔧 Sửa lỗi nhỏ.

- **0.1.3** – *(01/08/2025)*  
  ✅ Gộp hai hàm số mạnh mẽ thành một.  
  ⚡ Tối ưu Fibonacci với caching.  
  📚 Thêm type hints và docstring chuẩn NumPy.

- **0.1.2.1** – *(01/08/2025)*  
  🔧 Sửa lỗi nhỏ.

- **0.1.2** – *(01/08/2025)*  
  ✅ Cải thiện tính nhất quán của xác thực đầu vào.  
  ⚡ Tối ưu hóa hiệu suất cho Fibonacci và số nguyên tố.  
  📚 Mở rộng tài liệu với các lỗi dự kiến.

- **0.1.1.3** – *(31/07/2025)*  
  🔧 Sửa README.

- **0.1.1.2** – *(31/07/2025)*  
  🔧 Sửa README.

- **0.1.1.1** – *(31/07/2025)*  
  🔧 Sửa lỗi hiển thị.

- **0.1.1** – *(31/07/2025)*  
  🔧 Sửa lỗi và cập nhật phụ thuộc cho `numpy` và `roman`.

- **0.1.0.7** – *(31/07/2025)*  
  🔧 Sửa lỗi.

- **0.1.0.6** – *(30/07/2025)*  
  🔧 Sửa đổi nhẹ về hỗ trợ phiên bản Python.

- **0.1.0.5** – *(29/07/2025)*  
  🔧 Sửa lỗi.

- **0.1.0.4** – *(28/07/2025)*  
  🔧 Sửa lỗi.

- **0.1.0.3** – *(28/07/2025)*  
  ✏️ Sửa lại README.

- **0.1.0.2** – *(28/07/2025)*  
  ❌ Xóa hàm `thua_so_nguyen_to_day_du`.

- **0.1.0.1** – *(28/07/2025)*  
  🔧 Sửa lỗi nhỏ trong nội dung.

- **0.1.0** – *(28/07/2025)*  
  🧹 Chỉnh sửa toàn bộ.  
  ❌ Xóa hàm `giai_pt_bac_1va2_dang_string`, `tinh_toan_vat_ly_8`.

#### 🔵 0.0.5.x — Tinh chỉnh và cập nhật nhỏ

- **0.0.5.2.1** – *(27/07/2025)*  
  ✏️ Sửa README.

- **0.0.5.2** – *(27/07/2025)*  
  ✏️ Sửa README.

- **0.0.5.1** – *(27/07/2025)*  
  🆕 Cập nhật `teen_code_yahoo`.

- **0.0.5.0** – *(26/07/2025)*  
  ❌ Xóa hàm `an_ky_tu`.

---

### 📌 2024

- **0.0.4.1** – *(17/10/2024)*  
  🆕 Bổ sung hàm `tạo_dãy_chữ`.  
  🔄 Cập nhật `one_two_three`.

- **0.0.4.0** – *(05/05/2024)*  
  ✏️ Sửa README.

- **0.0.3.9** – *(05/05/2024)*  
  ✏️ Sửa README.

- **0.0.3.8** – *(05/05/2024)*  
  🎄 Cập nhật `mp_christmas_tree_cho_VSCode` và `mp_christmas_tree_cho_TEXT`.

- **0.0.3.7** – *(04/05/2024)*  
  🎄 Cập nhật `mp_christmas_tree`.

- **0.0.3.6** – *(03/03/2024)*  
  🧪 Thử nghiệm.

- **0.0.3.5** – *(01/03/2024)*  
  🧪 Thử nghiệm.

- **0.0.3.4** – *(26/02/2024)*  
  ➕ Bổ sung hàm `uoc_chung_cua_danh_sach`.

- **0.0.3.3** – *(21/02/2024)*  
  🔧 Nâng cấp README và metadata thư viện.

- **0.0.3.2** – *(20/02/2024)*  
  ➕ Bổ sung hàm kiểm tra số phong phú.

- **0.0.3.1** – *(20/02/2024)*  
  🔧 Nâng cấp thông tin thư viện.

- **0.0.3** – *(20/02/2024)*  
  ➕ Bổ sung `xau_ki_tu_khong_trung_lap`.  
  ❌ Xóa `ki_tu_trung_lap`.

- **0.0.2.10** – *(19/02/2024)*  
  🔧 Nâng cấp README.

- **0.0.2.9** – *(19/02/2024)*  
  🧪 Thử nghiệm.

- **0.0.2.8** – *(19/02/2024)*  
  🧪 Thử nghiệm.

- **0.0.2.7** – *(18/02/2024)*  
  🔧 Nâng cấp README.

- **0.0.2.6** – *(18/02/2024)*  
  ⚖️ Chuyển sang giấy phép **MIT License**.

- **0.0.2.4** → **0.0.2.5** – *(18/02/2024)*  
  🔧 Nâng cấp README.

- **0.0.2.3** – *(18/02/2024)*  
  🧪 Thử nghiệm.

- **0.0.2.1** → **0.0.2.2** – *(14/02/2024)*  
  🧪 Thử nghiệm.

- **0.0.2** – *(14/02/2024)*  
  🐞 Sửa lỗi thiếu phụ thuộc.

- **0.0.1.1** → **0.0.1.2** – *(14/02/2024)*  
  🧪 Thử nghiệm.

- **0.0.1** – *(14/02/2024)*  
  🎉 Phiên bản đầu tiên!

- **0.0.0.1** – *(14/02/2024)*  
  🧪 Thử nghiệm.
```

---