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
import streamlit as st

# Inisialisasi session state untuk navigasi
if "menu_state" not in st.session_state:
    st.session_state.menu_state = "Dashboard"

# CSS untuk styling menu, layout, dan navbar
st.markdown("""
    <style>
        /* Menu kolom kiri */
        [data-testid="column"]:first-of-type {
            background-color: #ffcccc;
            padding: 1rem;
            border-radius: 10px;
            height: 100vh;
            box-sizing: border-box;
        }

        /* Navbar */
        .navbar {
            background-color: #ffe6e6;
            padding: 1rem 2rem;
            font-size: 24px;
            font-weight: bold;
            border-radius: 10px;
            margin-bottom: 1rem;
        }

        html, body, [data-testid="stApp"] {
            overflow: hidden;
            height: 100vh;
        }

        button {
            margin-top: 0.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# === Baris 1: Judul/Navbar (di atas kolom 2 dan 3) ===
st.markdown('<div class="navbar">Selamat Datang</div>', unsafe_allow_html=True)

# === Baris 2: Layout fleksibel tergantung menu ===
if st.session_state.menu_state == "Rekomendasi":
    # Hanya dua kolom: Menu + Konten
    col_menu, col_content = st.columns([1, 5])
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

    with col_content:
        st.subheader("💡 Rekomendasi")
        st.write("Konten rekomendasi muncul di sini...")

else:
    # Tiga kolom: Menu + Plot + Tabel
    col_menu, col_plot, col_table = st.columns([1, 3, 2])

    # === Menu (Kolom 1) ===
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

    # === Konten Plot (Kolom 2) ===
    with col_plot:
        st.subheader(f"📌 {st.session_state.menu_state}")
        if st.session_state.menu_state == "Evaluasi Model":
            st.write("Plot hasil evaluasi model di sini.")
        elif st.session_state.menu_state == "Forecast":
            st.write("Grafik hasil forecast ditampilkan di sini.")
        elif st.session_state.menu_state == "Statistik Deskriptif":
            st.write("Visualisasi statistik data di sini.")

    # === Konten Tabel (Kolom 3) ===
    with col_table:
        st.subheader("📊 Tabel")
        st.write("Tabel data, hasil forecast, atau evaluasi...")
