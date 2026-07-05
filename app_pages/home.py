import streamlit as st

from utils import (
    load_data,
    get_kpi,
    get_vehicle_composition,
    get_yearly_trend,
    generate_insight,
    create_pie_chart,
    create_line_chart,
    hero,
    card,
    section_title,
    load_css
)

load_css()

df = load_data()

tahun = st.sidebar.selectbox(
    "Pilih Tahun",
    sorted(df["Tahun"].unique())
)

filtered = df[df["Tahun"] == tahun]

kpi = get_kpi(filtered)

hero()

section_title("📊 Ringkasan Nasional")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    card("🚗 Total", kpi["total"])

with c2:
    card("🚙 Mobil", kpi["mobil"])

with c3:
    card("🚌 Bus", kpi["bus"])

with c4:
    card("🚚 Truk", kpi["truk"])

with c5:
    card("🛵 Motor", kpi["motor"])

st.divider()

left, right = st.columns([2, 1])

with left:

    section_title("📈 Tren Kendaraan")

    trend = get_yearly_trend(df)

    st.plotly_chart(
        create_line_chart(
            trend,
            x="Tahun",
            y="Total",
            title="Total Kendaraan per Tahun"
        ),
        use_container_width=True
    )

with right:

    section_title("🥧 Komposisi")

    comp = get_vehicle_composition(filtered)

    st.plotly_chart(
        create_pie_chart(
            comp,
            names="Jenis Kendaraan",
            values="Jumlah",
            title="Komposisi Kendaraan"
        ),
        use_container_width=True
    )

st.divider()

section_title("💡 Executive Summary")

st.success(generate_insight(filtered))