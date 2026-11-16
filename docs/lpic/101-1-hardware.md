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
| Legacy IDE disk / Đĩa IDE cũ | `/dev/hda`, `/dev/hdb` (first channel / kênh 1), `/dev/hdc`, `/dev/hdd` (second channel / kênh 2); `/dev/hda1`, ... |
| Floppy / Đĩa mềm | `/dev/fd0`, `/dev/fd1` |
| SATA / SCSI / SSD / USB (kernel 2.4+) | `/dev/sda`, `/dev/sdb`, ...; `/dev/sda1`, `/dev/sda2`, ... |
| SD / memory card / Thẻ nhớ | `/dev/mmcblk0`; `/dev/mmcblk0p1`, `/dev/mmcblk0p2`, ... |
| NVMe SSD | `/dev/nvme0n1`; `/dev/nvme0n1p1`, `/dev/nvme0n1p2`, ... |

### 4.1 Naming Order Rules / Quy tắc thứ tự đặt tên

**sd\* (SATA / SCSI / SSD / USB)**

$\color{RoyalBlue}{\textbf{Letters are assigned in the order the kernel detects the disks: a, b, c, ...}}$<br>
$\color{RoyalBlue}{\textbf{The number after the letters is the partition number, starting from 1.}}$<br>
$\color{#374151}{\footnotesize\text{Chữ cái được cấp theo thứ tự kernel phát hiện đĩa: a, b, c, ...}}$<br>
$\color{#374151}{\footnotesize\text{Số đứng sau chữ cái là số thứ tự phân vùng, bắt đầu từ 1.}}$

| Device / Thiết bị | Meaning / Ý nghĩa |
|---|---|
| `/dev/sda` | $\color{RoyalBlue}{\textbf{1st disk}}$ $\color{#374151}{\footnotesize\text{(đĩa thứ 1)}}$ |
| `/dev/sdb` | $\color{RoyalBlue}{\textbf{2nd disk}}$ $\color{#374151}{\footnotesize\text{(đĩa thứ 2)}}$ |
| `/dev/sdc` | $\color{RoyalBlue}{\textbf{3rd disk, e.g. a USB stick plugged in later}}$ $\color{#374151}{\footnotesize\text{(đĩa thứ 3, ví dụ USB cắm sau)}}$ |
| `/dev/sdz` → `/dev/sdaa` | $\color{RoyalBlue}{\textbf{After z, naming continues with aa, ab, ...}}$ $\color{#374151}{\footnotesize\text{(sau z thì tiếp tục aa, ab, ...)}}$ |
| `/dev/sda1` | $\color{RoyalBlue}{\textbf{1st partition of the 1st disk}}$ $\color{#374151}{\footnotesize\text{(phân vùng 1 của đĩa 1)}}$ |
| `/dev/sdb2` | $\color{RoyalBlue}{\textbf{2nd partition of the 2nd disk}}$ $\color{#374151}{\footnotesize\text{(phân vùng 2 của đĩa 2)}}$ |

$\color{RoyalBlue}{\textbf{Warning: the letter depends on detection order and can change after a reboot}}$<br>
$\color{RoyalBlue}{\textbf{or when devices are added. Use UUID or LABEL in /etc/fstab for reliability.}}$<br>
$\color{#374151}{\footnotesize\text{Lưu ý: chữ cái phụ thuộc thứ tự phát hiện, có thể đổi sau khi khởi động lại}}$<br>
$\color{#374151}{\footnotesize\text{hoặc khi thêm thiết bị. Nên dùng UUID hoặc LABEL trong /etc/fstab cho ổn định.}}$

**hd\* (legacy IDE)**

$\color{RoyalBlue}{\textbf{Letters follow the IDE channel and master/slave position.}}$<br>
$\color{#374151}{\footnotesize\text{Chữ cái theo kênh IDE và vị trí master/slave.}}$

| Device / Thiết bị | Position / Vị trí |
|---|---|
| `/dev/hda` | Primary channel, master / Kênh 1, master |
| `/dev/hdb` | Primary channel, slave / Kênh 1, slave |
| `/dev/hdc` | Secondary channel, master / Kênh 2, master |
| `/dev/hdd` | Secondary channel, slave / Kênh 2, slave |

**fd\* (floppy)**

$\color{RoyalBlue}{\textbf{Numbered from 0: fd0 is the first drive, fd1 the second. No partitions.}}$<br>
$\color{#374151}{\footnotesize\text{Đánh số từ 0: fd0 là ổ thứ nhất, fd1 là ổ thứ hai. Không có phân vùng.}}$

**mmcblk\* (SD / memory card)**

$\color{RoyalBlue}{\textbf{Format: mmcblk<card number>p<partition number>. Cards are numbered from 0.}}$<br>
$\color{RoyalBlue}{\textbf{The letter p separates the disk number from the partition number.}}$<br>
$\color{#374151}{\footnotesize\text{Định dạng: mmcblk<số thẻ>p<số phân vùng>. Thẻ đánh số từ 0.}}$<br>
$\color{#374151}{\footnotesize\text{Chữ p ngăn cách số thẻ và số phân vùng.}}$

| Device / Thiết bị | Meaning / Ý nghĩa |
|---|---|
| `/dev/mmcblk0` | $\color{RoyalBlue}{\textbf{1st card}}$ $\color{#374151}{\footnotesize\text{(thẻ thứ 1)}}$ |
| `/dev/mmcblk0p1` | $\color{RoyalBlue}{\textbf{1st partition of the 1st card}}$ $\color{#374151}{\footnotesize\text{(phân vùng 1 của thẻ 1)}}$ |
| `/dev/mmcblk1p2` | $\color{RoyalBlue}{\textbf{2nd partition of the 2nd card}}$ $\color{#374151}{\footnotesize\text{(phân vùng 2 của thẻ 2)}}$ |

**nvme\* (NVMe SSD)**

$\color{RoyalBlue}{\textbf{Format: nvme<controller>n<namespace>p<partition>.}}$<br>
$\color{RoyalBlue}{\textbf{Controller and namespace start from 0 and 1 respectively; a typical SSD has one namespace.}}$<br>
$\color{#374151}{\footnotesize\text{Định dạng: nvme<bộ điều khiển>n<namespace>p<phân vùng>.}}$<br>
$\color{#374151}{\footnotesize\text{Controller bắt đầu từ 0, namespace bắt đầu từ 1; SSD thông thường chỉ có một namespace.}}$

| Device / Thiết bị | Meaning / Ý nghĩa |
|---|---|
| `/dev/nvme0n1` | $\color{RoyalBlue}{\textbf{1st NVMe controller, namespace 1 (the whole disk)}}$ $\color{#374151}{\footnotesize\text{(controller 0, namespace 1, tức cả ổ đĩa)}}$ |
| `/dev/nvme0n1p1` | $\color{RoyalBlue}{\textbf{Partition 1 of that disk}}$ $\color{#374151}{\footnotesize\text{(phân vùng 1 của ổ đó)}}$ |
| `/dev/nvme1n1p3` | $\color{RoyalBlue}{\textbf{Partition 3 of the 2nd NVMe SSD}}$ $\color{#374151}{\footnotesize\text{(phân vùng 3 của ổ NVMe thứ 2)}}$ |

### 4.2 Partition Numbering (MBR) / Đánh số phân vùng (MBR)

$\color{RoyalBlue}{\textbf{MBR allows at most 4 primary partitions (numbers 1 to 4).}}$<br>
$\color{RoyalBlue}{\textbf{To have more, one primary becomes an extended partition that holds logical partitions,}}$<br>
$\color{RoyalBlue}{\textbf{which are always numbered from 5, even if fewer than 4 primaries exist.}}$<br>
$\color{#374151}{\footnotesize\text{MBR cho phép tối đa 4 phân vùng primary (số 1 đến 4).}}$<br>
$\color{#374151}{\footnotesize\text{Muốn nhiều hơn, một primary được dùng làm extended chứa các phân vùng logical,}}$<br>
$\color{#374151}{\footnotesize\text{các logical luôn được đánh số từ 5, dù có ít hơn 4 primary.}}$

```shell
$ lsblk /dev/sda
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0  500G  0 disk
├─sda1   8:1    0  100G  0 part /
├─sda2   8:2    0   50G  0 part /home
├─sda3   8:3    0    8G  0 part [SWAP]
├─sda4   8:4    0    1K  0 part            <- extended / phân vùng mở rộng
├─sda5   8:5    0  200G  0 part            <- logical
└─sda6   8:6    0  142G  0 part            <- logical
```

$\color{RoyalBlue}{\textbf{GPT has no extended/logical concept: partitions are simply numbered 1, 2, 3, ...}}$<br>
$\color{#374151}{\footnotesize\text{GPT không có khái niệm extended/logical: các phân vùng chỉ đánh số 1, 2, 3, ...}}$

### 4.3 Examples / Ví dụ thực tế

**Example 1 / Ví dụ 1:** $\color{RoyalBlue}{\textbf{A PC with one SATA disk and one NVMe SSD}}$ $\color{#374151}{\footnotesize\text{(Máy có 1 đĩa SATA và 1 SSD NVMe)}}$

```shell
$ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 931.5G  0 disk
└─sda1        8:1    0 931.5G  0 part /data
nvme0n1     259:0    0 476.9G  0 disk
├─nvme0n1p1 259:1    0   512M  0 part /boot/efi
├─nvme0n1p2 259:2    0     1G  0 part /boot
└─nvme0n1p3 259:3    0 475.4G  0 part /
```

**Example 2 / Ví dụ 2:** $\color{RoyalBlue}{\textbf{Plug in a USB stick and an SD card}}$ $\color{#374151}{\footnotesize\text{(Cắm thêm USB và thẻ SD)}}$

```shell
$ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda           8:0    0 931.5G  0 disk
└─sda1        8:1    0 931.5G  0 part /data
sdb           8:16   1  14.9G  0 disk          <- USB stick / USB (letter b: next free) 
└─sdb1        8:17   1  14.9G  0 part /run/media/user/USB
mmcblk0     179:0    0  29.7G  0 disk          <- SD card / thẻ SD
└─mmcblk0p1 179:1    0  29.7G  0 part /run/media/user/SD
nvme0n1     259:0    0 476.9G  0 disk
└─nvme0n1p1 259:1    0 476.9G  0 part /
```

**Example 3 / Ví dụ 3:** $\color{RoyalBlue}{\textbf{A server with 3 SATA disks}}$ $\color{#374151}{\footnotesize\text{(Máy chủ có 3 đĩa SATA)}}$

| Device / Thiết bị | Description / Mô tả |
|---|---|
| `/dev/sda`, `/dev/sda1`, `/dev/sda2` | OS disk, 2 partitions / Đĩa hệ điều hành, 2 phân vùng |
| `/dev/sdb`, `/dev/sdb1` | Data disk 1 / Đĩa dữ liệu 1 |
| `/dev/sdc`, `/dev/sdc1` | Data disk 2 / Đĩa dữ liệu 2 |

**Example 4 / Ví dụ 4:** $\color{RoyalBlue}{\textbf{An old PC with 2 IDE disks and a floppy drive}}$ $\color{#374151}{\footnotesize\text{(Máy cũ có 2 đĩa IDE và 1 ổ mềm)}}$

| Device / Thiết bị | Description / Mô tả |
|---|---|
| `/dev/hda`, `/dev/hda1`, `/dev/hda2` | Primary master disk / Đĩa kênh 1 master |
| `/dev/hdc`, `/dev/hdc1` | Secondary master disk / Đĩa kênh 2 master |
| `/dev/fd0` | Floppy drive / Ổ đĩa mềm |

### 4.4 Quick Check Commands / Lệnh kiểm tra nhanh

| Command | Purpose | Mục đích |
|---|---|---|
| `lsblk` | $\color{RoyalBlue}{\textbf{Tree of disks and partitions}}$ | $\color{#374151}{\footnotesize\text{Hiển thị cây đĩa và phân vùng}}$ |
| `lsblk -f` | $\color{RoyalBlue}{\textbf{Add filesystem type, LABEL and UUID}}$ | $\color{#374151}{\footnotesize\text{Thêm loại hệ tệp, LABEL và UUID}}$ |
| `blkid` | $\color{RoyalBlue}{\textbf{Show UUID/LABEL of block devices}}$ | $\color{#374151}{\footnotesize\text{Hiện UUID/LABEL của các block device}}$ |
| `sudo fdisk -l` | $\color{RoyalBlue}{\textbf{List disks and partition tables}}$ | $\color{#374151}{\footnotesize\text{Liệt kê đĩa và bảng phân vùng}}$ |
| `ls -l /dev/disk/by-uuid/` | $\color{RoyalBlue}{\textbf{Stable names that do not change}}$ | $\color{#374151}{\footnotesize\text{Tên ổn định, không đổi}}$ |
