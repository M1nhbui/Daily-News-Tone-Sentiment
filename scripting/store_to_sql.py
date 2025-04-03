import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("data/processed_tones_articles.csv")

engine = create_engine("sqlite:///data/news_sentiment.db")

df.to_sql("news_sentiment", engine, if_exists="replace", index=False)

print("Data successfully stored in database!")

df1 = pd.read_sql("SELECT * FROM news_sentiment", engine)
print(df1)