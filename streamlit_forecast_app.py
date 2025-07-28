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

# === Tambahkan CSS agar tidak bisa scroll & layout terkunci di 1 halaman ===
st.markdown("""
    <style>
        html, body, [data-testid="stApp"] {
            overflow: hidden !important;
            height: 100vh;
        }

        /* Menu styling */
        .menu-box {
            background-color: #ffcccc;
            padding: 1rem;
            border-radius: 10px;
            height: 100vh;
            box-sizing: border-box;
        }

        /* Hilangkan scrollbar */
        ::-webkit-scrollbar {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# === Layout utama: kolom menu dan konten ===
col_menu, col_content = st.columns([1, 3])
col_menu = st.markdown("<div class='menu-box'>", unsafe_allow_html=True)

# === MENU SEBELAH KIRI ===
with col_menu:
    st.markdown("<div class='menu-box'>", unsafe_allow_html=True)
    st.markdown("### 📂 Menu", unsafe_allow_html=True)

    selected = None
    if st.button("📊 Evaluasi Model", use_container_width=True):
        selected = "evaluasi"
    elif st.button("📈 Forecast", use_container_width=True):
        selected = "forecast"
    elif st.button("📉 Statistik Deskriptif", use_container_width=True):
        selected = "statistik"
    elif st.button("💡 Rekomendasi", use_container_width=True):
        selected = "rekomendasi"

    st.markdown("</div>", unsafe_allow_html=True)

# === KONTEN SEBELAH KANAN ===
with col_content:
    if selected == "evaluasi":
        st.subheader("📊 Evaluasi Model")
        st.write("Konten evaluasi model ditampilkan di sini...")
    elif selected == "forecast":
        st.subheader("📈 Forecast")
        st.write("Konten forecast harga kopi ditampilkan di sini...")
    elif selected == "statistik":
        st.subheader("📉 Statistik Deskriptif")
        st.write("Statistik deskriptif harga kopi...")
    elif selected == "rekomendasi":
        st.subheader("💡 Rekomendasi")
        st.write("Rekomendasi berdasarkan hasil prediksi...")
    else:
        st.subheader("📊 Dashboard Prediksi Harga Kopi")
        st.write("Silakan pilih salah satu menu di samping.")
