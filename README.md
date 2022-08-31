Thử crawl data và clean data từ web: https://inxpress360.com/ma-buu-dien/

Bài toán được chia ra làm 3 bước:
-  Bước 1: Crawl data dạng bảng bằng pd.read_html. Kết quả thu được là các bảng dữ liệu từ các link riêng
-  Bước 2: Clean data - Chỉ giữ lại các hàng chứa tên quận, huyện, thành phố, phường, xã
-  Bước 3: Chuyển bảng về bảng có ô cột: province, district, ward và ward_code 
-  Bước 4: Kiểm tra và xử lý các ngoại lệ trong các bảng


