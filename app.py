import streamlit as st
import numpy as np
import pandas as pd
import random

st.set_page_config(page_title="BTC Trend Forecast", layout="centered")

st.title("BTC Trend Forecast (Simulated Prototype)")
st.markdown("This dashboard simulates 6h, 12h, and 24h BTC directional forecasts based on synthetic gamma, funding, skew, and flow data.")

# Simulated live signals
def generate_signal():
    return {
        "Gamma Exposure Z-Score": round(np.random.normal(0, 1), 2),
        "Funding Rate 12h Change": round(np.random.normal(0, 0.01), 4),
        "IV Skew 25d Change": round(np.random.normal(0, 0.015), 4),
        "OI Delta 6h": round(np.random.normal(0, 0.03), 4),
        "Whale Transactions": random.randint(60, 180),
        "Exchange Netflow (BTC)": round(np.random.normal(0, 400), 2),
        "Realized Vol (6h)": round(np.random.normal(0.03, 0.01), 4),
        "Price % Above VWAP": round(np.random.normal(0, 0.015), 4),
        "ADX": round(np.random.uniform(10, 35), 2),
    }

signal = generate_signal()

st.subheader("Live Simulated Market Signals")
st.dataframe(pd.DataFrame(signal.items(), columns=["Signal", "Value"]))

# Simulated prediction probabilities (based on signal randomness)
def predict_prob():
    base = 0.5
    skew = signal["Gamma Exposure Z-Score"] * -0.05
    funding_effect = signal["Funding Rate 12h Change"] * -10
    whale_boost = (signal["Whale Transactions"] - 120) / 300
    adx_boost = (signal["ADX"] - 20) / 50
    prob_up = base + skew + funding_effect + whale_boost + adx_boost
    prob_up = min(max(prob_up, 0.01), 0.99)
    return round(prob_up, 2)

prob_6h = predict_prob()
prob_12h = min(max(prob_6h + np.random.normal(0, 0.05), 0.01), 0.99)
prob_24h = min(max(prob_6h + np.random.normal(0, 0.08), 0.01), 0.99)

st.subheader("BTC Directional Probability Forecasts")

col1, col2, col3 = st.columns(3)
col1.metric("6h Prob Up", f"{int(prob_6h * 100)}%", delta=None)
col2.metric("12h Prob Up", f"{int(prob_12h * 100)}%", delta=None)
col3.metric("24h Prob Up", f"{int(prob_24h * 100)}%", delta=None)

st.markdown("---")
st.caption("This is a simulated prototype using randomly generated signals for testing dashboard logic.")
