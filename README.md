#Real-Time News Sentiment Dashboard
Overview
Automates the ingestion, cleaning, and sentiment classification of global news data using NewsAPI, a custom AI model, and Apache Airflow for daily automation. Processed data is stored in SQLite and visualized via a Streamlit dashboard.

Key Components

ETL Pipeline: Python scripts to fetch, clean, and transform data.

AI Model: Ensemble (Logistic Regression, SVM, Random Forest via a Voting Classifier) trained on 30K samples with TF-IDF vectorization to classify news tone.

Automation: Scheduled daily with Apache Airflow.

Visualization: Interactive dashboard built with Streamlit and Altair.

Storage: Data stored in SQLite with SQLAlchemy.

Setup & Execution

Install dependencies: pip install -r requirements.txt

Set up environment variables in a .env file (e.g., NEWS_API_KEY=your_key).

Place the DAG file in ~/airflow/dags or configure Airflow accordingly.

Initialize and run Airflow:

airflow db init

airflow scheduler

airflow webserver -p 8080

Trigger the DAG via the Airflow UI to run the pipeline.

Run the dashboard: streamlit run streamlit_dashboard.py

