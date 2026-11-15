---
bilingual: true
---

# 101.1 Determine and configure hardware settings

$\color{RoyalBlue}{\textbf{English: blue}}$ · $\color{#374151}{\footnotesize\text{Tiếng Việt: xám}}$

**Exam:** LPIC-1 v5.0 (Exam 101)

## Key Knowledge Areas / Kiến thức trọng tâm

- $\color{RoyalBlue}{\textbf{Enable and disable integrated peripherals.}}$<br>
  $\color{#374151}{\footnotesize\text{Bật và tắt các thiết bị ngoại vi tích hợp.}}$
- $\color{RoyalBlue}{\textbf{Differentiate between the various types of mass storage devices.}}$<br>
  $\color{#374151}{\footnotesize\text{Phân biệt các loại thiết bị lưu trữ lớn.}}$
- $\color{RoyalBlue}{\textbf{Determine hardware resources for devices.}}$<br>
  $\color{#374151}{\footnotesize\text{Xác định tài nguyên phần cứng cho các thiết bị.}}$
- $\color{RoyalBlue}{\textbf{Tools and utilities to list various hardware information}}$<br>
  $\color{RoyalBlue}{\textbf{(e.g. lsusb, lspci, etc.).}}$<br>
  $\color{#374151}{\footnotesize\text{Các công cụ và tiện ích để liệt kê thông tin phần cứng}}$<br>
  $\color{#374151}{\footnotesize\text{(ví dụ: lsusb, lspci, v.v.).}}$
- $\color{RoyalBlue}{\textbf{Tools and utilities to manipulate USB devices.}}$<br>
  $\color{#374151}{\footnotesize\text{Các công cụ và tiện ích để thao tác với thiết bị USB.}}$
- $\color{RoyalBlue}{\textbf{Conceptual understanding of sysfs, udev and dbus.}}$<br>
  $\color{#374151}{\footnotesize\text{Hiểu khái niệm về sysfs, udev và dbus.}}$

## Partial List of Used Files, Terms and Utilities / Danh sách một phần các tệp, thuật ngữ và tiện ích

```shell
/sys/
/proc/
/dev/
modprobe
lsmod
lspci
lsusb
```

---

## 1. BIOS / UEFI Setup / Cấu hình BIOS / UEFI

$\color{RoyalBlue}{\textbf{Press keys such as F12, F2 or Del (depends on the vendor)}}$<br>
$\color{RoyalBlue}{\textbf{right after power-on to open the firmware configuration utility.}}$<br>
$\color{#374151}{\footnotesize\text{Nhấn các phím như F12, F2, Del (tuỳ nhà sản xuất)}}$<br>
$\color{#374151}{\footnotesize\text{ngay khi vừa bật máy để mở chương trình cấu hình firmware.}}$

**Common uses / Các mục đích sử dụng phổ biến:**

- $\color{RoyalBlue}{\textbf{Enable or disable integrated peripherals.}}$<br>
  $\color{#374151}{\footnotesize\text{Bật hoặc tắt các thiết bị ngoại vi tích hợp.}}$
- $\color{RoyalBlue}{\textbf{Change hardware settings such as IRQ and DMA.}}$<br>
  $\color{#374151}{\footnotesize\text{Thay đổi thiết lập phần cứng như IRQ và DMA.}}$
- $\color{RoyalBlue}{\textbf{Set RAM to run at the manufacturer-specified speed.}}$<br>
  $\color{#374151}{\footnotesize\text{Thiết lập RAM chạy đúng tốc độ do nhà sản xuất quy định.}}$
- $\color{RoyalBlue}{\textbf{Disable unneeded CPU features to save power and}}$<br>
  $\color{RoyalBlue}{\textbf{mitigate known CPU vulnerabilities.}}$<br>
  $\color{#374151}{\footnotesize\text{Tắt các tính năng CPU không cần thiết để tiết kiệm điện}}$<br>
  $\color{#374151}{\footnotesize\text{và giảm các lỗ hổng bảo mật đã biết của CPU.}}$
- $\color{RoyalBlue}{\textbf{Set the boot order.}}$<br>
  $\color{#374151}{\footnotesize\text{Đặt thứ tự khởi động.}}$

---

## 2. Inspecting Devices / Kiểm tra thiết bị

$\color{RoyalBlue}{\textbf{If the OS does not detect a device, the component or port may be faulty.}}$<br>
$\color{RoyalBlue}{\textbf{If the OS detects it but it does not work, the cause is on the OS side}}$<br>
$\color{RoyalBlue}{\textbf{(e.g. a missing kernel module). Use sudo to see full information.}}$<br>
$\color{#374151}{\footnotesize\text{Nếu hệ điều hành không nhận thiết bị, linh kiện hoặc cổng kết nối có thể bị hỏng.}}$<br>
$\color{#374151}{\footnotesize\text{Nếu có nhận nhưng thiết bị không hoạt động, nguyên nhân nằm ở phía hệ điều hành}}$<br>
$\color{#374151}{\footnotesize\text{(ví dụ: thiếu kernel module). Dùng sudo để hiển thị đầy đủ thông tin.}}$

### 2.1 Command Summary / Tóm tắt lệnh

| Command | Purpose | Mục đích |
|---|---|---|
| `lspci` | $\color{RoyalBlue}{\textbf{List PCI devices (disk, graphics, NIC...)}}$ | $\color{#374151}{\footnotesize\text{Liệt kê thiết bị PCI (đĩa, card đồ hoạ, card mạng...)}}$ |
| `lspci -s <address> -v` | $\color{RoyalBlue}{\textbf{Details for one device}}$ | $\color{#374151}{\footnotesize\text{Chi tiết một thiết bị (địa chỉ lấy từ cột đầu của lspci)}}$ |
| `lspci -s <address> -k` | $\color{RoyalBlue}{\textbf{Show kernel driver/modules of one device}}$ | $\color{#374151}{\footnotesize\text{Chỉ hiện driver/module kernel của một thiết bị}}$ |
| `lsusb` | $\color{RoyalBlue}{\textbf{List USB devices}}$ | $\color{#374151}{\footnotesize\text{Liệt kê thiết bị USB}}$ |
| `lsusb -v -d <vendor:product>` | $\color{RoyalBlue}{\textbf{Detailed descriptor of one USB device}}$ | $\color{#374151}{\footnotesize\text{Mô tả chi tiết một thiết bị USB}}$ |
| `lsusb -t` | $\color{RoyalBlue}{\textbf{Tree view with class and driver}}$ | $\color{#374151}{\footnotesize\text{Dạng cây, gồm class và driver (vd Driver=btusb)}}$ |
| `lsusb -s <bus>:<dev>` | $\color{RoyalBlue}{\textbf{Identify a device by bus and device number}}$ | $\color{#374151}{\footnotesize\text{Xác định thiết bị theo số bus và số thiết bị}}$ |
| `lsmod` | $\color{RoyalBlue}{\textbf{List loaded kernel modules}}$ | $\color{#374151}{\footnotesize\text{Liệt kê các kernel module đang nạp}}$ |
| `modinfo -p <module>` | $\color{RoyalBlue}{\textbf{List parameters accepted by a module}}$ | $\color{#374151}{\footnotesize\text{Liệt kê tham số mà module hỗ trợ}}$ |
| `modprobe -r <module>` | $\color{RoyalBlue}{\textbf{Unload a module (fails if in use)}}$ | $\color{#374151}{\footnotesize\text{Gỡ module (thất bại nếu đang được dùng)}}$ |

### 2.2 Demo: `lspci`

$\color{RoyalBlue}{\textbf{The hexadecimal number at the start of each line is the device address.}}$<br>
$\color{#374151}{\footnotesize\text{Số thập lục phân ở đầu mỗi dòng là địa chỉ thiết bị.}}$

```shell
$ lspci
00:00.0 Host bridge: Intel Corporation Device a716
00:02.0 VGA compatible controller: Intel Corporation Raptor Lake-P [UHD Graphics] (rev 04)
00:0d.0 USB controller: Intel Corporation Raptor Lake-P Thunderbolt 4 USB Controller
00:14.0 USB controller: Intel Corporation Alder Lake PCH USB 3.2 xHCI Host Controller (rev 01)
00:14.3 Network controller: Intel Corporation Raptor Lake PCH CNVi WiFi (rev 01)
00:17.0 SATA controller: Intel Corporation Alder Lake-P SATA AHCI Controller (rev 01)
...
```

$\color{RoyalBlue}{\textbf{Use -s address -v for details (here, the Intel GPU).}}$<br>
$\color{#374151}{\footnotesize\text{Dùng -s địa chỉ -v để xem chi tiết (ở đây là GPU Intel).}}$

```shell
$ lspci -s 00:02.0 -v
00:02.0 VGA compatible controller: Intel Corporation Raptor Lake-P [UHD Graphics] (rev 04) (prog-if 00 [VGA controller])
	Subsystem: Acer Incorporated [ALI] Device 1693
	Flags: bus master, fast devsel, latency 0, IRQ 187, IOMMU group 0
	Memory at 6102000000 (64-bit, non-prefetchable) [size=16M]
	...
	Kernel driver in use: i915
	Kernel modules: i915, xe
```

```shell
$ lspci -s 00:02.0 -k
00:02.0 VGA compatible controller: Intel Corporation Raptor Lake-P [UHD Graphics] (rev 04)
	Subsystem: Acer Incorporated [ALI] Device 1693
	Kernel driver in use: i915
	Kernel modules: i915, xe
```

### 2.3 Demo: `lsusb`

```shell
$ lsusb
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 003 Device 002: ID 04f2:b777 Chicony Electronics Co., Ltd ACER FHD User Facing
Bus 003 Device 003: ID 04f3:0c4f Elan Microelectronics Corp. ELAN:Fingerprint
Bus 003 Device 004: ID 8087:0033 Intel Corp. AX211 Bluetooth
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
```

$\color{RoyalBlue}{\textbf{Detailed view of one device:}}$<br>
$\color{#374151}{\footnotesize\text{Xem chi tiết một thiết bị:}}$

```shell
$ sudo lsusb -v -d 1d6b:0003

Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Negotiated speed: SuperSpeed++ (20Gbps)
Device Descriptor:
  bLength                18
  bDescriptorType         1
  bcdUSB               3.10
  bDeviceClass            9 Hub
  idVendor           0x1d6b Linux Foundation
  idProduct          0x0003 3.0 root hub
  iManufacturer           3 Linux 7.2.11-200.fc44.x86_64 xhci-hcd
  iProduct                2 xHCI Host Controller
  ...
  Configuration Descriptor:
    ...
    Interface Descriptor:
      ...
      Endpoint Descriptor:
        ...
Binary Object Store Descriptor:
  ...
Hub Descriptor:
  ...
 Hub Port Status:
   Port 1: 0000.02a0 5Gbps power Rx.Detect
   Port 2: 0000.02a0 5Gbps power Rx.Detect
   Port 3: 0000.02a0 5Gbps power Rx.Detect
Device Status:     0x0001
  Self Powered
```

$\color{RoyalBlue}{\textbf{Tree view:}}$<br>
$\color{#374151}{\footnotesize\text{Dạng cây:}}$

```shell
$ sudo lsusb -t
/:  Bus 001.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/1p, 480M
/:  Bus 002.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/3p, 20000M/x2
/:  Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/12p, 480M
    |__ Port 006: Dev 002, If 0, Class=Video, Driver=uvcvideo, 480M
    |__ Port 008: Dev 003, If 0, Class=Vendor Specific Class, Driver=[none], 12M
    |__ Port 010: Dev 004, If 0, Class=Wireless, Driver=btusb, 12M
/:  Bus 004.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/4p, 10000M
```

$\color{RoyalBlue}{\textbf{Find which device uses btusb by passing Bus and Dev numbers to -s:}}$<br>
$\color{#374151}{\footnotesize\text{Tìm thiết bị dùng btusb bằng cách truyền số Bus và Dev cho -s:}}$

```shell
$ lsusb -s 003:004
Bus 003 Device 004: ID 8087:0033 Intel Corp. AX211 Bluetooth
```

### 2.4 Demo: Kernel Modules / Kernel module

$\color{RoyalBlue}{\textbf{A kernel module is software that controls a device.}}$<br>
$\color{RoyalBlue}{\textbf{The management tools come from the kmod package.}}$<br>
$\color{#374151}{\footnotesize\text{Kernel module là phần mềm điều khiển thiết bị.}}$<br>
$\color{#374151}{\footnotesize\text{Các công cụ quản lý nằm trong gói kmod.}}$

```shell
$ lsmod
Module                  Size  Used by
vmnet                  90112  13
nft_masq               12288  6
uhid                   24576  1
nvidia_uvm           2682880  0
bridge                483328  0
stp                    12288  1 bridge
llc                    16384  2 bridge,stp
...
```

$\color{RoyalBlue}{\textbf{Search for a specific module:}}$<br>
$\color{#374151}{\footnotesize\text{Tìm một module cụ thể:}}$

```shell
$ lsmod | fgrep -i nvidia
nvidia_uvm           2682880  0
nvidia_drm            180224  7
nvidia_modeset       2002944  4 nvidia_drm
nvidia              18522112  76 nvidia_uvm,nvidia_modeset
```

$\color{RoyalBlue}{\textbf{Unload a module. It fails with "Module ... is in use"}}$<br>
$\color{RoyalBlue}{\textbf{if a process or another module is using it.}}$<br>
$\color{#374151}{\footnotesize\text{Gỡ một module. Sẽ báo lỗi "Module ... is in use"}}$<br>
$\color{#374151}{\footnotesize\text{nếu có tiến trình hoặc module khác đang dùng nó.}}$

```shell
# modprobe -r snd-hda-intel
```

$\color{RoyalBlue}{\textbf{View the parameters a module accepts:}}$<br>
$\color{#374151}{\footnotesize\text{Xem các tham số mà module hỗ trợ:}}$

```shell
$ modinfo -p nouveau
vram_pushbuf:Create DMA push buffers in VRAM (int)
mst:Enable DisplayPort multi-stream (default: enabled) (int)
ignorelid:Ignore ACPI lid status (int)
modeset:enable driver (default: auto, 0 = disabled, 1 = enabled, 2 = headless) (int)
runpm:disable (0), force enable (1), optimus only default (-1) (int)
...
```

---

## 3. Information and Device Files / Thông tin và tệp thiết bị

$\color{RoyalBlue}{\textbf{lspci, lsusb and lsmod read data that the kernel exposes}}$<br>
$\color{RoyalBlue}{\textbf{through pseudo-filesystems that exist only in RAM.}}$<br>
$\color{#374151}{\footnotesize\text{lspci, lsusb và lsmod đọc dữ liệu mà kernel cung cấp}}$<br>
$\color{#374151}{\footnotesize\text{qua các hệ thống tệp giả chỉ tồn tại trong RAM.}}$

### 3.1 /proc

$\color{RoyalBlue}{\textbf{Process and hardware information:}}$<br>
$\color{#374151}{\footnotesize\text{Thông tin về tiến trình và phần cứng:}}$

- `/proc/cpuinfo`: $\color{RoyalBlue}{\textbf{CPU details, incl. a bugs line listing known vulnerabilities}}$<br>
  $\color{#374151}{\footnotesize\text{Chi tiết CPU, gồm dòng bugs liệt kê các lỗ hổng đã biết (vd cpu meltdown)}}$
- `/proc/interrupts`: $\color{RoyalBlue}{\textbf{Interrupts per I/O device per CPU}}$<br>
  $\color{#374151}{\footnotesize\text{Số ngắt của từng thiết bị I/O trên từng CPU}}$
- `/proc/ioports`: $\color{RoyalBlue}{\textbf{Registered I/O port regions}}$<br>
  $\color{#374151}{\footnotesize\text{Các vùng cổng I/O đã đăng ký}}$
- `/proc/dma`: $\color{RoyalBlue}{\textbf{Registered DMA channels}}$<br>
  $\color{#374151}{\footnotesize\text{Các kênh DMA đã đăng ký}}$

### 3.2 /sys

$\color{RoyalBlue}{\textbf{Device information and kernel data related to hardware (sysfs), used by udev.}}$<br>
$\color{#374151}{\footnotesize\text{Thông tin thiết bị và dữ liệu kernel liên quan phần cứng (sysfs), được udev sử dụng.}}$

### 3.3 /dev and udev / /dev và udev

$\color{RoyalBlue}{\textbf{Every file in /dev represents a device. The kernel passes hardware}}$<br>
$\color{RoyalBlue}{\textbf{detection events to udev, which creates device files dynamically}}$<br>
$\color{RoyalBlue}{\textbf{using rules in /etc/udev/rules.d/.}}$<br>
$\color{#374151}{\footnotesize\text{Mỗi tệp trong /dev đại diện cho một thiết bị. Kernel gửi sự kiện}}$<br>
$\color{#374151}{\footnotesize\text{phát hiện phần cứng cho udev, udev tạo tệp thiết bị một cách động}}$<br>
$\color{#374151}{\footnotesize\text{dựa trên các quy tắc trong /etc/udev/rules.d/.}}$

**$\color{RoyalBlue}{\textbf{Rules shipped by the distribution are the most important.}}$**<br>
**$\color{#374151}{\footnotesize\text{Các quy tắc đi kèm bản phân phối là quan trọng nhất.}}$**

- **Coldplug**: $\color{RoyalBlue}{\textbf{devices present at power-up.}}$<br>
  $\color{#374151}{\footnotesize\text{thiết bị có mặt lúc khởi động máy.}}$
- **Hotplug**: $\color{RoyalBlue}{\textbf{devices detected while the system is running (kernel 2.6+).}}$<br>
  $\color{#374151}{\footnotesize\text{thiết bị được phát hiện khi hệ thống đang chạy (từ kernel 2.6).}}$

---

## 4. Storage Device Naming / Đặt tên thiết bị lưu trữ

$\color{RoyalBlue}{\textbf{Storage devices are block devices, identified by files in /dev.}}$<br>
$\color{#374151}{\footnotesize\text{Thiết bị lưu trữ là block device, được nhận diện bằng các tệp trong /dev.}}$

| Device type / Loại thiết bị | Naming / Cách đặt tên |
|---|---|
| Legacy IDE disk / Đĩa IDE cũ | `/dev/hda`, `/dev/hdb` (first channel / kênh 1), `/dev/hdc`... (second channel / kênh 2); `/dev/hda1`, ... |
| Floppy / Đĩa mềm | `/dev/fd0`, `/dev/fd1` |
| SATA / SCSI / SSD / USB (kernel 2.4+) | `/dev/sda`, `/dev/sdb`, ...; `/dev/sda1`, `/dev/sda2`, ... |
| SD / memory card / Thẻ nhớ | `/dev/mmcblk0`; `/dev/mmcblk0p1`, `/dev/mmcblk0p2`, ... |
| NVMe SSD | `/dev/nvme0n1`; `/dev/nvme0n1p1`, `/dev/nvme0n1p2`, ... |
