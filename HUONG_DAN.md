# Hướng dẫn dùng project MkDocs song ngữ

Project này biến các file Markdown (`.md`) thành một trang web ghi chú. Trang nào có bản dịch thì mặc định hiện tiếng Anh; bấm nút **Dịch (VI)** hoặc bôi đen một đoạn để xem bản tiếng Việt do bạn viết sẵn. Trang không cần dịch thì viết Markdown bình thường.

> Quy tắc viết file md (cấu trúc, song ngữ, code, khung ghi chú, checklist): xem [QUY_TAC_MD.md](QUY_TAC_MD.md).

## 1. Các file trong zip để làm gì

```
vdoc/  (repo VietNote15t12)
├── mkdocs.yml                 cấu hình web + menu (nav)
├── pyproject.toml, uv.lock    môi trường Python (uv)
├── .github/workflows/deploy.yml  tự publish lên GitHub Pages
├── HUONG_DAN.md               file này (không đưa lên web)
├── hooks/
│   └── bilingual.py           biến cặp EN/VI trong file md thành HTML khi build
├── docs/                      TOÀN BỘ nội dung web nằm ở đây
│   ├── index.md               trang chủ
│   ├── assets/
│   │   ├── bilingual.css      ẩn/hiện bản dịch, màu sắc, popup
│   │   └── bilingual.js       nút Dịch + popup khi bôi đen
│   ├── lpic/   (index.md, 101-1-hardware.md)
│   ├── ccna/   (index.md)
│   ├── aws/    (index.md)
│   └── ptit/   (index.md)
└── templates/                 file mẫu để copy khi viết bài mới (không đưa lên web)
    ├── mau-song-ngu.md
    └── mau-mot-ngon-ngu.md
```

| File | Dùng để | Khi nào sửa |
|---|---|---|
| `mkdocs.yml` | Tên web, giao diện, danh sách menu `nav` | Mỗi khi thêm hoặc bỏ một trang trong menu |
| `hooks/bilingual.py` | Đọc file md song ngữ, tách EN và VI | Hầu như không cần sửa |
| `docs/assets/theme.css` | Màu sắc, chữ, trang chủ (hero), thẻ chủ đề | Khi muốn đổi màu web |
| `docs/assets/bilingual.css` | Giao diện bản dịch (màu, cỡ chữ, popup) | Khi muốn đổi màu hoặc kiểu hiển thị |
| `docs/assets/bilingual.js` | Nút Dịch và popup khi bôi đen | Khi muốn đổi nhãn nút hoặc hành vi |
| `docs/**/*.md` | Nội dung bài | Thường xuyên |
| `templates/*.md` | Khuôn mẫu | Khi muốn đổi khuôn mẫu của riêng bạn |
| `site/` (xuất hiện sau khi build) | Web hoàn chỉnh để đưa lên hosting | Không sửa tay, build lại là bị ghi đè |

## 2. Cài đặt và chạy

Môi trường được quản lý bằng **uv** (`pyproject.toml` + `uv.lock`, thay cho `requirements.txt`):

```bash
uv sync                  # tạo .venv và cài đúng phiên bản trong uv.lock
uv run mkdocs serve      # xem tại http://127.0.0.1:8000, tự tải lại khi bạn lưu file
uv run mkdocs build      # tạo thư mục site/
uv add <goi>             # thêm thư viện (ví dụ plugin mkdocs)
```

**Publish:** chỉ cần `git push` lên nhánh `main`. GitHub Actions (`.github/workflows/deploy.yml`) tự build và đăng lên GitHub Pages: https://viet15t12.github.io/VietNote15t12/

Logo web: `docs/assets/img/logo.svg` (từ `nqv2.svg`), favicon: `docs/assets/img/favicon.svg`.

## 3. Thêm một bài mới vào docs

1. Copy file mẫu từ `templates/` vào đúng thư mục môn, ví dụ `docs/ccna/vlan.md`.
2. Viết nội dung (xem mục 4 nếu là bài song ngữ).
3. Khai báo trong `mkdocs.yml`, mục `nav`:

   ```yaml
   - CCNA:
       - ccna/index.md
       - "VLAN": ccna/vlan.md
   ```

4. Lưu lại. Nếu đang chạy `mkdocs serve`, trang tự cập nhật.

Ghi chú:

- File nằm trong `docs/` nhưng chưa khai báo trong `nav` vẫn được build và mở được bằng đường dẫn; chỉ là không có trong menu.
- Tên file nên viết thường, không dấu, nối bằng dấu gạch ngang: `101-1-hardware.md`, `mang-may-tinh.md`.
- Ảnh để trong `docs/assets/img/` rồi chèn bằng đường dẫn tương đối, ví dụ trong `docs/ccna/vlan.md`: `![sơ đồ](../assets/img/vlan.png)`.

## 4. Hai loại trang

### 4.1 Trang song ngữ

Thêm **front matter** ở đầu file:

```markdown
---
bilingual: true
---

# Page title / Tên bài
```

Chỉ trang có dòng `bilingual: true` mới được xử lý song ngữ. Quên dòng này thì các dòng `EN:`, `VI:` hay LaTeX sẽ hiện thô trên web.

Có bốn cách viết cặp EN/VI, trộn lẫn trong cùng một file đều được:

**a) Tiêu đề: `English / Tiếng Việt`**

```markdown
## Inspecting Devices / Kiểm tra thiết bị
```

Trên web, tiêu đề chỉ hiện tiếng Anh (mục lục cũng vậy); bản tiếng Việt hiện khi bấm nút hoặc bôi đen. Hook nhận ra phần tiếng Việt nhờ các chữ có dấu. Hai điểm cần nhớ:

- Nếu phần tiếng Việt không có dấu (ví dụ `Kernel Modules / Kernel module`), tiêu đề chỉ được tách khi có đúng **một** dấu ` / `.
- Nếu phần tiếng Anh tự có dấu `/`, viết `&#47;` thay vào: `TCP &#47; UDP / TCP và UDP`.

**b) Đoạn văn và danh sách: `EN:` rồi `VI:` ở dòng kế tiếp** (cách dễ viết nhất)

```markdown
EN: A VLAN separates a switch into virtual networks.
VI: VLAN chia một switch thành các mạng ảo.

- EN: Access ports carry one VLAN.
  VI: Cổng access chỉ mang một VLAN.
```

Mỗi bên phải nằm trên **một dòng**. Với mục danh sách, dòng `VI:` thụt vào 2 dấu cách.

**c) Bảng: thêm `(EN)` và `(VI)` vào tiêu đề hai cột cuối**

```markdown
| Command | Purpose (EN) | Mục đích (VI) |
|---|---|---|
| `show vlan` | Show VLANs | Xem các VLAN |
```

Bảng phải có đúng 3 cột. Cột đầu (thường là lệnh) không dịch.

**d) Kiểu LaTeX màu cũ** (như file `lpic_101.1_song_ngu.md` ban đầu). Vẫn dùng được, không cần đổi file cũ, chỉ cần thêm front matter:

```markdown
$\color{RoyalBlue}{\textbf{English text}}$<br>
$\color{#374151}{\footnotesize\text{Tiếng Việt}}$
```

**Không dịch:** khối code (` ``` `), tên lệnh trong dấu backtick, tên riêng. Dòng nào viết bình thường (không có cặp EN/VI) thì luôn hiện và không có bản dịch.

Trên web:

- Nút **Dịch (VI)** trên thanh trên cùng: hiện bản dịch dưới mỗi đoạn cho cả trang, nhớ lựa chọn cho lần sau.
- Bôi đen một đoạn khi nút đang tắt: popup hiện bản dịch của đoạn (hoặc các đoạn) chứa vùng bôi đen.

### 4.2 Trang một ngôn ngữ (không song ngữ)

Không thêm front matter, viết Markdown bình thường (xem `templates/mau-mot-ngon-ngu.md`). Trang này không bị hook động vào, tiêu đề dạng `TCP / UDP` được giữ nguyên, và không có nút Dịch.

Nếu **cả web** không cần song ngữ, bạn chỉ cần không dùng `bilingual: true` ở trang nào. Có thể xoá `hooks/`, `bilingual.css`, `bilingual.js` cùng các dòng `hooks:`, `extra_css:`, `extra_javascript:` trong `mkdocs.yml`.

## 5. Tổ chức cho nhiều loại tài liệu

Mỗi chủ đề là một thư mục trong `docs/`, mỗi thư mục là một tab trên thanh trên cùng:

```
docs/
├── lpic/      LPIC-1: song ngữ (bilingual: true)
├── ccna/      CCNA: song ngữ hoặc một ngôn ngữ tuỳ bài
├── aws/       AWS: tương tự
└── ptit/      ghi chú môn học
    ├── mang-may-tinh/
    │   ├── index.md
    │   └── chuong-1.md
    └── he-dieu-hanh/
        └── index.md
```

Thêm một môn PTIT mới:

1. Tạo `docs/ptit/he-dieu-hanh/index.md` và các bài trong thư mục đó.
2. Khai báo trong `mkdocs.yml`:

   ```yaml
   - PTIT:
       - ptit/index.md
       - "Hệ điều hành":
           - ptit/he-dieu-hanh/index.md
           - "Chương 1": ptit/he-dieu-hanh/chuong-1.md
   ```

Thêm một tab chủ đề mới (ví dụ Docker): tạo `docs/docker/index.md` và thêm một mục cùng cấp với `LPIC-1`, `CCNA` trong `nav`.

Gợi ý thực tế: dùng song ngữ cho tài liệu tiếng Anh hay có thuật ngữ khó (LPIC, CCNA, AWS), dùng một ngôn ngữ cho ghi chú môn học ở trường viết bằng tiếng Việt.

## 6. Tuỳ chỉnh nhanh

| Muốn | Sửa ở đâu |
|---|---|
| Đổi tên web | `site_name` trong `mkdocs.yml` |
| Đổi màu chủ đạo | Biến `--md-primary-fg-color`, `--md-accent-fg-color` đầu file `docs/assets/theme.css` |
| Đổi màu thẻ từng chủ đề | Các lớp `.vn-lpic`, `.vn-ccna`, ... trong `theme.css` |
| Bỏ tab trên cùng, dùng menu bên trái | Xoá dòng `navigation.tabs` trong `mkdocs.yml` |
| Đổi nhãn nút ("Dịch (VI)", "Ẩn bản dịch") | Tìm hai chuỗi đó trong `bilingual.js` |
| Đổi màu, cỡ chữ của bản dịch | Khối `body.show-vi ...` trong `bilingual.css` |
| Đổi chữ "Tiếng Việt" trong popup | Tìm chuỗi đó trong `bilingual.js` |

## 7. Lỗi thường gặp

| Hiện tượng | Nguyên nhân và cách sửa |
|---|---|
| Thấy chữ `EN:` / `VI:` hoặc `\color` hiện thô trên web | Thiếu `bilingual: true` ở đầu file |
| Không có nút Dịch | Trang đó không có cặp EN/VI nào (nút chỉ hiện ở trang có bản dịch) |
| Tiêu đề không được tách | Phần tiếng Việt không có dấu và tiêu đề có nhiều hơn một dấu ` / `; thêm dấu cho từ tiếng Việt hoặc viết `&#47;` cho dấu `/` của phần tiếng Anh |
| Cặp `EN:`/`VI:` không ghép | `VI:` không nằm ngay dòng kế tiếp, hoặc câu bị xuống dòng giữa chừng; mỗi bên phải gọn trên một dòng |
| Bảng không ra song ngữ | Bảng không đúng 3 cột, hoặc tiêu đề hai cột cuối thiếu `(EN)` / `(VI)` |
| Trang mới không có trong menu | Chưa khai báo trong `nav` của `mkdocs.yml` |
| Bôi đen không hiện popup | Đang bật nút Dịch (bản dịch đã hiện sẵn), hoặc bôi đen trong khối code |
