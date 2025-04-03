import json
import os
import pandas as pd
import re
import string

def load_latest_news(directory="data/"):
    files = [f for f in os.listdir(directory) if f.endswith('.json')]    
    if not files:
        print("No JSON files found in the directory.")
        return None
    files = sorted(files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
    latest_file = files[-1]
    file_path = os.path.join(directory, latest_file)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    return data


def clean_text(text):
    if not text:
        return ""
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert text to lowercase
    text = text.lower()
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def process_articles(articles):
    articles = load_latest_news()


    processed_articles = []
    for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')
        content = article.get('content', '')
        processed_articles.append({
            'title': title,
            'description': description,
            'publishedAt': article.get('publishedAt', ''),
            'source': article.get('source', {}).get('name', ''),
            'content': clean_text(content)
        })
    return pd.DataFrame(processed_articles)

def save_to_csv(df, filename="data/processed_articles.csv"):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    articles = load_latest_news()
    df = process_articles(articles)
    save_to_csv(df)