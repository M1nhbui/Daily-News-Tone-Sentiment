import pickle
import os

MODEL_PATH = "train_model/prebuild_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

def predict_tone(text):
    if not isinstance(text, str):
        return "neutral"
    return model.predict([text])[0]["label"]
