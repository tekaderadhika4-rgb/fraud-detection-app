import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AI Fraud Detection", layout="centered")

st.title("🔐 AI Fraud Detection System")

st.write("Adjust transaction risk factors:")

nlp_risk = st.slider("NLP Risk Score", 0, 100, 50)
device_risk = st.slider("Device Risk", 0, 100, 50)
vpn_risk = st.slider("VPN Risk", 0, 100, 50)
trust_score = st.slider("Trust Score", 0, 100, 50)

risk_score = (
    0.3 * nlp_risk +
    0.3 * device_risk +
    0.2 * vpn_risk +
    0.2 * (100 - trust_score)
)

st.subheader("📊 Calculated Risk Score")
st.write(round(risk_score, 2))

if risk_score > 75:
    st.error("🚨 High Fraud Risk – Transaction Blocked")
elif risk_score > 50:
    st.warning("⚠ Medium Risk – OTP Required")
else:
    st.success("✅ Low Risk – Approved")
