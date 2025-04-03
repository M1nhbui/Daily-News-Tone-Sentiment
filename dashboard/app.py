import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import altair as alt

# Create the SQLite engine (adjust path as needed)
engine = create_engine("sqlite:///data/news_sentiment.db")

@st.cache_data
def load_data():
    query = "SELECT * FROM news_sentiment"
    df = pd.read_sql(query, engine)
    # Convert publishedAt to datetime if available
    if 'publishedAt' in df.columns:
        df['publishedAt'] = pd.to_datetime(df['publishedAt'], errors='coerce')
    return df

# Load data from the SQLite database
df = load_data()

st.title("News Sentiment Dashboard")
st.write("Displaying sentiment analysis of news articles.")

# Show latest 10 rows from the database
st.subheader("Latest News Articles")
st.dataframe(df.head(10))

# Create a tone distribution chart using Altair
st.subheader("Tone Distribution")
tone_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X("tone:N", title="Tone"),
    y=alt.Y("count()", title="Number of Articles"),
    tooltip=["tone", "count()"]
).properties(
    width=600,
    height=400
)
st.altair_chart(tone_chart, use_container_width=True)