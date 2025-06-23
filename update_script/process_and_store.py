import pandas as pd
from tone_analyze import predict_tone
from store_to_pg import store_record
from datetime import datetime

df = pd.read_csv('data/processed_articles.csv')

for _, row in df.iterrows():
    ts = datetime.fromisoformat(row['publishedAt'].replace('Z', '+00:00')) if 'Z' in row['publishedAt'] else datetime.utcnow()
    store_record(row['cleaned_text'], predict_tone(row['cleaned_text']), row['source'], ts)
