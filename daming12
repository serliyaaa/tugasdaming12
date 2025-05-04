import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("model_asuransi.pkl")

st.title("Estimasi Biaya Asuransi")

# Input user
age = st.number_input("Usia", min_value=18, max_value=100)
sex = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0)
children = st.number_input("Jumlah Anak", min_value=0, max_value=10)
smoker = st.selectbox("Perokok?", ["Ya", "Tidak"])
region = st.selectbox("Wilayah", ["southeast", "southwest", "northeast", "northwest"])

# Konversi input
sex_val = 1 if sex == "Perempuan" else 0
smoker_val = 1 if smoker == "Ya" else 0
region_dict = {"southeast": 0, "southwest": 1, "northeast": 2, "northwest": 3}
region_val = region_dict[region]

# Prediksi
if st.button("Hitung Estimasi"):
    data = np.array([[age, sex_val, bmi, children, smoker_val, region_val]])
    prediksi = model.predict(data)
    st.success(f"Estimasi Biaya Asuransi Anda: Rp {int(prediksi[0]):,}")
