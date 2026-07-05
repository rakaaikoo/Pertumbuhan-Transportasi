# 🚗 Dashboard Transportasi Indonesia

Dashboard interaktif berbasis **Streamlit** untuk analisis dan visualisasi data pertumbuhan kendaraan bermotor serta kondisi transportasi di Indonesia. Proyek ini dikembangkan sebagai Tugas Project Based Learning (PjBL) mata kuliah Visualisasi Data — Program Studi Informatika, Universitas Teknologi Digital Indonesia (UTDI).

## ✨ Fitur

- **Dashboard** — ringkasan KPI, grafik tren, dan komposisi jenis kendaraan bermotor.
- **Analisis** — statistik deskriptif, pertumbuhan tahunan, dan peringkat provinsi.
- **Dataset** — eksplorasi data mentah, distribusi nilai, dan profil kelengkapan data.
- **Peta Indonesia** — peta choropleth interaktif persebaran kendaraan bermotor per provinsi (Folium + GeoJSON).
- **Tentang** — informasi proyek dan profil pengembang.
- Filter interaktif di sidebar berdasarkan **tahun** dan **provinsi**, berlaku di seluruh halaman.

## 🛠️ Tech Stack

| Komponen | Teknologi |
|---|---|
| Bahasa pemrograman | Python |
| Framework dashboard | [Streamlit](https://streamlit.io) (multipage app) |
| Manipulasi & pembersihan data | Pandas |
| Grafik interaktif | Plotly |
| Peta choropleth | Folium (Leaflet.js) + GeoJSON |
| Baca file Excel | openpyxl |

## 📁 Struktur Proyek

```
PJBL-transportasi-dashboard/
├── app.py                     # Entry point & navigasi antar halaman
├── app_pages/
│   ├── home.py                 # Halaman beranda
│   ├── dashboard.py             # Ringkasan KPI & grafik utama
│   ├── analisis.py               # Statistik & peringkat provinsi
│   ├── dataset.py                 # Eksplorasi dataset mentah
│   ├── peta_indonesia.py           # Peta choropleth interaktif
│   └── tentang.py                   # Tentang proyek & pengembang
├── utils/
│   ├── data_loader.py           # Load & bersihkan data CSV/Excel
│   ├── province_mapper.py        # Normalisasi nama provinsi
│   ├── province_code.py           # Mapping provinsi → kode wilayah
│   ├── analytics.py                # KPI, statistik, agregasi data
│   ├── charts.py                    # Fungsi pembuatan grafik & peta
│   ├── sidebar.py                    # Komponen filter sidebar
│   ├── helper.py                      # CSS loader, kartu, judul section
│   └── formatter.py                    # Format angka & satuan
├── assets/
│   └── indonesia.geojson         # Batas wilayah provinsi Indonesia
├── data/                          # Dataset kendaraan bermotor (BPS)
├── style.css                       # Kustomisasi tampilan (tema biru)
└── requirements.txt
```

## 📊 Sumber Data

Data jumlah kendaraan bermotor menurut provinsi dan jenis kendaraan (2023–2025), bersumber dari **Badan Pusat Statistik (BPS)**.

## 🚀 Cara Menjalankan

1. **Clone / unduh** proyek ini, lalu masuk ke foldernya:
   ```bash
   cd PJBL-transportasi-dashboard
   ```

2. **(Opsional) buat virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi:**
   ```bash
   streamlit run app.py
   ```

5. Buka browser ke alamat yang muncul di terminal (biasanya `http://localhost:8501`).

## 👥 Tim Pengembang

Program Studi Informatika — Fakultas Teknologi Informasi — UTDI

| NIM | Nama |
|---|---|
| 235410023 | Muhammad Raka Aiko P |

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik (Tugas Project Based Learning) dan bebas digunakan untuk pembelajaran.
