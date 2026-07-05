"""
charts.py
Kumpulan fungsi visualisasi Plotly
"""

import json

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# BAR CHART
# ==========================================================

def create_bar_chart(
    df,
    x,
    y,
    title="",
    color=None,
):
    fig = px.bar(
        df,
        x=x,
        y=y,
        color=color,
        text_auto=True,
        title=title,
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        margin=dict(l=20, r=20, t=50, b=20),
    )

    return fig


# ==========================================================
# LINE CHART
# ==========================================================

def create_line_chart(
    df,
    x,
    y,
    title="",
):
    fig = px.line(
        df,
        x=x,
        y=y,
        markers=True,
        title=title,
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
    )

    return fig


# ==========================================================
# PIE CHART
# ==========================================================

def create_pie_chart(
    df,
    names,
    values,
    title="",
):
    fig = px.pie(
        df,
        names=names,
        values=values,
        hole=0.45,
        title=title,
    )

    fig.update_traces(textinfo="percent+label")

    return fig


# ==========================================================
# DONUT CHART
# ==========================================================

def create_donut_chart(
    df,
    names,
    values,
    title="",
):
    return create_pie_chart(
        df,
        names,
        values,
        title,
    )


# ==========================================================
# SCATTER
# ==========================================================

def create_scatter_chart(
    df,
    x,
    y,
    title="",
):
    fig = px.scatter(
        df,
        x=x,
        y=y,
        size=y,
        title=title,
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig


# ==========================================================
# HISTOGRAM
# ==========================================================

def create_histogram(
    df,
    x,
    title="",
):
    fig = px.histogram(
        df,
        x=x,
        title=title,
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig


# ==========================================================
# VEHICLE COMPOSITION
# ==========================================================

def create_vehicle_chart(df):

    fig = px.bar(
        df,
        x="Jenis Kendaraan",
        y="Jumlah",
        color="Jenis Kendaraan",
        text_auto=True,
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
    )

    return fig


# ==========================================================
# GROWTH CHART
# ==========================================================

def create_growth_chart(df):

    fig = px.line(
        df,
        x="Tahun",
        y="Total",
        markers=True,
    )

    fig.update_layout(
        template="plotly_white",
    )

    return fig


# ==========================================================
# CHOROPLETH INDONESIA
# ==========================================================

def create_indonesia_map(
    df,
    geojson_path,
):
    """
    Visualisasi peta Indonesia menggunakan KODE_PROV.

    Menggunakan Folium (Leaflet.js) alih-alih Plotly choropleth.
    Modul geo Plotly (px.choropleth) memiliki banyak kuirk saat
    dipakai dengan GeoJSON kustom (bukan database negara bawaan
    Plotly): fitbounds/lonaxis-lataxis tidak selalu terkunci
    dengan benar, sehingga wilayah yang berwarna bisa tampak
    sangat kecil di tengah kanvas kosong. Folium jauh lebih
    matang untuk kasus choropleth GeoJSON semacam ini dan
    renderingnya konsisten di berbagai browser.
    """

    import folium

    with open(
        geojson_path,
        "r",
        encoding="utf-8"
    ) as f:

        geojson = json.load(f)

    df = df.copy()
    df["KODE_PROV"] = df["KODE_PROV"].astype(str)

    m = folium.Map(
        location=[-2.5, 118],
        zoom_start=5,
        tiles="cartodbpositron",
        scrollWheelZoom=False,
    )

    choropleth = folium.Choropleth(
        geo_data=geojson,
        data=df,
        columns=["KODE_PROV", "Total"],
        key_on="feature.properties.KODE_PROV",
        fill_color="YlGnBu",
        fill_opacity=0.85,
        line_opacity=0.4,
        line_color="white",
        legend_name="Jumlah Kendaraan Bermotor",
        nan_fill_color="#E5E7EB",
        highlight=True,
    ).add_to(m)

    # Buat lookup cepat untuk tooltip per KODE_PROV
    info = df.set_index("KODE_PROV")[
        ["Provinsi", "Mobil", "Bus", "Truk", "Motor", "Total"]
    ].to_dict("index")

    for feature in choropleth.geojson.data["features"]:
        kode = str(feature["properties"].get("KODE_PROV"))
        row = info.get(kode)

        if row:
            feature["properties"]["tooltip"] = (
                f"<b>{row['Provinsi']}</b><br>"
                f"Mobil: {row['Mobil']:,.0f}<br>"
                f"Bus: {row['Bus']:,.0f}<br>"
                f"Truk: {row['Truk']:,.0f}<br>"
                f"Motor: {row['Motor']:,.0f}<br>"
                f"Total: {row['Total']:,.0f}"
            )
        else:
            nama = feature["properties"].get("PROVINSI", "")
            feature["properties"]["tooltip"] = (
                f"<b>{nama}</b><br>Tidak ada data"
            )

    folium.GeoJsonTooltip(
        fields=["tooltip"],
        labels=False,
        sticky=True,
    ).add_to(choropleth.geojson)

    bounds = choropleth.geojson.get_bounds()
    m.fit_bounds(bounds)

    return m


# ==========================================================
# DISTRIBUTION CHART (Dataset page)
# ==========================================================

def create_distribution_chart(df):
    """
    Bar chart distribusi jumlah per jenis kendaraan.
    Mengharapkan kolom "Jenis Kendaraan" dan "Jumlah".
    """

    fig = px.bar(
        df,
        x="Jenis Kendaraan",
        y="Jumlah",
        color="Jenis Kendaraan",
        text_auto=True,
        title="Distribusi Jenis Kendaraan",
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=450,
    )

    return fig


# ==========================================================
# MISSING VALUE CHART (Dataset page)
# ==========================================================

def create_missing_chart(df):
    """
    Bar chart jumlah missing value per kolom.
    """

    missing = df.isnull().sum().reset_index()
    missing.columns = ["Kolom", "Missing"]

    fig = px.bar(
        missing,
        x="Kolom",
        y="Missing",
        text_auto=True,
        title="Missing Value per Kolom",
    )

    fig.update_layout(
        template="plotly_white",
        height=400,
    )

    return fig


# ==========================================================
# PROFILE CHART (Dataset page)
# ==========================================================

def create_profile_chart(df):
    """
    Pie chart proporsi tipe data pada dataset (numerik vs kategorikal).
    """

    numeric_cols = df.select_dtypes(include="number").shape[1]
    categorical_cols = df.shape[1] - numeric_cols

    profile = pd.DataFrame({
        "Tipe Kolom": ["Numerik", "Kategorikal"],
        "Jumlah": [numeric_cols, categorical_cols],
    })

    fig = px.pie(
        profile,
        names="Tipe Kolom",
        values="Jumlah",
        hole=0.45,
        title="Profil Tipe Kolom",
    )

    fig.update_traces(textinfo="percent+label")

    return fig


# ==========================================================
# EMPTY CHART
# ==========================================================

def create_empty_chart(message="Tidak ada data"):

    fig = go.Figure()

    fig.add_annotation(

        text=message,

        x=0.5,

        y=0.5,

        showarrow=False,

        font=dict(size=20),

    )

    fig.update_xaxes(visible=False)

    fig.update_yaxes(visible=False)

    fig.update_layout(

        template="plotly_white",

        height=400,

    )

    return fig