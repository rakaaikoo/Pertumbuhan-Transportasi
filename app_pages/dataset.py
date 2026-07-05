import streamlit as st
import pandas as pd

from utils.data_loader import load_data
from utils.helper import load_css, section_title
from utils.formatter import format_number

from utils.charts import (
    create_distribution_chart,
    create_missing_chart,
    create_profile_chart
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

load_css()

# ==========================================================
# LOAD DATA
# ==========================================================

df = load_data()

# ==========================================================
# HEADER
# ==========================================================

section_title("📄 Dataset Kendaraan Bermotor")

st.markdown("""
Halaman ini menampilkan dataset yang digunakan
dalam dashboard beserta informasi kualitas data.
""")

st.divider()

# ==========================================================
# FILTER
# ==========================================================

col1, col2 = st.columns(2)

with col1:

    tahun = st.selectbox(
        "📅 Pilih Tahun",
        sorted(df["Tahun"].unique())
    )

with col2:

    keyword = st.text_input(
        "🔍 Cari Provinsi",
        placeholder="Misalnya: Jawa Barat"
    )

dataset = df[df["Tahun"] == tahun].copy()

if keyword:

    dataset = dataset[
        dataset["Provinsi"].str.contains(
            keyword,
            case=False,
            na=False
        )
    ]

# ==========================================================
# PROFIL DATASET
# ==========================================================

section_title("📊 Profil Dataset")

left, right = st.columns([1, 2])

with left:

    st.plotly_chart(
        create_profile_chart(dataset),
        use_container_width=True
    )

with right:

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Record",
            format_number(len(dataset))
        )

    with c2:
        st.metric(
            "Kolom",
            len(dataset.columns)
        )

    with c3:
        st.metric(
            "Provinsi",
            dataset["Provinsi"].nunique()
        )

    with c4:
        st.metric(
            "Missing",
            dataset.isnull().sum().sum()
        )
st.divider()

# ==========================================================
# DATA TABLE
# ==========================================================

section_title("📋 Data Kendaraan")

st.dataframe(
    dataset,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# DATA QUALITY
# ==========================================================

section_title("🧹 Kualitas Data")

quality = pd.DataFrame({

    "Kolom": dataset.columns,

    "Tipe Data": dataset.dtypes.astype(str).values,

    "Missing Value": dataset.isnull().sum().values,

    "Unique": dataset.nunique().values

})

st.dataframe(

    quality,

    use_container_width=True,

    hide_index=True

)
st.markdown("")

section_title("📉 Visualisasi Missing Value")

st.plotly_chart(
    create_missing_chart(dataset),
    use_container_width=True
)

st.divider()

# ==========================================================
# DESKRIPSI
# ==========================================================

section_title("📈 Statistik Deskriptif")

st.dataframe(

    dataset.describe(),

    use_container_width=True

)

st.divider()

# ==========================================================
# DISTRIBUSI
# ==========================================================

section_title("🚗 Distribusi Kendaraan")

vehicle = pd.DataFrame({

    "Jenis Kendaraan": [

        "Mobil",
        "Bus",
        "Truk",
        "Motor"

    ],

    "Jumlah": [

        dataset["Mobil"].sum(),

        dataset["Bus"].sum(),

        dataset["Truk"].sum(),

        dataset["Motor"].sum()

    ]

})

st.plotly_chart(
    create_distribution_chart(vehicle),
    use_container_width=True
)

st.divider()

# ==========================================================
# DOWNLOAD
# ==========================================================

section_title("⬇ Download Dataset")

csv = dataset.to_csv(
    index=False
).encode("utf-8")

st.download_button(

    "📥 Download CSV",

    csv,

    file_name=f"dataset_transportasi_{tahun}.csv",

    mime="text/csv"

)

st.divider()

# ==========================================================
# INFORMATION
# ==========================================================

section_title("ℹ Informasi Dataset")

st.info(f"""

Dataset berasal dari **Badan Pusat Statistik (BPS)**

Periode Data :

**2023–2025**

Jumlah Record :

**{format_number(len(df))}**

Jumlah Kolom :

**{len(df.columns)}**

Jumlah Provinsi :

**{df['Provinsi'].nunique()}**

""")

st.caption(
    "Dataset • Dashboard Transportasi Indonesia"
)