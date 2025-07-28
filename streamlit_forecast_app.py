import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Inisialisasi menu state
if "menu_state" not in st.session_state:
    st.session_state.menu_state = "Dashboard"

# === CSS Styling ===
st.markdown("""
    <style>
        /* Menu kolom kiri */
        [data-testid="column"]:first-of-type {
            background-color: #c22323 !important;
            padding: 1rem;
            border-radius: 10px;
            height: 100vh;
            box-sizing: border-box;
            box-shadow: 2px 0 8px rgba(0, 0, 0, 0.15);
        }

        /* Navbar */
        .navbar {
            background-color: #ac8b64;
            padding: 1rem 2rem;
            font-size: 20px;
            font-weight: bold;
            border-radius: 10px;
            margin-bottom: 1rem;
        }

        html, body, [data-testid="stApp"] {
            overflow: hidden;
            height: 100vh;
        }

        /* Hover: ubah warna latar dan teks */
        div.stButton > button:hover {
            background-color: #dcb991;
            color: white;
            border:none;
        }
    
        /* Klik: hilangkan outline saat tombol difokuskan */
        div.stButton > button:focus,
        div.stButton > button:active{
            outline: none !important;
            box-shadow: none !important;
            border: none !important;
            background-color: #dcb991 !important; /* jaga tetap sama saat aktif */
            color: white !important;
        }
    
        /* Gaya normal tombol */
        div.stButton > button {
            border: 1px solid transparent;
            border-radius: 8px;
            margin-top: 0.5rem;
            background-color: transparent;
            color: black;
            transition: all 0.2s ease;
        }
    </style>
""", unsafe_allow_html=True)

# === Navbar atas ===
st.markdown('<div class="navbar">Dashboard Prediksi Harga Kopi Berjangka (KC=F)</div>', unsafe_allow_html=True)

# === Layout fleksibel tergantung menu ===
if st.session_state.menu_state == "Rekomendasi":
    col_menu, col_content = st.columns([1, 5])

    # Kolom 1: Menu
    with col_menu:
        st.markdown("### 📂 Menu")
        if st.button("📊 Evaluasi Model", use_container_width=True):
            st.session_state.menu_state = "Evaluasi Model"
            st.rerun()
        if st.button("📈 Forecast", use_container_width=True):
            st.session_state.menu_state = "Forecast"
            st.rerun()
        if st.button("📉 Statistik Deskriptif", use_container_width=True):
            st.session_state.menu_state = "Statistik Deskriptif"
            st.rerun()
        if st.button("💡 Rekomendasi", use_container_width=True):
            st.session_state.menu_state = "Rekomendasi"
            st.rerun()

    # Kolom 2: Konten Rekomendasi
    with col_content:
        st.subheader("💡 Rekomendasi")
        st.write("Konten rekomendasi muncul di sini...")

else:
    col_menu, col_plot, col_table = st.columns([1, 3, 2])

    # Kolom 1: Menu
    with col_menu:
        st.markdown("### 📂 Menu")
        if st.button("📊 Evaluasi Model", use_container_width=True):
            st.session_state.menu_state = "Evaluasi Model"
            st.rerun()
        if st.button("📈 Forecast", use_container_width=True):
            st.session_state.menu_state = "Forecast"
            st.rerun()
        if st.button("📉 Statistik Deskriptif", use_container_width=True):
            st.session_state.menu_state = "Statistik Deskriptif"
            st.rerun()
        if st.button("💡 Rekomendasi", use_container_width=True):
            st.session_state.menu_state = "Rekomendasi"
            st.rerun()

    # Kolom 2: Konten Plot / Visualisasi
    with col_plot:
        st.subheader(f"📌 {st.session_state.menu_state}")
        if st.session_state.menu_state == "Evaluasi Model":
            st.write("Plot hasil evaluasi model di sini.")
        elif st.session_state.menu_state == "Forecast":
            st.write("Grafik hasil forecast ditampilkan di sini.")
        elif st.session_state.menu_state == "Statistik Deskriptif":
            st.write("Visualisasi statistik data di sini.")

    # Kolom 3: Tabel
    with col_table:
        st.subheader("📊 Tabel")
        st.write("Tabel data, hasil forecast, atau evaluasi...")
