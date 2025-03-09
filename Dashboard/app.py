import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import os

# Cek direktori kerja saat ini
current_dir = os.getcwd()
st.write(f" Direktori saat ini: {current_dir}")

# Cek isi folder Dashboard
dashboard_path = os.path.join(current_dir, "Dashboard")
st.write(f" Isi folder Dashboard: {os.listdir(dashboard_path) if os.path.exists(dashboard_path) else 'Folder tidak ditemukan'}")

# Tentukan path file
file_day = os.path.join(current_dir, "Dashboard", "day.csv")
file_hour = os.path.join(current_dir, "Dashboard", "hour.csv")

# Debugging apakah file ada
# st.write(f"📄 Path day.csv: {file_day}")
# st.write(f"📄 Path hour.csv: {file_hour}")
# st.write(f"✅ File day.csv ada? {os.path.exists(file_day)}")
# st.write(f"✅ File hour.csv ada? {os.path.exists(file_hour)}")

# Load dataset jika file ada
if os.path.exists(file_day) and os.path.exists(file_hour):
    df_day = pd.read_csv(file_day)
    df_hour = pd.read_csv(file_hour)
else:
    st.error(" File dataset tidak ditemukan! Pastikan 'day.csv' dan 'hour.csv' ada di dalam folder 'Dashboard'.")
    st.stop()  # Hentikan eksekusi jika file tidak ada
  
# Pastikan kolom "count" ada (rename jika perlu)
df_day.rename(columns={"cnt": "count", "hum": "humidity", "windspeed": "windspeed"}, inplace=True)
df_hour.rename(columns={"cnt": "count"}, inplace=True)

# 🔹 Sidebar untuk filter
st.sidebar.header("Filter Data")

# 🔹 Mapping angka musim ke nama musim
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df_day["season_label"] = df_day["season"].map(season_mapping)

# 🔹 Pilihan dropdown menggunakan label musim
selected_season = st.sidebar.selectbox("Pilih Musim", df_day["season_label"].unique())

# 🔹 Filter data berdasarkan musim yang dipilih
filtered_data = df_day[df_day["season_label"] == selected_season]

# 🔹 Menampilkan statistik dasar
st.subheader(f"Statistik Dasar untuk Musim {selected_season}")
st.write(filtered_data.describe())

# 1️⃣ Pola peminjaman berdasarkan musim
st.subheader("Pola Peminjaman Sepeda Berdasarkan Musim")
df_season = df_day.groupby("season_label")["count"].sum().reset_index()
df_season = df_season.sort_values(by="count", ascending=False)  # Urutkan berdasarkan jumlah peminjaman

# 🔹 Visualisasi dengan label musim
fig, ax = plt.subplots()
sns.barplot(x="season_label", y="count", data=df_season, estimator=sum, palette="viridis", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman")
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
st.pyplot(fig)

# 2️⃣ Hubungan faktor cuaca dengan jumlah peminjaman
st.subheader("Hubungan Faktor Cuaca dengan Peminjaman Sepeda")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.scatterplot(x="temp", y="count", data=df_day, ax=axes[0], alpha=0.5)
axes[0].set_title("Suhu vs Peminjaman")
sns.scatterplot(x="humidity", y="count", data=df_day, ax=axes[1], alpha=0.5, color="orange")
axes[1].set_title("Kelembaban vs Peminjaman")
sns.scatterplot(x="windspeed", y="count", data=df_day, ax=axes[2], alpha=0.5, color="green")
axes[2].set_title("Kecepatan Angin vs Peminjaman")
st.pyplot(fig)

# 3️⃣ Tren peminjaman harian
st.subheader("Tren Peminjaman Sepanjang Waktu")
df_day["dteday"] = pd.to_datetime(df_day["dteday"])
fig, ax = plt.subplots(figsize=(14, 5))
sns.lineplot(x="dteday", y="count", data=df_day, color="blue", ax=ax)
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

st.write("Dashboard ini dibuat menggunakan Streamlit")

