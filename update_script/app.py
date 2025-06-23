import streamlit as st
import pandas as pd
from sqlalchemy import text
from db.db_config import engine

st.set_page_config("News Sentiment Dashboard", layout="wide")

st.title("📰 Political News Sentiment Dashboard")

with engine.connect() as conn:
    df = pd.read_sql(text("SELECT * FROM news_sentiment ORDER BY timestamp DESC"), conn)

if df.empty:
    st.warning("No data available.")
    st.stop()

df["timestamp"] = pd.to_datetime(df["timestamp"])

# Filters
source_filter = st.multiselect("Filter by Source", options=df["source"].unique(), default=df["source"].unique())
tone_filter = st.multiselect("Filter by Sentiment", options=df["tone"].unique(), default=df["tone"].unique())
df_filtered = df[df["source"].isin(source_filter) & df["tone"].isin(tone_filter)]

st.dataframe(df_filtered[["timestamp", "source", "tone", "cleaned_text"]], use_container_width=True)

# Chart
st.bar_chart(df_filtered["tone"].value_counts())
