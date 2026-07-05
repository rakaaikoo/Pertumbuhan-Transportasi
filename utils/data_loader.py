import os
import pandas as pd
import streamlit as st

from utils.province_mapper import PROVINCE_MAPPING
from utils.province_code import PROVINCE_CODE

# ==========================================
# LOKASI DATASET
# ==========================================

DATA_FOLDER = "data"

FILES = {
    2023: "kendaraan_2023.csv",
    2024: "kendaraan_2024.csv",
    2025: "kendaraan_2025.csv"
}


# ==========================================
# MEMBERSIHKAN NAMA KOLOM
# ==========================================

def clean_columns(df):
    df.columns = (
        df.columns
        .str.replace("\n", " ", regex=False)
        .str.replace("  ", " ", regex=False)
        .str.strip()
    )

    df = df.rename(columns={
        "Jumlah Kendaraan Bermotor - Mobil Penumpang": "Mobil",
        "Jumlah Kendaraan Bermotor - Bus": "Bus",
        "Jumlah Kendaraan Bermotor - Truk": "Truk",
        "Jumlah Kendaraan Bermotor - Sepeda Motor": "Motor",
        "Jumlah Kendaraan Bermotor - Jumlah": "Total"
    })

    return df


# ==========================================
# LOAD DATA
# ==========================================

@st.cache_data
def load_data():

    dataframes = []

    for tahun, file in FILES.items():

        path = os.path.join(DATA_FOLDER, file)

        if not os.path.exists(path):
            st.error(f"File tidak ditemukan: {path}")
            continue

        # Separator menggunakan titik koma
        df = pd.read_csv(path, sep=";")

        df = clean_columns(df)

        df["Tahun"] = tahun

        numeric_columns = [
            "Mobil",
            "Bus",
            "Truk",
            "Motor",
            "Total"
        ]

        for col in numeric_columns:

            df[col] = (
                df[col]
                .astype(str)
                # BPS menambahkan catatan kaki seperti " (*)" pada
                # sebagian data (mis. dataset 2025) - buang semua
                # karakter selain digit agar parsing angka konsisten
                .str.replace(r"[^\d]", "", regex=True)
            )

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            ).fillna(0)

        dataframes.append(df)

    data = pd.concat(
        dataframes,
        ignore_index=True
    )

    # Membuang baris kosong/footer (mis. baris catatan kaki BPS
    # yang ikut terbaca tanpa nama provinsi)
    data = data.dropna(subset=["Provinsi"])
    data = data[data["Provinsi"].astype(str).str.strip() != ""]

    # Membersihkan nama provinsi (termasuk newline yang terbawa dari Excel)
    data["Provinsi"] = (
        data["Provinsi"]
        .astype(str)
        .str.replace("\n", " ", regex=False)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
        .str.upper()
    )

    # Menyesuaikan nama provinsi dengan GeoJSON
    data["Provinsi"] = data["Provinsi"].replace(PROVINCE_MAPPING)

    # Tambahkan kode provinsi
    data["KODE_PROV"] = data["Provinsi"].map(PROVINCE_CODE)

    return data