import pandas as pd
import plotly.express as px
import streamlit as st

st.title("🩺 Hypertension Monitoring Dashboard")

def load_data():
    df = pd.read_csv("hypertension_patients.csv", parse_dates=["last_visit"])
    return df

df = load_data()

# Sidebar filter
with st.sidebar:
    st.header("🔎 Filter Patients")
    providers = st.multiselect("Provider", options=sorted(df['provider'].unique()), default=df['provider'].unique())
    risk = st.slider("Risk Score", min_value=int(df['risk_score'].min()), max_value=int(df['risk_score'].max()), value=(2, 5))
    date_range = st.date_input("Last Visit After", value=pd.to_datetime("2025-7-01"))
    
    # Apply Filters
    filtered_df = df[
        (df['provider'].isin(providers)) &
        (df['risk_score'].between(risk[0], risk[1])) &
        (df['last_visit'] >= pd.to_datetime(date_range))
    ]
    
    # Table
    st.subheader("📋 Filtered Patient List")
    st.dataframe(filtered_df.sort_values(by="risk_score", ascending=False), use_container_width=True)
    
    # Chart
    st.subheader("📊 High-Risk Patients by Provider")
    fig = px.bar(
        filtered_df.sort_values(by="risk_score", ascending=False),
        x="last_name",
        y="risk_score",
        color="provider",
        title="Top Risk Scores by Patient",
        labels={"last_name": "Patient", "risk_score": "Risk Score"}
    )
    
    st.plotly_chart(fig, use_container_width=True)
