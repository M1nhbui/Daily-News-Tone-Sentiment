import json, re
import pandas as pd

def clean_text(text):
    text = re.sub(r"http\S+", "", str(text))
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()

def clean_and_save():
    with open("data/latest_articles.json", "r") as f:
        raw = json.load(f)

    df = pd.DataFrame(raw)
    df["cleaned_text"] = df["content"].apply(clean_text)
    df = df[["publishedAt", "source", "cleaned_text"]]
    df["source"] = df["source"].apply(lambda x: x.get("name", "Unknown"))
    df.to_csv("data/processed_articles.csv", index=False)
    print("✅ Cleaned and saved to processed_articles.csv")

if __name__ == "__main__":
    clean_and_save()
