
import streamlit as st

# Pengaturan halaman
st.set_page_config(
    page_title="Kalkulator Upcycle",
    page_icon="♻️",
    layout="centered"
)

# Judul aplikasi
st.title("♻️ Kalkulator Produksi Upcycle")
st.write("Hitung kebutuhan dan biaya produksi gantungan kunci dari tutup botol bekas.")
st.divider()

# Bagian input
st.subheader("Masukkan Data Produksi")

jumlah = st.number_input(
    "Target jumlah gantungan kunci",
    min_value=1,
    max_value=500,
    value=20,
    step=1
)

desain = st.selectbox(
    "Pilih desain gantungan kunci",
    ["Minimalis (1 tutup botol)", "Layered (2 tutup botol)"]
)

biaya = st.number_input(
    "Biaya bahan tambahan per gantungan (Rp)",
    min_value=0,
    value=2000,
    step=500
)

anggaran = st.number_input(
    "Total anggaran tersedia (Rp)",
    min_value=0,
    value=50000,
    step=5000
)

# Fungsi buatan sendiri
def hitung_produksi(jumlah, tutup_per_produk, biaya_per_produk):
    total_tutup = jumlah * tutup_per_produk
    total_biaya = jumlah * biaya_per_produk

    return total_tutup, total_biaya

# Menentukan kebutuhan tutup botol
if desain == "Minimalis (1 tutup botol)":
    kebutuhan = 1
else:
    kebutuhan = 2

# Menghitung hasil
total_tutup, total_biaya = hitung_produksi(
    jumlah, kebutuhan, biaya
)

st.divider()

# Menampilkan hasil
st.subheader("Hasil Perhitungan")

kolom1, kolom2 = st.columns(2)

with kolom1:
    st.metric("Kebutuhan Tutup Botol", f"{total_tutup} buah")

with kolom2:
    st.metric(
        "Total Biaya Produksi",
        f"Rp{total_biaya:,.0f}".replace(",", ".")
    )

# Logika kondisi anggaran
st.subheader("Status Anggaran")

if anggaran >= total_biaya:
    sisa = anggaran - total_biaya
    st.success(
        f"Anggaran mencukupi! Sisa anggaran Rp{sisa:,.0f}."
        .replace(",", ".")
    )
else:
    kurang = total_biaya - anggaran
    st.warning(
        f"Anggaran belum mencukupi. "
        f"Kekurangan Rp{kurang:,.0f}."
        .replace(",", ".")
    )

st.divider()

st.caption(
    "Kalkulator Upcycle | Kreatif, Hemat, dan Ramah Lingkungan"
)
