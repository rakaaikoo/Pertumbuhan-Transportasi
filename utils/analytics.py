"""
analytics.py
Berisi seluruh fungsi analisis data untuk Dashboard Transportasi Indonesia.
"""

import pandas as pd


# ==========================================================
# KPI DASHBOARD
# ==========================================================

def get_kpi(df):
    """
    Menghasilkan KPI utama dashboard.
    """

    return {
        "total": int(df["Total"].sum()),
        "mobil": int(df["Mobil"].sum()),
        "bus": int(df["Bus"].sum()),
        "truk": int(df["Truk"].sum()),
        "motor": int(df["Motor"].sum()),
        "provinsi": int(df["Provinsi"].nunique()),
    }


# ==========================================================
# STATISTIK DATA
# ==========================================================

def get_statistics(df):
    """
    Statistik deskriptif sederhana.
    """

    return df[
        ["Mobil", "Bus", "Truk", "Motor", "Total"]
    ].describe()


# ==========================================================
# TOP PROVINSI
# ==========================================================

def get_top_provinces(df, n=10):
    """
    Mengambil n provinsi dengan jumlah kendaraan terbesar.
    """

    return (
        df[
            ["Provinsi", "Total"]
        ]
        .sort_values(
            by="Total",
            ascending=False
        )
        .head(n)
        .reset_index(drop=True)
    )


# ==========================================================
# BOTTOM PROVINSI
# ==========================================================

def get_bottom_provinces(df, n=10):
    """
    Mengambil n provinsi dengan jumlah kendaraan terkecil.
    """

    return (
        df[
            ["Provinsi", "Total"]
        ]
        .sort_values(
            by="Total",
            ascending=True
        )
        .head(n)
        .reset_index(drop=True)
    )


# ==========================================================
# RANKING
# ==========================================================

def get_ranking(df):
    """
    Ranking seluruh provinsi.
    """

    ranking = (
        df
        .sort_values(
            by="Total",
            ascending=False
        )
        .reset_index(drop=True)
    )

    ranking.index += 1

    return ranking


# ==========================================================
# KOMPOSISI KENDARAAN
# ==========================================================

def get_vehicle_composition(df):
    """
    Menghasilkan total setiap jenis kendaraan.
    """

    return pd.DataFrame({

        "Jenis Kendaraan": [
            "Mobil",
            "Bus",
            "Truk",
            "Motor"
        ],

        "Jumlah": [

            df["Mobil"].sum(),

            df["Bus"].sum(),

            df["Truk"].sum(),

            df["Motor"].sum()

        ]

    })


# ==========================================================
# PERSENTASE KENDARAAN
# ==========================================================

def get_vehicle_percentage(df):
    """
    Persentase tiap jenis kendaraan.
    """

    total = df["Total"].sum()

    return pd.DataFrame({

        "Jenis Kendaraan": [
            "Mobil",
            "Bus",
            "Truk",
            "Motor"
        ],

        "Persentase": [

            df["Mobil"].sum()/total*100,

            df["Bus"].sum()/total*100,

            df["Truk"].sum()/total*100,

            df["Motor"].sum()/total*100

        ]

    })


# ==========================================================
# MAP DATA
# ==========================================================

def prepare_map_data(df):
    """
    Menyiapkan dataframe untuk visualisasi peta.
    """

    columns = [

        "KODE_PROV",

        "Provinsi",

        "Mobil",

        "Bus",

        "Truk",

        "Motor",

        "Total"

    ]

    return df[columns].copy()


# ==========================================================
# MAP KPI
# ==========================================================

def get_map_kpi(df):
    """
    KPI khusus halaman peta.
    """

    return {

        "total": int(df["Total"].sum()),

        "provinsi": int(df["Provinsi"].nunique()),

        "tertinggi": df.loc[
            df["Total"].idxmax(),
            "Provinsi"
        ]

    }


# ==========================================================
# GROWTH
# ==========================================================

def get_growth(df):
    """
    Menghitung pertumbuhan total kendaraan per tahun.
    """

    if "Tahun" not in df.columns:
        return pd.DataFrame()

    growth = (

        df

        .groupby("Tahun")["Total"]

        .sum()

        .reset_index()

    )

    growth["Growth (%)"] = (

        growth["Total"]

        .pct_change()

        * 100

    )

    return growth


# ==========================================================
# YEARLY TREND
# ==========================================================

def get_yearly_trend(df):
    """
    Menghasilkan total kendaraan per tahun (untuk grafik tren nasional).
    """

    return (
        df
        .groupby("Tahun", as_index=False)["Total"]
        .sum()
    )


# ==========================================================
# EXECUTIVE INSIGHT
# ==========================================================

def generate_insight(df):
    """
    Menghasilkan ringkasan naratif otomatis dari data yang difilter.
    """

    if df.empty:
        return "Tidak ada data untuk periode yang dipilih."

    def _id_number(n):
        return f"{int(n):,}".replace(",", ".")

    kpi = get_kpi(df)
    top = get_top_provinces(df, n=1).iloc[0]
    bottom = get_bottom_provinces(df, n=1).iloc[0]

    return (
        f"Total kendaraan bermotor tercatat sebanyak {_id_number(kpi['total'])} unit "
        f"di {kpi['provinsi']} provinsi. "
        f"Provinsi dengan jumlah kendaraan terbanyak adalah {top['Provinsi']} "
        f"({_id_number(top['Total'])} unit), sedangkan yang paling sedikit adalah "
        f"{bottom['Provinsi']} ({_id_number(bottom['Total'])} unit). "
        "Sepeda motor tetap menjadi jenis kendaraan yang paling mendominasi "
        "dibandingkan mobil, truk, dan bus."
    )