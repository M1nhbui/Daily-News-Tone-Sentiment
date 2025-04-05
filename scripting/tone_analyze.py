import csv
import pickle
import numpy as np

used_model = 'self_model.pkl'
with open('train_model/' + used_model, 'rb') as f:
    model = pickle.load(f)

def predict_tone(text):
    if not isinstance(text, str):
        text = str(text)
    prediction = model.predict([text])
    if (used_model == 'prebuild_model.pkl'):
        return prediction[0]['label']
    return prediction[0]

def classify_articles(input_csv):
    processed_articles = []
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            text = row.get('content', '')
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
    print("Data successfully stored in CSV!")