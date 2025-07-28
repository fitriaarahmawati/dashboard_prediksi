import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from math import sqrt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# ===== Dummy Best Params Dictionary =====
best_params = {
    "lstm_pso": {"units": 50, "sequence_length": 10, "batch_size": 16, "epochs": 50},
    "lstm_gs": {"units": 40, "sequence_length": 15, "batch_size": 32, "epochs": 30}
}

# ===== Dummy Data (Close price) =====
df = pd.DataFrame({
    'Close': np.sin(np.linspace(0, 10, 200)) * 10 + 100
})

# ===== Preprocessing =====
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

def evaluate(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    return {"MSE": mse, "RMSE": rmse, "MAE": mae, "MAPE": mape}

# ===== LSTM Prediction and Forecasting =====
def predict_lstm(df, params):
    seq_len = params['sequence_length']
    units = params['units']
    batch_size = params['batch_size']
    epochs = params['epochs']

    data = df['Close'].values.reshape(-1, 1)
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    split = int(len(data_scaled) * 0.8)
    train = data_scaled[:split]
    test = data_scaled[split - seq_len:]

    X_train, y_train = create_sequences(train, seq_len)
    X_test, y_test = create_sequences(test, seq_len)

    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

    model = Sequential()
    model.add(LSTM(units, input_shape=(seq_len, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=0)

    y_pred = model.predict(X_test)
    y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1)).flatten()
    y_pred_inv = scaler.inverse_transform(y_pred).flatten()
    return y_test_inv, y_pred_inv, scaler, model

def forecast_lstm(df, params, days, scaler, model):
    seq_len = params['sequence_length']
    last_data = df['Close'].values.reshape(-1, 1)
    last_scaled = scaler.transform(last_data)

    input_seq = last_scaled[-seq_len:].reshape(1, seq_len, 1)
    forecast = []

    for _ in range(days):
        next_val = model.predict(input_seq, verbose=0)
        forecast.append(next_val[0][0])
        input_seq = np.append(input_seq[:, 1:, :], next_val.reshape(1, 1, 1), axis=1)

    forecast = scaler.inverse_transform(np.array(forecast).reshape(-1, 1)).flatten()
    return forecast

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

# === MENU SEBELAH KIRI ===
with col_menu:
    st.markdown("<div class='menu-column'>", unsafe_allow_html=True)
    menu = st.button("📂 Menu", ["Evaluasi Model", "Forecast", "Statistik Deskriptif", "Rekomendasi"])
    st.markdown("</div>", unsafe_allow_html=True)
    # st.markdown("<div class='menu-box'>", unsafe_allow_html=True)
    # st.markdown("### 📂 Menu", unsafe_allow_html=True)

    # selected = None
    # if st.button("📊 Evaluasi Model", use_container_width=True):
    #     selected = "evaluasi"
    # elif st.button("📈 Forecast", use_container_width=True):
    #     selected = "forecast"
    # elif st.button("📉 Statistik Deskriptif", use_container_width=True):
    #     selected = "statistik"
    # elif st.button("💡 Rekomendasi", use_container_width=True):
    #     selected = "rekomendasi"

    # st.markdown("</div>", unsafe_allow_html=True)

# # === KONTEN SEBELAH KANAN ===
# with col_content:
#     if selected == "evaluasi":
#         st.subheader("📊 Evaluasi Model")
#         st.write("Konten evaluasi model ditampilkan di sini...")
#     elif selected == "forecast":
#         st.subheader("📈 Forecast")
#         st.write("Konten forecast harga kopi ditampilkan di sini...")
#     elif selected == "statistik":
#         st.subheader("📉 Statistik Deskriptif")
#         st.write("Statistik deskriptif harga kopi...")
#     elif selected == "rekomendasi":
#         st.subheader("💡 Rekomendasi")
#         st.write("Rekomendasi berdasarkan hasil prediksi...")
#     else:
#         st.subheader("📊 Dashboard Prediksi Harga Kopi")
#         st.write("Silakan pilih salah satu menu di samping.")
