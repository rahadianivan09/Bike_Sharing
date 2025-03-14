import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import os

# 🔹 Coba baca dataset dari folder Dashboard
data_path = "Dashboard/"  # Sesuaikan dengan struktur di GitHub

if os.path.exists(data_path + "day.csv") and os.path.exists(data_path + "hour.csv"):
    df_day = pd.read_csv(data_path + "day.csv")
    df_hour = pd.read_csv(data_path + "hour.csv")
    st.success("✅ Dataset berhasil dimuat dari file lokal di repository!")
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
df_hour["dteday"] = pd.to_datetime(df_hour["dteday"])

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

# 🔹 Terapkan filter musim & tanggal pada df_day
filtered_data = df_day.copy()
if selected_season != "All":
    filtered_data = filtered_data[filtered_data["season_label"] == selected_season]

filtered_data = filtered_data[(filtered_data["dteday"] >= pd.to_datetime(start_date)) & 
                              (filtered_data["dteday"] <= pd.to_datetime(end_date))]

# 🔹 Terapkan filter musim & tanggal pada df_hour
df_filtered_hour = df_hour.merge(filtered_data[["dteday", "season_label"]], on="dteday", how="inner")
if selected_season != "All":
    df_filtered_hour = df_filtered_hour[df_filtered_hour["season_label"] == selected_season]

# 🔹 Menampilkan statistik dasar
st.subheader(f"📊 Statistik Data untuk Musim {selected_season} dari {start_date} hingga {end_date}")
st.write(filtered_data.describe())

# 🔹 Pola peminjaman berdasarkan musim
st.subheader("📌 Pola Peminjaman Sepeda Berdasarkan Musim")
df_season = filtered_data.groupby("season_label")["count"].sum().reset_index()
df_season = df_season.sort_values(by="count", ascending=False)

fig, ax = plt.subplots()
sns.barplot(x="season_label", y="count", data=df_season, estimator=sum, palette="viridis", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Total Peminjaman")
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{int(x):,}"))
st.pyplot(fig)

# 🔹 Perbandingan peminjaman pada Hari Kerja vs Akhir Pekan (SESUAI FILTER)
st.subheader("🏢 Peminjaman Sepeda pada Hari Kerja vs Akhir Pekan")
df_filtered_hour["workingday_label"] = df_filtered_hour["workingday"].map({0: "Akhir Pekan", 1: "Hari Kerja"})

fig, ax = plt.subplots()
sns.barplot(x="workingday_label", y="count", data=df
