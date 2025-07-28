import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from math import sqrt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# ===== Streamlit UI (Custom Layout) =====
st.set_page_config(layout="wide")

# Setup session state
if "menu_state" not in st.session_state:
    st.session_state.menu_state = "Dashboard"

# Tambahkan CSS untuk membuat kolom kiri jadi kotak menu berwarna
st.markdown("""
    <style>
        /* Kolom pertama akan jadi kotak menu */
        [data-testid="column"]:first-of-type {
            background-color: #ffcccc;
            padding: 1rem;
            border-radius: 10px;
            height: 100vh;
            box-sizing: border-box;
        }

        /* Hilangkan scroll */
        html, body, [data-testid="stApp"] {
            overflow: hidden !important;
            height: 100vh;
        }

        /* Atur jarak antar tombol */
        button {
            margin-top: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# Layout 2 kolom: menu dan konten
col_menu, col_content = st.columns([1, 3])

# === KOLOM MENU SEBELAH KIRI ===
with col_menu:
    st.markdown("### 📂 Menu")
    if st.button("📊 Evaluasi Model", use_container_width=True):
        st.session_state.menu_state = "Evaluasi Model"
    if st.button("📈 Forecast", use_container_width=True):
        st.session_state.menu_state = "Forecast"
    if st.button("📉 Statistik Deskriptif", use_container_width=True):
        st.session_state.menu_state = "Statistik Deskriptif"
    if st.button("💡 Rekomendasi", use_container_width=True):
        st.session_state.menu_state = "Rekomendasi"

# === KOLOM KONTEN SEBELAH KANAN ===
with col_content:
    st.subheader(f"📌 {st.session_state.menu_state}")
    if st.session_state.menu_state == "Evaluasi Model":
        st.write("Konten evaluasi model...")
    elif st.session_state.menu_state == "Forecast":
        st.write("Konten forecast...")
    elif st.session_state.menu_state == "Statistik Deskriptif":
        st.write("Konten statistik deskriptif...")
    elif st.session_state.menu_state == "Rekomendasi":
        st.write("Konten rekomendasi...")
    else:
        st.write("Pilih menu dari kolom kiri.")
