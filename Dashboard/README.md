# 🚴‍♂️ Bike Sharing Dashboard 🚴‍♀️  

📌 **Bike Sharing Dashboard** adalah aplikasi interaktif berbasis **Streamlit** yang menganalisis data peminjaman sepeda berdasarkan **musim, cuaca, tren harian, serta perbandingan hari kerja vs akhir pekan**.  

## 🎯 **Fitur Utama**  
✅ **Statistik Dasar** → Ringkasan statistik dataset peminjaman sepeda  
✅ **Pola Peminjaman Berdasarkan Musim** → Analisis jumlah peminjaman di setiap musim  
✅ **Hubungan Cuaca dengan Peminjaman** → Visualisasi hubungan suhu, kelembaban, dan kecepatan angin terhadap peminjaman  
✅ **Tren Peminjaman Harian** → Grafik tren peminjaman sepeda dari waktu ke waktu  
✅ **Perbandingan Peminjaman Hari Kerja vs Akhir Pekan** → Menganalisis pola peminjaman antara weekday dan weekend  
✅ **Filter Interaktif** → Memilih **musim & rentang tanggal** untuk melihat pola spesifik  

---  

## 📂 **Struktur Folder**  
```
📦 Bike_Sharing
 ┣ 📂 Dashboard
 ┃ ┣ 📜 app.py              # Kode utama aplikasi Streamlit
 ┃ ┣ 📜 day.csv             # Dataset peminjaman harian
 ┃ ┣ 📜 hour.csv            # Dataset peminjaman per jam
 ┃ ┣ 📜 requirements.txt    # Daftar dependensi Python
 ┃ ┗ 📜 README.md           # Dokumentasi proyek
```  

---  

## 📊 **Dataset**  
Dataset yang digunakan berasal dari sistem **Bike Sharing** dan memiliki dua file utama:  

### **1️⃣ day.csv** → **Peminjaman sepeda per hari**  
- **dteday** → Tanggal peminjaman  
- **season** → Musim (1: Spring, 2: Summer, 3: Fall, 4: Winter)  
- **cnt** → Jumlah total peminjaman  
- **temp** → Suhu rata-rata (dalam skala 0-1)  
- **humidity** → Kelembaban rata-rata  
- **windspeed** → Kecepatan angin rata-rata  

### **2️⃣ hour.csv** → **Peminjaman sepeda per jam**  
- **dteday** → Tanggal peminjaman  
- **hour** → Jam dalam sehari (0-23)  
- **workingday** → 1 jika hari kerja, 0 jika akhir pekan  
- **cnt** → Jumlah total peminjaman per jam  

---  

## 🚀 **Cara Menjalankan di Lokal**  
### **1️⃣ Pastikan Python & Streamlit Terinstal**  
Jalankan perintah berikut di terminal (Command Prompt / Terminal / Git Bash):  
```bash
pip install streamlit pandas matplotlib seaborn
```  

### **2️⃣ Jalankan Aplikasi**  
1. **Masuk ke folder proyek**  
   ```bash
   cd "C:\Users\ivanr\Documents\Laskar Ai\Tugas-1\Submission_Ivan_Bike_3rd\Dashboard"
   ```  
2. **Jalankan Streamlit**  
   ```bash
   streamlit run app.py
   ```  
3. **Buka browser** dan akses:  
   ```
   http://localhost:8501/
   ```  

---  

## 🚀 **Cara Deploy ke Streamlit Cloud**  
1. **Upload semua file ke GitHub (`Dashboard/app.py`, `Dashboard/day.csv`, `Dashboard/hour.csv`, `Dashboard/requirements.txt`, `Dashboard/README.md`).**  
2. **Buka [Streamlit Cloud](https://share.streamlit.io/)** → Login dengan GitHub.  
3. **Klik "New App" → Pilih repository GitHub-mu**.  
4. **Isi konfigurasi:**  
   - **Repository:** `rahadianivan09/Bike_Sharing`  
   - **Branch:** `main`  
   - **Path ke app:** `Dashboard/app.py`  
5. **Klik "Deploy" dan tunggu hingga proses selesai.** 🎉  

---  

## ⚠ **Troubleshooting**  
❌ **Dataset tidak ditemukan?**  
✔ Pastikan file `day.csv` & `hour.csv` ada di folder `Dashboard`.  

❌ **Error "ModuleNotFoundError: No module named 'streamlit'"?**  
✔ Instal Streamlit dengan:  
```bash
pip install streamlit
```  

❌ **Grafik tidak muncul setelah filter?**  
✔ Pastikan dataset tidak kosong setelah filter diterapkan.  

---  

## 📜 **Lisensi**  
Proyek ini dibuat untuk **pembelajaran dan analisis data**. Bebas digunakan dengan menyebutkan sumber. 🚀  

---  

### 🎉 **README.md sudah siap!**  
Sekarang tinggal **upload ke GitHub**. Kalau ada tambahan, kasih tahu ya! 🚀😊

