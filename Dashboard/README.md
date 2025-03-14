# 🚴‍♂️ Bike Sharing Dashboard

Dashboard interaktif untuk menganalisis pola peminjaman sepeda

## 📌 Fitur Utama
✅ **Filter Interaktif**  
- **Filter Musim** → Bisa pilih musim tertentu atau **"All"** untuk melihat semua musim.  
- **Filter Rentang Tanggal** → Bisa memilih periode waktu tertentu untuk analisis.  

✅ **Visualisasi Data**  
- **Pola peminjaman sepeda berdasarkan musim**  
- **Hubungan faktor cuaca dengan jumlah peminjaman**  
- **Tren peminjaman sepanjang waktu**  
- **Perbandingan peminjaman pada hari kerja vs akhir pekan**  

## 📂 Dataset yang Digunakan
- `day.csv` → Data peminjaman per hari.  
- `hour.csv` → Data peminjaman per jam.  

## 🚀 Cara Menjalankan di Lokal
1. **Pastikan memiliki Python & Streamlit**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Pastikan dataset ada di folder yang sama dengan `app.py`**  
   ```
   ├── app.py
   ├── day.csv
   ├── hour.csv
   ├── requirements.txt
   ├── README.md
   ```

3. **Jalankan Streamlit**  
   ```bash
   streamlit run app.py
   ```

4. **Buka browser di URL berikut:**  
   ```
   http://localhost:8501/
   ```

## 🌐 Deploy ke Streamlit Cloud
1. **Upload file ke GitHub**  
2. **Buka Streamlit Cloud** → https://share.streamlit.io/  
3. **Deploy aplikasi dengan repository GitHub**  

## 🛠 Dependencies
Lihat `requirements.txt` untuk library yang digunakan.

