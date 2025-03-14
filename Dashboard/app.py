import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import os

# 🔹 Cek folder kerja di Streamlit Cloud
st.write("📂 Path saat ini:", os.getcwd())  # Menampilkan path kerja
st.write("📂 Daftar file di folder ini:", os.listdir())  # Menampilkan semua file

# 🔹 Coba baca dataset dari lokal dulu
data_path = "Dashboard/"  # Sesuaikan jika Streamlit berjalan dari root repo

if os.path.exists(data_path + "day.csv") and os.path.exists(data_path + "hour.csv"):
    df_day = pd.read_csv(data_path + "day.csv")
    df_hour = pd.read_csv(data_path + "hour.csv")
    st.success("✅ Dataset berhasil dimuat dari file lokal!")
else:
    # Jika tidak ditemukan, baca dari GitHub
    GITHUB_RAW_URL = "https://raw.githubusercontent.com/rahadianivan09/Bike_Sharing/main/Dashboard/"
    try:
        df_day = pd.read_csv(GITHUB_RAW_URL + "day.csv")
        df_hour = pd.read_csv(GITHUB_RAW_URL + "hour.csv")
        st.success("✅ Dataset berhasil dimuat dari GitHub!")
    except Exception as e:
        st.error("❌ Dataset tidak ditemukan! Pastikan file `day.csv` dan `hour.csv` ada.")
        st.error(f"Error: {e}")
        st.stop()

# 🔹 Pastikan kolom "count" ada (rename jika perlu)
df_day.rename(columns={"cnt": "count", "hum": "humidity", "windspeed": "windspeed"}, inplace=True)
df_hour.rename(columns={"cnt": "count"}, inplace=True)

# 🔹 Ubah kolom tanggal ke format datetime
df_day["dteday"] = pd.to_datetime(df_day["dteday"])

# 🔹 Sidebar untuk filter
st.sidebar.header("Filter Data")

# 🔹 Mapping angka musim ke nama musim
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df_day["season_label"] = df_day["season"].map(season_mapping)

# 🔹 Pilihan dropdown dengan opsi "All"
season_options = ["All"] + list(df_day["season_label"].unique())
selected_season = st.sidebar.selectbox("Pilih Musim", season_options)

# 🔹 Tambahkan filter berdasarkan rentang tanggal
min_date = df_day["dteday"].min()
max_date = df_day["dteday"].max()
start_date, end_date = st.sidebar.date_input("Pilih Rentang Tanggal", [min_date, max_date])

# 🔹 Terapkan filter musim & tanggal
filtered_data = df_day.copy()
if selected_season != "All":
    filtered_data = filtered_data[filtered_data["season_label"] == selected_season]

filtered_data = filtered_data[(filtered_data["dteday"] >= pd.to_datetime(start_date)) & 
                              (filtered_data["dteday"] <= pd.to_datetime(end_date))]

# 🔹 Menampilkan statistik dasar
st.subheader(f"Statistik Dasar untuk Musim {selected_season} dari {start_date} hingga {end_date}")
st.write(filtered_data.describe())

# 1️⃣ Pola peminjaman berdasarkan musim
st.subheader("Pola Peminjaman Sepeda Berdasarkan Musim")
df_season = filtered_data.groupby("season_label")["count"].sum().reset_index()
df_season = df_season.sort_values(by="count", ascending=False)

fig, ax = plt.subplots()
sns.barplot(x="season_label", y="count", data=df_season, estimator=sum, palette="viridis", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman")
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
st.pyplot(fig)

# 2️⃣ Hubungan faktor cuaca dengan jumlah peminjaman
st.subheader("Hubungan Faktor Cuaca dengan Peminjaman Sepeda")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.scatterplot(x="temp", y="count", data=filtered_data, ax=axes[0], alpha=0.5)
axes[0].set_title("Suhu vs Peminjaman")
sns.scatterplot(x="humidity", y="count", data=filtered_data, ax=axes[1], alpha=0.5, color="orange")
axes[1].set_title("Kelembaban vs Peminjaman")
sns.scatterplot(x="windspeed", y="count", data=filtered_data, ax=axes[2], alpha=0.5, color="green")
axes[2].set_title("Kecepatan Angin vs Peminjaman")
st.pyplot(fig)

# 3️⃣ Tren peminjaman harian
st.subheader("Tren Peminjaman Sepanjang Waktu")
fig, ax = plt.subplots(figsize=(14, 5))
sns.lineplot(x="dteday", y="count", data=filtered_data, color="blue", ax=ax)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman")
st.pyplot(fig)

# 4️⃣ Perbandingan peminjaman pada hari kerja vs akhir pekan
st.subheader("Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
df_hour["workingday_label"] = df_hour["workingday"].map({0: "Akhir Pekan", 1: "Hari Kerja"})
fig, ax = plt.subplots()
sns.barplot(x="workingday_label", y="count", data=df_hour, estimator=sum, palette="coolwarm", ax=ax)
ax.set_xlabel("Kategori Hari")
ax.set_ylabel("Total Peminjaman")
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
st.pyplot(fig)

st.write("✅ **Dashboard ini dibuat menggunakan Streamlit** 🚀")
