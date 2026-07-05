"""
Pemetaan nama provinsi (hasil pembersihan/UPPERCASE) ke penulisan baku
yang sesuai dengan kunci di PROVINCE_CODE dan properti "PROVINSI" pada
assets/indonesia.geojson.
"""

PROVINCE_MAPPING = {

    # Sumatera
    "ACEH": "Aceh",
    "SUMATERA UTARA": "Sumatera Utara",
    "SUMATERA BARAT": "Sumatera Barat",
    "RIAU": "Riau",
    "JAMBI": "Jambi",
    "SUMATERA SELATAN": "Sumatera Selatan",
    "BENGKULU": "Bengkulu",
    "LAMPUNG": "Lampung",
    "KEPULAUAN BANGKA BELITUNG": "Kepulauan Bangka Belitung",
    "KEPULAUAN RIAU": "Kepulauan Riau",

    # Jawa
    "DKI JAKARTA": "DKI Jakarta",
    "JAWA BARAT": "Jawa Barat",
    "JAWA TENGAH": "Jawa Tengah",
    "DI YOGYAKARTA": "Daerah Istimewa Yogyakarta",
    "DAERAH ISTIMEWA YOGYAKARTA": "Daerah Istimewa Yogyakarta",
    "JAWA TIMUR": "Jawa Timur",
    "BANTEN": "Banten",

    # Bali & Nusa Tenggara
    "BALI": "Bali",
    "NUSA TENGGARA BARAT": "Nusa Tenggara Barat",
    "NUSA TENGGARA TIMUR": "Nusa Tenggara Timur",

    # Kalimantan
    "KALIMANTAN BARAT": "Kalimantan Barat",
    "KALIMANTAN TENGAH": "Kalimantan Tengah",
    "KALIMANTAN SELATAN": "Kalimantan Selatan",
    "KALIMANTAN TIMUR": "Kalimantan Timur",
    "KALIMANTAN UTARA": "Kalimantan Utara",

    # Sulawesi
    "SULAWESI UTARA": "Sulawesi Utara",
    "SULAWESI TENGAH": "Sulawesi Tengah",
    "SULAWESI SELATAN": "Sulawesi Selatan",
    "SULAWESI TENGGARA": "Sulawesi Tenggara",
    "GORONTALO": "Gorontalo",
    "SULAWESI BARAT": "Sulawesi Barat",

    # Maluku
    "MALUKU": "Maluku",
    "MALUKU UTARA": "Maluku Utara",

    # Papua
    "PAPUA BARAT": "Papua Barat",
    "PAPUA": "Papua",
    "PAPUA SELATAN": "Papua Selatan",
    "PAPUA TENGAH": "Papua Tengah",
    "PAPUA PEGUNUNGAN": "Papua Pegunungan",
    "PAPUA BARAT DAYA": "Papua Barat Daya",
}
