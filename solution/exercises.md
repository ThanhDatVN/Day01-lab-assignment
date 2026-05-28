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

| Temperature | Latency | Tokens | Tóm tắt phản hồi |
|-------------|---------|--------|-------------------|
| 0.0 | 3.93s | 153 | Hang Sơn Đoòng, phát hiện 1991, công nhận 2009, dài hơn 5 km, cao 200 m, rộng 150 m, chứa được tòa nhà 40 tầng |
| 0.5 | 2.89s | 176 | Hang Sơn Đoòng, phát hiện 1991 bởi Hồ Khanh, khám phá bởi nhà thám hiểm Anh 2009, dài hơn 5 km, cao 200 m, rộng 150 m |
| 1.0 | 2.88s | 173 | Hang Sơn Đoòng, khám phá 2009 bởi Howard Limbert, dài khoảng 9 km, cao 200 m, rộng 150 m |
| 1.5 | 3.51s | 186 | Hang Sơn Đoòng, phát hiện 1991 bởi Hồ Khanh, khám phá 2009 bởi nhà thám hiểm Anh, dài hơn 5 km, cao 200 m, rộng 150 m |

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Cả bốn mức temperature đều chọn cùng chủ đề hang Sơn Đoòng, nhưng cách diễn đạt và chi tiết thay đổi rõ rệt khi temperature tăng. Ở temperature 0.0 và 0.5, phản hồi gần như giống hệt nhau về cấu trúc và số liệu (chiều dài hang đều ghi "hơn 5 km"), cho thấy model rất ổn định. Khi tăng lên 1.0, model bắt đầu đưa ra chi tiết khác biệt — đề cập tên trưởng đoàn Howard Limbert và ghi chiều dài hang là 9 km thay vì 5 km — cho thấy temperature cao khiến model "sáng tạo" hơn nhưng đồng thời có thể đưa ra thông tin kém nhất quán.

**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tôi sẽ đặt temperature từ 0.0 đến 0.3. Từ kết quả thí nghiệm, ở temperature 0.0 và 0.5 phản hồi rất nhất quán — cùng số liệu, cùng cấu trúc. Trong khi đó ở temperature 1.0, model đưa ra con số khác nhau cho cùng một sự thật (5 km vs 9 km). Chatbot hỗ trợ khách hàng cần đảm bảo thông tin về sản phẩm, chính sách luôn chính xác và nhất quán giữa các lần trả lời, nên temperature thấp là lựa chọn an toàn nhất.

---

### Bài tập 2.2 — Đánh Đổi Chi Phí
Xem xét kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người thực hiện 3 lần gọi API, mỗi lần trung bình ~350 token.

**Ước tính xem GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này:**
> **Tính toán chi tiết:**
> - Tổng token output mỗi ngày: 10.000 người × 3 lần × 350 token = 10.500.000 token = 10.500 × 1K token
> - Chi phí GPT-4o mỗi ngày: 10.500 × $0.010 = **$105.00/ngày**
> - Chi phí GPT-4o-mini mỗi ngày: 10.500 × $0.0006 = **$6.30/ngày**
> - Tỉ lệ: $105.00 ÷ $6.30 = **16.67 lần**
> - Theo tháng (30 ngày): GPT-4o tốn $3.150 vs GPT-4o-mini tốn $189, chênh lệch $2.961/tháng
>
> **Kết luận:** GPT-4o đắt hơn GPT-4o-mini khoảng **16.67 lần** cho workload này.

**Mô tả một trường hợp mà chi phí cao hơn của GPT-4o là xứng đáng, và một trường hợp GPT-4o-mini là lựa chọn tốt hơn:**
> **GPT-4o xứng đáng:** Phân tích hợp đồng pháp lý hoặc tư vấn y khoa — nơi một câu trả lời sai có thể gây hậu quả nghiêm trọng. Chi phí thiệt hại từ sai sót (kiện tụng, chẩn đoán sai) vượt xa chi phí API. Từ kết quả so sánh thực tế, GPT-4o cũng cho phản hồi chi tiết hơn (165 token, đề cập thạch nhũ, sông ngầm, khu rừng bên trong hang).
>
> **GPT-4o-mini là lựa chọn tốt hơn:** Trả lời FAQ, phân loại email, tóm tắt nội dung ngắn với khối lượng lớn. Từ kết quả thực tế, GPT-4o-mini vẫn cho câu trả lời chất lượng tốt (129 token, nội dung chính xác về bờ biển và đảo Việt Nam) với latency tương đương (2.69s vs 2.67s) nhưng tiết kiệm được gần 94% chi phí.

---

### Bài tập 2.3 — Trải Nghiệm Người Dùng với Streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming đặc biệt quan trọng trong các ứng dụng chatbot tương tác trực tiếp với người dùng, đặc biệt khi phản hồi dài. Từ kết quả thí nghiệm thực tế, mỗi lần gọi GPT-4o mất khoảng 2.67–3.93 giây để sinh 153–186 token — nếu không dùng streaming, người dùng phải nhìn màn hình trống suốt gần 4 giây mà không biết ứng dụng có đang hoạt động hay không, tạo cảm giác bị treo. Với streaming, token đầu tiên xuất hiện gần như ngay lập tức, người dùng bắt đầu đọc trong khi model vẫn đang sinh tiếp, tạo trải nghiệm mượt mà giống như đang trò chuyện thật. Ngược lại, non-streaming phù hợp hơn trong các trường hợp: (1) khi cần xử lý toàn bộ phản hồi trước khi hiển thị — ví dụ trích xuất dữ liệu JSON có cấu trúc để parse; (2) khi phản hồi được dùng làm đầu vào cho bước xử lý tiếp theo trong pipeline tự động; (3) khi phản hồi rất ngắn (vài token) nên sự khác biệt về thời gian chờ không đáng kể.


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
