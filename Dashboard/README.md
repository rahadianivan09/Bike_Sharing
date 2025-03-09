Bike Sharing Dashboard

📌 Deskripsi Proyek

Dashboard ini dibuat menggunakan Streamlit untuk menganalisis dan menampilkan visualisasi dari dataset Bike Sharing. Dashboard ini mencakup berbagai analisis seperti pola penggunaan sepeda berdasarkan musim, cuaca, dan waktu.

📂 Struktur Folder

Bike-Sharing-Dashboard/
│── Dashboard/
│   ├── app.py              # File utama Streamlit
│   ├── day.csv             # Dataset harian
│   ├── hour.csv            # Dataset per jam
│   ├── requirements.txt    # Dependencies
│   ├── Readme.txt          # Dokumentasi tambahan
│── README.md               # Dokumentasi proyek

⚙️ Cara Menjalankan Dashboard

1️⃣ Install Dependensi

Pastikan Python sudah terinstall, lalu jalankan perintah berikut untuk menginstal semua dependencies:

pip install -r requirements.txt

2️⃣ Jalankan Aplikasi

Setelah dependensi terinstal, jalankan aplikasi Streamlit dengan perintah berikut:

streamlit run Dashboard/app.py

Akses dashboard di browser melalui alamat:

http://localhost:8501/

🚀 Deploy ke Streamlit Cloud

Untuk menjalankan di Streamlit Cloud:

Upload proyek ke GitHub

**Buka **Streamlit Cloud

Klik `` → Hubungkan ke repo GitHub

Isi pengaturan seperti berikut:

Repository: Bike-Sharing-Dashboard

Branch: main

File: Dashboard/app.py

**Klik **`` dan tunggu hingga aplikasi berjalan.

💡 Pastikan file day.csv dan hour.csv ada di dalam folder Dashboard sebelum menjalankan aplikasi.