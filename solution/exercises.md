# Ngày 1 — Bài Tập & Phản Ánh
## Nền Tảng LLM API | Phiếu Thực Hành

**Thời lượng:** 1:30 giờ  
**Cấu trúc:** Lập trình cốt lõi (60 phút) → Bài tập mở rộng (30 phút)

---

## Phần 1 — Lập Trình Cốt Lõi (0:00–1:00)

Chạy các ví dụ trong Google Colab tại: https://colab.research.google.com/drive/172zCiXpLr1FEXMRCAbmZoqTrKiSkUERm?usp=sharing

Triển khai tất cả TODO trong `template.py`. Chạy `pytest tests/` để kiểm tra tiến độ.

**Điểm kiểm tra:** Sau khi hoàn thành 4 nhiệm vụ, chạy:
```bash
python template.py
```
Bạn sẽ thấy output so sánh phản hồi của GPT-4o và GPT-4o-mini.

---

## Phần 2 — Bài Tập Mở Rộng (1:00–1:30)

### Bài tập 2.1 — Độ Nhạy Của Temperature
Gọi `call_openai` với các giá trị temperature 0.0, 0.5, 1.0 và 1.5 sử dụng prompt **"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Kết quả chạy thực tế:**

**Temperature 0.0** (latency: 3.93s, 153 token):
> Một sự thật thú vị về Việt Nam là đất nước này có một trong những hệ thống hang động lớn nhất thế giới, đó là hang Sơn Đoòng. Nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng ở tỉnh Quảng Bình, hang Sơn Đoòng được phát hiện vào năm 1991 và chính thức được công nhận là hang động lớn nhất thế giới vào năm 2009. Hang có chiều dài hơn 5 km, cao 200 m và rộng 150 m, đủ lớn để chứa cả một tòa nhà chọc trời 40 tầng. Bên trong hang có cả một hệ sinh thái riêng với rừng cây, sông ngầm và các loài động thực vật độc đáo.

**Temperature 0.5** (latency: 2.89s, 176 token):
> Một sự thật thú vị về Việt Nam là đất nước này có một trong những hệ thống hang động lớn nhất thế giới, đó là hang Sơn Đoòng. Nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng ở tỉnh Quảng Bình, hang Sơn Đoòng được phát hiện vào năm 1991 bởi một người dân địa phương tên là Hồ Khanh và sau đó được khám phá chi tiết bởi các nhà thám hiểm hang động người Anh vào năm 2009. Hang có kích thước khổng lồ với chiều dài hơn 5 km, cao 200 mét và rộng 150 mét, đủ lớn để chứa cả một tòa nhà chọc trời 40 tầng. Bên trong hang có cả một hệ sinh thái riêng với rừng cây, sông ngầm và các loài động thực vật đặc hữu.

**Temperature 1.0** (latency: 2.88s, 173 token):
> Một sự thật thú vị về Việt Nam là đất nước này có hang động lớn nhất thế giới, được gọi là Hang Sơn Đoòng. Nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng thuộc tỉnh Quảng Bình, Hang Sơn Đoòng được khám phá lần đầu vào năm 2009 bởi một nhóm thám hiểm người Anh do Howard Limbert dẫn đầu. Hang này có kích thước khổng lồ, với chiều dài khoảng 9 km, chiều cao có nơi lên đến 200 mét và rộng khoảng 150 mét. Trong hang có cả một hệ sinh thái riêng biệt, với rừng cây, sông ngầm và hệ động thực vật độc đáo. Sơn Đoòng đã trở thành điểm đến hấp dẫn cho các nhà thám hiểm và du khách từ khắp nơi trên thế giới.

**Temperature 1.5** (latency: 3.51s, 186 token):
> Một sự thật thú vị về Việt Nam là đất nước này có hệ thống hang động tự nhiên lớn nhất thế giới, được gọi là Hang Sơn Đoòng. Hang này nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng, tỉnh Quảng Bình. Hang Sơn Đoòng được phát hiện vào năm 1991 bởi một người dân địa phương tên là Hồ Khanh và chính thức được khám phá bởi các nhà thám hiểm hang động người Anh vào năm 2009. Với chiều dài hơn 5 km, chiều cao có điểm lên đến 200 m và rộng khoảng 150 m, Hang Sơn Đoòng đủ lớn để chứa cả một tòa nhà chọc trời 40 tầng. Bên trong hang còn có hệ sinh thái riêng với rừng, sông ngầm và hệ động thực vật đa dạng, tạo nên một cảnh quan kỳ vĩ và độc đáo.

**Kết quả so sánh GPT-4o vs GPT-4o-mini:**

**GPT-4o** (latency: 2.67s, 165 token):
> Một sự thật thú vị về Việt Nam là đất nước này có hang động lớn nhất thế giới, đó là hang Sơn Đoòng. Nằm trong Vườn quốc gia Phong Nha-Kẻ Bàng ở tỉnh Quảng Bình, hang Sơn Đoòng được phát hiện vào năm 1991 bởi một người dân địa phương và sau đó được thám hiểm và công bố rộng rãi vào năm 2009. Hang động này có những khối thạch nhũ khổng lồ, một dòng sông ngầm, và thậm chí cả một khu rừng bên trong. Với chiều cao có thể lên tới 200 mét, chiều rộng 150 mét và chiều dài khoảng 9 kilômét, hang Sơn Đoòng là một kỳ quan thiên nhiên đáng kinh ngạc.

**GPT-4o-mini** (latency: 2.69s, 129 token):
> Một sự thật thú vị về Việt Nam là nước này có hơn 3.000 km bờ biển và hơn 4.000 hòn đảo lớn nhỏ. Đặc biệt, quần đảo Trường Sa và Hoàng Sa là hai trong số những nhóm đảo nổi tiếng của Việt Nam. Bờ biển dài này không chỉ mang lại cảnh quan tuyệt đẹp mà còn là nguồn tài nguyên phong phú cho ngành thủy sản, du lịch và giao thương. Việt Nam cũng nổi tiếng với nhiều bãi biển đẹp như Đà Nẵng, Nha Trang và Phú Quốc, thu hút hàng triệu du khách mỗi năm.

---

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Cả bốn mức temperature đều chọn cùng chủ đề hang Sơn Đoòng, nhưng cách diễn đạt và chi tiết thay đổi rõ rệt khi temperature tăng. Ở temperature 0.0 và 0.5, phản hồi gần như giống hệt nhau về cấu trúc và số liệu (chiều dài hang đều ghi "hơn 5 km"), cho thấy model rất ổn định và có tính xác định cao. Khi tăng lên 1.0, model đưa ra chi tiết khác biệt — đề cập tên trưởng đoàn Howard Limbert và ghi chiều dài hang là "khoảng 9 km" thay vì "hơn 5 km" — cho thấy temperature cao khiến model "sáng tạo" hơn nhưng đồng thời có thể đưa ra thông tin kém nhất quán.

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tôi sẽ đặt temperature từ 0.0 đến 0.3. Từ kết quả thí nghiệm, ở temperature 0.0 và 0.5 phản hồi rất nhất quán — cùng số liệu, cùng cấu trúc câu. Trong khi đó ở temperature 1.0, model đưa ra con số khác nhau cho cùng một sự thật (5 km vs 9 km). Chatbot hỗ trợ khách hàng cần đảm bảo thông tin về sản phẩm, chính sách luôn chính xác và nhất quán giữa các lần trả lời, nên temperature thấp là lựa chọn an toàn nhất.

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> **Tính toán chi tiết:**
> - Tổng số lần gọi API mỗi ngày: 10.000 × 3 = 30.000 lần
> - Tổng token output mỗi ngày: 30.000 × 350 = 10.500.000 token = 10.500 × 1K token
> - Chi phí GPT-4o mỗi ngày: 10.500 × $0.010 = **$105.00/ngày**
> - Chi phí GPT-4o-mini mỗi ngày: 10.500 × $0.0006 = **$6.30/ngày**
> - Tỉ lệ chênh lệch: $105.00 ÷ $6.30 = **16.67 lần**
> - Quy ra tháng (30 ngày): GPT-4o tốn $3.150 vs GPT-4o-mini tốn $189, chênh lệch $2.961/tháng
>
> **Kết luận:** GPT-4o đắt hơn GPT-4o-mini khoảng **16.67 lần** cho workload này.

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> **GPT-4o xứng đáng:** Phân tích hợp đồng pháp lý hoặc tư vấn y khoa — nơi một câu trả lời sai có thể gây hậu quả nghiêm trọng. Chi phí thiệt hại từ sai sót (kiện tụng, chẩn đoán sai) vượt xa chi phí API. Từ kết quả so sánh thực tế, GPT-4o cho phản hồi chi tiết hơn với 165 token, đề cập cụ thể đến thạch nhũ khổng lồ, sông ngầm và khu rừng bên trong hang — thể hiện khả năng phân tích sâu hơn.
>
> **GPT-4o-mini là lựa chọn tốt hơn:** Trả lời FAQ, phân loại email, tóm tắt nội dung ngắn với khối lượng lớn. Từ kết quả thực tế, GPT-4o-mini vẫn cho câu trả lời chất lượng tốt (129 token, nội dung chính xác về hơn 3.000 km bờ biển và hơn 4.000 hòn đảo của Việt Nam) với latency tương đương (2.69s vs 2.67s) nhưng tiết kiệm được gần 94% chi phí.

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming đặc biệt quan trọng trong các ứng dụng chatbot tương tác trực tiếp với người dùng, đặc biệt khi phản hồi dài. Từ kết quả thí nghiệm thực tế, mỗi lần gọi GPT-4o mất khoảng 2.67–3.93 giây để sinh 153–186 token — nếu không dùng streaming, người dùng phải nhìn màn hình trống suốt gần 4 giây mà không biết ứng dụng có đang hoạt động hay không, tạo cảm giác bị treo. Với streaming, token đầu tiên xuất hiện gần như ngay lập tức, người dùng bắt đầu đọc trong khi model vẫn đang sinh tiếp, tạo trải nghiệm mượt mà giống như đang trò chuyện thật. Ngược lại, non-streaming phù hợp hơn trong các trường hợp: (1) khi cần xử lý toàn bộ phản hồi trước khi hiển thị — ví dụ trích xuất dữ liệu JSON có cấu trúc để parse; (2) khi phản hồi được dùng làm đầu vào cho bước xử lý tiếp theo trong pipeline tự động mà không cần hiển thị trực tiếp; (3) khi phản hồi rất ngắn (vài token) nên sự khác biệt về thời gian chờ không đáng kể.


## Danh Sách Kiểm Tra Nộp Bài
- [x] Tất cả tests pass: `pytest tests/ -v`
- [x] `call_openai` đã triển khai và kiểm thử
- [x] `call_openai_mini` đã triển khai và kiểm thử
- [x] `compare_models` đã triển khai và kiểm thử
- [x] `streaming_chatbot` đã triển khai và kiểm thử
- [x] `retry_with_backoff` đã triển khai và kiểm thử
- [x] `batch_compare` đã triển khai và kiểm thử
- [x] `format_comparison_table` đã triển khai và kiểm thử
- [x] `exercises.md` đã điền đầy đủ
- [x] Sao chép bài làm vào folder `solution` và đặt tên theo quy định
