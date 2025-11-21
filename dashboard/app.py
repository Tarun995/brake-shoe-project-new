import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/defect_model.joblib")


st.title("Brake Pad Defect Probability Dashboard")

temp = st.slider("Temperature", 100, 300)
pressure = st.slider("Pressure", 50, 150)
cycle_time = st.slider("Cycle Time", 20, 60)
vibration = st.slider("Machine Vibration", 1.0, 10.0)
humidity = st.slider("Humidity", 20, 80)

X = pd.DataFrame([[temp, pressure, cycle_time, vibration, humidity]],
                 columns=['temp','pressure','cycle_time','vibration','humidity'])

prob = model.predict_proba(X)[0][1]

st.subheader(f"Probability of Defect: **{prob:.2f}**")

if prob > 0.5:
    st.error("⚠ High Defect Risk — Check production parameters!")
else:
    st.success("✔ Production quality is stable.")
