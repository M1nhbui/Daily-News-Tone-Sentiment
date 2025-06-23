import requests, json, os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

def fetch_and_save():
    url = f"https://newsapi.org/v2/top-headlines?category=politics&language=en&pageSize=50&apiKey={API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    with open("data/latest_articles.json", "w") as f:
        json.dump(articles, f, indent=2)
    print(f"✅ Fetched and saved {len(articles)} articles.")

if __name__ == "__main__":
    fetch_and_save()
