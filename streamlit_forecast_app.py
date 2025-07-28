import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.markdown("""
    <style>
        html, body, [data-testid="stApp"] {
            overflow: hidden !important;
            height: 100vh;
        }
        
        /* Menu kolom kiri */
        [data-testid="column"]:first-of-type {
            background-color: #c22323 !important;
            padding: 1rem;
            border-radius: 10px;
            height: 100vh;
            box-sizing: border-box;
            box-shadow: 2px 0 8px rgba(0, 0, 0, 0.15);
        }
        .menu-container {
            background-color: #c22323 !important;
            padding: 1rem;
            border-radius: 10px;
            height: 100vh;
            box-sizing: border-box;
            box-shadow: 2px 0 8px rgba(0, 0, 0, 0.15);
            color: white;
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

        /* Hover: ubah warna latar dan teks */
        div.stButton > button:hover {
            background-color: #dcb991;
            color: white;
            border:none;
        }
    
        /* Button: hilangkan outline saat tombol difokuskan */
        div.stButton > button:focus,
        div.stButton > button:active{
            outline: none !important;
            box-shadow: none !important;
            border: none !important;
            background-color: #dcb991 !important; /* jaga tetap sama saat aktif */
            color: white !important;
            font-weight: bold;
        }
    
        /* Gaya normal tombol */
        div.stButton > button {
            box-shadow: 1px solid;
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

# Inisialisasi menu state
if "menu_state" not in st.session_state:
    st.session_state.menu_state = "Dashboard"

# Fungsi Tombol Menu
def render_button(label, target_state):
    is_active = st.session_state.menu_state == target_state
    btn_container = f'data-menu="active"' if is_active else ""
    with st.container():
        st.markdown(f'<div class="stButton" {btn_container}>', unsafe_allow_html=True)
        if st.button(label, use_container_width=True, key=label):
            st.session_state.menu_state = target_state
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# Layout Dinamis 
if st.session_state.menu_state in ["Rekomendasi", "Dashboard"]:
    # === 2 Kolom ===
    col_menu, col_content = st.columns([1, 5])

    # Kolom Menu
    with col_menu:
        st.markdown('<div class="menu-box"><h4 style="color:white">📂 Menu</h4>', unsafe_allow_html=True)
        render_button("📊 Evaluasi Model", "Evaluasi Model")
        render_button("📈 Forecast", "Forecast")
        render_button("📉 Statistik Deskriptif", "Statistik Deskriptif")
        render_button("💡 Rekomendasi", "Rekomendasi")
        st.markdown('</div>', unsafe_allow_html=True)

    # Konten Rekomendasi
    with col_content:
        st.subheader("💡 Rekomendasi")
        st.write("Konten rekomendasi muncul di sini...")

else:
    # === 3 Kolom ===
    col_menu, col_plot, col_table = st.columns([1, 3, 2])

    # Kolom Menu
    with col_menu:
        st.markdown('<div class="menu-box"><h4 style="color:white">📂 Menu</h4>', unsafe_allow_html=True)
        render_button("📊 Evaluasi Model", "Evaluasi Model")
        render_button("📈 Forecast", "Forecast")
        render_button("📉 Statistik Deskriptif", "Statistik Deskriptif")
        render_button("💡 Rekomendasi", "Rekomendasi")
        st.markdown('</div>', unsafe_allow_html=True)

    # Konten Visualisasi
    with col_plot:
        st.subheader(f"📌 {st.session_state.menu_state}")
        if st.session_state.menu_state == "Evaluasi Model":
            st.write("Plot hasil evaluasi model di sini.")
        elif st.session_state.menu_state == "Forecast":
            st.write("Grafik hasil forecast ditampilkan di sini.")
        elif st.session_state.menu_state == "Statistik Deskriptif":
            st.write("Visualisasi statistik data di sini.")

    # Tabel
    with col_table:
        st.subheader("📊 Tabel")
        st.write("Tabel data, hasil forecast, atau evaluasi...")
