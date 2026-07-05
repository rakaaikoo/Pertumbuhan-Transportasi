import streamlit as st

from utils import (
    load_data,
    load_css,
    sidebar_filter,
    section_title,
    format_number,

    get_kpi,
    get_top_provinces,
    get_vehicle_composition,
    get_ranking,
    get_growth,

    create_bar_chart,
    create_pie_chart,
    create_line_chart,
    create_scatter_chart,
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
# KPI
# ==========================================================

kpi = get_kpi(filtered_df)

# ==========================================================
# HEADER
# ==========================================================

section_title("📊 Dashboard Transportasi Indonesia")

st.markdown(
"""
Dashboard ini menyajikan visualisasi interaktif jumlah kendaraan bermotor
berdasarkan provinsi dan tahun yang dipilih.
"""
)

st.divider()

# ==========================================================
# KPI CARD
# ==========================================================

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "🚗 Total Kendaraan",
    format_number(kpi["total"])
)

c2.metric(
    "🚙 Mobil",
    format_number(kpi["mobil"])
)

c3.metric(
    "🚌 Bus",
    format_number(kpi["bus"])
)

c4.metric(
    "🚚 Truk",
    format_number(kpi["truk"])
)

c5.metric(
    "🛵 Motor",
    format_number(kpi["motor"])
)

st.divider()

# ==========================================================
# TOP 10 & PIE
# ==========================================================

left, right = st.columns([2, 1])

with left:

    section_title("🏆 Top 10 Provinsi")

    top10 = get_top_provinces(filtered_df)

    fig = create_bar_chart(
        top10,
        x="Provinsi",
        y="Total",
        title="Top 10 Provinsi"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    section_title("🥧 Komposisi Kendaraan")

    composition = get_vehicle_composition(filtered_df)

    pie = create_pie_chart(
        composition,
        names="Jenis Kendaraan",
        values="Jumlah",
        title="Komposisi Kendaraan"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

st.divider()

# ==========================================================
# TREND
# ==========================================================

section_title("📈 Tren Kendaraan Nasional")

trend = (
    df.groupby("Tahun", as_index=False)["Total"]
    .sum()
)

trend_chart = create_line_chart(
    trend,
    x="Tahun",
    y="Total",
    title="Total Kendaraan per Tahun"
)

st.plotly_chart(
    trend_chart,
    use_container_width=True
)

st.divider()

# ==========================================================
# SCATTER
# ==========================================================

section_title("🔍 Hubungan Mobil dan Sepeda Motor")

scatter = create_scatter_chart(
    filtered_df,
    x="Mobil",
    y="Motor",
    title="Mobil vs Sepeda Motor"
)

st.plotly_chart(
    scatter,
    use_container_width=True
)

st.divider()
# ==========================================================
# RANKING PROVINSI
# ==========================================================

section_title("🥇 Ranking Provinsi")

ranking = get_ranking(filtered_df)

ranking_display = ranking.copy()

ranking_display["Mobil"] = ranking_display["Mobil"].apply(format_number)
ranking_display["Bus"] = ranking_display["Bus"].apply(format_number)
ranking_display["Truk"] = ranking_display["Truk"].apply(format_number)
ranking_display["Motor"] = ranking_display["Motor"].apply(format_number)
ranking_display["Total"] = ranking_display["Total"].apply(format_number)

st.dataframe(
    ranking_display,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# STORYTELLING
# ==========================================================

section_title("📖 Data Storytelling")

top = ranking.iloc[0]
bottom = ranking.iloc[-1]

st.info(
    f"""
### Ringkasan Hasil Analisis

Pada **tahun {tahun}**, jumlah kendaraan bermotor di Indonesia mencapai
**{format_number(kpi['total'])} unit**.

Provinsi dengan jumlah kendaraan terbanyak adalah
**{top['Provinsi']}**
dengan total **{format_number(top['Total'])} kendaraan**.

Provinsi dengan jumlah kendaraan terendah adalah
**{bottom['Provinsi']}**
dengan total **{format_number(bottom['Total'])} kendaraan**.

Jenis kendaraan yang paling mendominasi adalah **sepeda motor**,
diikuti mobil penumpang, truk, dan bus.
"""
)

st.divider()

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

section_title("📌 Executive Summary")

left, center, right = st.columns(3)

with left:

    st.success(
        f"""
### 🚗 Provinsi Tertinggi

**{top['Provinsi']}**

Jumlah kendaraan

**{format_number(top['Total'])}**
"""
    )

with center:

    st.warning(
        f"""
### 📍 Provinsi Terendah

**{bottom['Provinsi']}**

Jumlah kendaraan

**{format_number(bottom['Total'])}**
"""
    )

with right:

    st.info(
        f"""
### 📊 Informasi Dataset

Jumlah Provinsi

**{filtered_df['Provinsi'].nunique()}**

Tahun

**{tahun}**
"""
    )

st.divider()

# ==========================================================
# DATASET PREVIEW
# ==========================================================

section_title("📄 Preview Dataset")

preview = filtered_df.copy()

preview["Mobil"] = preview["Mobil"].apply(format_number)
preview["Bus"] = preview["Bus"].apply(format_number)
preview["Truk"] = preview["Truk"].apply(format_number)
preview["Motor"] = preview["Motor"].apply(format_number)
preview["Total"] = preview["Total"].apply(format_number)

st.dataframe(
    preview,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==========================================================
# FOOTER
# ==========================================================

st.caption(
    "Dashboard Transportasi Indonesia • Dibuat menggunakan Streamlit & Plotly"
)