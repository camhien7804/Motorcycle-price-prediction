🏍️ Motorcycle Price Prediction

📌 Giới thiệu

Dự án **Motorcycle Price Prediction** xây dựng một hệ thống dự đoán giá xe máy dựa trên dữ liệu thực tế được crawl từ web.
Pipeline bao gồm: **thu thập dữ liệu → làm sạch → phân tích khám phá (EDA) → huấn luyện mô hình ML → triển khai ứng dụng web**.

---
⚙️ Chức năng chính

 📊 **Data Pipeline**: Crawl dữ liệu xe máy, làm sạch & chuẩn hóa.
 🔍 **EDA**: Phân tích dữ liệu để tìm ra các yếu tố ảnh hưởng đến giá (hãng, năm, số km, tình trạng).
 🤖 **Machine Learning**: So sánh nhiều mô hình (**SGD, Random Forest, XGBoost**) và chọn mô hình tốt nhất.
 🌐 **Web App**: Giao diện cho phép nhập thông tin xe và nhận ngay giá dự đoán.

---

 🛠️ Công nghệ sử dụng

 **Ngôn ngữ:** Python
 **Thư viện chính:** Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn
 **Triển khai mô hình:** Pickle
 **Ứng dụng web:** Flask/Streamlit (tuỳ file app triển khai)

---

📂 Cấu trúc thư mục

🚀 Cách chạy project

1️⃣ Clone repo
git clone https://github.com/camhien7804/Motorcycle-price-prediction.git
cd Motorcycle-price-prediction

2️⃣ Cài đặt dependencies
pip install -r requirements.txt


3️⃣ Chạy app dự đoán
python app/app.py


---

📊 Kết quả nổi bật

* Pipeline xử lý dữ liệu **tự động & chuẩn hóa** từ dữ liệu thô.
* Huấn luyện mô hình với **XGBoost**, đạt sai số MSE thấp.
* Ứng dụng web cho phép **dự đoán giá xe máy tức thì** dựa trên các thuộc tính đầu vào.

---

👨‍💻 Tác giả

* **Nguyen Cam Hien**
  📧 Email: [camhien708@gmail.com](mailto:camhien708@gmail.com)
  🌐 GitHub: [camhien7804](https://github.com/camhien7804)

---

👉 Bạn có muốn mình tạo luôn file **requirements.txt** (danh sách thư viện cần thiết) để người khác có thể chạy project dễ dàng không?
