import streamlit as st

from utils.data_loader import load_data
from utils.helper import load_css, section_title

# ==========================================================
# PAGE CONFIG
# ==========================================================

load_css()

df = load_data()

# ==========================================================
# HEADER
# ==========================================================

section_title("ℹ️ Tentang Dashboard")

st.markdown(
"""
Dashboard ini dikembangkan sebagai **Project Based Learning (PjBL)** pada mata kuliah **Visualisasi Data**.

Tujuan dashboard adalah membantu pengguna memahami perkembangan jumlah kendaraan bermotor di Indonesia melalui visualisasi data yang interaktif dan mudah dipahami.
"""
)

st.divider()

# ==========================================================
# INFORMASI DASHBOARD
# ==========================================================

section_title("📌 Informasi Dashboard")

col1, col2 = st.columns(2)

with col1:

    st.info(
        """
### Teknologi

- Python
- Streamlit
- Pandas
- Plotly
- CSS

Framework yang digunakan adalah Streamlit dengan visualisasi interaktif menggunakan Plotly.
"""
    )

with col2:

    st.success(
        f"""
### Dataset

Sumber Data:

**Badan Pusat Statistik (BPS)**

Periode:

**2023–2025**

Jumlah Provinsi:

**{df['Provinsi'].nunique()}**

Jumlah Record:

**{len(df)}**
"""
    )

st.divider()

# ==========================================================
# FITUR DASHBOARD
# ==========================================================

section_title("✨ Fitur Dashboard")

fitur = [
    "📊 Dashboard Interaktif",
    "📈 Analisis Pertumbuhan Kendaraan",
    "🏆 Ranking Provinsi",
    "📄 Dataset Viewer",
    "📥 Download Dataset CSV",
    "🔍 Filter Tahun dan Provinsi",
    "🤖 Executive Insight Otomatis"
]

for item in fitur:
    st.markdown(f"- {item}")

st.divider()

# ==========================================================
# PENGEMBANG
# ==========================================================

section_title("👨‍💻 Pengembang")

left, right = st.columns([1, 2])

with left:

    st.image(
        "assets/pengembang.jpg",
        width=180
    )

with right:

    st.markdown(
        """
### Muhammad Raka Aiko Pramudityo

Mahasiswa Semester 6 

Project Based Learning

Visualisasi Data

Universitas Teknologi Digital Indonesia

Dashboard ini dikembangkan sebagai media visualisasi data transportasi menggunakan Python dan Streamlit.
"""
    )

st.divider()

# ==========================================================
# STATISTIK PROJECT
# ==========================================================

section_title("📊 Statistik Project")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Halaman", "5")

with c2:
    st.metric("Visualisasi", "8+")

with c3:
    st.metric("Dataset", "3")

with c4:
    st.metric("Bahasa", "Python")

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.caption(
    "© 2026 Dashboard Transportasi Indonesia | Visualisasi Data Project"
)