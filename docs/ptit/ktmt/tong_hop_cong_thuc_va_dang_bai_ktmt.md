# Kiến trúc máy tính: Công thức và bài tập ôn tập

&lt;p class=&quot;vn-lead&quot;&gt;Tổng hợp ký hiệu, công thức cốt lõi và các dạng bài tập mẫu đa dạng phục vụ ôn tập môn Kiến trúc máy tính.&lt;/p&gt;

!!! abstract "Mục tiêu ôn tập"
    Tài liệu cô đọng các công thức tính hiệu năng CPU, hệ thống bus, tổ chức bộ nhớ (RAM, Cache, bộ nhớ ảo), biểu diễn số và đĩa từ, kèm bài tập mẫu có lời giải chi tiết theo từng dạng.

## 1. Bảng ký hiệu và đơn vị chuẩn

| Ký hiệu | Ý nghĩa | Đơn vị |
| :--- | :--- | :--- |
| $T$ | Thời gian thực thi chương trình của CPU | s, ms, $\mu$s, ns |
| $I_c$ | Tổng số lệnh thực thi của chương trình | Lệnh |
| $CPI$ | Số chu kỳ xung nhịp trung bình trên một lệnh | Chu kỳ/lệnh |
| $\tau$ | Thời gian một chu kỳ xung nhịp ($\tau = 1/f$) | s, ns, ps |
| $f$ | Tần số xung nhịp đồng hồ hệ thống | Hz, MHz, GHz |
| $N_{\text{cycles}}$ | Tổng số chu kỳ xung nhịp | Chu kỳ |
| $MIPS$ | Triệu lệnh thực thi mỗi giây | Triệu lệnh/giây |
| $P, V, C, \alpha$ | Công suất, điện áp, điện dung tải, hệ số chuyển mạch | W, V, F, không thứ nguyên |
| $S$ | Hệ số tăng tốc (Speedup) | Không thứ nguyên |
| $L, \lambda, W$ | Số tác vụ trung bình, tốc độ đến, thời gian lưu hệ thống | Tác vụ, tác vụ/s, s |
| $Width_{\text{data}}$ | Độ rộng bus dữ liệu | Bit hoặc Byte |
| $f_{\text{bus}}, T_{\text{bus}}$ | Tần số và thời gian một chu kỳ bus | Hz (MHz), s (ns) |
| $BW$ | Băng thông truyền dữ liệu tối đa | Byte/s, MB/s, GB/s |
| $S_{MM}, S_{\text{Cache}}$ | Dung lượng bộ nhớ chính và bộ nhớ Cache | Byte, KB, MB, GB |
| $B$ | Kích thước một khối nhớ hoặc dòng Cache | Byte, Word |
| $m, v, k$ | Tổng số dòng Cache, số tập hợp, mức kết hợp ($k$-way) | Dòng, tập hợp, dòng/tập |
| $w, r, d, t$ | Số bit trường Offset, Line, Set, Tag | Bit |
| $h, m_{\text{miss}}$ | Tỷ lệ trúng (Hit) và tỷ lệ trượt (Miss = $1 - h$) | Phần trăm hoặc thập phân |
| $t_h, t_p, AMAT$ | Thời gian trúng, thời gian phạt trượt, thời gian truy nhập TB | ns, chu kỳ |
| $T_s, T_r, T_t, AAT$ | Thời gian tìm rãnh, trễ quay, truyền dữ liệu, truy nhập TB | ms |

## 2. Hiệu năng bộ xử lý (CPU)

### 2.1. Định luật hiệu năng sắt (Iron Law)

$$T = I_c \times CPI \times \tau = \frac{I_c \times CPI}{f}, \qquad N_{\text{cycles}} = I_c \times CPI$$

Khi chương trình gồm $n$ nhóm lệnh, mỗi nhóm có số lượng $I_i$ (tỷ lệ $f_i = I_i / I_c$) và chu kỳ $CPI_i$:

$$CPI = \frac{\sum_{i=1}^n (I_i \times CPI_i)}{I_c} = \sum_{i=1}^n (f_i \times CPI_i)$$

### 2.2. Tốc độ MIPS và MFLOPS

$$MIPS = \frac{I_c}{T \times 10^6} = \frac{f}{CPI \times 10^6}, \qquad MFLOPS = \frac{\text{Số phép tính dấu chấm động}}{T \times 10^6}$$

!!! warning "Dễ nhầm"
    $MIPS$ không phản ánh độ phức tạp của từng lệnh (một lệnh CISC làm nhiều việc hơn một lệnh RISC). Luôn dùng thời gian thực thi $T$ làm chuẩn so sánh hiệu năng giữa hai kiến trúc khác nhau.

### 2.3. Định luật Amdahl

Với $f$ là tỷ lệ thời gian được cải tiến ($0 \le f \le 1$) và $N$ là mức tăng tốc cục bộ:

$$S = \frac{1}{(1 - f) + \frac{f}{N}}, \qquad \lim_{N \to \infty} S = \frac{1}{1 - f}$$

### 2.4. Định luật Little và công suất động

- **Định luật Little (hệ thống hàng đợi ổn định):** $L = \lambda \times W$.
- **Công suất động (Active Power):** $P \approx C \times V^2 \times f \times \alpha$.

Khi so sánh hai điểm hoạt động trên cùng một chip:

$$\frac{P_1}{P_0} = \left(\frac{V_1}{V_0}\right)^2 \times \left(\frac{f_1}{f_0}\right)$$

## 3. Hệ thống Bus và băng thông bộ nhớ

- **Không gian địa chỉ cực đại** với bus địa chỉ $n$ bit: $2^n$ ô nhớ.
- **Chu kỳ bus** (kéo dài $k_{\text{bus}}$ chu kỳ CPU): $T_{\text{bus}} = k_{\text{bus}} \times \tau = \frac{k_{\text{bus}}}{f}$ và $f_{\text{bus}} = \frac{f}{k_{\text{bus}}}$.
- **Băng thông tối đa:**

$$BW = \frac{Width_{\text{data}}\text{ (bit)}}{8} \times f_{\text{bus}}$$

- **Băng thông RAM (bus 64 bit = 8 Byte):**
    - SDR SDRAM: $BW = f_{\text{clock}} \times 8\text{ Byte/s}$.
    - DDR SDRAM (truyền 2 sườn xung): $BW = 2 \times f_{\text{clock}} \times 8\text{ Byte/s}$.

## 4. Ghép nối chip nhớ bán dẫn

Khi thiết kế module nhớ $W_m \times B_m$ từ các chip thành phần $W_c \times B_c$:

- **Số chip ghép ngang (mở rộng độ rộng từ):** $N_{\text{ngang}} = \frac{B_m}{B_c}$
- **Số nhóm ghép dọc (mở rộng dung lượng từ):** $N_{\text{dọc}} = \frac{W_m}{W_c}$
- **Tổng số chip cần dùng:** $N_{\text{tổng}} = N_{\text{ngang}} \times N_{\text{dọc}}$

Phân bố $n = \log_2(W_m)$ đường địa chỉ: $k = \log_2(W_c)$ đường thấp nối song song vào tất cả chip; $p = n - k = \log_2(N_{\text{dọc}})$ đường cao đưa vào bộ giải mã $p \to 2^p$ để chọn chân $\overline{CS}$ của từng nhóm.

## 5. Bộ nhớ đệm (Cache) và thuật toán thay thế

### 5.1. Cấu trúc địa chỉ vật lý ($PA = \log_2 S_{MM}$)

| Kỹ thuật ánh xạ | Trường Tag ($t$) | Trường chỉ số | Trường Offset ($w$) |
| :--- | :--- | :--- | :--- |
| Trực tiếp (Direct) | $PA - (r + w)$ | Line: $r = \log_2(m)$ | $\log_2(B)$ |
| Kết hợp toàn phần (Fully) | $PA - w$ | Không có (0 bit) | $\log_2(B)$ |
| Tập kết hợp ($k$-way Set) | $PA - (d + w)$ | Set: $d = \log_2(v)$, $v = m/k$ | $\log_2(B)$ |

Kích thước thư mục thẻ nhớ: $\text{Tag Directory Size} = m \times t\text{ (bit)}$.

### 5.2. Thuật toán thay thế dòng Cache

- **LRU (Least Recently Used):** Thay khối lâu nhất không được truy cập.
- **FIFO (First-In-First-Out):** Thay khối được nạp vào Cache sớm nhất.
- **LFU (Least Frequently Used):** Thay khối có số lần truy cập ít nhất.
- **Random:** Chọn ngẫu nhiên một khối để thay thế.

Với $N_{\text{req}} = N_{\text{hit}} + N_{\text{miss}}$:

$$h = \frac{N_{\text{hit}}}{N_{\text{req}}}, \qquad m_{\text{miss}} = \frac{N_{\text{miss}}}{N_{\text{req}}} = 1 - h$$

## 6. Thời gian truy nhập trung bình (AMAT) và Bộ nhớ ảo

### 6.1. Thời gian truy nhập bộ nhớ trung bình

- **Cache 1 cấp:** $AMAT = t_{h1} + m_1 \times t_{p1}$
- **Cache 2 cấp:** $AMAT = t_{h1} + m_1 \times \left( t_{h2} + m_2 \times t_{p2} \right)$
- **Cache – RAM – Bộ nhớ ảo (đĩa):**

$$T_{\text{avg}} = h_C \cdot t_C + (1 - h_C) \cdot h_{MM} \cdot (t_C + t_{MM}) + (1 - h_C)(1 - h_{MM}) \cdot (t_C + t_{MM} + t_{\text{Disk}})$$

### 6.2. Chuyển đổi địa chỉ bộ nhớ ảo

- **Phân trang (Paging):** Với kích thước trang $S_{\text{page}} = 2^d$:
    - Số hiệu trang: $p = \lfloor \text{Địa chỉ logic} / S_{\text{page}} \rfloor$, độ lệch: $d = \text{Địa chỉ logic} \pmod{S_{\text{page}}}$.
    - Tra bảng trang lấy khung $f \implies \text{Địa chỉ vật lý} = f \times S_{\text{page}} + d$.
- **Phân đoạn (Segmentation):** Với cặp $(s, d)$, tra bảng đoạn lấy $(Base, Limit)$:
    - Nếu $d < Limit \implies \text{Địa chỉ vật lý} = Base + d$.
    - Nếu $d \ge Limit \implies$ Báo lỗi bẫy địa chỉ (Addressing Fault).

## 7. Biểu diễn số nguyên, IEEE 754 và Đĩa từ

### 7.1. Số nguyên có dấu $n$ bit

| Định dạng | Trọng số bit dấu | Miền giá trị ($n$ bit) |
| :--- | :--- | :--- |
| Không dấu (Unsigned) | $2^{n-1}$ | $[0, 2^n - 1]$ |
| Dấu - Độ lớn | Dấu ($0: +, 1: -$) | $[-(2^{n-1} - 1), 2^{n-1} - 1]$ |
| Bù 1 (1's Complement) | $-(2^{n-1} - 1)$ | $[-(2^{n-1} - 1), 2^{n-1} - 1]$ |
| Bù 2 (2's Complement) | $-2^{n-1}$ | $[-2^{n-1}, 2^{n-1} - 1]$ |

### 7.2. Chuẩn số thực IEEE 754

Giá trị chuẩn tắc: $X = (-1)^S \times (1.M) \times 2^{E - \text{Bias}}$.

| Định dạng | Tổng bit | Dấu ($S$) | Mũ ($e$) | Bias | Định trị ($m$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Single (32-bit) | 32 | 1 | 8 | 127 | 23 |
| Double (64-bit) | 64 | 1 | 11 | 1023 | 52 |

Quy ước đặc biệt: $E = 0, M = 0 \to \pm 0$; $E = 11\dots 1, M = 0 \to \pm \infty$; $E = 11\dots 1, M \ne 0 \to \text{NaN}$; $E = 0, M \ne 0 \to (-1)^S \times (0.M) \times 2^{1-\text{Bias}}$.

### 7.3. Hiệu năng đĩa từ

$$AAT = T_s + T_r + T_t$$

Trong đó độ trễ quay trung bình $T_r = \frac{60}{2 \times RPM}\text{ (s)}$ và thời gian truyền $T_t = \frac{\text{Số sector đọc}}{\text{Số sector/track}} \times \frac{60}{RPM}\text{ (s)}$.

## 8. Các dạng bài tập mẫu đa dạng

### Dạng 1: Hiệu năng CPU, Instruction Mix và MIPS

#### Bài 1.1: Iron Law cơ bản

Một chương trình thực hiện $3 \times 10^9$ lệnh trên CPU có $CPI = 2$ và tần số xung nhịp $3\text{ GHz}$. Tính thời gian thực thi chương trình.

**Lời giải:**

$$T = \frac{I_c \times CPI}{f} = \frac{3 \times 10^9 \times 2}{3 \times 10^9} = 2\text{ s}$$

#### Bài 1.2: Instruction Mix

Một chương trình gồm $50$ tỷ lệnh: $10$ tỷ lệnh rẽ nhánh ($CPI = 4$), $15$ tỷ lệnh Load ($CPI = 2$), $5$ tỷ lệnh Store ($CPI = 3$) và $20$ tỷ lệnh Integer ALU ($CPI = 1$). Tính thời gian thực thi trên CPU $4\text{ GHz}$.

**Lời giải:**

1. Tổng số chu kỳ: $N_{\text{cycles}} = (10 \times 4) + (15 \times 2) + (5 \times 3) + (20 \times 1) = 105$ tỷ chu kỳ.
2. $CPI$ trung bình: $CPI_{\text{tb}} = \frac{105}{50} = 2.1$ chu kỳ/lệnh.
3. Thời gian thực thi: $T = \frac{105 \times 10^9}{4 \times 10^9} = 26.25\text{ s}$.

#### Bài 1.3: Tốc độ MIPS

Chương trình có $2$ triệu lệnh chạy trên CPU $400\text{ MHz}$ với tỷ lệ lệnh: A chiếm $40\%$ ($CPI=1$), B chiếm $25\%$ ($CPI=2$), C chiếm $25\%$ ($CPI=3$), D chiếm $10\%$ ($CPI=4$). Tính tốc độ $MIPS$ và thời gian thực thi.

**Lời giải:**

1. $CPI = (0.40 \times 1) + (0.25 \times 2) + (0.25 \times 3) + (0.10 \times 4) = 2.05$ chu kỳ/lệnh.
2. $MIPS = \frac{400 \times 10^6}{2.05 \times 10^6} \approx 195.12\text{ MIPS}$.
3. Thời gian thực thi: $T = \frac{2 \times 10^6 \times 2.05}{400 \times 10^6} = 0.01025\text{ s} = 10.25\text{ ms}$.

### Dạng 2: Công suất động, Định luật Amdahl và Định luật Little

#### Bài 2.1: Công suất tiêu thụ (Active Power)

Một CPU hoạt động trong dải điện áp $[0.9\text{ V} \dots 1.5\text{ V}]$ và tần số $[1.8\text{ GHz} \dots 3.0\text{ GHz}]$. Biết công suất đo được là $30\text{ W}$ tại $1.0\text{ V}$ và $2.0\text{ GHz}$. Tính công suất ở chế độ tiết kiệm điện nhất và hiệu suất cao nhất.

**Lời giải:**

- **Tiết kiệm điện nhất ($0.9\text{ V}$, $1.8\text{ GHz}$):**

$$P_{\text{min}} = 30 \times \left(\frac{0.9}{1.0}\right)^2 \times \left(\frac{1.8}{2.0}\right) = 30 \times 0.81 \times 0.9 = 21.87\text{ W}$$

- **Hiệu suất cao nhất ($1.5\text{ V}$, $3.0\text{ GHz}$):**

$$P_{\text{max}} = 30 \times \left(\frac{1.5}{1.0}\right)^2 \times \left(\frac{3.0}{2.0}\right) = 30 \times 2.25 \times 1.5 = 101.25\text{ W}$$

#### Bài 2.2: Định luật Amdahl

So sánh hệ số tăng tốc của hai phương án: (1) tăng tốc $20$ lần phần mã chiếm $10\%$ thời gian, và (2) tăng tốc $1.6$ lần phần mã chiếm $80\%$ thời gian.

**Lời giải:**

- Phương án 1: $S_1 = \frac{1}{(1 - 0.1) + \frac{0.1}{20}} = \frac{1}{0.905} \approx 1.105$.
- Phương án 2: $S_2 = \frac{1}{(1 - 0.8) + \frac{0.8}{1.6}} = \frac{1}{0.7} \approx 1.43$.
- Kết luận: Phương án 2 hiệu quả hơn vì tối ưu phần chiếm tỷ trọng thời gian lớn.

#### Bài 2.3: Định luật Little

Một ổ đĩa nhận trung bình $\lambda = 25$ yêu cầu I/O mỗi giây. Thời gian trung bình để hoàn thành một yêu cầu là $W = 0.2\text{ s}$. Tính số yêu cầu trung bình đang nằm trong hàng đợi hệ thống.

**Lời giải:**

$$L = \lambda \times W = 25 \times 0.2 = 5\text{ yêu cầu}$$

### Dạng 3: Băng thông Bus và chuẩn RAM

#### Bài 3.1: Băng thông Bus vi xử lý

Vi xử lý $32$ bit có bus dữ liệu ngoài $16$ bit, xung nhịp $8\text{ MHz}$, mỗi chu kỳ bus tốn tối thiểu $4$ chu kỳ xung nhịp.
a. Tính tốc độ truyền tối đa qua bus.
b. Nên mở rộng bus ngoài lên $32$ bit hay tăng xung nhịp lên $16\text{ MHz}$?

**Lời giải:**

a. Độ rộng bus $= 16 / 8 = 2\text{ Byte}$. Tần số bus $f_{\text{bus}} = \frac{8\text{ MHz}}{4} = 2\text{ MHz}$.
Băng thông tối đa: $BW = 2\text{ Byte} \times 2 \times 10^6 = 4\text{ MB/s}$.

b. Cả hai phương án đều tăng băng thông lý thuyết lên $8\text{ MB/s}$. Tuy nhiên, chọn **mở rộng bus ngoài lên $32$ bit** tối ưu hơn vì khớp với kích thước từ $32$ bit của CPU (chỉ cần $1$ chu kỳ bus để nạp $1$ từ thay vì $2$ chu kỳ), đồng thời giữ xung nhịp $8\text{ MHz}$ giúp giảm tiêu thụ điện năng và nhiễu mạch.

#### Bài 3.2: Băng thông chuẩn DDR SDRAM

Tính băng thông tối đa của thanh RAM DDR3 có bus dữ liệu $64$ bit hoạt động ở xung nhịp I/O $800\text{ MHz}$.

**Lời giải:**

Do DDR truyền dữ liệu ở cả hai sườn xung nhịp, tốc độ truyền hiệu dụng là $2 \times 800 = 1600\text{ MT/s}$ (chuẩn DDR3-1600).

$$BW = 1600 \times 10^6 \times \frac{64}{8} = 12.800\text{ MB/s} = 12.8\text{ GB/s}$$

### Dạng 4: Cấu trúc địa chỉ Cache và Tag Directory

#### Bài 4.1: Ánh xạ trực tiếp (Direct Mapping)

Bộ nhớ chính $16\text{ GB}$ (định địa chỉ theo byte), kích thước khối $16\text{ KB}$, trường $Tag = 10$ bit. Xác định phân rã địa chỉ và dung lượng Cache.

**Lời giải:**

1. $S_{MM} = 16\text{ GB} = 2^{34}\text{ Byte} \implies PA = 34$ bit.
2. $B = 16\text{ KB} = 2^{14}\text{ Byte} \implies w = 14$ bit.
3. Số bit Line: $r = 34 - (10 + 14) = 10$ bit $\implies$ Số dòng $m = 2^{10}$ dòng.
4. Dung lượng Cache: $S_{\text{Cache}} = 2^{10} \times 16\text{ KB} = 16\text{ MB}$.

#### Bài 4.2: Ánh xạ tập kết hợp (Set Associative)

Bộ nhớ chính $4\text{ MB}$, kích thước khối $64\text{ Byte}$, Cache 4-way Set Associative, $Tag = 10$ bit. Xác định phân rã địa chỉ và dung lượng Cache.

**Lời giải:**

1. $S_{MM} = 4\text{ MB} = 2^{22}\text{ Byte} \implies PA = 22$ bit.
2. $B = 64\text{ Byte} = 2^6\text{ Byte} \implies w = 6$ bit.
3. Số bit Set: $d = 22 - (10 + 6) = 6$ bit $\implies$ Số tập hợp $v = 2^6 = 64$.
4. Tổng số dòng: $m = v \times k = 64 \times 4 = 256$ dòng.
5. Dung lượng Cache: $S_{\text{Cache}} = 256 \times 64\text{ Byte} = 16\text{ KB}$.

#### Bài 4.3: Kết hợp toàn phần và Tag Directory

Hệ thống có bộ nhớ chính $64\text{ MB}$, Cache $128\text{ KB}$, kích thước khối $32\text{ Byte}$, dùng ánh xạ kết hợp toàn phần. Tính số bit các trường địa chỉ và kích thước Tag Directory.

**Lời giải:**

1. $PA = \log_2(64\text{ MB}) = 26$ bit; $w = \log_2(32\text{ B}) = 5$ bit.
2. Do kết hợp toàn phần không có trường chỉ số: $Tag = 26 - 5 = 21$ bit.
3. Số dòng Cache: $m = \frac{128\text{ KB}}{32\text{ B}} = 4096$ dòng.
4. Kích thước Tag Directory $= 4096 \times 21 = 86.016\text{ bit} = 10.5\text{ KB}$.

### Dạng 5: Mô phỏng thuật toán thay thế Cache

#### Bài 5.1: Chính sách FIFO

Cache kết hợp toàn phần $4$ dòng trống ban đầu, dùng **FIFO**, chuỗi truy cập khối: `2, 3, 4, 7, 6, 3, 4, 7, 5, 4, 7, 8`. Tính tỷ lệ Hit và Miss.

**Lời giải:**

| Yêu cầu | 2 | 3 | 4 | 7 | 6 | 3 | 4 | 7 | 5 | 4 | 7 | 8 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Dòng 0 | **2** | 2 | 2 | 2 | **6** | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| Dòng 1 | | **3** | 3 | 3 | 3 | 3 | 3 | 3 | **5** | 5 | 5 | 5 |
| Dòng 2 | | | **4** | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 | **8** |
| Dòng 3 | | | | **7** | 7 | 7 | 7 | 7 | 7 | 7 | 7 | 7 |
| Kết quả | M | M | M | M | M | H | H | H | M | H | H | M |

Tổng cộng $12$ yêu cầu: $5$ Hit, $7$ Miss $\implies h = \frac{5}{12} \approx 41.67\%$, $m_{\text{miss}} = \frac{7}{12} \approx 58.33\%$.

#### Bài 5.2: Chính sách LRU

Cache kết hợp toàn phần $3$ dòng trống ban đầu, dùng **LRU**, chuỗi truy cập khối: `1, 2, 3, 2, 4, 1, 5, 2, 1, 3`. Tính tỷ lệ Hit và Miss.

**Lời giải:**

| Yêu cầu | 1 | 2 | 3 | 2 | 4 | 1 | 5 | 2 | 1 | 3 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Dòng 0 | **1** | 1 | 1 | 1 | **4** | 4 | 4 | **2** | 2 | 2 |
| Dòng 1 | | **2** | 2 | 2 | 2 | 2 | **5** | 5 | 5 | **3** |
| Dòng 2 | | | **3** | 3 | 3 | **1** | 1 | 1 | 1 | 1 |
| Kết quả | M | M | M | H | M | M | M | M | H | M |

Tổng cộng $10$ yêu cầu: $2$ Hit (tại `2` và `1` ở cuối), $8$ Miss $\implies h = 20\%$, $m_{\text{miss}} = 80\%$.

### Dạng 6: Thiết kế ghép nối chip nhớ

#### Bài 6.1: Ghép module 1 MB

Thiết kế module $1\text{M} \times 8$ bit từ các chip $256\text{K} \times 1$ bit. Xác định số chip và phân phối đường địa chỉ.

**Lời giải:**

1. $N_{\text{ngang}} = \frac{8}{1} = 8$ chip; $N_{\text{dọc}} = \frac{1024\text{K}}{256\text{K}} = 4$ nhóm $\implies$ Tổng $8 \times 4 = 32$ chip.
2. Số đường địa chỉ module: $n = \log_2(1\text{M}) = 20$ đường ($A_0 \dots A_{19}$).
3. $18$ đường thấp ($A_0 \dots A_{17}$) nối chung tới tất cả chip; $2$ đường cao ($A_{18}, A_{19}$) đưa vào bộ giải mã $2 \to 4$ để xuất $4$ tín hiệu $\overline{CS}$ chọn từng nhóm $8$ chip.

#### Bài 6.2: Xác định dải địa chỉ từng nhóm chip

Thiết kế module $64\text{K} \times 16$ bit từ chip $16\text{K} \times 8$ bit. Tính số chip và dải địa chỉ Hex của từng nhóm chip.

**Lời giải:**

1. $N_{\text{ngang}} = \frac{16}{8} = 2$ chip; $N_{\text{dọc}} = \frac{64\text{K}}{16\text{K}} = 4$ nhóm $\implies$ Tổng $8$ chip.
2. Địa chỉ module $16$ bit ($A_0 \dots A_{15}$); địa chỉ vào chip $14$ bit ($A_0 \dots A_{13}$); $2$ bit cao ($A_{15}, A_{14}$) giải mã chọn nhóm:
    - Nhóm 0 (`00`): `0000H` – `3FFFH`
    - Nhóm 1 (`01`): `4000H` – `7FFFH`
    - Nhóm 2 (`10`): `8000H` – `BFFFH`
    - Nhóm 3 (`11`): `C000H` – `FFFFH`

### Dạng 7: Thời gian truy nhập bộ nhớ trung bình (AMAT)

#### Bài 7.1: Cache 2 cấp

Cho Cache L1 ($t_{h1} = 1\text{ ns}$, $m_1 = 5\%$), Cache L2 ($t_{h2} = 10\text{ ns}$, $m_2 = 20\%$) và RAM ($t_{p2} = 100\text{ ns}$). Tính $AMAT$.

**Lời giải:**

$$AMAT = 1 + 0.05 \times (10 + 0.2 \times 100) = 1 + 0.05 \times 30 = 2.5\text{ ns}$$

#### Bài 7.2: Cache – RAM – Bộ nhớ ảo

Cho $t_C = 10\text{ ns}$ ($h_C = 0.92$), $t_{MM} = 60\text{ ns}$ ($h_{MM} = 0.65$) và $t_{\text{Virtual}} = 10\text{ ms} = 10^7\text{ ns}$. Tính thời gian truy nhập trung bình.

**Lời giải:**

- Hit Cache: $P_1 = 0.92$, $T_1 = 10\text{ ns}$.
- Miss Cache, Hit RAM: $P_2 = 0.08 \times 0.65 = 0.052$, $T_2 = 10 + 60 = 70\text{ ns}$.
- Miss Cache, Miss RAM: $P_3 = 0.08 \times 0.35 = 0.028$, $T_3 = 10 + 60 + 10^7 = 10.000.070\text{ ns}$.

$$T_{\text{avg}} = (0.92 \times 10) + (0.052 \times 70) + (0.028 \times 10.000.070) = 280.014,8\text{ ns} \approx 280.01\text{ }\mu\text{s}$$

### Dạng 8: Bộ nhớ ảo (Phân trang và Phân đoạn)

#### Bài 8.1: Phân trang (Paging)

Tiến trình có $4$ trang, mỗi trang $2048\text{ Byte}$. Bảng trang ánh xạ: $0 \to 3$, $1 \to 0$, $2 \to$ không hợp lệ, $3 \to 5$. Tính số bit địa chỉ logic và địa chỉ vật lý của địa chỉ logic $1000$ và $2500$.

**Lời giải:**

1. Số bit địa chỉ logic: $\log_2(4) + \log_2(2048) = 2 + 11 = 13$ bit.
2. Địa chỉ $1000$: $p = \lfloor 1000/2048 \rfloor = 0$, $d = 1000$. Tra bảng $p=0 \to f=3 \implies \text{Vật lý} = 3 \times 2048 + 1000 = 7144$.
3. Địa chỉ $2500$: $p = \lfloor 2500/2048 \rfloor = 1$, $d = 452$. Tra bảng $p=1 \to f=0 \implies \text{Vật lý} = 0 \times 2048 + 452 = 452$.

#### Bài 8.2: Phân đoạn (Segmentation)

Cho đoạn $0$ ($Base = 200, Limit = 600$) và đoạn $1$ ($Base = 2500, Limit = 50$). Tính địa chỉ vật lý của $(0, 450)$ và $(1, 60)$.

**Lời giải:**

- $(0, 450)$: $d = 450 < 600$ (hợp lệ) $\implies 200 + 450 = 650$.
- $(1, 60)$: $d = 60 > 50 \implies$ Lỗi bẫy địa chỉ (Addressing Fault).

### Dạng 9: Số nguyên có dấu và IEEE 754

#### Bài 9.1: Biểu diễn số nguyên âm 8-bit

Biểu diễn số $-45_{10}$ trên $8$ bit theo 3 dạng: Dấu - Độ lớn, Bù 1 và Bù 2.

**Lời giải:**

Ta có $+45_{10} = 00101101_2$.

- **Dấu - Độ lớn:** Đổi bit dấu thành $1 \implies$ `10101101`.
- **Bù 1:** Đảo toàn bộ bit của $+45 \implies$ `11010010`.
- **Bù 2:** Cộng $1$ vào Bù 1 $\implies$ `11010011`.

#### Bài 9.2: Thập phân sang IEEE 754 (32-bit)

Chuyển $-13.3125_{10}$ sang chuẩn IEEE 754 32-bit dạng Hex.

**Lời giải:**

1. Bit dấu: số âm $\implies S = 1$.
2. Đổi nhị phân: $13 = 1101_2$; $0.3125 = 0.0101_2 \implies 13.3125 = 1101.0101_2 = 1.1010101_2 \times 2^3$.
3. Trường mũ lệch: $E_{\text{biased}} = 3 + 127 = 130 = 10000010_2$.
4. Ghép $32$ bit: `1 10000010 10101010000000000000000` $\implies$ Mã Hex: `C1550000H`.

#### Bài 9.3: IEEE 754 (32-bit) sang thập phân

Chuyển mã Hex `422A0000H` (chuẩn IEEE 754 32-bit) về số thập phân.

**Lời giải:**

1. Đổi sang $32$ bit: `0 10000100 01010100000000000000000`.
2. $S = 0$ (số dương); $E_{\text{biased}} = 10000100_2 = 132 \implies E = 132 - 127 = 5$.
3. Giá trị: $X = +1.010101_2 \times 2^5 = 101010.1_2 = 32 + 8 + 2 + 0.5 = 42.5_{10}$.

### Dạng 10: Hiệu năng đĩa từ

#### Bài 10.1: Đọc 1 sector

Ổ đĩa quay $7200\text{ RPM}$, $T_s = 8\text{ ms}$, mỗi track có $500$ sector ($512\text{ Byte/sector}$). Tính $AAT$ để đọc $1$ sector.

**Lời giải:**

1. Thời gian quay 1 vòng: $T_{\text{quay}} = \frac{60}{7200} = 8.333\text{ ms} \implies T_r = \frac{8.333}{2} \approx 4.167\text{ ms}$.
2. Thời gian truyền 1 sector: $T_t = \frac{8.333}{500} \approx 0.0167\text{ ms}$.
3. $AAT = 8 + 4.167 + 0.0167 = 12.184\text{ ms}$.

#### Bài 10.2: Đọc nhiều sector liên tiếp

Với ổ đĩa ở Bài 10.1, tính tổng thời gian đọc $100$ sector nằm liên tiếp nhau trên cùng một track.

**Lời giải:**

Do các sector nằm liên tiếp trên cùng một track, đầu đọc chỉ cần tìm rãnh và chờ quay một lần:

1. $T_t = \frac{100}{500} \times 8.333\text{ ms} = 1.667\text{ ms}$.
2. Tổng thời gian: $T = 8 + 4.167 + 1.667 = 13.834\text{ ms}$.

## 9. Bảng tổng hợp quan hệ tương hỗ phần cứng

| Thay đổi thông số | Đại lượng bị ảnh hưởng | Xu hướng | Ràng buộc thiết kế |
| :--- | :--- | :--- | :--- |
| Tăng tần số $f \uparrow$ | Thời gian $T$ | Giảm ($\downarrow$) | Công suất $P$ và nhiệt lượng tăng tuyến tính |
| Giảm điện áp $V \downarrow$ | Công suất $P$ | Giảm mạnh ($\downarrow\downarrow$) | $P \propto V^2$, nhưng giới hạn tần số $f$ cực đại |
| Tăng độ rộng bus $Width \uparrow$ | Băng thông $BW$ | Tăng ($\uparrow$) | Giảm số chu kỳ bus nạp từ dài, tăng số chân |
| Tăng kích thước khối $B \uparrow$ | Tỷ lệ trúng $h$ | Tăng rồi giảm ($\cap$) | Quá lớn làm giảm số khối, tăng miss penalty |
| Tăng mức kết hợp $k \uparrow$ | Xung đột (Conflict miss) | Giảm ($\downarrow$) | Mạch so sánh Tag phức tạp, Hit time tăng nhẹ |
| Tăng tốc độ quay $RPM \uparrow$ | Độ trễ quay $T_r$ | Giảm ($\downarrow$) | Rút ngắn thời gian chờ đọc đĩa |
