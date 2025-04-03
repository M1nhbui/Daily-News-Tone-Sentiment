import csv
import pickle
import numpy as np

with open('train_model/prebuild_model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict_tone(text):
    if not isinstance(text, str):
        text = str(text)
    prediction = model.predict([text])
    return prediction[0]

def classify_articles(input_csv):
    processed_articles = []
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            text = row.get('clean_title', '')
            row['tone'] = predict_tone(text)
            processed_articles.append(row)
    return processed_articles

def save_to_csv():
    input_csv = 'data/processed_articles.csv'

    articles = classify_articles(input_csv)
    output_csv = 'data/processed_tones_articles.csv'

    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=articles[0].keys())
            writer.writeheader()
            writer.writerows(articles)
    
if __name__ == "__main__":
    save_to_csv()