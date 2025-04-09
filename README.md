# Real-Time News Sentiment Dashboard

**Overview**  
Automates ingestion, cleaning, and sentiment classification of global news data using NewsAPI, a custom AI model, and Apache Airflow for daily automation. Processed data is stored in SQLite and visualized via a Streamlit dashboard.

**Key Components**  
- **ETL Pipeline:** Python scripts fetch, clean, and transform global news data.  
- **AI Model:** Ensemble of Logistic Regression, SVM, and Random Forest via a Voting Classifier—trained on 30K samples using a TF-IDF vectorizer—to classify news tone (positive, neutral, negative).  
- **Automation:** Daily pipeline scheduled using Apache Airflow.  
- **Visualization:** Interactive dashboard built with Streamlit and Altair.  
- **Storage:** Data stored in SQLite using SQLAlchemy.
