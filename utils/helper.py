import streamlit as st

from utils.formatter import format_number


def load_css():

    try:
        with open("style.css", encoding="utf-8") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.warning("style.css tidak ditemukan.")


def section_title(title):

    st.markdown(
        f'<h2 style="color:#2563EB;margin-top:10px;margin-bottom:10px;">'
        f'{title}</h2>',
        unsafe_allow_html=True
    )


def card(title, value):

    st.markdown(
        f'<div class="card">'
        f'<div class="card-title">{title}</div>'
        f'<div class="card-value">{format_number(value)}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


def hero():

    st.markdown(
        '<div class="hero">'
        '<h1>🚗 Dashboard Transportasi Indonesia</h1>'
        '<p>Visualisasi Data Kendaraan Bermotor '
        'Berdasarkan Data Badan Pusat Statistik (BPS) '
        'Tahun 2023–2025</p>'
        '</div>',
        unsafe_allow_html=True
    )