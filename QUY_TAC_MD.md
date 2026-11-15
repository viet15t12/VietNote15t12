# Quy tắc soạn file Markdown cho VietNote15t12

Bộ quy tắc này dùng cho mọi file `.md` đặt trong `docs/`. Viết theo đúng quy tắc thì trang hiển thị đẹp, bản dịch tách đúng và build không lỗi. File này nằm ngoài `docs/` nên không lên web.

> Tóm tắt nhanh: **một file, một chủ đề** · **một H1 duy nhất** · **EN và VI mỗi bên một dòng** · **code block luôn ghi ngôn ngữ** · **bài mới phải khai báo trong `nav` và thêm thẻ vào `index.md` của môn**.

---

## 1. Tên file và vị trí

| Quy tắc | Đúng | Sai |
|---|---|---|
| Chữ thường, không dấu, nối bằng `-` | `101-1-hardware.md` | `101.1 Hardware.md` |
| Đặt trong thư mục của chủ đề | `docs/ccna/vlan.md` | `docs/vlan.md` |
| Môn PTIT: mỗi môn một thư mục, có `index.md` | `docs/ptit/mang-may-tinh/chuong-1.md` | `docs/ptit/chuong-1-mmt.md` |
| Bài LPIC đặt tên theo mã objective | `103-4-streams-pipes.md` | `bai-4.md` |
| Ảnh để trong `docs/assets/img/<chu-de>/` | `docs/assets/img/ccna/vlan-topo.png` | ảnh nằm lẫn với file md |

## 2. Cấu trúc một bài

```markdown
---
bilingual: true          # chỉ khi bài song ngữ; bài tiếng Việt thì bỏ cả khối này
---

# Tiêu đề bài            ← đúng MỘT dấu # cấp 1, ở đầu file

Một câu tóm tắt.         ← bài 1 ngôn ngữ có thể dùng <p class="vn-lead">...</p>

## Phần 1                ← các phần chính dùng ##
### Phần con             ← không nhảy cấp (## rồi mới đến ###)
```

- Mỗi file chỉ một `#` (H1). Tiêu đề H1 trở thành tên trang và tên trên tab trình duyệt.
- Không nhảy cấp tiêu đề: `##` → `###` → `####`. Không dùng `#####` trở xuống.
- Không đặt icon `:material-...:` trong H1 (sẽ hiện thô trên menu).
- Không in đậm cả dòng để thay tiêu đề; dùng `##`/`###` để mục lục bên phải nhận ra.
- Đánh số phần nếu bài dài và có thứ tự: `## 1. BIOS / UEFI Setup / Cấu hình BIOS / UEFI`.
- Bài dài hơn khoảng 400 dòng thì tách thành nhiều file.

## 3. Viết song ngữ (chỉ khi có `bilingual: true`)

### 3.1 Bốn dạng được hỗ trợ

| Dạng | Cách viết |
|---|---|
| Tiêu đề | `## English title / Tiêu đề tiếng Việt` |
| Đoạn văn | dòng `EN: ...` ngay sau là dòng `VI: ...` |
| Mục danh sách | `- EN: ...` rồi dòng sau thụt 2 dấu cách `  VI: ...` |
| Bảng | đúng 3 cột, tiêu đề hai cột cuối có đuôi `(EN)` và `(VI)` |

Cặp `EN:`/`VI:` dùng được cả bên trong khung ghi chú (`!!!`), khối thu gọn (`???`) và tab (`===`), miễn là thụt lề đúng 4 dấu cách.

### 3.2 Quy tắc bắt buộc

1. **Mỗi bên đúng một dòng.** Câu dài vẫn viết trên một dòng; trình soạn thảo tự xuống dòng khi hiển thị (bật *word wrap*).
2. **`VI:` nằm ngay dòng sau `EN:`**, không có dòng trống chen giữa.
3. **Tiêu đề có `/` trong phần tiếng Anh** thì viết `&#47;`: `## TCP &#47; UDP / TCP và UDP`.
4. **Phần tiếng Việt của tiêu đề nên có dấu**, hook nhận ra tiếng Việt nhờ chữ có dấu.
5. **Không dịch:** code block, lệnh trong backtick, đường dẫn file, tên riêng, tên tuỳ chọn (`-r`, `--help`).
6. Dòng viết bình thường (không có `EN:`/`VI:`) luôn hiện và không có bản dịch, dùng cho ghi chú phụ, ví dụ ngắn.
7. File cũ dạng LaTeX `$\color{RoyalBlue}...$` vẫn chạy được, nhưng **bài mới dùng dạng `EN:`/`VI:`**.

### 3.3 Ví dụ

```markdown
## Kernel Modules / Mô-đun nhân

EN: The kernel loads drivers as modules at runtime.
VI: Nhân nạp trình điều khiển dưới dạng mô-đun khi đang chạy.

- EN: `lsmod` lists loaded modules.
  VI: `lsmod` liệt kê các mô-đun đã nạp.

| Command | Purpose (EN) | Mục đích (VI) |
|---|---|---|
| `modprobe -r snd` | Unload a module | Gỡ một mô-đun |
```

## 4. Định dạng nội dung

### 4.1 Nhấn mạnh

| Muốn | Cú pháp | Dùng khi |
|---|---|---|
| **In đậm** | `**chữ**` | Thuật ngữ quan trọng xuất hiện lần đầu |
| *Nghiêng* | `*chữ*` | Từ mượn, tên sách, nhấn nhẹ |
| `Code` | `` `lệnh` `` | Lệnh, tên file, đường dẫn, tuỳ chọn, giá trị |
| ==Tô vàng== | `==chữ==` | Ý cực kỳ quan trọng, **tối đa 1 đến 2 chỗ mỗi phần** |
| Phím | `++ctrl+alt+del++` | Phím tắt |

Không lạm dụng in đậm: nếu cả đoạn đều đậm thì không còn gì nổi bật.

### 4.2 Code block

- Luôn ghi ngôn ngữ: ` ```shell `, ` ```bash `, ` ```yaml `, ` ```python `, ` ```text ` (cho output thuần), ` ```cisco ` không có thì dùng ` ```text `.
- Lệnh gõ vào terminal có dấu nhắc `$` (người dùng thường) hoặc `#` (root), output để ngay dưới, không có dấu nhắc.
- Thêm tiêu đề khi cần: ` ```shell title="Liệt kê thiết bị PCI" `.
- Đánh dấu dòng quan trọng: ` ```yaml hl_lines="2 3" `.
- Một khối code chỉ minh hoạ một ý; output dài thì cắt bớt và ghi `...`.

````markdown
```shell title="Xem thiết bị USB"
$ lsusb
Bus 001 Device 002: ID 8087:0024 Intel Corp. Integrated Rate Matching Hub
```
````

### 4.3 Khung ghi chú (admonition)

Chọn đúng loại để màu sắc mang ý nghĩa, không dùng tuỳ tiện:

| Loại | Màu | Dùng cho |
|---|---|---|
| `note` | xanh dương | Ghi chú bổ sung |
| `abstract` | xanh nhạt | Tóm tắt, mục tiêu bài / exam objective |
| `info` | xanh ngọc | Thông tin nền |
| `tip` | xanh lá | Mẹo thi, mẹo dùng lệnh |
| `warning` | cam | Dễ nhầm, lỗi hay gặp |
| `danger` | đỏ | Lệnh nguy hiểm (`rm -rf`, `dd`, xoá cấu hình) |
| `example` | tím | Ví dụ, bài lab |
| `question` | xanh lục | Câu hỏi ôn tập (thường dùng dạng thu gọn `???`) |

```markdown
!!! warning "Dễ nhầm"
    `/proc` là hệ thống tệp ảo, không nằm trên ổ đĩa.

??? question "Câu hỏi ôn tập"
    Lệnh nào gỡ một mô-đun nhân?

    **Đáp án:** `modprobe -r <ten>`
```

- Nội dung bên trong thụt **4 dấu cách**.
- `!!!` luôn mở, `???` thu gọn (bấm để mở), `???+` thu gọn nhưng mở sẵn.
- Không quá 2 khung liền nhau; tối đa khoảng 1 khung cho mỗi phần `##`.

### 4.4 Danh sách

- Dùng `-` cho danh sách không thứ tự, `1.` cho các bước có thứ tự.
- Danh sách lồng nhau thụt **4 dấu cách** (riêng dòng `VI:` thụt 2 dấu cách dưới `- EN:`).
- Có dòng trống trước và sau danh sách.
- Danh sách việc cần làm: `- [ ] chưa xong`, `- [x] đã xong`.

### 4.5 Bảng

- Dùng bảng khi so sánh từ 2 thuộc tính trở lên; danh sách đơn giản thì dùng `-`.
- Cột đầu là thứ được tra cứu (lệnh, thuật ngữ), các cột sau là giải thích.
- Ô bảng ngắn gọn, không xuống dòng trong ô, không đặt code block trong ô.
- Trang song ngữ: bảng 3 cột `| Command | ... (EN) | ... (VI) |` để có bản dịch.

### 4.6 Tab (so sánh nhiều cách làm)

```markdown
=== "Debian/Ubuntu"

    ```shell
    $ sudo apt install pciutils
    ```

=== "RHEL/Fedora"

    ```shell
    $ sudo dnf install pciutils
    ```
```

### 4.7 Liên kết và ảnh

- Liên kết nội bộ dùng **đường dẫn tương đối tới file `.md`**: `[VLAN](../ccna/vlan.md)`, không dùng URL web.
- Liên kết tới một mục: `[udev](101-1-hardware.md#udev)`.
- Liên kết ngoài ghi rõ nguồn: `[LPI objectives](https://www.lpi.org/...)`.
- Ảnh luôn có mô tả: `![Sơ đồ VLAN](../assets/img/ccna/vlan-topo.png)`.
- Ảnh PNG/SVG, chiều rộng không quá 1600px, dung lượng dưới 300 KB.

### 4.8 Thuật ngữ và chú thích

```markdown
IRQ
:   Interrupt Request, tín hiệu thiết bị gửi tới CPU.

Câu có chú thích cuối trang.[^1]

[^1]: Nội dung chú thích.
```

## 5. Chính tả và văn phong

- Tiếng Việt có dấu đầy đủ, dùng một kiểu bỏ dấu thống nhất (`hoà`, `tuỳ`, `thuỷ`).
- Thuật ngữ kỹ thuật giữ nguyên tiếng Anh khi chưa có từ Việt phổ biến (`kernel`, `module`, `switch`); lần đầu có thể chú thích: *nhân (kernel)*.
- Câu ngắn, mỗi đoạn một ý, đoạn không quá 4 đến 5 câu.
- Dấu câu sát chữ phía trước: `ví dụ: lsusb`, không viết `ví dụ : lsusb`.
- Đơn vị viết cách số: `4 GB`, `100 Mbps`.
- Không dùng HTML thuần khi Markdown làm được; ngoại lệ: `<p class="vn-lead">` và khối thẻ trong `index.md`.

## 6. Khi thêm bài mới: cập nhật 3 chỗ

1. **File bài**: copy từ `templates/mau-song-ngu.md` hoặc `templates/mau-mot-ngon-ngu.md`.
2. **`mkdocs.yml`**: thêm vào `nav`.

   ```yaml
   - CCNA:
       - ccna/index.md
       - "VLAN": ccna/vlan.md
   ```

3. **`index.md` của chủ đề**: thêm một thẻ vào khối `grid cards` (xoá thẻ "Sắp có" nếu còn).

   ```markdown
   -   **VLAN**

       ---

       Chia mạng LAN thành nhiều miền broadcast.

       [:octicons-arrow-right-24: Đọc bài](vlan.md)
   ```

   Mỗi thẻ gồm: tên bài in đậm, dòng `---`, một câu mô tả, link "Đọc bài". Nội dung thẻ thụt 4 dấu cách.

## 7. Kiểm tra trước khi đẩy lên

```bash
uv run mkdocs build --strict    # phải không có WARNING
uv run mkdocs serve             # mở http://127.0.0.1:8000 để xem
```

- [ ] Có đúng một `#` H1
- [ ] Bài song ngữ có `bilingual: true`; trên web không còn chữ `EN:`, `VI:` hay `\color` hiện thô
- [ ] Bấm **Dịch (VI)** thấy bản dịch dưới mỗi đoạn
- [ ] Mọi code block có ghi ngôn ngữ
- [ ] Ảnh hiện được, link nội bộ không lỗi (`--strict` sẽ báo)
- [ ] Đã khai báo trong `nav` và thêm thẻ vào `index.md`
- [ ] Xem thử cả chế độ sáng và tối

Sau đó `git add -A && git commit -m "Thêm bài ..." && git push`, web tự cập nhật sau khoảng 1 phút.

