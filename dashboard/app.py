import streamlit as st
import pandas as pd
import joblib
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

# ---------------------------------------------------------
# FIX: SAFE MODEL PATH (WORKS ON STREAMLIT CLOUD & LOCAL)
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "defect_model.joblib")

# Debug (optional)
# st.write("Model path:", MODEL_PATH)

model = joblib.load(MODEL_PATH)

# ---------------------------------------------------------
# STREAMLIT APP CONFIG
# ---------------------------------------------------------
st.set_page_config(page_title="Brake Pad Defect Dashboard", layout="wide")

# ---- HEADER ----
st.markdown("""
<h1 style='text-align:center; color:#1a3e6f; margin-bottom:0;'>Brake Pad Defect Probability Dashboard</h1>
<p style='text-align:center; color:#444; font-size:17px;'>Real-time defect analysis using production parameters.</p>
""", unsafe_allow_html=True)

# ---- SIDEBAR ----
st.sidebar.header("⚙️ Adjust Production Parameters")

temp = st.sidebar.slider("Temperature (°C)", 100, 300, 160)
pressure = st.sidebar.slider("Pressure (psi)", 50, 150, 90)
cycle_time = st.sidebar.slider("Cycle Time (sec)", 20, 60, 35)
vibration = st.sidebar.slider("Machine Vibration", 1.0, 10.0, 4.2)
humidity = st.sidebar.slider("Humidity (%)", 20, 80, 45)

# ---- PREDICT ----
X = pd.DataFrame([[temp, pressure, cycle_time, vibration, humidity]],
                 columns=['temp','pressure','cycle_time','vibration','humidity'])
prob = model.predict_proba(X)[0][1]
prob_pct = int(prob*100)

# TABS
tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📈 Analytics", "📉 Trends"])


# -----------------------------------------------
# TAB 1: DASHBOARD VIEW
# -----------------------------------------------
with tab1:
    st.subheader("Production Overview")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Temperature", f"{temp} °C")
    with c2:
        st.metric("Pressure", f"{pressure} psi")
    with c3:
        st.metric("Cycle Time", f"{cycle_time} sec")

    c4, c5 = st.columns(2)
    with c4:
        st.metric("Machine Vibration", f"{vibration}")
    with c5:
        st.metric("Humidity", f"{humidity}%")

    st.subheader("Defect Probability")
    st.progress(prob)

    if prob > 0.5:
        st.error(f"⚠ High Risk! Defect Probability: {prob:.2f}")
    else:
        st.success(f"✔ Safe! Defect Probability: {prob:.2f}")


# -----------------------------------------------
# TAB 2: ANALYTICS (Graphs)
# -----------------------------------------------
with tab2:
    st.subheader("Parameter Radar Chart")

    radar_df = pd.DataFrame({
        "Parameter": ["Temperature", "Pressure", "Cycle Time", "Vibration", "Humidity"],
        "Value": [temp, pressure, cycle_time, vibration, humidity]
    })

    fig_radar = go.Figure(data=go.Scatterpolar(
        r=radar_df["Value"],
        theta=radar_df["Parameter"],
        fill='toself'
    ))
    fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True)))
    st.plotly_chart(fig_radar, use_container_width=True)


    st.subheader("Parameter Comparison Bar Graph")
    ideal_values = [180, 90, 35, 4, 40]

    bar_df = pd.DataFrame({
        "Parameter": ["Temp", "Pressure", "Cycle", "Vibration", "Humidity"],
        "Current": [temp, pressure, cycle_time, vibration, humidity],
        "Ideal": ideal_values
    })

    fig_bar = px.bar(bar_df, x="Parameter", y=["Current", "Ideal"], barmode='group')
    st.plotly_chart(fig_bar, use_container_width=True)



# -----------------------------------------------
# TAB 3: LIVE TRENDS
# -----------------------------------------------
with tab3:
    st.subheader("Defect Probability Trend Line")

    # Creating a fake trend for now (real sensors can replace this)
    trend_x = np.linspace(1, 10, 10)
    trend_y = np.clip(np.random.normal(prob, 0.05, 10), 0, 1)

    fig_line = px.line(
        x=trend_x, y=trend_y,
        labels={"x": "Time", "y": "Defect Probability"},
        markers=True
    )

    st.plotly_chart(fig_line, use_container_width=True)
