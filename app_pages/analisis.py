import streamlit as st

from utils import (
    load_data,
    load_css,
    sidebar_filter,
    section_title,
    format_number,

    get_statistics,
    get_growth,
    get_ranking,
    get_vehicle_composition,
    get_top_provinces,

    create_line_chart,
    create_bar_chart,
    create_pie_chart,
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

load_css()

# ==========================================================
# LOAD DATA
# ==========================================================

df = load_data()

filtered_df, tahun, provinsi = sidebar_filter(df)

# ==========================================================
# HEADER
# ==========================================================

section_title("📈 Analisis Data Kendaraan Bermotor")

st.markdown(
"""
Halaman ini menyajikan analisis deskriptif terhadap data kendaraan
bermotor berdasarkan provinsi dan tahun yang dipilih.
"""
)

st.divider()

# ==========================================================
# STATISTIK DESKRIPTIF
# ==========================================================

section_title("📊 Statistik Deskriptif")

stats = get_statistics(filtered_df)

st.dataframe(
    stats,
    use_container_width=True,
)

st.divider()

# ==========================================================
# TOP 10 PROVINSI
# ==========================================================

section_title("🏆 Top 10 Provinsi")

top10 = get_top_provinces(filtered_df)

fig = create_bar_chart(
    top10,
    x="Provinsi",
    y="Total",
    title="Top 10 Provinsi dengan Kendaraan Terbanyak",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.divider()

# ==========================================================
# KOMPOSISI KENDARAAN
# ==========================================================

section_title("🚗 Komposisi Kendaraan")

composition = get_vehicle_composition(filtered_df)

pie = create_pie_chart(
    composition,
    names="Jenis Kendaraan",
    values="Jumlah",
    title="Komposisi Kendaraan Bermotor",
)

st.plotly_chart(
    pie,
    use_container_width=True,
)

st.divider()

# ==========================================================
# PERTUMBUHAN NASIONAL
# ==========================================================

section_title("📈 Pertumbuhan Kendaraan Nasional")

growth = get_growth(df)

if not growth.empty:

    line = create_line_chart(
        growth,
        x="Tahun",
        y="Total",
        title="Pertumbuhan Kendaraan Nasional",
    )

    st.plotly_chart(
        line,
        use_container_width=True,
    )

    growth_display = growth.copy()

    growth_display["Total"] = growth_display["Total"].apply(format_number)

    if "Growth (%)" in growth_display.columns:
        growth_display["Growth (%)"] = (
            growth_display["Growth (%)"]
            .fillna(0)
            .round(2)
        )

    st.dataframe(
        growth_display,
        use_container_width=True,
        hide_index=True,
    )

else:

    st.warning(
        "Dataset hanya memiliki satu tahun sehingga pertumbuhan belum dapat dihitung."
    )

st.divider()

# ==========================================================
# RANKING
# ==========================================================

section_title("🥇 Ranking Provinsi")

ranking = get_ranking(filtered_df)

ranking_display = ranking.copy()

for col in ["Mobil", "Bus", "Truk", "Motor", "Total"]:
    ranking_display[col] = ranking_display[col].apply(format_number)

st.dataframe(
    ranking_display,
    use_container_width=True,
    hide_index=True,
)

st.divider()

# ==========================================================
# INTERPRETASI
# ==========================================================

section_title("📝 Interpretasi Hasil")

top = ranking.iloc[0]
bottom = ranking.iloc[-1]

st.success(
f"""
### Kesimpulan Analisis

• Provinsi dengan jumlah kendaraan terbanyak adalah **{top['Provinsi']}**
sebanyak **{format_number(top['Total'])} kendaraan**.

• Provinsi dengan jumlah kendaraan paling sedikit adalah
**{bottom['Provinsi']}**
sebanyak **{format_number(bottom['Total'])} kendaraan**.

• Berdasarkan komposisi kendaraan,
**sepeda motor merupakan jenis kendaraan yang paling dominan**
dibandingkan mobil, bus maupun truk.

• Perbedaan jumlah kendaraan antar provinsi dipengaruhi oleh
jumlah penduduk, aktivitas ekonomi, tingkat urbanisasi,
dan perkembangan infrastruktur transportasi.
"""
)

st.divider()

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

section_title("📌 Executive Summary")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Provinsi Tertinggi",
        top["Provinsi"],
        format_number(top["Total"]),
    )

with c2:

    st.metric(
        "Provinsi Terendah",
        bottom["Provinsi"],
        format_number(bottom["Total"]),
    )

with c3:

    st.metric(
        "Jumlah Provinsi",
        filtered_df["Provinsi"].nunique(),
    )

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.caption(
    "Dashboard Transportasi Indonesia • Halaman Analisis"
)