import streamlit as st

from utils import load_css

st.set_page_config(
    page_title="Dashboard Transportasi Indonesia",
    page_icon="🚗",
    layout="wide"
)

load_css()

pages = [
    st.Page("app_pages/home.py", title="Home", icon="🚗", default=True),
    st.Page("app_pages/dashboard.py", title="Dashboard", icon="📊"),
    st.Page("app_pages/analisis.py", title="Analisis", icon="📈"),
    st.Page("app_pages/dataset.py", title="Dataset", icon="📄"),
    st.Page("app_pages/tentang.py", title="Tentang", icon="ℹ️"),
    st.Page("app_pages/peta_indonesia.py", title="Peta Indonesia", icon="🗺️"),
]

pg = st.navigation(pages)
pg.run()
