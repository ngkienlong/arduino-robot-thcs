# Syllabus: Khoá học Arduino — Xe Robot Tránh Vật Cản

**Đối tượng:** Học sinh THCS
**Số buổi:** 8 buổi (90 phút/buổi)
**Mục tiêu cuối khoá:** Học sinh tự lắp ráp và lập trình xe robot Arduino di chuyển tiến/lùi/xoay trái/xoay phải, tích hợp cảm biến siêu âm để tự động tránh vật cản.

---

## Tổng quan khoá học & Nhóm mục tiêu

| # | Buổi | Dự án | Nhóm mục tiêu | Kiến thức cốt lõi | Mục tiêu theo thang Bloom | Số buổi |
|---|------|-------|---------------|-------------------|--------------------------|---------|
| 1 | 1 | Đèn SOS cứu hộ | Làm quen Arduino + output digital | Board Arduino Uno, breadboard, LED, điện trở, dây nối, `setup()`, `loop()`, `digitalWrite()`, `delay()` | • Nhận biết và gọi tên các thành phần cơ bản của Arduino • Kết nối mạch LED trên breadboard theo sơ đồ cho trước • Viết chương trình với `setup()`, `loop()`, `digitalWrite()`, `delay()` để điều khiển LED | 1 |
| 2 | 2 | Chuông cửa thông minh | Input digital + logic điều kiện | Nút bấm, `digitalRead()`, buzzer, `tone()`, `noTone()`, `if/else`, biến trạng thái | • Kết nối nút bấm và đọc trạng thái bằng `digitalRead()` • Điều khiển buzzer bằng `tone()` và `noTone()` • Áp dụng `if/else` để ra quyết định dựa trên input • Sử dụng biến trạng thái để chuyển đổi chế độ | 1 |
| 3 | 3 | Cảm biến lùi xe ô tô | Cảm biến siêu âm + đọc dữ liệu | HC-SR04, Serial Monitor, `if/else if/else`, công thức tính khoảng cách | • Giải thích được nguyên lý hoạt động của HC-SR04 • Kết nối và lập trình đọc khoảng cách từ HC-SR04 • Sử dụng Serial Monitor để hiển thị và debug • Áp dụng `if/else if/else` để phân loại khoảng cách | 1 |
| 4 | 4 | Máy trộn màu | Điều khiển motor DC + PWM | Motor DC, driver L298N, PWM, `analogWrite()`, chiều quay motor | • Kết nối motor DC qua driver L298N theo sơ đồ • Giải thích được PWM và dùng `analogWrite()` điều chỉnh tốc độ • Điều khiển chiều quay motor thuận/nghịch | 1 |
| 5 | 5-6 | Xe robot chạy theo lộ trình | Lắp ráp xe robot + lái vi sai | Khung xe 2 bánh, bánh tự lựa, lái vi sai, hàm tự định nghĩa | • Lắp ráp khung xe robot 2 bánh theo hướng dẫn • Điều khiển 2 motor đồng thời để xe tiến/lùi/xoay trái/xoay phải • Giải thích được nguyên lý lái vi sai • Viết hàm tự định nghĩa để tổ chức code | 2 |
| 6 | 7-8 | Xe robot thám hiểm | Tích hợp cảm biến + thuật toán tránh vật cản | Tích hợp HC-SR04 lên xe, thuật toán, flowchart, debug, trình bày | • Tích hợp cảm biến siêu âm lên xe robot • Thiết kế thuật toán tránh vật cản và vẽ flowchart • Debug và cải tiến qua thử nghiệm thực tế • Trình bày sản phẩm và phản biện | 2 |

---

## Vật tư và công cụ cần thiết cho toàn khoá học

**Phần cứng (mỗi nhóm):**
- Arduino Uno ×1 + cáp USB
- Breadboard ×1
- Dây nối (jumper wires) đực-đực, đực-cái
- LED (đỏ, xanh lá, xanh dương) + điện trở 220Ω ×3
- Nút bấm ×1 + điện trở 10kΩ ×1
- Buzzer thụ động ×1
- Cảm biến siêu âm HC-SR04 ×1
- Module driver motor L298N ×1
- Motor DC ×2 + bánh xe ×2
- Bánh tự lựa (caster wheel) ×1
- Khung xe robot (acrylic hoặc in 3D) ×1
- Servo SG90 ×1
- Nguồn pin / pin lithium + hộp
- Que khuấy + cốc nhựa (cho dự án 4)

**Phần mềm:**
- Arduino IDE

---

## Đánh giá chung

**Rubric chung** (áp dụng cho tất cả dự án, phát cho học sinh từ buổi đầu):

| Tiêu chí | Chưa đạt (1) | Đạt (2) | Tốt (3) | Xuất sắc (4) |
|----------|---------------|---------|---------|---------------|
| Quy trình EDP | Bỏ qua nhiều bước, không quay lại cải tiến | Đi đủ các bước nhưng qua loa | Đi đủ các bước, có quay lại cải tiến khi cần | Đi đủ, chủ động quay lại cải tiến, ghi chép rõ ràng |
| Làm việc nhóm | 1 người làm hết | Có phân vai nhưng không đều | Phân vai rõ, mọi người tham gia | Phân vai rõ, hỗ trợ lẫn nhau, giải quyết xung đột tốt |
| Trình bày | Không trình bày được | Trình bày nhưng không rõ ràng | Giải thích rõ, demo thuyết phục | Giải thích rõ, demo tốt, trả lời được câu hỏi |

*Tiêu chí "Sản phẩm" và "Code" được thiết kế riêng cho từng dự án — xem rubric trong phần mô tả từng dự án bên dưới.*

**Peer feedback** có cấu trúc (đặc biệt dự án 5 và 6): Các nhóm nhận xét lẫn nhau theo mẫu "Điều mình thích — Điều mình thắc mắc — Gợi ý cải tiến".

---

## Dự án 1: Đèn SOS cứu hộ — 1 buổi

**Câu hỏi dẫn dắt:** "Làm sao để gửi tín hiệu cầu cứu bằng ánh sáng?"

**Mục tiêu (STEM/AI):**
- Nhận biết và gọi tên các thành phần cơ bản của Arduino (board, breadboard, LED, điện trở, dây nối)
- Kết nối mạch LED trên breadboard theo sơ đồ cho trước
- Viết chương trình điều khiển LED phát tín hiệu SOS theo mã Morse bằng `digitalWrite()` và `delay()`

**Sản phẩm đầu ra:** LED phát tín hiệu SOS theo mã Morse (ngắn-ngắn-ngắn / dài-dài-dài / ngắn-ngắn-ngắn), lặp liên tục.

**Phần cứng:** Arduino Uno ×1, breadboard ×1, LED ×1, điện trở 220Ω ×1, dây nối
**Phần mềm:** Arduino IDE

**Phân hoá:**
- Yêu cầu cơ bản: Phát tín hiệu SOS cố định
- Yêu cầu nâng cao: Mã hoá thêm các ký tự khác (tên mình bằng Morse), hoặc thêm buzzer phát âm thanh kèm ánh sáng

**Rubric dự án:**

| Tiêu chí | Chưa đạt (1) | Đạt (2) | Tốt (3) | Xuất sắc (4) |
|----------|---------------|---------|---------|---------------|
| Sản phẩm | LED không nhấp nháy hoặc nhấp nháy ngẫu nhiên | LED nhấp nháy nhưng chưa đúng pattern SOS | LED phát đúng tín hiệu SOS (3 ngắn — 3 dài — 3 ngắn), lặp liên tục | Phát SOS đúng + thêm ký tự Morse khác hoặc kèm buzzer |
| Code | Không upload được hoặc không chạy | Chạy được nhưng timing sai, không có comment | Code chạy đúng, timing hợp lý, có comment giải thích | Code sạch, dùng biến cho timing (dễ thay đổi), comment rõ ràng |

---

## Dự án 2: Chuông cửa thông minh — 1 buổi

**Câu hỏi dẫn dắt:** "Làm sao để tạo chuông cửa phát nhạc khi có khách bấm?"

**Mục tiêu (STEM/AI):**
- Kết nối nút bấm làm input digital và đọc trạng thái bằng `digitalRead()`
- Điều khiển buzzer phát giai điệu bằng `tone()` và `noTone()`
- Áp dụng `if/else` để ra quyết định: khi nút được nhấn → phát chuông, khi thả → tắt
- Sử dụng biến trạng thái để đếm số lần nhấn và chuyển đổi giai điệu

**Sản phẩm đầu ra:** Chuông cửa — nhấn nút → buzzer phát giai điệu. Nhấn nhiều lần → chuyển sang giai điệu khác.

**Phần cứng:** Arduino Uno ×1, breadboard ×1, nút bấm ×1, điện trở 10kΩ ×1, buzzer thụ động ×1, dây nối
**Phần mềm:** Arduino IDE

**Phân hoá:**
- Yêu cầu cơ bản: Nhấn nút → buzzer phát 1 giai điệu cố định
- Yêu cầu nâng cao: Nhấn giữ lâu → giai điệu khác, hoặc tự sáng tác giai điệu riêng bằng cách thay đổi tần số và thời lượng nốt

**Rubric dự án:**

| Tiêu chí | Chưa đạt (1) | Đạt (2) | Tốt (3) | Xuất sắc (4) |
|----------|---------------|---------|---------|---------------|
| Sản phẩm | Nhấn nút không có phản hồi | Buzzer kêu nhưng chỉ 1 tần số đơn, không thành giai điệu | Nhấn nút → buzzer phát giai điệu rõ ràng, nhả nút → tắt | Phát giai điệu + chuyển đổi giai điệu khi nhấn nhiều lần hoặc nhấn giữ |
| Code | Không upload được hoặc không chạy | Chạy được nhưng logic `if/else` sai hoặc thiếu | Code đúng, dùng `if/else` + `tone()` hợp lý, có comment | Code sạch, dùng biến trạng thái rõ ràng, giai điệu được tổ chức thành mảng hoặc hàm riêng |

---

## Dự án 3: Cảm biến lùi xe ô tô — 1 buổi

**Câu hỏi dẫn dắt:** "Làm sao ô tô biết sắp đâm vào vật phía sau khi lùi?"

**Mục tiêu (STEM/AI):**
- Giải thích được nguyên lý hoạt động của cảm biến siêu âm HC-SR04 (phát sóng → phản xạ → đo thời gian → tính khoảng cách)
- Kết nối và lập trình đọc giá trị khoảng cách từ HC-SR04
- Sử dụng Serial Monitor để hiển thị và debug dữ liệu
- Áp dụng `if/else if/else` để phân loại khoảng cách: xa → buzzer kêu chậm, gần → kêu nhanh, rất gần → kêu liên tục

**Sản phẩm đầu ra:** Hệ thống cảnh báo khoảng cách — buzzer kêu nhanh/chậm theo khoảng cách (giống cảm biến lùi xe ô tô).

**Phần cứng:** Arduino Uno ×1, breadboard ×1, cảm biến siêu âm HC-SR04 ×1, buzzer thụ động ×1, dây nối
**Phần mềm:** Arduino IDE

**Phân hoá:**
- Yêu cầu cơ bản: Buzzer kêu khi vật ở gần (dưới 20cm), tắt khi xa
- Yêu cầu nâng cao: Buzzer kêu với tần suất thay đổi liên tục theo khoảng cách, thêm LED xanh/vàng/đỏ hiển thị 3 mức

**Rubric dự án:**

| Tiêu chí | Chưa đạt (1) | Đạt (2) | Tốt (3) | Xuất sắc (4) |
|----------|---------------|---------|---------|---------------|
| Sản phẩm | Cảm biến không đọc được khoảng cách | Đọc được khoảng cách trên Serial Monitor nhưng buzzer không phản hồi đúng | Buzzer kêu/tắt đúng theo ngưỡng khoảng cách, Serial Monitor hiển thị đúng | Buzzer thay đổi tần suất mượt mà theo khoảng cách + thêm LED 3 mức |
| Code | Không upload được hoặc không chạy | Chạy được nhưng công thức tính khoảng cách sai hoặc `if/else if` thiếu nhánh | Code đúng, dùng `if/else if/else` phân loại 3 vùng, Serial Monitor hiển thị đúng | Code sạch, comment giải thích công thức, ngưỡng dễ thay đổi bằng biến hằng |

---

## Dự án 4: Máy trộn màu — 1 buổi

**Câu hỏi dẫn dắt:** "Làm sao để trộn sơn đều mà không cần khuấy tay?"

**Mục tiêu (STEM/AI):**
- Kết nối motor DC qua driver L298N theo sơ đồ
- Giải thích được khái niệm PWM và sử dụng `analogWrite()` để điều chỉnh tốc độ motor
- Điều khiển chiều quay motor (thuận/nghịch) bằng cách thay đổi tín hiệu trên driver

**Sản phẩm đầu ra:** Motor quay que khuấy trong cốc nước màu, điều chỉnh tốc độ + đảo chiều.

**Phần cứng:** Arduino Uno ×1, driver L298N ×1, motor DC ×1, que khuấy, cốc nhựa, nguồn pin, dây nối
**Phần mềm:** Arduino IDE

**Phân hoá:**
- Yêu cầu cơ bản: Motor quay 1 chiều với 2 mức tốc độ
- Yêu cầu nâng cao: Thêm chế độ "trộn tự động" — quay nhanh 5 giây → chậm 3 giây → đảo chiều, lặp lại

**Rubric dự án:**

| Tiêu chí | Chưa đạt (1) | Đạt (2) | Tốt (3) | Xuất sắc (4) |
|----------|---------------|---------|---------|---------------|
| Sản phẩm | Motor không quay | Motor quay nhưng chỉ 1 tốc độ, không điều chỉnh được | Motor quay với 2 mức tốc độ khác nhau bằng PWM | Motor quay 2+ mức tốc độ + đảo chiều + chế độ trộn tự động |
| Code | Không upload được hoặc không chạy | Chạy được nhưng `analogWrite()` dùng sai hoặc không thay đổi tốc độ | Code đúng, dùng `analogWrite()` với các giá trị PWM khác nhau, có comment | Code sạch, giá trị PWM dùng biến hằng, có hàm riêng cho từng chế độ |

---

## Dự án 5: Xe robot chạy theo lộ trình — 2 buổi

**Câu hỏi dẫn dắt:** "Làm sao để lập trình xe chạy theo đường đã vạch sẵn trong đầu?"

**Mục tiêu (STEM/AI):**
- Lắp ráp khung xe robot 2 bánh (2 motor DC + 1 bánh tự lựa) theo hướng dẫn
- Điều khiển đồng thời 2 motor qua driver L298N để xe tiến/lùi/xoay trái/xoay phải
- Giải thích được nguyên lý lái vi sai (differential steering)
- Viết hàm tự định nghĩa (`moveForward()`, `turnLeft()`,...) và gọi chúng theo chuỗi lệnh để xe chạy theo lộ trình

**Sản phẩm đầu ra:** Xe robot chạy theo chuỗi lệnh định sẵn (tiến 2s → xoay phải 90° → tiến 1s → xoay trái →...) để hoàn thành một đường đua đơn giản.

**Phần cứng:** Arduino Uno ×1, driver L298N ×1, motor DC ×2, bánh xe ×2, bánh tự lựa ×1, khung xe ×1, nguồn pin, dây nối
**Phần mềm:** Arduino IDE

**Phân hoá:**
- Yêu cầu cơ bản: Xe chạy theo lộ trình cố định (3-4 bước)
- Yêu cầu nâng cao: Xe chạy theo lộ trình phức tạp hơn (hình vuông, hình chữ L), tinh chỉnh thời gian xoay để chính xác

**Phân bổ 2 buổi:**
- Buổi 5a: Xác định vấn đề → Tìm hiểu kiến thức (lái vi sai) → Lên ý tưởng → Lắp ráp khung xe. *Sản phẩm trung gian: xe lắp xong, motor quay được.*
- Buổi 5b: Lập trình lộ trình → Thử nghiệm trên đường đua → Debug + cải tiến → Trình bày demo.

**Rubric dự án:**

| Tiêu chí | Chưa đạt (1) | Đạt (2) | Tốt (3) | Xuất sắc (4) |
|----------|---------------|---------|---------|---------------|
| Sản phẩm | Xe không lắp xong hoặc motor không quay | Xe chạy được nhưng chỉ tiến/lùi, không xoay được | Xe chạy theo lộ trình cố định 3-4 bước (tiến, xoay, tiến) | Xe chạy lộ trình phức tạp (hình vuông/chữ L), xoay chính xác |
| Code | Không upload được hoặc không chạy | Chạy được nhưng không dùng hàm, code lặp lại nhiều | Code dùng hàm tự định nghĩa (`moveForward()`, `turnLeft()`,...), có comment | Code sạch, hàm có tham số (thời gian, tốc độ), dễ thay đổi lộ trình |

---

## Dự án 6: Xe robot thám hiểm — 2 buổi

**Câu hỏi dẫn dắt:** "Làm sao để robot tự khám phá một căn phòng mà không bị kẹt?"

**Mục tiêu (STEM/AI):**
- Tích hợp cảm biến siêu âm HC-SR04 lên xe robot đã lắp
- Thiết kế thuật toán thám hiểm: di chuyển → gặp vật cản → quét trái/phải → chọn hướng trống → tiếp tục
- Debug và cải tiến thuật toán qua thử nghiệm thực tế
- Trình bày sản phẩm, giải thích thuật toán, phản biện và nhận phản hồi từ bạn

**Sản phẩm đầu ra:** Xe robot tự di chuyển khám phá không gian, tránh vật cản thông minh (quét trái/phải trước khi chọn hướng). LED/buzzer cảnh báo khi phát hiện vật cản.

**Phần cứng:** Xe robot từ dự án 5 + cảm biến siêu âm HC-SR04 ×1, servo SG90 ×1 (để quét trái/phải), LED ×1, buzzer ×1, dây nối
**Phần mềm:** Arduino IDE

**Phân hoá:**
- Yêu cầu cơ bản: Xe tránh vật cản cơ bản (dừng → xoay cố định → đi tiếp)
- Yêu cầu nâng cao: Xe quét trái/phải bằng servo, so sánh khoảng cách 2 bên để chọn hướng tối ưu

**Phân bổ 2 buổi:**
- Buổi 6a: Xác định vấn đề → Tìm hiểu kiến thức (ôn cảm biến + motor) → Lên ý tưởng thuật toán (vẽ flowchart) → Gắn cảm biến + servo lên xe + lập trình phiên bản đầu. *Sản phẩm trung gian: cảm biến + servo hoạt động trên xe.*
- Buổi 6b: Thử nghiệm thuật toán trên trường chướng ngại vật → Debug + cải tiến → Trình bày demo + Q&A giữa các nhóm.

**Rubric dự án:**

| Tiêu chí | Chưa đạt (1) | Đạt (2) | Tốt (3) | Xuất sắc (4) |
|----------|---------------|---------|---------|---------------|
| Sản phẩm | Cảm biến không gắn được hoặc xe không phản hồi vật cản | Xe dừng khi gặp vật cản nhưng không xoay tránh | Xe phát hiện vật cản → dừng → xoay → tiếp tục đi, tránh được hầu hết vật cản | Xe quét trái/phải bằng servo, chọn hướng tối ưu, tránh mượt mà + LED/buzzer cảnh báo |
| Code | Không upload được hoặc không chạy | Chạy được nhưng thuật toán thiếu logic (không xoay sau khi dừng) | Code đúng thuật toán flowchart, dùng hàm tự định nghĩa, có comment | Code sạch, thuật toán có quét trái/phải + so sánh, ngưỡng dùng biến hằng, dễ tinh chỉnh |

---
