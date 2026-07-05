import streamlit as st


def sidebar_filter(df):
    """
    Menampilkan filter pada sidebar dan
    mengembalikan dataframe yang sudah difilter.
    """

    st.sidebar.header("🎛️ Filter Dashboard")

    # Filter Tahun
    tahun = st.sidebar.selectbox(
        "📅 Pilih Tahun",
        sorted(df["Tahun"].unique())
    )

    # Filter Provinsi
    provinsi = st.sidebar.selectbox(
        "📍 Pilih Provinsi",
        ["Semua"] + sorted(df["Provinsi"].unique())
    )

    # Filter Data
    filtered_df = df[df["Tahun"] == tahun]

    if provinsi != "Semua":
        filtered_df = filtered_df[
            filtered_df["Provinsi"] == provinsi
        ]

    return filtered_df, tahun, provinsi