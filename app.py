# app.py

import streamlit as st
from monitor import Monitor

monitor = Monitor()

st.set_page_config(page_title="Twitter Keyword Monitor", layout="centered")
st.title("📡 Twitter Keyword Alert Bot")

# Sidebar input
keyword = st.text_input("Keyword to Monitor", value="bitcoin")
threshold = st.number_input("Tweet Threshold", min_value=1, value=100)
interval = st.number_input("Check Interval (minutes)", min_value=1, value=5)

start = st.button("🚀 Start Monitoring")
stop = st.button("🛑 Stop Monitoring")

log_placeholder = st.empty()
logs = []

def log(msg):
    logs.append(f"{msg}")
    log_placeholder.text_area("Logs", value="\n".join(logs[-50:]), height=300)

if start:
    logs.clear()
    log(f"Started monitoring '{keyword}' every {interval} min(s)...")
    monitor.start(keyword, threshold, interval, log)

if stop:
    monitor.stop()
    log("Monitoring stopped.")
