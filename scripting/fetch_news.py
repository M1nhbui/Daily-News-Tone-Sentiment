import os
from dotenv import load_dotenv
from newsapi import NewsApiClient
import json
from datetime import datetime


load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

newsapi = NewsApiClient(API_KEY)

def fetch_news() :
    top_headlines = newsapi.get_top_headlines(country="us", page_size=100)
    articles = top_headlines['articles']

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(f"data/news_{timestamp}.json", "w") as f:
        json.dump(articles, f, indent=4)

    print(f"Fetched {len(articles)} articles.")

    # for article in articles:
    #     title = article['title']
    #     content = article['content']
    #     published_at = article['publishedAt']
    #     print(f"Title: {title}")
    #     print(f"Published at: {published_at}")
    #     print(f"Content: {content}")

    return articles

if __name__ == "__main__":
    fetch_news()
