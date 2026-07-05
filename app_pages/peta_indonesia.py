import streamlit as st

from streamlit_folium import st_folium

from utils import (
    load_data,
    load_css,
    section_title,
    sidebar_filter,

    create_indonesia_map,

    prepare_map_data,
    get_top_provinces,
    get_map_kpi
)

load_css()

# =====================================================
# LOAD DATA
# =====================================================

df = load_data()

filtered_df, tahun, provinsi = sidebar_filter(df)

# =====================================================
# HEADER
# =====================================================

section_title("🗺️ Peta Persebaran Kendaraan Bermotor")

st.markdown(
"""
Visualisasi persebaran jumlah kendaraan bermotor
berdasarkan provinsi di Indonesia.
"""
)

st.divider()

# =====================================================
# KPI
# =====================================================

kpi = get_map_kpi(filtered_df)

c1, c2, c3 = st.columns(3)

c1.metric(
    "Total Kendaraan",
    f"{kpi['total']:,}"
)

c2.metric(
    "Jumlah Provinsi",
    kpi["provinsi"]
)

c3.metric(
    "Provinsi Tertinggi",
    kpi["tertinggi"]
)

st.divider()

# =====================================================
# MAP
# =====================================================

map_df = prepare_map_data(filtered_df)

if map_df.empty:
    st.warning(
        "Tidak ada data untuk kombinasi filter yang dipilih, "
        "sehingga peta tidak dapat ditampilkan."
    )
else:
    peta = create_indonesia_map(
        map_df,
        "assets/indonesia.geojson"
    )

    st_folium(
        peta,
        use_container_width=True,
        height=650,
        returned_objects=[],
    )

st.divider()

# =====================================================
# TOP 10
# =====================================================

section_title("🏆 Top 10 Provinsi")

ranking = get_top_provinces(filtered_df)

st.dataframe(
    ranking,
    use_container_width=True,
    hide_index=True
)