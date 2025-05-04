import streamlit as st
import pandas as pd
import joblib

# Load model dan encoder
model = joblib.load('model.pkl')
le_sex = joblib.load('le_sex.pkl')
le_smoker = joblib.load('le_smoker.pkl')
le_region = joblib.load('le_region.pkl')

st.title('Prediksi Estimasi Biaya Asuransi')

# Input user
age = st.number_input('Usia', min_value=18, max_value=100, step=1)
sex = st.selectbox('Jenis Kelamin', ['male', 'female'])
bmi = st.number_input('BMI', min_value=10.0, max_value=50.0)
children = st.number_input('Jumlah Anak', min_value=0, max_value=10, step=1)
smoker = st.selectbox('Perokok?', ['yes', 'no'])
region = st.selectbox('Region', ['southwest', 'southeast', 'northwest', 'northeast'])

if st.button('Prediksi'):
    input_data = pd.DataFrame({
        'age': [age],
        'sex': le_sex.transform([sex]),
        'bmi': [bmi],
        'children': [children],
        'smoker': le_smoker.transform([smoker]),
        'region': le_region.transform([region])
    })

    prediction = model.predict(input_data)[0]
    st.success(f"Estimasi biaya asuransi Anda: ${prediction:,.2f}")
